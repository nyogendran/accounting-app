import json
import os
import subprocess
import sys
import unittest

from tools.governance import approvals
from tools.governance.tests.helpers import REPO_ROOT, TempRepo, decision

HOOK_PATH = REPO_ROOT / ".claude/hooks/capture_approval.py"


class CaptureHookTests(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        self.request = approvals.create_request(
            self.repo.root, ["DEC-0001"], role="governance-owner"
        )

    def tearDown(self):
        self.repo.cleanup()

    def run_hook(self, prompt):
        payload = {
            "hook_event_name": "UserPromptSubmit",
            "prompt": prompt,
            "session_id": "session-1",
            "cwd": str(self.repo.root),
        }
        env = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.repo.root))
        return subprocess.run(
            [sys.executable, str(HOOK_PATH)],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            env=env,
        )

    def decisions(self):
        return sorted(self.repo.path("ledger/approval-decisions").glob("APR-*.json"))

    def test_phrase_records_decision_and_reports_context(self):
        result = self.run_hook(approvals.phrase_for(self.request))
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        context = output["hookSpecificOutput"]["additionalContext"]
        self.assertIn("APR-", context)
        self.assertEqual(len(self.decisions()), 1)

    def test_ordinary_prompt_has_no_output(self):
        result = self.run_hook("please continue with F0")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")
        self.assertEqual(self.decisions(), [])

    def test_framed_report_is_ignored(self):
        prompt = "[Subagent hand-back] report text\n" + approvals.phrase_for(self.request)
        result = self.run_hook(prompt)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.decisions(), [])

    def test_rejected_phrase_explains_without_recording(self):
        bad = f"APPROVE {self.request['id']} ffffffffffff"
        result = self.run_hook(bad)
        self.assertEqual(result.returncode, 0)
        self.assertIn("not recorded", json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"])
        self.assertEqual(self.decisions(), [])

    def test_capture_log_is_written(self):
        self.run_hook(approvals.phrase_for(self.request))
        log = self.repo.path(".claude/state/capture-log.jsonl").read_text(encoding="utf-8")
        self.assertIn(self.decisions()[0].stem, log)


if __name__ == "__main__":
    unittest.main()
