---
id: REV-01M5C56YPY0TASJC9E84X1PWYS
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 0272342d71b2b76253bd40c4b61bfd34c540eca9
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      Residual of the same class as finding 1 of REV-01M5C44F4G2E9W08D7YH4587J3, unconfirmed. The
      new check is a deny-list over the text of the pattern, not a check of what the pattern expands
      to. GLOB_ESCAPE recognises a parent segment only where two adjacent dots are delimited by the
      start or end of the pattern, "/", "{", "}" or ",". Glob syntax can also form a path segment
      from a brace alternative joined to the text next to it, from a bracket expression, or from a
      backslash escape where a matcher treats "\" as an escape rather than a separator. The guard
      neither expands nor rejects these constructs, and the literal-prefix check stops at the first
      wildcard, bracket or brace, so the change does not show that no expansion of an allowed
      pattern contains a ".." segment. Whether the Claude Code Glob tool expands such a pattern into
      a parent traversal is not documented in the repository, and I ran no live Glob or Grep probe,
      so the effect is unconfirmed, as it was for the original finding. If confirmed, the exposure
      is file names outside the repository listed by Glob, not their contents: Read is resolved by
      path, and Grep's glob only filters files under its search path, which is resolved.
      Recommendation: make the agent check fail closed by expanding brace alternatives (with a cap)
      and applying the segment test to every expansion, and by blocking bracket expressions and
      escapes that can produce a dot, or by allowing only a known set of pattern shapes; add tests
      built from each construct that fail before the fix.
    citation: >-
      .claude/hooks/guard.py:48 (GLOB_ESCAPE; a ".." segment is matched only as two literal adjacent
      dots), .claude/hooks/guard.py:249-251 (the only inspection of the Glob pattern and the Grep
      glob; no expansion) and .claude/hooks/guard.py:253-257 (the literal prefix ends at the first
      * ? [ or {), at 0272342; `rg --help` lines 586-589, observed in this review: "-g GLOB,
      --glob=GLOB Include or exclude files and directories for searching that match the given glob"
  - severity: non-blocking
    text: >-
      New fail-safe over-block. Because any ":" and any leading "/" now block, an agent Glob pattern
      written as an absolute path inside the repository is refused, for example
      C:/yogi/tiq-accounting-app/docs/**/*.md (alternative B, the colon) or the Git Bash form
      /c/yogi/tiq-accounting-app/docs/**/*.md (alternative A, the leading "/"). So is a ".." segment
      that stays inside the repository, for example pattern ../CLAUDE.md with path
      C:/yogi/tiq-accounting-app/docs (alternative C). At the parent 5892c0f all three were allowed,
      because their literal prefix resolved inside the repository through canonical_path. The block
      message says the pattern "leaves" the repository, which is wrong for these cases. It fails
      closed, and agents can use a relative pattern with a path argument instead, so this is a
      usability limitation, not a hole. Record it with the other limitations, or resolve an absolute
      literal prefix inside the repository before applying the escape test.
    citation: >-
      .claude/hooks/guard.py:48 (alternatives A and B) and .claude/hooks/guard.py:249-251 (the block
      runs before the candidate checks at :252-266), at 0272342; tools/governance/common.py:174-182
      (canonical_path maps the /c/... and drive forms that the parent's prefix check relied on), at
      0272342
  - severity: non-blocking
    text: >-
      Test coverage of the new rule is partial. The new test pins the seven cases named in the
      commit message and three allowed patterns, and its blocked cases would have failed at the
      parent (see the body). These forms, which the regex blocks, have no test: a network pattern
      written with backslashes (\\server\share\**), a root-relative backslash pattern (\Windows\**),
      a drive-relative pattern with no slash (c:x*), a brace alternative with leading whitespace
      ({ /x,docs}/**), and an absolute pattern inside the repository (finding 2, which should be
      pinned as intended behaviour or fixed). A later edit to GLOB_ESCAPE could drop any of them
      without a failing test. No test was weakened, skipped or deleted.
    citation: >-
      tools/governance/tests/test_guard.py:279-298 at 0272342; `git show --stat 0272342`
      (test_guard.py 21 insertions, guard.py 9 insertions, no deletions)
  - severity: non-blocking
    text: >-
      The orchestrator's dispositions of REV-01M5C44F4G2E9W08D7YH4587J3 findings 2 to 4 (recorded as
      limitations) do not resolve to an artifact yet. No file at 0272342 records them; there is no
      ledger/workflows/ folder, so no workflow record for WF-01M5BJDGB5536WYT96GNTQWH4K exists yet;
      and the RISK-003 mitigation still says the guard blocks agent reads outside the repository
      without naming the textual Glob-pattern residual (finding 1 above) or the glued-option
      residual. I agree with all three dispositions on the merits (see the body). Record them, for
      example in the workflow record or the RISK-003 residual, so the Gate 0 brief can cite them.
    citation: >-
      docs/governance/risk-register.yaml:35-44 at 0272342; docs/governance/conventions.md:95
      (workflow records live in ledger/workflows/); a repository search at 0272342 for the
      dispositions and for WF-01M5BJDGB5536WYT96GNTQWH4K found only the three review records in
      ledger/reviews/
created_at: "2026-10-20"
---

# Gate 0 review of commit 0272342 (fix for REV-01M5C44F4G2E9W08D7YH4587J3, finding 1)

This is an independent E4 review for WF-01M5BJDGB5536WYT96GNTQWH4K step 11. I reviewed
`git show 0272342` against its parent 5892c0f. HEAD was 0272342 and the working tree was clean, so
the `path:line` citations below are valid at 0272342.

**Decision: finding 1 is closed for every vector it named and every vector in the brief: Glob
patterns that begin with a wildcard, brace alternatives, Windows backslashes and drive letters, and
Grep's `glob`. The change only adds a block path ahead of the unchanged checks, so it is strictly
tighter than its parent and fails closed. A narrower residual of the same class remains and is
unconfirmed (finding 1 above): the check reads the pattern's text and does not consider constructs
that can form a `..` segment without two literal adjacent dots. Verdict: non-blocking-findings.** No
Gate 0 escalation condition is confirmed. The human reviewer still decides.

## Verification (observed)

- `python -m unittest discover -s tools/governance/tests -t .` gave `Ran 160 tests in 36.344s` and
  `OK`. This matches the commit message ("160 tests pass").
- `python tools/governance/check.py` gave `check: 0 error(s), 0 warning(s)`.
- `python -m unittest tools.governance.tests.test_guard -v -k test_agent_glob_patterns_and_grep_filters_stay_inside_repository`:
  the new test ran and passed (`ok`).
- `git diff --stat 6fb17248d1497e85d698787e4072fb7c9eb3a667 0272342` lists only
  `ledger/evidence/EVD-01M5C56J4F50JB6PEQ73MV6ND6.json`. The tree that EVD-01M5C56J4F50JB6PEQ73MV6ND6
  tested is therefore the committed code.
- `python tools/governance/check.py --file ledger/reviews/REV-01M5C56YPY0TASJC9E84X1PWYS.md` was run
  after writing this record; the result is in the handoff report.

Limits: my shell profile cannot run ad hoc Python. Verdicts below on patterns that the test does not
contain come from reading `guard.py:48` and `:246-266`, not from running them. I ran no live Glob or
Grep probe of the guard.

## How the fix works

`_decide_read` now collects Glob's `pattern` and, when given, Grep's `glob` (`guard.py:246-248`). It
turns backslashes into slashes and blocks on any `GLOB_ESCAPE` match (`:249-251`), before the
unchanged checks of `path`, `file_path` and the Glob literal prefix (`:252-266`). `GLOB_ESCAPE`
(`:48`) has three alternatives:

- A: at the start, or just after `{` or `,`, optional whitespace followed by `/`, `~`, or a drive
  letter and colon;
- B: any colon;
- C: `..` with the start, `/`, `{` or `,` before it, and the end, `/`, `}` or `,` after it.

Read tools reach `_decide_read` only for agents (`:339-340`). The hook matcher includes Read, Grep
and Glob (`.claude/settings.json:82`), and any exception exits 2 (`guard.py:349-356`). The new code
adds no exception path.

## Finding 1 of REV-01M5C44F4G2E9W08D7YH4587J3: closed for the named vectors

| Vector | Pattern | Result | Why | Test |
| --- | --- | --- | --- | --- |
| Starts with a wildcard | `**/../../*.txt`, `*/../../x` | blocked | C | test_guard.py:282-283 |
| Ends in a parent segment | `**/..` | blocked | C (end) | by reading |
| Brace alternative at a root | `{/c/Users,docs}/**` | blocked | A after `{` | :284 |
| Brace alternative climbing | `{docs,..}/x`, `{..,docs}/x` | blocked | C | by reading |
| Brace alternative with whitespace | `{ /x,docs}/**` | blocked | A (`\s*`) | by reading |
| Home folder | `~/**`, `{docs,~}/x` | blocked | A | :285 (first only) |
| Windows backslashes | `**\..\..\x` | blocked | becomes `**/../../x`, C | :286 |
| Network path | `\\server\share\**` | blocked | becomes `//server/...`, A | by reading |
| Root-relative backslash | `\Windows\**` | blocked | A | by reading |
| Drive letters | `C:/x/**`, `C:\x\**`, `c:x*`, `\\?\C:\x` | blocked | B (and A) | by reading |
| Grep `glob` climbing | `../../**` | blocked | C | :287 |
| Grep `glob` drive in a brace | `{C:/x,*.md}` | blocked | A and B | :288 |

Before the change, the wildcard-, brace- and Grep-led forms were allowed: an empty literal prefix
added no candidate (`:253-257`), and the Grep `glob` was not read at all. Grep's `pattern`, the
search regex, is still not inspected. That is correct, because it is content, not a path.

## Ordinary agent patterns (false positives)

These are allowed, by reading `:48` and the candidate checks at `:252-266`:

- `**/*.md`: starts with `*` and has no `{`, `,`, colon or `..` segment. The empty literal prefix
  adds no candidate.
- `docs/**/*.{md,yaml}`: after `{` comes `m` and after `,` comes `y`; neither is `/`, `~`, or a
  letter followed by a colon. There is no colon or `..`, and the literal prefix `docs/` resolves
  inside the repository. The test pins the same brace shape (`**/*.{md,yaml}`, test_guard.py:293).
- `*.py`: the same reasoning as `**/*.md`.
- `tools/governance/tests/test_*.py`: nothing triggers, and the literal prefix
  `tools/governance/tests/test_` resolves inside the repository.
- Also allowed: `.claude/**` (a single dot does not match C), `docs/{requirements,accounting}/**/*.md`
  (:294) and the Grep `glob` `*.md` (:295).

These are blocked although they stay inside the repository (finding 2 above):
`C:/yogi/tiq-accounting-app/docs/**/*.md` (B), `/c/yogi/tiq-accounting-app/docs/**/*.md` (A), and
`../CLAUDE.md` with `path` `C:/yogi/tiq-accounting-app/docs` (C). The parent allowed each of them.

## The remaining residual (finding 1 above)

The fix lists the spellings of an escape that can appear in the pattern's text. A glob pattern is
expanded or matched by the tool, though, and glob syntax can also form a segment through brace
alternation, bracket expressions and escapes. A deny-list of literal spellings therefore fails open
for any spelling it does not list, which is the same design property as the original finding, now
over a smaller remainder. I did not build or run an exact input. Confirming one would mean driving
the Glob tool against the guard that confines me, which is outside my brief.

There are two ways to settle this without that. The guard's author can add unit tests against
`decide()` for each construct, which needs no tool call. The orchestrator can find out, in a
temporary directory, whether the Glob tool expands such constructs into a parent traversal. Until
then this is a non-blocking residual under RISK-003, like the original finding: the guard is a
guardrail, not a boundary (`guard.py:19-21`), and the exposure is file names, not contents.

## Claims in the commit message and evidence

- "Tests first: seven blocked cases failed before the change; the three allowed cases passed before
  and after." This is consistent with the parent's code, by reading. The diff to `guard.py` is
  additions only (+9, -0), so at 5892c0f `_decide_read` ran only the candidate checks now at
  `:252-266`. The six wildcard-, brace- and Grep-led cases add no candidate there. `~/**` gives the
  prefix `~/`, which `canonical_path` does not expand: it has no home expansion and joins
  non-absolute text to the base (`tools/governance/common.py:160-182`). The prefix therefore
  resolved inside the repository and the pattern was allowed. The three allowed cases pass with
  either version. I did not re-run the test at the parent, because my profile cannot check it out.
- "160 tests pass": observed (above).
- EVD-01M5C56J4F50JB6PEQ73MV6ND6 has `tests_run` 160, `result` pass and `exit_code` 0. Its `head`
  is 5892c0f, the parent, as expected for evidence captured before the commit. `clean: false` is
  expected because the changes were not yet committed. Its `tree` is the committed tree apart from
  the evidence file (above).
- No test was weakened, skipped or deleted: `test_guard.py` is +21, -0.
- Conformance: the `Agent: orchestrator` and `Evidence:` trailers and the `[F0-6]` tag are
  present. There is one authoring agent and one commit.

## Dispositions of REV-01M5C44F4G2E9W08D7YH4587J3 findings 2 to 4

I agree with all three. Finding 4 above asks only that they be recorded.

- Finding 2 (glued option-path tokens) as a limitation: agreed. On the allow-listed commands, a
  glued option either reorders output (`git -O`) or reads a file as patterns (`grep` or `rg -f`).
  No allowed command prints outside content through one, and the separate-token forms are checked
  (`guard.py:168-185`, called at `:289-291`). A pattern file still influences which lines print, so
  the residual is low rather than nil. It belongs in the RISK-003 residual, which already names
  command-text analysis.
- Finding 3 (`$` blocked for agents) as a fail-safe usability limitation: agreed. The block comes
  before the allow-list (`guard.py:274-278`), so it over-blocks and opens nothing. The guard does not
  inspect the Grep tool's `pattern`, so end anchors work there.
- Finding 4 (an orchestrator over-block) as a limitation: agreed. It affects only the orchestrator
  and fails closed (`guard.py:188-190`).

## Gate 0 escalation conditions

None is confirmed. The change only adds a block path to the agent read check. It does not widen
any write scope, shell profile or orchestrator rule, and it does not touch approvals, decision
records or registered sources. The one read path still open in principle (finding 1 above) is
unconfirmed and limited to file names. It is flagged at the top of the handoff report so the
orchestrator can decide whether to escalate.
