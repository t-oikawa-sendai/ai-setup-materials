#!/usr/bin/env python3
"""Sync the thirty selected student-template paths without touching other paths."""

from __future__ import annotations

import argparse
import posixpath
import re
import stat
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


# Destination paths are the entire selected add/overwrite boundary. Deletion
# retains the narrower original nine-path boundary below.
STUDENT_GUIDE = "docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md"
MANAGED = (
    ("README.md", "README.md"),
    ("personas/education/README.md", "personas/education/README.md"),
    ("LICENSE", "LICENSE"),
    (STUDENT_GUIDE, STUDENT_GUIDE),
    ("personas/education/GEM_CODE_GENERATOR.md", "personas/education/GEM_CODE_GENERATOR.md"),
    ("personas/education/GEM_RESEARCHER_DEVELOPMENT.md", "personas/education/GEM_RESEARCHER_DEVELOPMENT.md"),
    ("personas/education/GEM_RESEARCHER_FULL.md", "personas/education/GEM_RESEARCHER_FULL.md"),
    ("personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md", "personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md"),
    ("personas/education/GEM_REVIEWER.md", "personas/education/GEM_REVIEWER.md"),
    ("personas/education/GEM_SOLUTION_PARTNER.md", "personas/education/GEM_SOLUTION_PARTNER.md"),
    ("personas/WHY_PERSONA_MATTERS.md", "personas/WHY_PERSONA_MATTERS.md"),
    ("personas/AI_ISSUES_EVIDENCE.md", "personas/AI_ISSUES_EVIDENCE.md"),
    ("personas/SYCOPHANCY_CHALLENGER_PERSONAS.md", "personas/SYCOPHANCY_CHALLENGER_PERSONAS.md"),
    ("personas/assets/sycophancy_frontier_models_2026.png", "personas/assets/sycophancy_frontier_models_2026.png"),
    ("personas/PERSONA_IDENTIFICATION_AND_SETUP.md", "personas/PERSONA_IDENTIFICATION_AND_SETUP.md"),
    ("personas/education/SKILLS/CODE_GENERATOR.md", "personas/education/SKILLS/CODE_GENERATOR.md"),
    ("personas/education/SKILLS/RESEARCHER_CAREER.md", "personas/education/SKILLS/RESEARCHER_CAREER.md"),
    ("personas/education/SKILLS/RESEARCHER_DEVELOPMENT.md", "personas/education/SKILLS/RESEARCHER_DEVELOPMENT.md"),
    ("personas/education/SKILLS/RESEARCHER_LEARNING.md", "personas/education/SKILLS/RESEARCHER_LEARNING.md"),
    ("personas/education/SKILLS/REVIEWER.md", "personas/education/SKILLS/REVIEWER.md"),
    ("personas/education/SKILLS/SOLUTION_PARTNER.md", "personas/education/SKILLS/SOLUTION_PARTNER.md"),
    ("personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md", "personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md"),
    ("personas/reference/README.md", "personas/reference/README.md"),
    ("personas/reference/CHATGPT_PERSONA.md", "personas/reference/CHATGPT_PERSONA.md"),
    ("personas/reference/CLAUDE_PERSONA.md", "personas/reference/CLAUDE_PERSONA.md"),
    ("personas/reference/CURSOR_PERSONA.md", "personas/reference/CURSOR_PERSONA.md"),
    ("personas/reference/GEMINI_PERSONA.md", "personas/reference/GEMINI_PERSONA.md"),
    ("personas/reference/PERSONA_OPERATION_CASE_STUDY.md", "personas/reference/PERSONA_OPERATION_CASE_STUDY.md"),
    ("personas/reference/PERSONA_PROMPT_TEMPLATE.md", "personas/reference/PERSONA_PROMPT_TEMPLATE.md"),
    ("personas/reference/CHAT_HANDOFF_TEMPLATE.md", "personas/reference/CHAT_HANDOFF_TEMPLATE.md"),
)

DELETE_ALLOWED = frozenset({
    "README.md",
    "personas/education/README.md",
    "LICENSE",
    "personas/education/GEM_CODE_GENERATOR.md",
    "personas/education/GEM_RESEARCHER_DEVELOPMENT.md",
    "personas/education/GEM_RESEARCHER_FULL.md",
    "personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md",
    "personas/education/GEM_REVIEWER.md",
    "personas/education/GEM_SOLUTION_PARTNER.md",
})
BASELINE_APPROVED_DOCUMENTS = frozenset({
    "personas/PERSONA_IDENTIFICATION_AND_SETUP.md",
    "personas/reference/CHATGPT_PERSONA.md",
    "personas/reference/CLAUDE_PERSONA.md",
    "personas/reference/CURSOR_PERSONA.md",
    "personas/reference/GEMINI_PERSONA.md",
    *(name for name in DELETE_ALLOWED if name.startswith("personas/education/GEM_")),
})
BASELINE_DRAFT_DOCUMENTS = frozenset({
    "README.md",
    "personas/education/README.md",
    "personas/AI_ISSUES_EVIDENCE.md",
    "personas/SYCOPHANCY_CHALLENGER_PERSONAS.md",
    "personas/education/SKILLS/CODE_GENERATOR.md",
    "personas/education/SKILLS/RESEARCHER_CAREER.md",
    "personas/education/SKILLS/RESEARCHER_DEVELOPMENT.md",
    "personas/education/SKILLS/RESEARCHER_LEARNING.md",
    "personas/education/SKILLS/REVIEWER.md",
    "personas/education/SKILLS/SOLUTION_PARTNER.md",
    "personas/reference/README.md",
    "personas/reference/PERSONA_OPERATION_CASE_STUDY.md",
    "personas/reference/PERSONA_PROMPT_TEMPLATE.md",
    "personas/reference/CHAT_HANDOFF_TEMPLATE.md",
})
ARCHIVED_DOCUMENT = "personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md"
STATUSLESS_DOCUMENT = "personas/WHY_PERSONA_MATTERS.md"
STATUS_BEARING_DOCUMENTS = BASELINE_APPROVED_DOCUMENTS | BASELINE_DRAFT_DOCUMENTS
DESTINATIONS = frozenset(destination for _, destination in MANAGED)
assert len(MANAGED) == len(DESTINATIONS) == 30
assert len(DELETE_ALLOWED) == 9 and DELETE_ALLOWED <= DESTINATIONS
assert STUDENT_GUIDE not in DELETE_ALLOWED
assert (STATUS_BEARING_DOCUMENTS | {ARCHIVED_DOCUMENT, STATUSLESS_DOCUMENT, STUDENT_GUIDE}) == {
    name for name in DESTINATIONS if name.endswith(".md")
}
assert not (BASELINE_APPROVED_DOCUMENTS & BASELINE_DRAFT_DOCUMENTS)

# Only these five selected documents currently contain links to excluded
# material. All other new relative links cause the sync to stop for review.
EXCLUDED_LINKS = {
    "README.md": frozenset({
        "docs/AI_SERVICE_UPDATES.md",
        "project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md",
    }),
    "personas/WHY_PERSONA_MATTERS.md": frozenset({
        "project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md",
    }),
    "personas/PERSONA_IDENTIFICATION_AND_SETUP.md": frozenset({
        "AGENTS.md", "project-notes/DECISIONS.md", "project-notes/CURRENT.md",
        "personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md",
    }),
    "personas/education/README.md": frozenset({"project-notes/DECISIONS.md"}),
    "personas/reference/README.md": frozenset({
        "personas/reference/EMPLOYMENT_SUPPORT_ADVISOR.md",
        "personas/reference/IT_EDUCATION_CONTENT_DESIGNER.md",
        "personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md",
    }),
}

WEB_URL = re.compile(r"https?://[^\s<>\[\]()\"']+", re.IGNORECASE)

DOCUMENT_INFO = re.compile(
    r"\A(?:\ufeff)?<details>\r?\n"
    r"<summary>Document Info（文書情報）</summary>\r?\n"
    r"(?P<body>.*?)\r?\n</details>(?:\r?\n|\Z)",
    re.DOTALL,
)
DOCUMENT_INFO_ANYWHERE = re.compile(
    r"<details>\r?\n<summary>Document Info（文書情報）</summary>\r?\n"
    r"(?P<body>.*?)\r?\n</details>",
    re.DOTALL,
)
STATUS_ROW = re.compile(r"^\|[ \t]*Status（ステータス）[ \t]*\|[ \t]*([^|\r\n]*?)[ \t]*\|[ \t]*$")
OBVIOUS_SECRET = re.compile(
    rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
    rb"|\bgh[pousr]_[A-Za-z0-9_]{20,}\b"
    rb"|\bgithub_pat_[A-Za-z0-9_]{20,}\b"
    rb"|\bAKIA[A-Z0-9]{16}\b"
    rb"|\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"
    rb"|\bxox[baprs]-[A-Za-z0-9-]{20,}\b"
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


def has_allowed_gem_document_info(content: bytes) -> bool:
    body = content.decode("utf-8")
    document_info = DOCUMENT_INFO.match(body)
    if document_info is None:
        return False
    if len(DOCUMENT_INFO_ANYWHERE.findall(body)) != 1:
        return False
    status_rows = [line for line in document_info.group("body").splitlines()
                   if re.match(r"^\|[ \t]*Status", line)]
    if len(status_rows) != 1:
        return False
    status = STATUS_ROW.fullmatch(status_rows[0])
    return status is not None and status.group(1) in {"Draft", "Approved"}


def document_status(content: bytes) -> str | None:
    body = content.decode("utf-8")
    matches = list(DOCUMENT_INFO_ANYWHERE.finditer(body))
    if len(matches) != 1 or len(re.findall(r"<summary>\s*Document\s+Info", body, re.IGNORECASE)) != 1:
        return None
    rows = [line for line in matches[0].group("body").splitlines()
            if re.match(r"^\|[ \t]*Status", line)]
    if len(rows) != 1:
        return None
    match = STATUS_ROW.fullmatch(rows[0])
    return match.group(1) if match is not None else None


def validate_selected_status(name: str, content: bytes) -> None:
    # This operational guide is not a Persona or a status-governed lesson.
    if not name.endswith(".md") or name == STUDENT_GUIDE:
        return
    body = content.decode("utf-8")
    if name == STATUSLESS_DOCUMENT:
        if re.search(r"Document\s+Info|\bStatus\b", body, re.IGNORECASE):
            raise ValueError(f"New or malformed document status needs review: {name}")
    elif name == ARCHIVED_DOCUMENT:
        if document_status(content) != "Draft":
            raise ValueError(f"Archive document status changed: {name}")
    elif name in STATUS_BEARING_DOCUMENTS:
        if document_status(content) not in {"Draft", "Approved"}:
            raise ValueError(f"Selected document status needs review: {name}")
    if name == ARCHIVED_DOCUMENT:
        archive_rows = [line for line in body.splitlines()
                        if re.match(r"^\|[ \t]*Status", line)]
        archive_statuses = [STATUS_ROW.fullmatch(line) for line in archive_rows]
        if len(archive_statuses) != 2 or any(row is None for row in archive_statuses) or [row.group(1) for row in archive_statuses] != ["Deprecated", "Draft"]:
            raise ValueError(f"Archive status changed: {name}")


def unlink_selected_exclusions(name: str, text: str) -> str:
    """Unlink only excluded targets identified during this selection."""
    excluded = EXCLUDED_LINKS.get(name, frozenset())

    def replace_link(match: re.Match[str]) -> str:
        target = urlsplit(match.group("target"))
        if target.scheme or target.netloc or not target.path:
            return match.group(0)
        linked = posixpath.normpath(
            posixpath.join(posixpath.dirname(name), unquote(target.path))
        )
        if linked in excluded:
            return match.group("label") + "（講師用正本の資料。配布対象外）"
        return match.group(0)

    return re.sub(r"\[(?P<label>[^\]\n]+)\]\((?P<target>[^)\n]+)\)", replace_link, text)


def distribution_copy(name: str, content: bytes) -> bytes:
    """Adapt five selected documents while keeping their source status."""
    if name not in EXCLUDED_LINKS:
        return content
    text = content.decode("utf-8")

    if name == "README.md":
        notice = (
            "このPrivate Templateには、講師が選択した教材と生徒用マニュアルを収録しています。"
            "講師用の内部文書やAIサービス変更情報は配布していません。"
            "各文書のDraft・Approved・Deprecated表示は元の状態のままです。"
            "配布手順は[生徒用マニュアル](docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md)を参照してください。"
        )
        if "</details>\n" not in text:
            raise ValueError("Distribution document info needs review: README.md")
        text = text.replace("</details>\n", "</details>\n\n" + notice + "\n", 1)
        expected_intro = "Persona本文と検証Evidenceを公開します。"
        if text.count(expected_intro) != 1:
            raise ValueError("Distribution introduction needs review: README.md")
        text = text.replace(expected_intro, "Persona本文と検証Evidenceを収録します。", 1)
        setup_intro = "設定案内専用Personaの定義本文は、S-SETUPに限り例外として管理します。"
        if text.count(setup_intro) != 1:
            raise ValueError("Distribution setup introduction needs review: README.md")
        text = text.replace(setup_intro, "", 1)
        structure = re.compile(
            r"(?<=## 5\. Structure（構成）\n\n)```text\n\.\n.*?\n```",
            re.DOTALL,
        )
        destination_tree = """```text
.
├── README.md                  本配布の入口・設計方針
├── LICENSE                    ライセンス
├── docs/
│   └── distribution/
│       └── STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md  生徒用の配布手順
└── personas/
    ├── PERSONA_IDENTIFICATION_AND_SETUP.md  識別・検証の共通仕様
    ├── WHY_PERSONA_MATTERS.md               詳細比較・検証例
    ├── AI_ISSUES_EVIDENCE.md                外部研究Evidence
    ├── SYCOPHANCY_CHALLENGER_PERSONAS.md    迎合研究の解説
    ├── assets/                              Evidence図表
    ├── education/                           GEM・SKILLS・選択済み旧資料
    └── reference/                           選択済み実務参考Persona・運用資料
```"""
        text, replacements = structure.subn(destination_tree, text, count=1)
        if replacements != 1:
            raise ValueError("Distribution structure needs review: README.md")

    elif name == "personas/reference/README.md":
        section = re.compile(
            r"## 4\.1 Verification Persona（検証専用Persona）\n\n.*?(?=## 4\.2 Draft Personas（提案中のPersona）)",
            re.DOTALL,
        )
        text, replacements = section.subn(
            "## 4.1 Verification Persona（検証専用Persona）\n\n検証専用Personaは、この配布には収録していません。中核4種のSSOT定義は変更しません。\n\n",
            text, count=1,
        )
        if replacements != 1:
            raise ValueError("Distribution navigation needs review: personas/reference/README.md")
        text = re.sub(
            r"(?m)^- \[`IT_EDUCATION_CONTENT_DESIGNER\.md`\]\(IT_EDUCATION_CONTENT_DESIGNER\.md\)：[^\n]*\n",
            "", text,
        )
        setup_link = "<br>[`PERSONA_SETUP_ADVISOR.md`](PERSONA_SETUP_ADVISOR.md)"
        if text.count(setup_link) != 1:
            raise ValueError("Distribution setup metadata needs review: personas/reference/README.md")
        text = text.replace(setup_link, "", 1)
        text, replacements = re.subn(
            r"(?m)^- \[`PERSONA_SETUP_ADVISOR\.md`\]\(PERSONA_SETUP_ADVISOR\.md\)：[^\n]*\n",
            "", text,
        )
        if replacements != 1:
            raise ValueError("Distribution setup navigation needs review: personas/reference/README.md")

    text = unlink_selected_exclusions(name, text)
    rendered = text.encode("utf-8")
    if document_status(content) != document_status(rendered):
        raise ValueError(f"Document status changed in distribution: {name}")
    return rendered


def reject_source_repository_urls(name: str, markdown: str) -> None:
    """Reject links and plain URLs to the instructor source after Private conversion."""
    for match in WEB_URL.finditer(markdown):
        raw = match.group(0).rstrip(".,;:!?。．、）］】」』|>")
        parsed = urlsplit(raw)
        host = (parsed.hostname or "").lower()
        if host not in {"github.com", "www.github.com", "raw.githubusercontent.com"}:
            continue
        segments = [unquote(part).lower() for part in parsed.path.split("/") if part]
        if segments[:2] != ["t-oikawa-sendai", "ai-setup-materials"]:
            continue
        raise ValueError(f"Source repository URL needs review: {name}")


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

    # Validate every source before touching the destination. Only the original
    # nine managed paths retain deletion permission; new selections must exist.
    plan: list[tuple[str, Path, bytes | None]] = []
    for source_name, destination_name in MANAGED:
        source_path = regular_file_or_absent(source, source_name)
        destination_path = regular_file_or_absent(destination, destination_name)
        content = source_path.read_bytes() if source_path.exists() else None
        if content is None and destination_name not in DELETE_ALLOWED:
            raise ValueError(f"Selected source is missing; deletion not approved: {source_name}")
        if content is not None:
            validate_selected_status(destination_name, content)
            source_status = document_status(content) if destination_name.endswith(".md") and destination_name != STUDENT_GUIDE else None
            if source_name.startswith("personas/education/GEM_") and not has_allowed_gem_document_info(content):
                raise ValueError(f"GEM Document Info needs review: {source_name}")
            if OBVIOUS_SECRET.search(content):
                raise ValueError(f"Possible credential in managed source: {source_name}")
            content = distribution_copy(destination_name, content)
            if destination_name.endswith(".md") and destination_name != STUDENT_GUIDE and document_status(content) != source_status:
                raise ValueError(f"Distribution status differs from source: {destination_name}")
            if OBVIOUS_SECRET.search(content):
                raise ValueError(f"Possible credential in distribution: {destination_name}")
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

    # A Markdown file may link only to another file that will actually be
    # present in this template. This prevents new links into excluded source docs.
    planned_content = {name: content for name, _, content in plan}
    for name, _, content in plan:
        if content is None or not name.endswith(".md"):
            continue
        markdown = content.decode("utf-8")
        reject_source_repository_urls(name, markdown)
        targets = re.findall(r"\]\(([^)\n]+)\)", markdown)
        targets += re.findall(r"<a\s+[^>]*?href\s*=\s*[\"']([^\"']+)[\"']", markdown, re.IGNORECASE)
        targets += re.findall(r"^\s*\[[^\]\n]+\]:\s*<?([^\s>]+)>?", markdown, re.MULTILINE)
        for raw_target in targets:
            target = urlsplit(raw_target)
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
