#!/usr/bin/env python3
"""Copy the nine approved student-template paths without touching other paths."""

from __future__ import annotations

import argparse
import posixpath
import re
import stat
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


# Destination paths are the entire approved write/delete boundary. Each source
# path is explicit so the Draft source READMEs cannot enter the template.
MANAGED = (
    ("distribution/student/README.md", "README.md"),
    ("distribution/student/personas/education/README.md", "personas/education/README.md"),
    ("LICENSE", "LICENSE"),
    ("personas/education/GEM_CODE_GENERATOR.md", "personas/education/GEM_CODE_GENERATOR.md"),
    ("personas/education/GEM_RESEARCHER_DEVELOPMENT.md", "personas/education/GEM_RESEARCHER_DEVELOPMENT.md"),
    ("personas/education/GEM_RESEARCHER_FULL.md", "personas/education/GEM_RESEARCHER_FULL.md"),
    ("personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md", "personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md"),
    ("personas/education/GEM_REVIEWER.md", "personas/education/GEM_REVIEWER.md"),
    ("personas/education/GEM_SOLUTION_PARTNER.md", "personas/education/GEM_SOLUTION_PARTNER.md"),
)

DOCUMENT_INFO = re.compile(
    r"\A(?:\ufeff)?<details>\r?\n"
    r"<summary>Document Info（文書情報）</summary>\r?\n"
    r"(?P<body>.*?)\r?\n</details>(?:\r?\n|\Z)",
    re.DOTALL,
)
STATUS_ROW = re.compile(r"^\|[ \t]*Status（ステータス）[ \t]*\|[ \t]*([^|\r\n]*?)[ \t]*\|[ \t]*$")
OBVIOUS_SECRET = re.compile(
    rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
    rb"|\bgh[pousr]_[A-Za-z0-9_]{20,}\b"
    rb"|\bgithub_pat_[A-Za-z0-9_]{20,}\b"
    rb"|\bAKIA[A-Z0-9]{16}\b"
)


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def regular_file_or_absent(root: Path, relative: str) -> Path:
    current = root
    parts = Path(relative).parts
    for part in parts[:-1]:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Refusing symlink parent: {relative}")
        if current.exists() and not current.is_dir():
            raise ValueError(f"Refusing non-directory parent: {relative}")
    path = root / relative
    if path.is_symlink():
        raise ValueError(f"Refusing symlink: {relative}")
    if path.exists() and not stat.S_ISREG(path.stat().st_mode):
        raise ValueError(f"Refusing non-file: {relative}")
    return path


def has_approved_document_info(content: bytes) -> bool:
    document_info = DOCUMENT_INFO.match(content.decode("utf-8"))
    if document_info is None:
        return False
    status_rows = [
        line
        for line in document_info.group("body").splitlines()
        if re.match(r"^\|[ \t]*Status（ステータス）[ \t]*\|", line)
    ]
    if len(status_rows) != 1:
        return False
    status = STATUS_ROW.fullmatch(status_rows[0])
    return status is not None and status.group(1) == "Approved"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve(strict=True)
    destination = args.destination.resolve(strict=True)
    if source == destination:
        raise ValueError("Source and destination must differ")
    if git(destination, "status", "--porcelain"):
        raise ValueError("Destination checkout is not clean")

    # Validate every source before touching the destination. Missing managed
    # source paths are the only paths eligible for deletion in the destination.
    plan: list[tuple[str, Path, bytes | None]] = []
    for source_name, destination_name in MANAGED:
        source_path = regular_file_or_absent(source, source_name)
        destination_path = regular_file_or_absent(destination, destination_name)
        content = source_path.read_bytes() if source_path.exists() else None
        if content is not None:
            if source_name.startswith("personas/education/GEM_") and not has_approved_document_info(content):
                raise ValueError(f"Persona is not Approved: {source_name}")
            if OBVIOUS_SECRET.search(content):
                raise ValueError(f"Possible credential in managed source: {source_name}")
        if content is None:
            operation = "delete" if destination_path.exists() else "absent"
        elif not destination_path.exists():
            operation = "add"
        elif destination_path.read_bytes() == content:
            operation = "same"
        else:
            operation = "replace"
        print(f"{operation}: {destination_name}")
        plan.append((destination_name, destination_path, content))

    # A README or Persona may link only to another file that will actually be
    # present in this template. This prevents links into excluded source docs.
    planned_content = {name: content for name, _, content in plan}
    for name, _, content in plan:
        if content is None or not name.endswith(".md"):
            continue
        for raw_target in re.findall(rb"\]\(([^)]+)\)", content):
            target = urlsplit(raw_target.decode("utf-8"))
            if target.scheme or target.netloc or not target.path:
                continue
            linked = posixpath.normpath(
                posixpath.join(posixpath.dirname(name), unquote(target.path))
            )
            if planned_content.get(linked) is None:
                raise ValueError(f"Link leaves managed contents: {name} -> {linked}")

    if args.dry_run:
        return

    for destination_name, destination_path, content in plan:
        if content is None:
            if destination_path.exists():
                destination_path.unlink()
            git(destination, "rm", "--ignore-unmatch", "--", destination_name)
        else:
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            destination_path.write_bytes(content)
            git(destination, "add", "--", destination_name)

    staged = set(git(destination, "diff", "--cached", "--name-only").splitlines())
    allowed = set(planned_content)
    if not staged <= allowed:
        raise ValueError(f"Unexpected staged paths: {sorted(staged - allowed)}")


if __name__ == "__main__":
    main()
