#!/usr/bin/env python3
# Program Name: test_student_distribution.py
# Language: Python
# Function: Check student-template distribution boundaries in a temporary repository.
# Created: 2026-11-09
# Last Updated: 2026-11-09
# Author: Takashi Oikawa
# AI: Cursor
# Memo: D-093. Standard-library unittest only. Do not write to the production student repository.

"""Tests for the thirty-path student distribution."""

from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "sync_student_template.py"
REFERENCE_README = "personas/reference/README.md"
MARKER = "KEEP_OUT_OF_DISTRIBUTION.txt"
EXISTING_SETUP = "personas/reference/PERSONA_SETUP_ADVISOR.md"
EXISTING_SETUP_TEXT = "existing-s-setup-not-managed\n"
EXCLUDED_LINKS = (
    "PERSONA_SETUP_ADVISOR.md",
    "IT_GENERAL_ADVISOR_TEST_PERSONA.md",
    "IT_EDUCATION_CONTENT_DESIGNER.md",
    "EMPLOYMENT_SUPPORT_ADVISOR.md",
)
EXPECTED_PATHS = frozenset({
    "README.md",
    "personas/education/README.md",
    "LICENSE",
    "docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md",
    "personas/education/GEM_CODE_GENERATOR.md",
    "personas/education/GEM_RESEARCHER_DEVELOPMENT.md",
    "personas/education/GEM_RESEARCHER_FULL.md",
    "personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md",
    "personas/education/GEM_REVIEWER.md",
    "personas/education/GEM_SOLUTION_PARTNER.md",
    "personas/WHY_PERSONA_MATTERS.md",
    "personas/AI_ISSUES_EVIDENCE.md",
    "personas/SYCOPHANCY_CHALLENGER_PERSONAS.md",
    "personas/assets/sycophancy_frontier_models_2026.png",
    "personas/PERSONA_IDENTIFICATION_AND_SETUP.md",
    "personas/education/SKILLS/CODE_GENERATOR.md",
    "personas/education/SKILLS/RESEARCHER_CAREER.md",
    "personas/education/SKILLS/RESEARCHER_DEVELOPMENT.md",
    "personas/education/SKILLS/RESEARCHER_LEARNING.md",
    "personas/education/SKILLS/REVIEWER.md",
    "personas/education/SKILLS/SOLUTION_PARTNER.md",
    "personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md",
    "personas/reference/README.md",
    "personas/reference/CHATGPT_PERSONA.md",
    "personas/reference/CLAUDE_PERSONA.md",
    "personas/reference/CURSOR_PERSONA.md",
    "personas/reference/GEMINI_PERSONA.md",
    "personas/reference/PERSONA_OPERATION_CASE_STUDY.md",
    "personas/reference/PERSONA_PROMPT_TEMPLATE.md",
    "personas/reference/CHAT_HANDOFF_TEMPLATE.md",
})
EXPECTED_DELETE = frozenset({
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
HEADING = re.compile(r"(?m)^## (?P<number>4\.[12])(?:[ \t]+[^\n]*)?[ \t]*$")
GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "Distribution Test",
    "GIT_AUTHOR_EMAIL": "distribution-test@example.com",
    "GIT_COMMITTER_NAME": "Distribution Test",
    "GIT_COMMITTER_EMAIL": "distribution-test@example.com",
}


def load_sync_module():
    spec = importlib.util.spec_from_file_location("sync_student_template", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SYNC = load_sync_module()


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def source_fingerprint() -> tuple[str, bytes, bytes]:
    status = run_git(ROOT, "status", "--porcelain")
    unstaged = subprocess.run(
        ["git", "-C", str(ROOT), "diff"],
        check=True,
        capture_output=True,
    ).stdout
    staged = subprocess.run(
        ["git", "-C", str(ROOT), "diff", "--cached"],
        check=True,
        capture_output=True,
    ).stdout
    return status, unstaged, staged


def run_sync(source: Path, destination: Path, dry_run: bool = False) -> subprocess.CompletedProcess[str]:
    if "OSLIB21-materials" in str(destination) or "ai-setup-materials-student" in str(destination):
        raise AssertionError(f"Refusing production destination: {destination}")
    command = [sys.executable, str(SCRIPT), str(source), str(destination)]
    if dry_run:
        command.append("--dry-run")
    return subprocess.run(command, capture_output=True, text=True)


def make_destination(root: Path) -> Path:
    destination = root / "student-repo"
    destination.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=destination, check=True, capture_output=True, text=True)
    (destination / MARKER).write_text("keep\n", encoding="utf-8", newline="\n")
    setup = destination / EXISTING_SETUP
    setup.parent.mkdir(parents=True, exist_ok=True)
    setup.write_text(EXISTING_SETUP_TEXT, encoding="utf-8", newline="\n")
    subprocess.run(["git", "add", "--", MARKER, EXISTING_SETUP], cwd=destination, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "-c", "commit.gpgsign=false", "commit", "-m", "test baseline"],
        cwd=destination,
        check=True,
        capture_output=True,
        text=True,
        env=GIT_ENV,
    )
    return destination


def copy_managed_source() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    temp = tempfile.TemporaryDirectory()
    source = Path(temp.name) / "source"
    for source_name, _destination_name in SYNC.MANAGED:
        target = source / source_name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / source_name, target)
    return temp, source


def replace_heading_text(text: str, number: str, title: str) -> str:
    matches = [match for match in HEADING.finditer(text) if match.group("number") == number]
    if len(matches) != 1:
        raise AssertionError(f"Expected one {number} heading, found {len(matches)}")
    match = matches[0]
    return text[:match.start()] + f"## {number} {title}" + text[match.end():]


def remove_heading(text: str, number: str) -> str:
    pattern = re.compile(rf"(?m)^## {re.escape(number)}(?:[ \t]+[^\n]*)?[ \t]*\n")
    updated, count = pattern.subn("", text, count=1)
    if count != 1:
        raise AssertionError(f"Could not remove {number}")
    return updated


def duplicate_heading(text: str, number: str) -> str:
    pattern = re.compile(rf"(?m)^## {re.escape(number)}(?:[ \t]+[^\n]*)?[ \t]*\n")
    match = pattern.search(text)
    if match is None:
        raise AssertionError(f"Could not duplicate {number}")
    return text[:match.end()] + match.group(0) + text[match.end():]


class StudentDistributionTest(unittest.TestCase):
    temp: tempfile.TemporaryDirectory[str]
    destination: Path
    source_state: tuple[str, bytes, bytes]

    @classmethod
    def setUpClass(cls) -> None:
        cls.source_state = source_fingerprint()
        cls.temp = tempfile.TemporaryDirectory()
        cls.destination = make_destination(Path(cls.temp.name))
        result = run_sync(ROOT, cls.destination, dry_run=False)
        if result.returncode != 0:
            raise AssertionError(result.stderr)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def tearDown(self) -> None:
        self.assertEqual(source_fingerprint(), self.source_state)

    def test_dry_run_succeeds_on_current_readme(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            destination = make_destination(Path(raw))
            result = run_sync(ROOT, destination, dry_run=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("add: personas/reference/README.md", result.stdout)
            self.assertFalse((destination / REFERENCE_README).exists())

    def test_heading_description_change_still_succeeds(self) -> None:
        temp, source = copy_managed_source()
        self.addCleanup(temp.cleanup)
        readme = source / REFERENCE_README
        text = readme.read_text(encoding="utf-8")
        text = replace_heading_text(text, "4.1", "Changed verification description")
        text = replace_heading_text(text, "4.2", "Changed following description")
        readme.write_text(text, encoding="utf-8", newline="\n")
        with tempfile.TemporaryDirectory() as raw:
            destination = make_destination(Path(raw))
            result = run_sync(source, destination, dry_run=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_or_duplicate_boundaries_fail(self) -> None:
        mutations = (
            ("missing-4.1", lambda text: remove_heading(text, "4.1")),
            ("missing-4.2", lambda text: remove_heading(text, "4.2")),
            ("duplicate-4.1", lambda text: duplicate_heading(text, "4.1")),
            ("duplicate-4.2", lambda text: duplicate_heading(text, "4.2")),
        )
        for name, mutate in mutations:
            with self.subTest(name=name):
                temp, source = copy_managed_source()
                self.addCleanup(temp.cleanup)
                readme = source / REFERENCE_README
                readme.write_text(mutate(readme.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
                with tempfile.TemporaryDirectory() as raw:
                    destination = make_destination(Path(raw))
                    result = run_sync(source, destination, dry_run=False)
                    status = run_git(destination, "status", "--porcelain")
                    self.assertNotEqual(result.returncode, 0, name)
                    self.assertIn(
                        "Distribution navigation needs review: personas/reference/README.md",
                        result.stderr,
                    )
                    self.assertEqual(status, "")
                    self.assertFalse((destination / REFERENCE_README).exists())

    def test_distributes_only_the_thirty_paths(self) -> None:
        self.assertEqual(frozenset(destination for _source, destination in SYNC.MANAGED), EXPECTED_PATHS)
        self.assertEqual(SYNC.DELETE_ALLOWED, EXPECTED_DELETE)
        staged = set(run_git(self.destination, "diff", "--cached", "--name-only").splitlines())
        self.assertEqual(staged, set(EXPECTED_PATHS))
        tracked = set(run_git(self.destination, "ls-files").splitlines())
        self.assertEqual(tracked, set(EXPECTED_PATHS) | {MARKER, EXISTING_SETUP})
        self.assertEqual((self.destination / MARKER).read_text(encoding="utf-8"), "keep\n")

    def test_excluded_persona_files_and_links_are_not_distributed(self) -> None:
        self.assertEqual((self.destination / EXISTING_SETUP).read_text(encoding="utf-8"), EXISTING_SETUP_TEXT)
        distributed = (self.destination / REFERENCE_README).read_text(encoding="utf-8")
        for name in EXCLUDED_LINKS:
            self.assertNotIn(f"]({name})", distributed)
            distributed_path = self.destination / "personas" / "reference" / name
            if name == "PERSONA_SETUP_ADVISOR.md":
                self.assertEqual(distributed_path.read_text(encoding="utf-8"), EXISTING_SETUP_TEXT)
            else:
                self.assertFalse(distributed_path.exists(), name)
        self.assertIn("検証専用Personaは、この配布には収録していません。", distributed)
        self.assertIn("## 4.2 Other Reference Personas（その他のReference Persona）", distributed)

    def test_source_status_is_preserved(self) -> None:
        for source_name, destination_name in SYNC.MANAGED:
            if not destination_name.endswith(".md") or destination_name == SYNC.STUDENT_GUIDE:
                continue
            source_status = SYNC.document_status((ROOT / source_name).read_bytes())
            distributed_status = SYNC.document_status((self.destination / destination_name).read_bytes())
            self.assertEqual(distributed_status, source_status, destination_name)

    def test_destination_changes_stay_in_temporary_repository(self) -> None:
        temporary_root = Path(self.temp.name).resolve()
        destination = self.destination.resolve()
        self.assertTrue(destination.is_relative_to(temporary_root))
        self.assertNotIn("OSLIB21-materials", str(destination))
        self.assertNotIn("ai-setup-materials-student", str(destination))
        self.assertEqual(source_fingerprint(), self.source_state)


if __name__ == "__main__":
    unittest.main()
