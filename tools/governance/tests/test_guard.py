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


def short_path(path):
    """Windows 8.3 short form of an existing path, or None where unavailable."""
    if os.name != "nt":
        return None
    import ctypes

    buffer = ctypes.create_unicode_buffer(32768)
    length = ctypes.windll.kernel32.GetShortPathNameW(str(path), buffer, 32768)
    return buffer.value if length else None


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

    def test_capture_log_is_protected(self):
        self.assertFalse(self.write(".claude/state/capture-log.jsonl").allowed)
        self.assertFalse(self.shell("echo {} >> .claude/state/capture-log.jsonl").allowed)

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

    def test_denied_subpath_message_names_the_deny_pattern(self):
        decision = self.write("docs/requirements/assurance/R.md", agent="requirements-engineer")
        self.assertIn("docs/requirements/assurance/**", decision.reason)

    def test_unknown_agent_cannot_write_in_repository(self):
        self.assertFalse(self.write("docs/notes.md", agent="general-purpose").allowed)

    def test_orchestrator_may_write_governance(self):
        self.assertTrue(self.write("docs/governance/project-state.md", tool="Edit").allowed)

    def test_orchestrator_may_write_outside_repository(self):
        outside = Path(tempfile.gettempdir()) / "tiqacc-outside.txt"
        self.assertTrue(self.decide("Write", {"file_path": str(outside)}).allowed)

    def test_agents_cannot_write_outside_repository(self):
        outside = Path(tempfile.gettempdir()) / "tiqacc-outside.txt"
        for agent in ("general-purpose", "requirements-engineer"):
            with self.subTest(agent=agent):
                self.assertFalse(self.decide("Write", {"file_path": str(outside)}, agent=agent).allowed)

    def test_network_paths_blocked(self):
        for path in ("\\\\localhost\\c$\\x.txt", "\\\\?\\UNC\\server\\share\\x.txt"):
            with self.subTest(path=path):
                self.assertFalse(self.decide("Write", {"file_path": path}).allowed)

    def test_git_internals_are_protected(self):
        self.assertFalse(self.write(".git/hooks/pre-commit").allowed)
        self.assertFalse(self.write(".git/config", tool="Edit").allowed)

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

    # Findings of the independent review (F0-6)

    def test_command_substitution_blocked_for_agents(self):
        for command in (
            "git show $(python bad.py)",
            "git diff `rm notes.md`",
            "git log ${HOME}",
            "git status & python bad.py",
            "python tools/governance/check.py & del notes.md",
            "git show @(Remove-Item x)",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="requirements-assurance").allowed)

    def test_git_output_options_blocked_for_agents(self):
        for command in ("git log --output=docs/x.md", "git diff --output docs/x.md", "git diff --ext-diff"):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="code-security-reviewer").allowed)

    # Findings of the code-security-reviewer smoke test (WF-01M5BJDGB5536WYT96GNTQWH4K step 7)

    def test_quoted_or_escaped_options_blocked_for_agents(self):
        for agent in ("requirements-engineer", "code-security-reviewer"):
            for command in (
                'git log -1 "--output=x"',
                "git log -1 '--output=x'",
                "git log -1 --outpu\\t=x",
                "git log -1 $'--output=x'",
                'git log -1 --out"put"=x',
                "git log -1 --out''put=x",
                "git log -1 {--output=x,}",
            ):
                with self.subTest(agent=agent, command=command):
                    self.assertFalse(self.shell(command, agent=agent).allowed)
        for command in ('find . "-delete"', 'find . "-exec" echo x', 'rg "--pre=cat" x'):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="code-security-reviewer").allowed)

    def test_options_that_run_programs_blocked_for_agents(self):
        for command in ("rg --hostname-bin=python x", "rg --hostname-bin python x"):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="code-security-reviewer").allowed)

    def test_agent_shell_paths_must_be_inside_repository(self):
        outside = Path(tempfile.gettempdir()) / "tiqacc-outside.txt"
        for command in (
            f"cat {outside.as_posix()}",
            "cat ~/notes.txt",
            "cat ../notes.txt",
            "head docs/../../notes.txt",
            f"git diff --no-index {outside.as_posix()} CLAUDE.md",
            "ls //server/share",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="code-security-reviewer").allowed)
        for command in (
            "git log 8e6a69a..fa9a669 -- docs",
            "git show HEAD~1:CLAUDE.md",
            "rg -n \"^def \" tools",
            "cat docs/governance/x.md",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command, agent="code-security-reviewer").allowed)

    def test_agents_read_only_inside_repository(self):
        outside = str(Path(tempfile.gettempdir()) / "tiqacc-outside.txt")
        inside = str(self.repo.path("docs/governance/x.md"))
        for tool, tool_input in (
            ("Read", {"file_path": outside}),
            ("Grep", {"pattern": "secret", "path": tempfile.gettempdir()}),
            ("Glob", {"pattern": "**/*", "path": tempfile.gettempdir()}),
            ("Glob", {"pattern": "../**/*.txt"}),
            ("Read", {"file_path": "\\\\server\\share\\x.txt"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertFalse(self.decide(tool, tool_input, agent="requirements-engineer").allowed)
        for tool, tool_input in (
            ("Read", {"file_path": inside}),
            ("Grep", {"pattern": "secret"}),
            ("Glob", {"pattern": "docs/**/*.md"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertTrue(self.decide(tool, tool_input, agent="requirements-engineer").allowed)
        self.assertTrue(self.decide("Read", {"file_path": outside}).allowed)

    def test_agent_glob_patterns_and_grep_filters_stay_inside_repository(self):
        # REV-01M5C44F4G2E9W08D7YH4587J3, finding 1: patterns that start with a wildcard were not checked.
        for tool, tool_input in (
            ("Glob", {"pattern": "**/../../*.txt"}),
            ("Glob", {"pattern": "*/../../x"}),
            ("Glob", {"pattern": "{/c/Users,docs}/**"}),
            ("Glob", {"pattern": "~/**"}),
            ("Glob", {"pattern": "**\\..\\..\\x"}),
            ("Grep", {"pattern": "x", "glob": "../../**"}),
            ("Grep", {"pattern": "x", "glob": "{C:/x,*.md}"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertFalse(self.decide(tool, tool_input, agent="requirements-engineer").allowed)
        for tool, tool_input in (
            ("Glob", {"pattern": "**/*.{md,yaml}"}),
            ("Glob", {"pattern": "docs/{requirements,accounting}/**/*.md"}),
            ("Grep", {"pattern": "x", "glob": "*.md"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertTrue(self.decide(tool, tool_input, agent="requirements-engineer").allowed)

    def test_agent_glob_syntax_that_could_form_an_escape_is_blocked(self):
        # REV-01M5C56YPY0TASJC9E84X1PWYS, finding 1: a brace, bracket, escape or extglob can form '..'
        # or a root without the pattern's text showing one.
        for tool, tool_input in (
            ("Glob", {"pattern": "[.][.]/*.txt"}),
            ("Glob", {"pattern": ".[.]/*.txt"}),
            ("Glob", {"pattern": "{.,x}./*.txt"}),
            ("Glob", {"pattern": ".{.,x}/*.txt"}),
            ("Glob", {"pattern": "{x,.}./*.txt"}),
            ("Glob", {"pattern": ".\\./*.txt"}),
            ("Glob", {"pattern": "+(.)/*.txt"}),
            ("Glob", {"pattern": "{,}/Windows/*"}),
            ("Glob", {"pattern": "{x,}/Windows/*"}),
            ("Glob", {"pattern": "{{,},x}/Windows/*"}),
            ("Glob", {"pattern": "[/]Windows/*"}),
            ("Grep", {"pattern": "x", "glob": "{.,x}./**"}),
            ("Grep", {"pattern": "x", "glob": "[.][.]/**"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertFalse(self.decide(tool, tool_input, agent="requirements-engineer").allowed)
        for tool, tool_input in (
            ("Glob", {"pattern": "{README,CHANGELOG}.md"}),
            ("Glob", {"pattern": "**/*.[ch]"}),
            ("Glob", {"pattern": "ledger/reviews/REV-*[0-9A-Z].md"}),
            ("Glob", {"pattern": ".claude/**/*.md"}),
            ("Grep", {"pattern": "x", "glob": "*.{md,yaml}"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertTrue(self.decide(tool, tool_input, agent="requirements-engineer").allowed)

    def test_agent_glob_root_drive_and_network_forms_blocked(self):
        # REV-01M5C56YPY0TASJC9E84X1PWYS, findings 2 and 3: forms already blocked, pinned. An absolute
        # pattern is blocked even inside the repository; agents use a relative pattern and the path.
        for pattern in (
            "\\\\server\\share\\**",
            "\\Windows\\**",
            "c:x*",
            "{ /x,docs}/**",
            f"{self.repo.root.as_posix()}/docs/**/*.md",
        ):
            with self.subTest(pattern=pattern):
                self.assertFalse(self.decide("Glob", {"pattern": pattern}, agent="requirements-engineer").allowed)
        inside_climb = {"pattern": "../CLAUDE.md", "path": str(self.repo.path("docs"))}
        self.assertFalse(self.decide("Glob", inside_climb, agent="requirements-engineer").allowed)

    def test_agent_glob_leading_dot_wildcards_and_shell_syntax_blocked(self):
        # REV-01M5C6QDYWRZJC39SDZ1FBJEKY, finding 1: a folder segment that starts with a dot and a
        # wildcard can match '..' in some matchers, and shell syntax can name a root or home folder.
        for pattern in (
            ".?/*.md",
            ".*/*.md",
            ".[!a]/*.md",
            ".[x.y]/*.md",
            ".{?,x}/*.md",
            "**/.*/x.md",
            "$HOME/**",
            "${HOME}/**",
            "''/Windows/*",
            "'.''.'/*.md",
            "$'\\x2e\\x2e'/*.md",
            "`pwd`/**",
        ):
            with self.subTest(pattern=pattern):
                self.assertFalse(self.decide("Glob", {"pattern": pattern}, agent="requirements-engineer").allowed)
        for pattern in ("**/.*", "**/.git*", "**/.*.md", "docs/**/.gitkeep"):
            with self.subTest(pattern=pattern):
                self.assertTrue(self.decide("Glob", {"pattern": pattern}, agent="requirements-engineer").allowed)

    def test_agent_glob_rule_alternatives_each_pinned(self):
        # REV-01M5C6QDYWRZJC39SDZ1FBJEKY, finding 4: each input is refused by one alternative only.
        # The delimited '..' of GLOB_ESCAPE is a subset of "two dots anywhere" and cannot be pinned alone.
        for pattern in (
            "{x,,y}/Windows/*",
            "[\\]Windows/*",
            "*..*/x",
            "[x.]/*.md",
            "{,x}/Windows/*",
            "@(.)/x",
            "*(x)/y",
            "?(x)/y",
            "!(x)/y",
            "*/C:/Windows/*",
        ):
            with self.subTest(pattern=pattern):
                self.assertFalse(self.decide("Glob", {"pattern": pattern}, agent="requirements-engineer").allowed)

    # Claude Code trims whitespace and a byte-order mark from tool paths and expands a leading '~'
    # (observed in 2.1.301 for Read, Write, Grep and Glob; WF-01M5BJDGB5536WYT96GNTQWH4K step 12a).

    def test_agent_padded_or_home_paths_are_judged_as_the_tool_resolves_them(self):
        outside = str(Path(tempfile.gettempdir()) / "tiqacc-outside.txt")
        for tool, tool_input in (
            ("Read", {"file_path": " " + outside}),
            ("Read", {"file_path": "\ufeff" + outside}),
            ("Read", {"file_path": "\t" + outside}),
            ("Read", {"file_path": "~/tiqacc-outside.txt"}),
            ("Read", {"file_path": "~\\tiqacc-outside.txt"}),
            ("Grep", {"pattern": "x", "path": " " + tempfile.gettempdir()}),
            ("Grep", {"pattern": "x", "path": "~"}),
            ("Glob", {"pattern": "*.txt", "path": " " + tempfile.gettempdir()}),
            ("Glob", {"pattern": "*.txt", "path": "~/"}),
            ("Glob", {"pattern": "\ufeff/Windows/*"}),
        ):
            with self.subTest(tool=tool, tool_input=tool_input):
                self.assertFalse(self.decide(tool, tool_input, agent="requirements-engineer").allowed)
        padded_inside = " " + str(self.repo.path("docs/governance/x.md"))
        self.assertTrue(self.decide("Read", {"file_path": padded_inside}, agent="requirements-engineer").allowed)

    def test_padded_paths_to_protected_files_and_records_blocked(self):
        self.repo.write_text("ledger/reviews/REV-A.md", "x\n")
        for relative, tool in (
            ("requirement-doc/spec.pdf", "Write"),
            ("ledger/approval-decisions/APR-X.json", "Write"),
            ("ledger/reviews/REV-A.md", "Edit"),
        ):
            path = str(self.repo.path(relative))
            for padded in (" " + path, "\ufeff" + path, path + " "):
                with self.subTest(tool=tool, path=padded):
                    self.assertFalse(self.decide(tool, {"file_path": padded}).allowed)

    def test_orchestrator_quoted_options_next_to_protected_paths_blocked(self):
        for command in (
            'find docs/sources/SRC-001-spec-v1 "-delete"',
            "find docs/sources/SRC-001-spec-v1 $'-delete'",
            'git log -1 "--output=ledger/approval-decisions/APR-X.json"',
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_orchestrator_quoted_push_blocked(self):
        for command in ('git "push"', "git 'push' origin main", 'git p"ush"'):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_extended_length_path_is_recognised(self):
        path = "\\\\?\\" + str(self.repo.path("ledger/approval-decisions/APR-X.json")).replace("/", "\\")
        self.assertFalse(self.decide("Write", {"file_path": path}).allowed)

    def test_short_name_path_is_recognised(self):
        long_dir = self.repo.path("ledger/approval-decisions")
        short_dir = short_path(long_dir)
        if not short_dir or Path(short_dir).name.lower() == long_dir.name.lower():
            self.skipTest("8.3 short names are not available on this volume")
        self.assertFalse(self.decide("Write", {"file_path": short_dir + "\\APR-X.json"}).allowed)
        relative_short = "ledger/" + Path(short_dir).name
        self.assertFalse(self.shell(f"cp x.json {relative_short}/APR-X.json").allowed)

    def test_orchestrator_interpreter_writes_to_protected_paths_blocked(self):
        for command, tool in (
            ("py -c \"open('ledger/approval-decisions/APR-X.json','w')\"", "Bash"),
            ("python forge.py ledger/approval-decisions/APR-X.json", "Bash"),
            ("node -e \"require('fs').writeFileSync('requirement-doc/x','y')\"", "Bash"),
            ("[IO.File]::WriteAllText('.claude/state/capture-log.jsonl','x')", "PowerShell"),
            ("install -m 644 x requirement-doc/x.pdf", "Bash"),
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, tool=tool).allowed)

    def test_orchestrator_reads_of_protected_paths_allowed(self):
        for command in (
            "ls ledger/approval-decisions",
            "cat requirement-doc/notes.txt",
            "git log --oneline -- requirement-doc",
            "sha256sum docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt",
            "python tools/governance/approvals.py status DEC-0001",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command).allowed)

    def test_orchestrator_recursive_delete_variants_blocked(self):
        for command, tool in (
            ("rm -r docs", "Bash"),
            ("rm -R docs", "Bash"),
            ("rm --recursive docs", "Bash"),
            ("Remove-Item docs -Recurse", "PowerShell"),
            ("ri docs -Recurse", "PowerShell"),
            ("rd docs -Recurse -Force", "PowerShell"),
            ("del docs -Recurse", "PowerShell"),
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, tool=tool).allowed)

    def test_orchestrator_push_and_approval_variants_blocked(self):
        for command in (
            "git -C . push origin master",
            "git -c user.name=\"A B\" push",
            "bash -c \"git push\"",
            "git push",
            "gh api repos/o/r/pulls/1/reviews -f event=APPROVE",
            "gh api -X PUT repos/o/r/pulls/1/merge",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_agents_cannot_change_directory_or_run_code_of_their_choice(self):
        for command in (
            "cd C:/Users",
            "python -m unittest discover -s ledger/reviews -p *.py",
            "python -m unittest discover -s C:/Temp",
            "find . -name x -exec rm {} +",
            "find . -delete",
            "rg --pre cat pattern",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command, agent="code-security-reviewer").allowed)

    def test_reviewer_may_run_the_repository_tests(self):
        for command in (
            "python -m unittest discover -s tools/governance/tests -t .",
            "python -m unittest tools.governance.tests.test_guard -v",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command, agent="code-security-reviewer").allowed)

    def test_agents_may_not_run_the_evidence_wrapper(self):
        # run_tests.py writes an evidence record under ledger/evidence/, outside every agent's scope.
        for agent in ("code-security-reviewer", "requirements-assurance"):
            with self.subTest(agent=agent):
                self.assertFalse(self.shell("python tools/governance/run_tests.py", agent=agent).allowed)

    def test_orchestrator_relative_and_disguised_protected_paths_blocked(self):
        for command in (
            "cd ledger && echo x > approval-decisions/APR-X.json",
            "cp x.json ledger/./approval-decisions/APR-X.json",
            "cp x.json ledger./approval-decisions/APR-X.json",
            "cp x.json 'ledger/'approval-decisions/APR-X.json",
            "cp x.json ledger/approval-decisions",
            "cp x.json ledger/approval-*/",
            "ls requirement-doc | xargs rm",
            "cat requirement-doc/a.txt $(cp b requirement-doc/a.txt)",
            "cat requirement-doc/a.txt > requirement-doc/b.txt",
            "cd requirement-doc",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_orchestrator_git_flow_and_reads_allowed(self):
        for command in (
            "git add ledger/approval-decisions/APR-X.json",
            "git commit -m \"Record the Gate 0 decision in ledger/approval-decisions\"",
            "git diff HEAD~1 -- requirement-doc",
            "cat requirement-doc/a.txt > notes.txt",
            "ls requirement-doc | sort",
            "python -m unittest discover -s tools/governance/tests -t .",
            "echo done > notes.txt",
            "git -c user.name=\"TIQACC Orchestrator (Claude)\" -c user.email=\"orchestrator@agents.tiqacc.invalid\" "
            "commit -q -F C:/Users/x/scratchpad/commit-message.txt",
            "python tools/governance/approvals.py request --subject GATE-0 --subject DEC-0001 --role governance-owner",
        ):
            with self.subTest(command=command):
                self.assertTrue(self.shell(command).allowed)

    def test_orchestrator_cannot_bypass_git_hooks(self):
        for command in (
            "git commit --no-verify -m x",
            "git commit -n -m x",
            "git config core.hooksPath /dev/null",
            "git -c core.hooksPath=x commit -m y",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.shell(command).allowed)

    def test_subagent_without_agent_type_is_restricted(self):
        payload = {
            "hook_event_name": "PreToolUse",
            "tool_name": "Write",
            "tool_input": {"file_path": str(self.repo.path("docs/notes.md"))},
            "cwd": str(self.repo.root),
            "agent_id": "agent-123",
        }
        self.assertFalse(self.guard.decide(payload, self.repo.root).allowed)

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
