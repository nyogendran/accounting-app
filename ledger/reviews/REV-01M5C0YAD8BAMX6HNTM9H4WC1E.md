---
id: REV-01M5C0YAD8BAMX6HNTM9H4WC1E
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: fa9a669687d6c38bcdce6d08a5426da4eee56b80
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      Scope-control gap (pre-existing, not introduced by these commits). The code-security-reviewer
      shell profile still permits `python tools/governance/run_tests.py`, which writes an E3 evidence
      record to ledger/evidence/EVD-<ulid>.json. The reviewer's write scope is ledger/reviews/ only.
      The PreToolUse guard cannot block this, because the write happens inside the interpreter, not
      through a Write/Edit tool call that the guard sees. A reviewer agent can therefore create an
      evidence record outside its declared scope. Impact is limited: run_tests.py writes only
      machine-generated content from a real test run (not arbitrary/forgeable text), EVD is not a
      decision or approval and does not count toward tier gating, and committing it is still governed
      by the pre-commit checks. Recommend removing run_tests.py from the review-readonly allow-list
      (reviewers can use `python -m unittest discover -s tools/governance/tests -t .`, which writes
      nothing) or reconciling the reviewer's write scope with it. This is why the brief directed me to
      avoid run_tests.py.
    citation: >-
      tools/governance/run_tests.py:78-79 (writes ledger/evidence EVD) and
      .claude/hooks/agent-scopes.json:57 (review-readonly allows run_tests.py) and
      .claude/agents/code-security-reviewer.md:44, at fa9a669
  - severity: non-blocking
    text: >-
      Residual limits of the orchestrator shell guard (already accepted as RISK-003, not a new
      defect). The protected-path analysis is text-based: _tokens() drops any token containing `$`, so
      a protected write assembled from a shell variable (for example D=ledger/approval-decisions; cp x
      $D/APR.json) is not seen as touching a protected path and is allowed. The recursive-delete and
      other deny patterns are anchored on the bare command word, so a full-path spelling such as
      /bin/rm -rf is not matched. These are backstopped by the commit-time checks (check_staged and the
      capture-log match), which read actual staged content rather than parsing shell text, and the
      guard is explicitly documented as a guardrail, not a security boundary. Worth recording as a
      known limitation; no action required for Gate 0.
    citation: >-
      .claude/hooks/guard.py:119-128 (_tokens drops $ tokens) and
      .claude/hooks/agent-scopes.json:72 (rm deny anchored on the command word), at fa9a669
  - severity: non-blocking
    text: >-
      Defensive-default observation. The actor is resolved as agent_type, or "unknown" when agent_id
      is present but agent_type is absent, else None (orchestrator). If a subagent ever supplied
      neither agent_type nor agent_id, it would be treated as the orchestrator (fail-open for an
      unidentified agent). The brief records that agent_type is present in live subagent hook input, so
      this is theoretical, but a stricter default (treat any Task/subagent context without a known
      agent as "unknown") would remove the dependency on the platform always populating one of the two
      fields.
    citation: ".claude/hooks/guard.py:269, at fa9a669"
  - severity: non-blocking
    text: >-
      Minor over-block / false-positive surface, mitigated by the git commit -F convention. The
      orchestrator deny list matches core.hooksPath case-insensitively anywhere in the command, so even
      a harmless read such as `git config --get core.hooksPath` is blocked; and the commit -n and
      --force patterns can match flag-like tokens inside an inline -m message. CLAUDE.md and the tests
      establish that commit messages are passed with `git commit -F <file>`, which avoids this, and the
      regressed-in test suite confirms the real -F commit flow is allowed. No change required; noted so
      a future editor does not treat these as bugs.
    citation: >-
      .claude/hooks/agent-scopes.json:68-69 (core.hooksPath and commit -n deny patterns), at fa9a669
created_at: "2026-10-20"
---

# Gate 0 re-review of the F0-6 fixes (commits d0d422d, 658ed21, fa9a669)

Independent E4 re-review for WF-01M5BJDGB5536WYT96GNTQWH4K step 4. Reviewed the full diff
`git diff 8e6a69a fa9a669` (HEAD = fa9a669, working tree clean, so line numbers below are at
fa9a669). Decision: the three commits **close every listed finding and gap without introducing a
blocking defect.** Four non-blocking observations are recorded above; none lets an agent approve,
write a decision record, edit a registered source, or makes the guard fail open, so the Gate 0
escalation conditions are **not** triggered. The human reviewer still decides.

## Verification run

- `python -m unittest discover -s tools/governance/tests -t .` -> `Ran 151 tests ... OK`.
- `python tools/governance/check.py` -> `check: 0 error(s), 0 warning(s)`.
- `python -m unittest tools.governance.tests.test_guard -v` -> 40 tests OK; the 8.3 short-name test
  (`test_short_name_path_is_recognised`) **ran** on this volume (not skipped), as did the
  extended-length, network-path and git-internals tests.
- `python tools/governance/check.py --file ledger/reviews/REV-01M5C0YAD8BAMX6HNTM9H4WC1E.md` after
  writing this record (result in the handoff report).

No test was weakened, skipped or deleted to pass; the suite grew (new failure-case tests were added
for each finding, and the commit messages state they failed before the fix).

## Finding-by-finding closure (citations at fa9a669)

Original independent-review findings 1-9:

1. **Closed.** Command substitution / background / here-docs blocked for agents by AGENT_FORBIDDEN
   and the `>` check in `_agent_shell`. guard.py:43, guard.py:214-220; test_guard.py:196-206.
2. **Closed.** 8.3 short names and `\\?\` extended-length prefixes resolve via `os.path.realpath` in
   `canonical_path`, compared in `repo_relative`. common.py:160-197; test_guard.py (extended-length,
   short-name), test_common.py RepoRelativeTests.
3. **Closed.** The orchestrator approach inverted to fail-closed: a command touching a protected path
   must match the READ_ONLY allow-list, else it is blocked. Interpreter writes (`py -c`, `node -e`,
   `install`) are blocked. guard.py:49-62, guard.py:231-258; test_guard.py
   (interpreter_writes_to_protected_paths_blocked).
4. **Closed / handled.** `agent_type` is used, with an `agent_id`->"unknown" fallback.
   guard.py:269; test_guard.py:333-344 (see non-blocking note 3 above).
5. **Closed.** `check_capture_log` now errors (not warns) on an uncommitted Stage 0 decision absent
   from the capture log. check.py:226-248; test_check.py
   (uncommitted_forged_decision_is_an_error_without_pre_commit).
6. **Closed.** Added files under a protected path are checked by `_check_new_protected` in
   `check_staged`. check.py:411-454; test_check.py PreCommitAdditionTests.
7. **Closed.** Deny list now covers PowerShell delete aliases, `git -C . push`, `-c ... push`,
   `bash -c "git push"`, and `gh api .../reviews|/merge` plus GraphQL mutation names.
   agent-scopes.json:64-76; test_guard.py (push_and_approval_variants, recursive_delete_variants).
8. **Closed.** `effective_tier` treats missing/invalid tier as Tier 1; TIERED_TYPES = NORMATIVE_TYPES
   so decision/adr/change-request/gate must declare a tier. approvals.py:48-51, approvals.py:216,
   common.py:53; test_approvals.py (tierless_artifact_is_treated_as_tier1), test_check.py
   (tier_required_for_normative_types).
9. **Closed.** Guard docstring and RISK-003 now state the guard is a guardrail, not a security
   boundary, with the mitigation chain. guard.py:17-20; risk-register.yaml:24-41.

Additional gaps found while fixing:

- **Agents writing outside the repository: Closed.** `_decide_write` blocks an agent when the path is
  outside the repo. guard.py:193-194; test_guard.py:116-120.
- **cd / unittest discover -s <any> / find -exec / rg --pre: Closed.** `cd` removed from the profiles;
  the unittest allow pattern is pinned to the repo suite; `agent_shell_deny` blocks `--pre` and
  find's writing/executing actions. agent-scopes.json:41-47, agent-scopes.json:58;
  test_guard.py (cannot_change_directory_or_run_code_of_their_choice, reviewer_may_run_the_repository_tests).
- **Skipping git hooks / editing .git: Closed.** Deny patterns for `--no-verify`, `core.hooksPath` and
  `commit -n`; `.git/**` added to protected paths (guard and settings). agent-scopes.json:10,
  agent-scopes.json:67-69, settings.json:9; test_guard.py (cannot_bypass_git_hooks,
  git_internals_are_protected).
- **Hand-made E1 / git-host decision passing Tier 1: Closed.** `approval_state` counts only
  `stage0-session` (ACCEPTED_CHANNELS); the checker forces Stage 0 to E1-op and rejects `git-host`
  until Stage 1 (matches DEC-0003). approvals.py:45, approvals.py:233-235; check.py:200-205;
  test_approvals.py (git_host_decisions_are_not_counted_before_stage1,
  stage0_decision_claiming_e1_is_treated_as_e1_op).

658ed21 claims:

- **Review may name a full commit hash that exists: Closed.** REV subjects accept `commit`, validated
  by `_commit_exists` (40-hex + `git cat-file -e <sha>^{commit}`). check.py:212-217, check.py:346-350;
  test_check.py (review_of_a_commit_is_valid, unknown/short hash errors). Template updated
  (review.md).
- **Workflow written once; checker requires title and steps: Closed.** WF branch requires type/title/
  steps; the delegate skill no longer says "update" the record. check.py:222-223;
  skills/delegate/SKILL.md:11-13; test_check.py (workflow_record_needs_title_and_steps).

fa9a669 smoke-test findings:

- **R2 (deny message names the pattern): Closed.** `_decide_write` reports the matching deny
  pattern(s). guard.py:204-206; test_guard.py:102-104.
- **OQ-1 (Markdown without front matter / id no longer silently skipped; registered sources exempt):
  Closed.** `load_index` records a problem for any governed Markdown under docs/ lacking front matter
  or `id`, except files listed in the source register; docs/sources/ and templates/ are already
  excluded by `artifact_paths`. Verified against the live repo: SRC-002
  (docs/architecture/01-strategic-architecture-discovery.md) is registered and exempt, and
  `check.py` reports 0 errors. common.py:444-463, common.py:354, conventions.md:39-44; test_check.py
  (markdown_without_front_matter_is_an_error, front_matter_without_id_is_an_error,
  registered_source_without_front_matter_passes).

## Defects the changes could have introduced (checked, none blocking)

- **Bypasses of the orchestrator protected-path analysis:** the read-only-allow-list design is
  fail-closed for recognised write commands; residual text-analysis gaps (shell variables, full-path
  command spellings) remain and are backstopped at commit time and covered by RISK-003 (non-blocking
  note 2).
- **False positives on normal work:** confirmed allowed by the suite and by inspection -
  `git commit -F <file>` (incl. the `git -c ... commit -q -F <path>` form), `git add` of a captured
  decision, running the tests, `python tools/governance/approvals.py request ...`, reads of protected
  paths, and orchestrator edits of governed Markdown. No regression.
- **Regex mistakes in agent-scopes.json:** reviewed each deny/allow pattern; the only effects are the
  minor, convention-mitigated over-blocks in non-blocking note 4.
- **Guard fail-open:** all exceptions exit 2 (fail closed); unknown/unidentified agents get an empty
  write scope and the governance-readonly profile. The one theoretical fail-open (neither agent_type
  nor agent_id) is non-blocking note 3.
- **Slow path resolution / network lookups:** UNC paths are returned unresolved and write-blocked;
  glob expansion is capped (500) and working-directory discovery is capped (16). No network lookup on
  the hot path.
- **New front-matter rule:** does not reject templates or registered sources and does not miss a
  non-front-matter Markdown file under docs/; verified by `check.py` (0 errors) over the 25 docs
  Markdown files.
