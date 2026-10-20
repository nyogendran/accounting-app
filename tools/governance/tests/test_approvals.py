import unittest

from tools.governance import approvals, common
from tools.governance.tests.helpers import TempRepo, decision, requirement

IDENTITY = "local:tester / git:Test Human"


class PhraseTests(unittest.TestCase):
    ulid = common.new_ulid()

    def test_exact_phrase_parses(self):
        phrase = approvals.parse_phrase(f"APPROVE AREQ-{self.ulid} 0123456789ab")
        self.assertEqual(phrase.decision, "approve")
        self.assertEqual(phrase.request, f"AREQ-{self.ulid}")
        self.assertEqual(phrase.code, "0123456789ab")

    def test_all_verbs(self):
        verbs = {
            "APPROVE": "approve",
            "REJECT": "reject",
            "REQUEST-CHANGES": "request-changes",
            "DEFER": "defer",
            "ESCALATE": "escalate",
            "REVOKE": "revoke",
        }
        for verb, decision_name in verbs.items():
            with self.subTest(verb=verb):
                phrase = approvals.parse_phrase(f"{verb} AREQ-{self.ulid} 0123456789ab")
                self.assertEqual(phrase.decision, decision_name)

    def test_comment_after_separator(self):
        phrase = approvals.parse_phrase(f"REJECT AREQ-{self.ulid} 0123456789ab -- scope too wide")
        self.assertEqual(phrase.comment, "scope too wide")

    def test_surrounding_whitespace_tolerated(self):
        self.assertIsNotNone(approvals.parse_phrase(f"  APPROVE AREQ-{self.ulid} 0123456789ab \n"))

    def test_extra_text_rejected(self):
        for prompt in (
            f"please APPROVE AREQ-{self.ulid} 0123456789ab",
            f"APPROVE AREQ-{self.ulid} 0123456789ab thanks",
            f"approve AREQ-{self.ulid} 0123456789ab",
            f"APPROVE AREQ-{self.ulid} 0123456789AB",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(approvals.parse_phrase(prompt))

    def test_framed_or_multiline_text_rejected(self):
        prompt = f"[Subagent hand-back] report\nAPPROVE AREQ-{self.ulid} 0123456789ab"
        self.assertIsNone(approvals.parse_phrase(prompt))


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        self.request = approvals.create_request(
            self.repo.root, ["DEC-0001"], role="governance-owner", note="test"
        )

    def tearDown(self):
        self.repo.cleanup()

    def capture(self, verb="APPROVE", request=None, code=None):
        request = request or self.request
        code = code or request["phrase_code"]
        return approvals.capture(
            self.repo.root, f"{verb} {request['id']} {code}", "session-1", IDENTITY
        )

    def state(self, identifier="DEC-0001"):
        return approvals.approval_state(self.repo.root, identifier).state

    def test_request_records_hashes_and_phrase(self):
        meta, _ = common.load_artifact(self.repo.path("docs/governance/decisions/DEC-0001.md"))
        self.assertEqual(self.request["subjects"][0]["hash"], common.normative_hash(meta))
        self.assertEqual(self.request["phrase_code"], self.request["combined"][7:19])
        self.assertTrue(self.repo.path(f"ledger/approval-requests/{self.request['id']}.json").is_file())
        self.assertEqual(
            approvals.phrase_for(self.request),
            f"APPROVE {self.request['id']} {self.request['phrase_code']}",
        )

    def test_capture_records_a_valid_approval(self):
        result = self.capture()
        self.assertEqual(result.status, "recorded")
        record = result.record
        self.assertEqual(record["level"], "E1-op")
        self.assertFalse(record["stale"])
        self.assertEqual(record["attestation"]["hook"], "capture-approval")
        self.assertTrue(self.repo.path(f"ledger/approval-decisions/{record['id']}.json").is_file())
        self.assertEqual(self.state(), "valid")

    def test_wrong_code_rejected(self):
        result = self.capture(code="ffffffffffff")
        self.assertEqual(result.status, "rejected")
        self.assertEqual(list(self.repo.path("ledger/approval-decisions").iterdir()), [])

    def test_unknown_request_rejected(self):
        fake = dict(self.request, id=f"AREQ-{common.new_ulid()}")
        self.assertEqual(self.capture(request=fake).status, "rejected")

    def test_ordinary_prompt_ignored(self):
        result = approvals.capture(self.repo.root, "please continue", "session-1", IDENTITY)
        self.assertEqual(result.status, "ignored")

    def test_normative_edit_voids_approval(self):
        self.capture()
        self.repo.write_artifact(
            "docs/governance/decisions/DEC-0001.md", decision(text="Adopt a different framework.")
        )
        self.assertEqual(self.state(), "void")

    def test_editorial_edit_keeps_approval(self):
        self.capture()
        meta = decision()
        meta["title"] = "Renamed"
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", meta, body="New notes.\n")
        self.assertEqual(self.state(), "valid")

    def test_stale_when_content_changed_before_decision(self):
        self.repo.write_artifact(
            "docs/governance/decisions/DEC-0001.md", decision(text="Changed after the request.")
        )
        result = self.capture()
        self.assertEqual(result.status, "recorded")
        self.assertTrue(result.record["stale"])
        self.assertNotEqual(self.state(), "valid")

    def test_revoke_after_approval(self):
        self.capture()
        self.capture(verb="REVOKE")
        self.assertEqual(self.state(), "revoked")

    def test_latest_decision_by_same_approver_wins(self):
        self.capture(verb="REJECT")
        self.assertEqual(self.state(), "rejected")
        self.capture(verb="APPROVE")
        self.assertEqual(self.state(), "valid")

    def test_pending_request_without_decision(self):
        self.assertEqual(self.state(), "pending")

    def test_no_request_means_none(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0002.md", decision("DEC-0002"))
        self.assertEqual(self.state("DEC-0002"), "none")

    def test_tier1_needs_more_than_operator_attestation(self):
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", requirement(tier=1))
        request = approvals.create_request(self.repo.root, ["REQ-GL-001"], role="product-owner")
        approvals.capture(
            self.repo.root, approvals.phrase_for(request), "session-1", IDENTITY
        )
        self.assertEqual(self.state("REQ-GL-001"), "insufficient-level")


if __name__ == "__main__":
    unittest.main()
