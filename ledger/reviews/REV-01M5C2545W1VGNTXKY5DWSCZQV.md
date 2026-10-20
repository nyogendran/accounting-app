---
id: REV-01M5C2545W1VGNTXKY5DWSCZQV
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: c449dc1b901abd84b4d3120bdf044fe60f088f5c
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      Clarification, not a regression. settings.json still lists
      `Bash(python tools/governance/run_tests.py)` in permissions.allow, so a reader could think
      finding 1 is only half-closed. It is not. The guard is a PreToolUse hook wired for every
      Bash/PowerShell/Write/Edit call with onFailure "block", and it runs independently of the
      permission allow-list. For an actor whose hook input carries agent_type (a subagent), the
      guard's _agent_shell rejects run_tests.py because it is no longer in the review-readonly or
      governance-readonly allow-lists. The settings.allow entry only suppresses the permission
      prompt for the main session (the orchestrator), which is the correct actor to record E3
      evidence. Confirmed by the passing test_agents_may_not_run_the_evidence_wrapper. No action
      needed; recorded so the settings.json line is not mistaken for a reopened hole.
    citation: >-
      .claude/settings.json:71 (allow) and .claude/settings.json:80-91 (guard PreToolUse,
      onFailure block) and .claude/hooks/agent-scopes.json:55-61 (review-readonly allow-list,
      run_tests removed) and .claude/hooks/guard.py:210-228 (_agent_shell), at c449dc1
  - severity: non-blocking
    text: >-
      The dry run exercises "two reviews" as presence, hash-binding and voiding, but not as a
      gate. approval_state() and the Specified derived state do not depend on reviews, and the test
      never calls trace.readiness(), so the approval step would still reach state "valid" even if
      the two reviews were absent. The reviews are still meaningfully tested: two at the current
      hash before the edit (assertEqual(len..., 2) and all at_current_hash), none at the current
      hash after the normative edit. The literal F0 criterion ("goes through ... two reviews") is
      met; a stronger dry run would also assert that trace.readiness reflects the two mandatory
      reviews. Non-blocking.
    citation: >-
      tools/governance/tests/test_dry_run.py:73-77 (two reviews, at current hash) and
      tools/governance/tests/test_dry_run.py:101 (none at current hash after edit) and
      tools/governance/trace.py:113 (Specified depends only on approval state), at c449dc1
  - severity: non-blocking
    text: >-
      The capture step's `assertEqual(result.returncode, 0, ...)` is weak on its own: the capture
      hook always exits 0, even when it records nothing (it never blocks a prompt). The assertion
      is adequately backed by assertIn("APR-", context) and assertEqual(approved["approval"].state,
      "valid"), which cannot both hold unless the real hook wrote a counting decision: the request
      id "AREQ-..." does not contain the substring "APR-", and approval_state returns "valid" only
      for a non-stale Stage 0 decision at the current hash. So the test is not vacuous. Recorded so
      a future editor keeps the two backing assertions if the returncode check is ever changed.
    citation: >-
      tools/governance/tests/test_dry_run.py:82-86 (returncode, APR- in context, state valid) and
      .claude/hooks/capture_approval.py:32-47 (hook always returns 0), at c449dc1
created_at: "2026-10-20"
---

# Gate 0 review of commit c449dc1 (finding 1 fix and the F0 dry run)

Independent E4 review for WF-01M5BJDGB5536WYT96GNTQWH4K step 8. Reviewed `git show c449dc1`
(parent 1a7c423 added only REV-01M5C0YAD8BAMX6HNTM9H4WC1E). HEAD is c449dc1 and the working tree is
clean, so the line numbers below are at c449dc1.

**Decision: finding 1 is closed and the new test demonstrates the F0 criterion, with no blocking
defect and no new defect introduced.** Three non-blocking observations are above. None of the Gate 0
escalation conditions is triggered: the change does not let an agent write outside its scope, approve
anything, write a decision record or edit a registered source, and it does not make the guard fail
open - it makes the guard strictly tighter. The human reviewer still decides.

## 1. Is finding 1 closed?

**Yes.** Finding 1 was that the review-readonly shell profile allowed
`python tools/governance/run_tests.py`, which writes an E3 evidence record under `ledger/evidence/`,
outside the reviewer's `ledger/reviews/**` write scope.

- The allow pattern no longer lists `run_tests`: it is now
  `^python3? tools/governance/(check|trace)\.py( .*)?$`
  (`.claude/hooks/agent-scopes.json:57`). `check.py` and `trace.py` are read-only (the only
  write-shaped token in check.py, line 146, is an f-string message; trace.py only prints).
- The agent prose was updated to match: the reviewer runs the suite with `python -m unittest`, and
  "Evidence records are written by the orchestrator's `run_tests.py`, which you cannot run"
  (`.claude/agents/code-security-reviewer.md:44-46`).
- The control is tightened, not weakened: the test that asserted run_tests.py was *allowed* was
  removed from `test_reviewer_may_run_the_repository_tests`, and a new failure-case test
  `test_agents_may_not_run_the_evidence_wrapper` asserts it is *blocked* for two agents
  (`tools/governance/tests/test_guard.py:293-297`). This is red-before-green: before the
  agent-scopes change, run_tests.py matched the review-readonly allow-list, so `assertFalse(allowed)`
  would have failed. I ran it: it passes now.

**Does any agent's shell profile still allow a command that writes outside that agent's write
scope? No.**

- `review-readonly` (code-security-reviewer) allows only check.py/trace.py, `python -m unittest`
  (the repo suite, which runs in throwaway temp repos and writes nothing to the real tree), git
  read-only subcommands, and rg/grep/ls/cat/head/tail/wc/find/sha256sum. None writes to the repo.
  `find` cannot write or execute: `-exec/-execdir/-ok/-okdir/-delete/-fprint*/-fprintf/-fls` are in
  `agent_shell_deny` (`agent-scopes.json:46`), and `>` redirection plus command substitution are
  blocked in `_agent_shell` (`guard.py:214-220`).
- `governance-readonly` (requirements-engineer, requirements-assurance, accounting-domain-expert,
  unknown_agent) allows only check.py/trace.py and git read-only subcommands. It never contained
  run_tests.py. None writes.

So after c449dc1 no agent shell profile can run a command that writes outside the agent's write
scope.

## 2. Does test_dry_run show the F0 criterion, and could it pass vacuously?

The criterion (SRC-005, section F, quoted in the test's module docstring): "A synthetic requirement
goes through drafting, two reviews and a hook-captured approval, and a normative edit then voids
it." Each part is covered, and the test is hermetic (a `TempRepo`, cleaned up; the real repo is not
touched).

- **Drafting:** writes a Proposed REQ-GL-001, asserts the checker is clean, approval state "none"
  and Specified "no" (`test_dry_run.py:66-71`).
- **Two reviews:** iterates the two mandatory reviewers for a requirement
  (`trace.MANDATORY_REVIEWERS["requirement"]`), each bound to the drafted hash, then asserts there
  are exactly two and all are at the current hash (`test_dry_run.py:73-77`). The `assertEqual(len,
  2)` prevents a vacuous zero-iteration pass. See non-blocking finding 2 on depth.
- **Hook-captured approval:** creates a real approval request, then runs the real UserPromptSubmit
  script `.claude/hooks/capture_approval.py` as a subprocess on the exact phrase
  `approvals.phrase_for(request)`, with CLAUDE_PROJECT_DIR set to the temp repo. It asserts the
  additionalContext contains "APR-" and that the approval state becomes "valid" and Specified "yes"
  (`test_dry_run.py:79-87`). This is a genuine end-to-end of the Stage 0 capture hook, not a stub.
- **Normative edit voids it:** rewrites the requirement at version 2 with an edited statement, then
  asserts the approval state is "void", Specified "no", no review is at the current hash, and the
  checker reports "approval state is 'void'" (`test_dry_run.py:93-102`).

**Could it pass vacuously? No.** The approval assertions require the hook to have written a counting
decision: state "valid" is returned only for a non-stale Stage 0 decision at the current hash, and
"APR-" is not a substring of the request id "AREQ-..." (so the context check is not satisfied by the
echoed request id). The void assertion requires a prior real approval - approval_state returns
"void" only when an earlier approved, non-stale decision exists whose request is no longer at the
current hash - so it cannot be reached without the capture step having succeeded first. The
commit's claim that a mutated copy with a wrong approval code fails is consistent with this: a wrong
code makes `capture()` return "rejected", no decision is written, and the state stays "pending", so
`assertEqual(... "valid")` fails. The only soft spot (returncode 0 alone) is non-blocking finding 3,
and it is backed by the two stronger assertions.

## 3. Verification run (observed)

- `python -m unittest discover -s tools/governance/tests -t .` -> `Ran 153 tests in 24.471s` `OK`.
  This matches the commit message ("153 tests pass") and the committed evidence record
  EVD-01M5C23M9DY7HGSVGN1PAKEMHW (tests_run 153, result pass).
- `python tools/governance/check.py` -> `check: 0 error(s), 0 warning(s)`.
- `python -m unittest tools.governance.tests.test_dry_run -v` -> 1 test, `OK` (ran, not skipped).
- `python -m unittest tools.governance.tests.test_guard -v -k evidence_wrapper` -> 1 test, `OK`
  (the new block test ran and passed).
- `python tools/governance/check.py --file ledger/reviews/REV-01M5C2545W1VGNTXKY5DWSCZQV.md` after
  writing this record (result in the handoff report).

No test was weakened, skipped or deleted to make the change pass: the suite grew by one end-to-end
test and one failure-case guard test, and the reviewer's allow-list was tightened.

## 4. The other three findings of REV-01M5C0YAD8BAMX6HNTM9H4WC1E

I agree with the orchestrator's dispositions, which concern the earlier review, not this commit.

- **Finding 2 (RISK-003):** I accept the correction. My original illustration
  (`D=ledger/approval-decisions; cp x $D/APR.json`) is in fact blocked, because the literal string
  `ledger/approval-decisions` appears in the assignment and is caught by the fragment check in
  `_references_protected` before `_tokens` ever drops the `$` token. The substance of the finding
  still holds: a path assembled so the protected literal never appears contiguously
  (`A=approval; cp x ledger/${A}-decisions/APR-X.json`) and a full-path command spelling
  (`/bin/rm -rf`) are allowed, because `_tokens` drops any `$` token and the rm deny pattern is
  anchored on the bare command word. Recording this as a known limitation under RISK-003, backstopped
  by the commit-time checks, is the right call for Gate 0.
- **Finding 3:** recording the neither-agent_type-nor-agent_id fail-open as a limitation is
  acceptable given three live smoke tests confirm agent_type is populated for subagents. A stricter
  default would remove the platform dependency but is not required for Gate 0.
- **Finding 4:** the convention-mitigated over-blocks (core.hooksPath reads, inline `-m` messages)
  are correctly recorded as a limitation; they are over-blocks, not fail-open holes.

## Defects the change could have introduced (checked, none found)

- **New write path for agents:** none - the change only removes an allow entry.
- **Broken reviewer workflow:** the reviewer still runs the suite via `python -m unittest` (allowed
  and confirmed by `test_reviewer_may_run_the_repository_tests`); evidence capture moves to the
  orchestrator, which is in scope.
- **The added EVD record:** machine-generated by run_tests.py, written and committed by the
  orchestrator (write scope `**`); head 1a7c423 is this commit's parent and tests_run 153 matches my
  run, so the evidence resolves.
- **test_dry_run side effects:** all writes (requirement, reviews, approval request/decision, the
  capture log) go to the temp repo via CLAUDE_PROJECT_DIR and are removed in tearDown; the real
  repository is untouched.
- **Guard fail-open:** none introduced; the guard is strictly tighter after this commit.
