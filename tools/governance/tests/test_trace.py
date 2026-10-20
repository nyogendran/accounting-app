import unittest

from tools.governance import approvals, common, trace
from tools.governance.tests.helpers import TempRepo, requirement, story

IDENTITY = "local:tester / git:Test Human"


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", requirement())
        self.repo.write_artifact(
            "docs/requirements/US-GL-001.md", story(links={"refines": ["REQ-GL-001"]})
        )

    def tearDown(self):
        self.repo.cleanup()

    def current_hash(self, identifier="US-GL-001"):
        index = common.load_index(self.repo.root)
        return common.normative_hash(index.artifacts[identifier].meta)

    def approve(self, identifier="US-GL-001", role="product-owner"):
        request = approvals.create_request(self.repo.root, [identifier], role=role)
        approvals.capture(self.repo.root, approvals.phrase_for(request), "s", IDENTITY)

    def review(self, reviewer, digest=None, verdict="pass", identifier="US-GL-001"):
        ulid = common.new_ulid()
        meta = {
            "id": f"REV-{ulid}",
            "type": "review",
            "reviewer": reviewer,
            "level": "E4",
            "subjects": [{"id": identifier, "hash": digest or self.current_hash(identifier)}],
            "verdict": verdict,
            "findings": [],
            "created_at": common.utc_now(),
        }
        self.repo.write_artifact(f"ledger/reviews/REV-{ulid}.md", meta, body="Review notes.\n")

    def conditions(self, identifier="US-GL-001"):
        result = trace.readiness(common.load_index(self.repo.root), identifier)
        return result, {c.name: c.ok for c in result.conditions}

    def test_explain_reports_links_and_approval_state(self):
        text = trace.render_explain(trace.explain(common.load_index(self.repo.root), "US-GL-001"))
        self.assertIn("REQ-GL-001", text)
        self.assertIn("approval: none", text)

    def test_explain_lists_downstream_links(self):
        text = trace.render_explain(trace.explain(common.load_index(self.repo.root), "REQ-GL-001"))
        self.assertIn("US-GL-001", text)

    def test_not_ready_without_approval_or_reviews(self):
        result, conditions = self.conditions()
        self.assertFalse(result.ready)
        self.assertFalse(conditions["approved at current hash"])
        self.assertFalse(conditions["mandatory reviews at current hash"])

    def test_ready_when_all_conditions_hold(self):
        self.review("requirements-assurance")
        self.review("accounting-domain-expert")
        self.approve()
        result, conditions = self.conditions()
        self.assertTrue(result.ready, conditions)

    def test_review_on_an_old_hash_does_not_count(self):
        self.review("requirements-assurance", digest="sha256:" + "0" * 64)
        self.review("accounting-domain-expert")
        self.approve()
        _, conditions = self.conditions()
        self.assertFalse(conditions["mandatory reviews at current hash"])

    def test_blocking_review_finding_fails_readiness(self):
        self.review("requirements-assurance", verdict="blocking-findings")
        self.review("accounting-domain-expert")
        self.approve()
        _, conditions = self.conditions()
        self.assertFalse(conditions["mandatory reviews at current hash"])

    def test_missing_planned_test_fails_readiness(self):
        self.repo.write_artifact(
            "docs/requirements/US-GL-001.md",
            story(planned_tests=(), links={"refines": ["REQ-GL-001"]}),
        )
        _, conditions = self.conditions()
        self.assertFalse(conditions["every acceptance criterion has a planned test"])

    def test_blocking_question_fails_readiness(self):
        self.repo.write_artifact(
            "docs/governance/questions/Q-001.md",
            {
                "id": "Q-001",
                "type": "question",
                "title": "Rounding rule",
                "status": "Proposed",
                "version": 1,
                "owner": "orchestrator",
                "links": {"blocks": ["US-GL-001"]},
            },
        )
        _, conditions = self.conditions()
        self.assertFalse(conditions["no open blocking question or issue"])

    def test_coverage_counts_artifacts(self):
        summary = trace.coverage(common.load_index(self.repo.root))
        self.assertEqual(summary["by_type"]["requirement"], 1)
        self.assertEqual(summary["by_type"]["story"], 1)


if __name__ == "__main__":
    unittest.main()
