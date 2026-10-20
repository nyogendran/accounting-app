"""F0 acceptance dry run on synthetic data (SRC-005, section F, F0).

"A synthetic requirement goes through drafting, two reviews and a hook-captured approval, and a
normative edit then voids it." The approval is captured by running the real UserPromptSubmit hook
script on the exact phrase, in a throwaway repository.
"""
import json
import os
import subprocess
import sys
import unittest

from tools.governance import approvals, check, common, trace
from tools.governance.tests.helpers import REPO_ROOT, TempRepo, requirement

HOOK_PATH = REPO_ROOT / ".claude/hooks/capture_approval.py"
REQUIREMENT = "docs/requirements/REQ-GL-001.md"


class SyntheticRequirementDryRun(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()

    def tearDown(self):
        self.repo.cleanup()

    def explain(self):
        return trace.explain(common.load_index(self.repo.root), "REQ-GL-001")

    def errors(self):
        return [f.message for f in check.run_checks(self.repo.root) if f.level == "error"]

    def readiness(self):
        result = trace.readiness(common.load_index(self.repo.root), "REQ-GL-001")
        return result.ready, {condition.name: condition.ok for condition in result.conditions}

    def review(self, reviewer, digest):
        ulid = common.new_ulid()
        self.repo.write_artifact(
            f"ledger/reviews/REV-{ulid}.md",
            {
                "id": f"REV-{ulid}",
                "type": "review",
                "reviewer": reviewer,
                "level": "E4",
                "subjects": [{"id": "REQ-GL-001", "hash": digest}],
                "verdict": "pass",
                "findings": [],
                "created_at": common.utc_now(),
            },
        )

    def run_hook(self, prompt):
        payload = {
            "hook_event_name": "UserPromptSubmit",
            "prompt": prompt,
            "session_id": "dry-run",
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

    def test_draft_review_capture_then_normative_edit_voids(self):
        # Drafting: a Proposed requirement passes the checker but is not specified.
        self.repo.write_artifact(REQUIREMENT, requirement())
        self.assertEqual(self.errors(), [])
        drafted = self.explain()
        self.assertEqual(drafted["approval"].state, "none")
        self.assertEqual(drafted["derived"]["Specified"], "no")
        self.assertFalse(self.readiness()[1]["mandatory reviews at current hash"])

        # Two independent reviews, bound to the current normative hash.
        for reviewer in trace.MANDATORY_REVIEWERS["requirement"]:
            self.review(reviewer, drafted["hash"])
        self.assertEqual(len(self.explain()["reviews"]), 2)
        self.assertTrue(all(review["at_current_hash"] for review in self.explain()["reviews"]))
        ready, conditions = self.readiness()
        self.assertTrue(conditions["mandatory reviews at current hash"])
        self.assertFalse(ready)  # not yet approved

        # The person's exact phrase, captured by the real hook script.
        request = approvals.create_request(self.repo.root, ["REQ-GL-001"], role="product-owner")
        result = self.run_hook(approvals.phrase_for(request))
        self.assertEqual(result.returncode, 0, result.stderr)
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("APR-", context)
        approved = self.explain()
        self.assertEqual(approved["approval"].state, "valid")
        self.assertEqual(approved["derived"]["Specified"], "yes")
        self.assertTrue(self.readiness()[0])

        # Only now may the status say Approved.
        self.repo.write_artifact(REQUIREMENT, requirement(status="Approved"))
        self.assertEqual(self.errors(), [])

        # A normative edit voids the approval and the reviews, and Approved is no longer accepted.
        edited_statement = "When a journal is approved, the system shall post it to the ledger (edited)."
        self.repo.write_artifact(
            REQUIREMENT, requirement(status="Approved", statement=edited_statement, version=2)
        )
        edited = self.explain()
        self.assertEqual(edited["approval"].state, "void")
        self.assertEqual(edited["derived"]["Specified"], "no")
        self.assertFalse(any(review["at_current_hash"] for review in edited["reviews"]))
        ready, conditions = self.readiness()
        self.assertFalse(ready)
        self.assertFalse(conditions["approved at current hash"])
        self.assertFalse(conditions["mandatory reviews at current hash"])
        self.assertTrue(any("approval state is 'void'" in message for message in self.errors()))


if __name__ == "__main__":
    unittest.main()
