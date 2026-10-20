import hashlib
import json
import unittest

from tools.governance import approvals, check, common
from tools.governance.tests.helpers import TempRepo, decision, requirement

IDENTITY = "local:tester / git:Test Human"
AGENT_EMAIL = "orchestrator@agents.tiqacc.invalid"


class CheckTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()

    def tearDown(self):
        self.repo.cleanup()

    def errors(self, **kwargs):
        return [f for f in check.run_checks(self.repo.root, **kwargs) if f.level == "error"]

    def warnings(self, **kwargs):
        return [f for f in check.run_checks(self.repo.root, **kwargs) if f.level == "warning"]

    def assertErrorMentions(self, text, **kwargs):
        messages = [f.message for f in self.errors(**kwargs)]
        self.assertTrue(any(text in m for m in messages), f"no error mentions {text!r}: {messages}")


class ArtifactRuleTests(CheckTestCase):
    def test_clean_repository_has_no_errors(self):
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", requirement())
        self.assertEqual(self.errors(), [])

    def test_missing_required_field(self):
        meta = requirement()
        del meta["owner"]
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", meta)
        self.assertErrorMentions("owner")

    def test_unknown_status(self):
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", requirement(status="Done"))
        self.assertErrorMentions("status")

    def test_id_must_match_type(self):
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", requirement(identifier="DEC-0001"))
        self.assertErrorMentions("DEC-0001")

    def test_duplicate_ids(self):
        self.repo.write_artifact("docs/requirements/a.md", requirement())
        self.repo.write_artifact("docs/requirements/b.md", requirement())
        self.assertErrorMentions("duplicate")

    def test_broken_link(self):
        self.repo.write_artifact(
            "docs/requirements/REQ-GL-001.md", requirement(links={"governed_by": ["POL-999"]})
        )
        self.assertErrorMentions("POL-999")

    def test_unknown_link_type(self):
        self.repo.write_artifact(
            "docs/requirements/REQ-GL-001.md", requirement(links={"depends": ["DEC-0001"]})
        )
        self.assertErrorMentions("depends")

    def test_clause_links_warn_until_clause_index_exists(self):
        self.repo.write_artifact(
            "docs/requirements/REQ-GL-001.md", requirement(links={"derives_from": ["S1-2.2.4-c01"]})
        )
        self.assertEqual(self.errors(), [])
        self.assertTrue(any("S1-2.2.4-c01" in w.message for w in self.warnings()))

    def test_normative_block_required_once_proposed(self):
        meta = requirement()
        del meta["normative"]
        self.repo.write_artifact("docs/requirements/REQ-GL-001.md", meta)
        self.assertErrorMentions("normative")

    def test_approved_without_decision_is_an_error(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision(status="Approved"))
        self.assertErrorMentions("Approved")

    def test_approved_with_valid_decision_passes(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        approvals.capture(self.repo.root, approvals.phrase_for(request), "s", IDENTITY)
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision(status="Approved"))
        self.assertEqual(self.errors(), [])

    def test_templates_are_not_checked(self):
        self.repo.write_text("docs/governance/templates/requirement.md", "---\nid: REQ-AREA-000\n---\n")
        self.assertEqual(self.errors(), [])


class RecordRuleTests(CheckTestCase):
    def test_decision_record_without_attestation(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        ulid = common.new_ulid()
        forged = {
            "id": f"APR-{ulid}",
            "type": "approval-decision",
            "request": request["id"],
            "decision": "approve",
            "subjects": request["subjects"],
            "combined": request["combined"],
            "stale": False,
            "by": {"role": "governance-owner", "identity": "agent"},
            "channel": "stage0-session",
            "level": "E1-op",
            "recorded_at": common.utc_now(),
        }
        common.write_json(self.repo.path(f"ledger/approval-decisions/APR-{ulid}.json"), forged)
        self.assertErrorMentions("attestation")

    def test_record_id_must_match_file_name(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        path = self.repo.path(f"ledger/approval-requests/{request['id']}.json")
        path.rename(path.with_name(f"AREQ-{common.new_ulid()}.json"))
        self.assertErrorMentions("file name")

    def test_request_role_must_exist(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        approvals.create_request(self.repo.root, ["DEC-0001"], role="chief-wizard")
        self.assertErrorMentions("chief-wizard")


class SourceRegisterTests(CheckTestCase):
    def register(self, digest):
        self.repo.write_text("requirement-doc/spec.txt", "the specification\n")
        self.repo.write_yaml(
            "docs/sources/source-register.yaml",
            {"version": 1, "sources": [{
                "id": "SRC-001",
                "title": "Spec",
                "files": [{"path": "requirement-doc/spec.txt", "sha256": digest}],
            }]},
        )

    def test_matching_hash_passes(self):
        self.register(hashlib.sha256(b"the specification\n").hexdigest())
        self.assertEqual(self.errors(), [])

    def test_hash_mismatch_is_an_error(self):
        self.register("0" * 64)
        self.assertErrorMentions("SHA-256")

    def test_source_ids_resolve_as_links(self):
        self.register(hashlib.sha256(b"the specification\n").hexdigest())
        self.repo.write_artifact(
            "docs/governance/decisions/DEC-0001.md", decision(links={"related": ["SRC-001"]})
        )
        self.assertEqual(self.errors(), [])


class ClaudeConfigTests(CheckTestCase):
    def agent(self, front):
        self.repo.write_text(".claude/agents/test-agent.md", f"---\n{front}---\n\nInstructions.\n")

    def test_valid_agent(self):
        self.agent("name: test-agent\ndescription: Does things.\ntools: Read, Grep\nmodel: inherit\n")
        self.assertEqual(self.errors(), [])

    def test_agent_without_tools(self):
        self.agent("name: test-agent\ndescription: Does things.\n")
        self.assertErrorMentions("tools")

    def test_agent_with_misspelled_key(self):
        self.agent("name: test-agent\ndescription: Does things.\ntool: Read\ntools: Read\n")
        self.assertErrorMentions("tool")

    def test_agent_may_not_spawn_agents(self):
        self.agent("name: test-agent\ndescription: Does things.\ntools: Read, Agent\n")
        self.assertErrorMentions("Agent")

    def test_agent_memory_is_not_allowed(self):
        self.agent("name: test-agent\ndescription: Does things.\ntools: Read\nmemory: project\n")
        self.assertErrorMentions("memory")

    def test_agent_name_must_match_file(self):
        self.agent("name: other-name\ndescription: Does things.\ntools: Read\n")
        self.assertErrorMentions("other-name")

    def test_skill_needs_description(self):
        self.repo.write_text(".claude/skills/demo/SKILL.md", "---\nname: demo\n---\n\nSteps.\n")
        self.assertErrorMentions("description")


class PreCommitTests(CheckTestCase):
    def setUp(self):
        super().setUp()
        self.repo.git_init()
        self.repo.write_text("ledger/reviews/REV-01JB0000000000000000000000.md", "x\n")
        self.repo.write_text("requirement-doc/spec.txt", "spec\n")
        self.repo.git("add", "-A")
        self.repo.git("commit", "-q", "-m", "base")

    def test_modifying_a_committed_record_is_blocked(self):
        self.repo.write_text("ledger/reviews/REV-01JB0000000000000000000000.md", "changed\n")
        self.repo.git("add", "-A")
        self.assertErrorMentions("never edited", pre_commit=True)

    def test_deleting_a_committed_record_is_blocked(self):
        self.repo.git("rm", "-q", "ledger/reviews/REV-01JB0000000000000000000000.md")
        self.assertErrorMentions("never edited", pre_commit=True)

    def test_new_record_is_allowed(self):
        self.repo.write_text("ledger/evidence/EVD-01JB0000000000000000000001.json", "{}\n")
        self.repo.git("add", "-A")
        messages = [f.message for f in self.errors(pre_commit=True)]
        self.assertFalse(any("never edited" in m for m in messages), messages)

    def test_modifying_a_protected_source_is_blocked(self):
        self.repo.write_text("requirement-doc/spec.txt", "edited spec\n")
        self.repo.git("add", "-A")
        self.assertErrorMentions("protected", pre_commit=True)

    def _decision_setup(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        return request

    def test_captured_decision_can_be_committed(self):
        request = self._decision_setup()
        approvals.capture(self.repo.root, approvals.phrase_for(request), "s", IDENTITY)
        self.repo.git("add", "-A")
        messages = [f.message for f in self.errors(pre_commit=True)]
        self.assertFalse(any("capture hook" in m for m in messages), messages)

    def test_decision_not_in_capture_log_is_blocked(self):
        request = self._decision_setup()
        result = approvals.capture(
            self.repo.root, approvals.phrase_for(request), "s", IDENTITY, log=False
        )
        self.assertEqual(result.status, "recorded")
        self.repo.git("add", "-A")
        self.assertErrorMentions("capture hook", pre_commit=True)

    def test_decision_altered_after_capture_is_blocked(self):
        request = self._decision_setup()
        result = approvals.capture(self.repo.root, approvals.phrase_for(request), "s", IDENTITY)
        path = self.repo.path(f"ledger/approval-decisions/{result.record['id']}.json")
        data = common.read_json(path)
        data["comment"] = "edited afterwards"
        common.write_json(path, data)
        self.repo.git("add", "-A")
        self.assertErrorMentions("capture hook", pre_commit=True)


class ReviewFindingTests(CheckTestCase):
    """Findings of the independent review (F0-6)."""

    def test_uncommitted_forged_decision_is_an_error_without_pre_commit(self):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        ulid = common.new_ulid()
        forged = {
            "id": f"APR-{ulid}",
            "type": "approval-decision",
            "request": request["id"],
            "decision": "approve",
            "subjects": request["subjects"],
            "combined": request["combined"],
            "stale": False,
            "by": {"role": "governance-owner", "identity": "forger"},
            "channel": "stage0-session",
            "level": "E1-op",
            "attestation": {"hook": "capture-approval", "session_id": "x", "prompt_sha256": "0" * 64},
            "recorded_at": common.utc_now(),
        }
        common.write_json(self.repo.path(f"ledger/approval-decisions/APR-{ulid}.json"), forged)
        self.assertErrorMentions("capture hook")

    def _decision_record(self, channel, level):
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", decision())
        request = approvals.create_request(self.repo.root, ["DEC-0001"], role="governance-owner")
        result = approvals.capture(self.repo.root, approvals.phrase_for(request), "s", IDENTITY)
        path = self.repo.path(f"ledger/approval-decisions/{result.record['id']}.json")
        data = common.read_json(path)
        data.update(channel=channel, level=level, source_event="event-1")
        common.write_json(path, data)

    def test_stage0_decision_must_be_operator_attested_level(self):
        self._decision_record("stage0-session", "E1")
        self.assertErrorMentions("E1-op")

    def test_git_host_decisions_rejected_before_stage1(self):
        self._decision_record("git-host", "E1")
        self.assertErrorMentions("Stage 1")

    def test_tier_required_for_normative_types(self):
        meta = decision()
        del meta["tier"]
        self.repo.write_artifact("docs/governance/decisions/DEC-0001.md", meta)
        self.assertErrorMentions("tier")


class PreCommitAdditionTests(CheckTestCase):
    def setUp(self):
        super().setUp()
        self.repo.git_init()
        self.repo.write_text("README.md", "x\n")
        self.repo.git("add", "-A")
        self.repo.git("commit", "-q", "-m", "base")

    def test_unregistered_file_added_to_a_protected_tree_is_blocked(self):
        self.repo.write_text("requirement-doc/annex-b.txt", "volumes\n")
        self.repo.git("add", "-A")
        self.assertErrorMentions("register", pre_commit=True)

    def test_registered_file_added_to_a_protected_tree_is_allowed(self):
        self.repo.write_text("requirement-doc/annex-b.txt", "volumes\n")
        self.repo.write_yaml(
            "docs/sources/source-register.yaml",
            {"version": 1, "sources": [{
                "id": "SRC-007",
                "title": "Annex B",
                "files": [{
                    "path": "requirement-doc/annex-b.txt",
                    "sha256": hashlib.sha256(b"volumes\n").hexdigest(),
                }],
            }]},
        )
        self.repo.git("add", "-A")
        messages = [f.message for f in self.errors(pre_commit=True)]
        self.assertFalse(any("register" in m for m in messages), messages)

    def test_capture_state_cannot_be_committed(self):
        self.repo.write_text(".claude/state/capture-log.jsonl", "{}\n")
        self.repo.git("add", "-f", ".claude/state/capture-log.jsonl")
        self.assertErrorMentions("protected", pre_commit=True)


class CommitMessageTests(CheckTestCase):
    def setUp(self):
        super().setUp()
        self.repo.git_init()
        self.repo.write_text("README.md", "x\n")
        self.repo.git("add", "-A")
        self.repo.git("commit", "-q", "-m", "base")

    def stage(self, relative):
        self.repo.write_text(relative, "content\n")
        self.repo.git("add", "-A")

    def message_errors(self, message, email):
        return [
            f for f in check.check_commit_message(self.repo.root, message, author_email=email)
            if f.level == "error"
        ]

    def test_agent_commit_needs_agent_trailer(self):
        self.stage("docs/requirements/REQ-GL-001.md")
        self.assertTrue(self.message_errors("feat: add requirement\n", AGENT_EMAIL))

    def test_unknown_agent_name_is_an_error(self):
        self.stage("docs/requirements/REQ-GL-001.md")
        self.assertTrue(self.message_errors("feat: x\n\nAgent: wizard\n", AGENT_EMAIL))

    def test_agent_commit_outside_scope_is_blocked(self):
        self.stage("docs/accounting/POL-001.md")
        errors = self.message_errors("feat: x\n\nAgent: requirements-engineer\n", AGENT_EMAIL)
        self.assertTrue(any("docs/accounting/POL-001.md" in f.message for f in errors))

    def test_agent_commit_inside_scope_passes(self):
        self.stage("docs/requirements/REQ-GL-001.md")
        self.assertEqual(self.message_errors("feat: x\n\nAgent: requirements-engineer\n", AGENT_EMAIL), [])

    def test_orchestrator_commit_passes(self):
        self.stage("docs/governance/project-state.md")
        self.assertEqual(self.message_errors("docs: x\n\nAgent: orchestrator\n", AGENT_EMAIL), [])

    def test_human_commit_must_not_claim_an_agent(self):
        self.stage("docs/governance/project-state.md")
        self.assertTrue(self.message_errors("docs: x\n\nAgent: orchestrator\n", "human@example.com"))

    def test_plain_human_commit_passes(self):
        self.stage("docs/governance/project-state.md")
        self.assertEqual(self.message_errors("docs: x\n", "human@example.com"), [])


if __name__ == "__main__":
    unittest.main()
