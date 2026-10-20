import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.tests.helpers import REPO_ROOT, TempRepo

GUARD_PATH = REPO_ROOT / ".claude/hooks/guard.py"


def load_guard():
    spec = importlib.util.spec_from_file_location("tiqacc_guard", GUARD_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["tiqacc_guard"] = module
    spec.loader.exec_module(module)
    return module


class GuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guard = load_guard()

    def setUp(self):
        self.repo = TempRepo()

    def tearDown(self):
        self.repo.cleanup()

    def decide(self, tool, tool_input, agent=None):
        payload = {
            "hook_event_name": "PreToolUse",
            "tool_name": tool,
            "tool_input": tool_input,
            "cwd": str(self.repo.root),
        }
        if agent:
            payload["agent_type"] = agent
        return self.guard.decide(payload, self.repo.root)

    def write(self, relative, agent=None, tool="Write"):
        return self.decide(tool, {"file_path": str(self.repo.path(relative))}, agent)

    def shell(self, command, agent=None, tool="Bash"):
        return self.decide(tool, {"command": command}, agent)

    # File writes

    def test_protected_source_blocked_for_orchestrator(self):
        self.assertFalse(self.write("requirement-doc/spec.pdf", tool="Edit").allowed)

    def test_windows_backslash_path_is_normalised(self):
        path = str(self.repo.path("docs/sources/SRC-001-spec-v1/x.txt")).replace("/", "\\")
        self.assertFalse(self.decide("Write", {"file_path": path}).allowed)

    def test_decision_records_blocked_for_everyone(self):
        self.assertFalse(self.write("ledger/approval-decisions/APR-X.json").allowed)
        self.assertFalse(
            self.write("ledger/approval-decisions/APR-X.json", agent="requirements-assurance").allowed
        )

    def test_existing_record_cannot_be_rewritten(self):
        self.repo.write_text("ledger/reviews/REV-A.md", "x\n")
        self.assertFalse(self.write("ledger/reviews/REV-A.md").allowed)
        self.assertFalse(self.write("ledger/reviews/REV-A.md", tool="Edit").allowed)

    def test_new_record_in_scope_allowed(self):
        self.assertTrue(self.write("ledger/reviews/REV-B.md", agent="requirements-assurance").allowed)

    def test_agent_inside_scope_allowed(self):
        self.assertTrue(self.write("docs/requirements/REQ-GL-001.md", agent="requirements-engineer").allowed)

    def test_agent_outside_scope_blocked(self):
        decision = self.write("docs/accounting/POL-001.md", agent="requirements-engineer")
        self.assertFalse(decision.allowed)
        self.assertIn("requirements-engineer", decision.reason)

    def test_agent_denied_subpath_blocked(self):
        self.assertFalse(
            self.write("docs/requirements/assurance/R.md", agent="requirements-engineer").allowed
        )

    def test_unknown_agent_cannot_write_in_repository(self):
        self.assertFalse(self.write("docs/notes.md", agent="general-purpose").allowed)

    def test_orchestrator_may_write_governance(self):
        self.assertTrue(self.write("docs/governance/project-state.md", tool="Edit").allowed)

    def test_paths_outside_repository_not_governed(self):
        outside = Path(tempfile.gettempdir()) / "tiqacc-outside.txt"
        self.assertTrue(
            self.decide("Write", {"file_path": str(outside)}, agent="general-purpose").allowed
        )

    def test_notebook_path_is_checked(self):
        decision = self.decide(
            "NotebookEdit", {"notebook_path": str(self.repo.path("requirement-doc/n.ipynb"))}
        )
        self.assertFalse(decision.allowed)

    # Shell commands

    def test_readonly_agent_allowlist(self):
        for command in (
            "python tools/governance/check.py",
            "python tools/governance/trace.py explain REQ-GL-001",
            "git log -3 --oneline",
            "git diff HEAD~1 2>&1",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command, agent="requirements-assurance").allowed)

    def test_readonly_agent_cannot_write_through_shell(self):
        for command in (
            "echo x > docs/requirements/a.md",
            "python tools/governance/check.py && rm notes.md",
            "cp a.md docs/requirements/b.md",
            "python -c \"open('x','w')\"",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="requirements-engineer").allowed)

    def test_powershell_is_handled(self):
        self.assertFalse(
            self.shell("Set-Content docs/x.md 'a'", agent="requirements-assurance", tool="PowerShell").allowed
        )

    def test_orchestrator_push_and_force_blocked(self):
        for command in (
            "git push origin master",
            "git push --force",
            "git reset --hard HEAD~1",
            "rm -rf docs",
            "gh pr review 1 --approve",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_orchestrator_shell_write_to_protected_paths_blocked(self):
        for command in (
            "cp x.pdf requirement-doc/spec.pdf",
            "echo {} > ledger/approval-decisions/APR-X.json",
            "sed -i s/a/b/ docs/sources/SRC-003-kickoff-analysis/k.md",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_orchestrator_normal_shell_allowed(self):
        for command in (
            "python tools/governance/check.py",
            "git status --short",
            "ls ledger/approval-decisions",
            "python tools/governance/approvals.py request --subject DEC-0001 --role governance-owner",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command).allowed)

    # Process behaviour

    def run_hook(self, stdin_text):
        env = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.repo.root))
        return subprocess.run(
            [sys.executable, str(GUARD_PATH)],
            input=stdin_text,
            capture_output=True,
            text=True,
            env=env,
        )

    def test_blocked_call_exits_2_with_reason(self):
        payload = {
            "hook_event_name": "PreToolUse",
            "tool_name": "Edit",
            "tool_input": {"file_path": str(self.repo.path("requirement-doc/spec.pdf"))},
            "cwd": str(self.repo.root),
        }
        result = self.run_hook(json.dumps(payload))
        self.assertEqual(result.returncode, 2)
        self.assertIn("protected", result.stderr)

    def test_allowed_call_exits_0(self):
        payload = {
            "hook_event_name": "PreToolUse",
            "tool_name": "Read",
            "tool_input": {"file_path": str(self.repo.path("docs/x.md"))},
            "cwd": str(self.repo.root),
        }
        self.assertEqual(self.run_hook(json.dumps(payload)).returncode, 0)

    def test_malformed_input_fails_closed(self):
        self.assertEqual(self.run_hook("this is not json").returncode, 2)


if __name__ == "__main__":
    unittest.main()
