---
id: REV-01M5CT5C97V1T7W6ZHY99DQHJM
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 6c0f138050e76efe4813ce6f763be38714e6530a
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      The new test pins the outcome, not the branch. test_home_path_that_cannot_be_expanded_fails_closed
      asserts only the exit code. Exit 2 is also what main() returns for any other exception in
      decide(), and what the guard returns when a path does expand to a folder outside the repository.
      So the test passing at 6c0f138 does not by itself show that the new raise did the blocking. Its
      fail-before property rests on CPython's documented os.path.expanduser behaviour (with neither
      USERPROFILE nor HOMEPATH, or for '~x' without USERNAME, the path comes back unchanged). I
      confirmed that by reading the parent, not by running it, because my shell profile cannot check out
      910069f. On a POSIX runner the first case would be blocked by the outside-the-repository check
      instead, because posixpath falls back to the password database when HOME is unset. Only Grep
      'path' is pinned. Read 'file_path', Glob 'path' and the write path (which also applies to the
      orchestrator) share _tool_path but have no case. Recommendation: assert "cannot expand" in stderr,
      as test_blocked_call_exits_2_with_reason already does with "protected", and add one write-tool
      case.
    citation: >-
      tools/governance/tests/test_guard.py:609-624 (new test, exit code only) and :586-595 (stderr
      assertion precedent) at 6c0f138; .claude/hooks/guard.py:247, :286 and :290 (the _tool_path call
      sites) and :388-390 (main fails closed on any exception) at 6c0f138; git diff 910069f 6c0f138
  - severity: non-blocking
    text: >-
      The new branch can also raise in an ordinary session, for the '~user' form, and its message is
      then wrong. For '~x' naming another user, CPython guesses the folder only when USERNAME equals the
      name of the current home folder. In a session whose profile folder is named differently (a renamed
      account, or a 'name.DOMAIN' or 'name.000' profile folder), '~x/...' comes back unchanged. It now
      raises "cannot expand ...: no home folder in the environment", although a home folder exists. The
      outcome is a block, which is fail-safe, and it is the outcome a matching session already gave. On
      this workstation USERNAME matches: my step-13 calls saw Grep and Glob of '~x/../docs/governance'
      blocked as 'C:\Users\x/../docs/governance'. So here the branch does not trigger for '~x'. At
      910069f a mismatched session judged '~x/...' as a name inside the repository. My step-13 Read call
      showed that the tool also takes '~x' literally. Grep's handling of '~x' was not observed, because
      the guard blocked it. So that allow agreed with the tool, and the new block is stricter than the
      tool rather than the closing of a bypass. No path in the repository starts with '~', so nothing
      legitimate is blocked. The branch cannot raise for a path that does not start with '~' after
      trimming. Nor can it raise for '~', '~/...' and '~\...' while USERPROFILE names a folder.
      Recommendation: word the message for both forms, for example "cannot expand the leading '~' of
      <path>".
    citation: >-
      .claude/hooks/guard.py:239-242 at 6c0f138 (branch, comment and message);
      REV-01M5CPZDD4BGSK5HJG00SY8TRH finding 2 (step-13 '~x' calls); git ls-files --cached --others
      --exclude-standard and Glob '**/~*' over the repository at 6c0f138 (no path starts with '~')
  - severity: non-blocking
    text: >-
      Three premises in the commit message are reasoned or imprecise rather than observed; none changes
      the verdict. (a) "Grep expands '~/' and would search the home folder": the only observation is the
      orchestrator's probe in an ordinary session ("Read and Grep expand a leading '~'", message of
      67a91d4). My step-13 calls showed that Grep and Glob paths reach the hook as typed, so for Grep the
      guard's own expansion is what decides. Nobody observed how Claude Code resolves '~' with
      USERPROFILE and HOMEPATH absent. That would need Claude Code itself to run in such an environment.
      The fix is right either way: when the guard cannot expand '~', it cannot know which folder the tool
      will use, so blocking is the correct fail-closed choice. (b) "exited 0 before the change": I did
      not run it; I confirmed it by reading. At the parent, os.path.expanduser returned both test paths
      unchanged. common.repo_relative then joins an unexpanded '~/AppData' or '~x/AppData' to the root
      and returns it as a name inside the repository. So the parent allowed both cases, and the test's
      assertion of 2 would fail there. (c) "neither USERPROFILE nor HOMEDRIVE and HOMEPATH": CPython
      falls back to HOMEPATH alone (HOMEDRIVE is optional) and has ignored HOME on Windows since 3.8. The
      exact condition is therefore "neither USERPROFILE nor HOMEPATH". The test drops all four variables,
      so it is unaffected. The step-13 carry-over still stands: GOV-F0-VALIDATION does not exist yet, so
      the probe behind (a) lives only in commit messages. This commit's own observation is better
      placed, because the new test re-runs it.
    citation: >-
      message of commit 6c0f138; message of commit 67a91d4 (probe); tools/governance/common.py:160-197
      at 6c0f138 (canonical_path, repo_relative); git diff 910069f 6c0f138 (parent line "return
      os.path.expanduser(text) if text.startswith("~") else text"); REV-01M5CPZDD4BGSK5HJG00SY8TRH
      findings 1 and 2; Grep for GOV-F0-VALIDATION over the repository at 6c0f138 (prose mentions only)
  - severity: non-blocking
    text: >-
      Residual, outside this commit: the fix catches a '~' that CPython leaves unexpanded. It does not
      catch a home folder that CPython and the tool resolve differently. With USERPROFILE absent and
      HOMEPATH present, CPython uses HOMEDRIVE plus HOMEPATH, which in a domain is often a network home
      share. Node's os.homedir() (libuv) instead falls back to the account's profile folder. If Claude
      Code resolves '~' that way (not verified), the guard and the tool judge different folders. The
      guard still blocks unless HOMEDRIVE plus HOMEPATH names a folder inside the repository, and that
      needs control of Claude Code's own environment. Whoever has that control can already choose which
      'python' runs the hook, because the hook command is found through PATH. So this adds no new
      exposure and lies outside the guard's threat model (RISK-003). Recommendation: record in
      GOV-F0-VALIDATION that the guard's '~' handling assumes USERPROFILE is set, so that the gate probe
      notices an environment where it is not.
    citation: >-
      .claude/hooks/guard.py:236-243 at 6c0f138; .claude/settings.json:86 at 6c0f138 (hook command
      'python "$CLAUDE_PROJECT_DIR/.claude/hooks/guard.py"'); docs/governance/risk-register.yaml:47-49 at
      6c0f138 (RISK-003: "a guardrail against mistakes and casual misuse, not a security boundary")
created_at: "2026-10-20"
---

# Gate 0 review of commit 6c0f138 (a '~' path that cannot be expanded fails closed)

This is an independent E4 review for WF-01M5BJDGB5536WYT96GNTQWH4K step 14. I reviewed `git show
6c0f138` against its parent 910069f. HEAD was 6c0f138 and the working tree was clean, so the
`path:line` citations are valid at 6c0f138. The subject is the full hash
`6c0f138050e76efe4813ce6f763be38714e6530a`.

**Decision: the change does what it says. `_tool_path` now raises `ValueError` when
`os.path.expanduser` returns a '~' path unchanged. The raise reaches `main()`, whose catch-all
returns 2, so the call is blocked. For every input on which it does not raise, `_tool_path` returns
exactly what it returned at 910069f. So the change can only turn an allow into a block, never the
reverse. The new test passes at 6c0f138, and by reading the parent, both of its cases were allowed
at 910069f. Nothing was weakened. The evidence's tree equals the committed tree except for the
evidence file itself.**

All four findings are non-blocking:

1. The test pins the outcome but not the branch.
2. The '~user' form can also raise in an ordinary session, with a wrong message.
3. Three commit-message premises are reasoned rather than observed.
4. A home-folder divergence remains, outside this commit.

**Verdict: non-blocking-findings.** No escalation condition is met:

- I confirmed no agent read or write outside the repository and no write to a protected path. The
  fail-open at the parent needs an environment without USERPROFILE and HOMEPATH, and this commit
  closes it.
- No test or control was weakened.
- The commit touches no approval, decision record or registered source.

The human reviewer still decides.

## Verification (observed)

- `python tools/governance/check.py`: `check: 0 error(s), 0 warning(s)`, before this record was
  written. The result after writing it is in the handoff report.
- `python -m unittest discover -s tools/governance/tests -t .`: `Ran 167 tests in 32.343s` and `OK`.
  This matches the commit message ("167 tests pass") and the evidence record's `tests_run` of 167.
- `python -m unittest tools.governance.tests.test_guard -v -k home_path`: `Ran 2 tests in 0.869s` and
  `OK`. `test_home_path_that_cannot_be_expanded_fails_closed ... ok`, and
  `test_agent_padded_or_home_paths_are_judged_as_the_tool_resolves_them ... ok`, which also matches
  `home_path`.
- `git show --stat 6c0f138`: 3 files, 44 insertions and 3 deletions.
- `git diff --numstat 910069f 6c0f138`: guard.py 6/2, the new evidence record 18/0, test_guard.py
  20/1.
- `git show --name-status 6c0f138`: guard.py `M`, the evidence record `A` (added, not modified),
  test_guard.py `M`. The parent is 910069f and the author is
  `TIQACC Orchestrator (Claude) <orchestrator@agents.tiqacc.invalid>`.
- `git diff --stat 4429fc1fa6a8f6408aa202b34877f3e690021474 6c0f138`: only
  `ledger/evidence/EVD-01M5CT4WP4TFNRCZMNQ0W6C3BP.json`, with 18 insertions.
- `git rev-parse 6c0f138: 910069f: 6c0f138^ 4429fc1…`: commit tree `8c99268c…`, parent tree
  `02bc6ca6…`, parent `910069f7…`. The evidence tree object resolves.

Limits. My shell profile runs no ad hoc Python and cannot check out the parent. The live hook
inherits Claude Code's environment, where USERPROFILE is set, so the case without a home folder cannot
be reproduced live. Statements about 910069f are therefore by reading, and are marked so. I made no
Read, Grep or Glob call outside the repository. Three first attempts of the form `git -C <repo> …` were
blocked by the guard, because the review-readonly profile allows `git show|log|status …` only without
`-C`. I re-ran them from the repository root.

## Criterion 2: correctness of the change

**It fails closed through `main()`.**

- `_tool_path` (guard.py:236-243) has three call sites: `_decide_write` (guard.py:247) and
  `_decide_read` (guard.py:286 and :290).
- None of them is inside a `try`. The `try` blocks in those functions (guard.py:252-255 and :295-298)
  wrap only `common.repo_relative`, and they turn its errors into blocks.
- `decide()` (guard.py:361-380) has no `try`.
- `main()` (guard.py:383-394) catches `Exception`, prints "TIQACC governance guard failed closed: …"
  and returns 2. `sys.exit(main())` (guard.py:397-398) makes that the process exit code.
- The hook is registered for `Edit|Write|MultiEdit|NotebookEdit|Bash|PowerShell|Read|Grep|Glob`
  (settings.json:82) and runs as a script (settings.json:86).
- The only other importer of guard.py is the test module (`load_guard`, test_guard.py:26-31).

So no code catches the `ValueError` and turns it into an allow. The error is raised inside `decide()`,
not at import time, so it cannot produce a crash exit code other than 2. The new test's exit 2 shows
that the hook still imports and runs without the home variables. No other tool code calls `expanduser`
or `Path.home()` (Grep over `*.py`).

**It cannot raise for an ordinary path.** The branch runs only when the trimmed path starts with '~'
(guard.py:239). A path with '~' elsewhere, such as an 8.3 short name like `PROGRA~1`, skips it.

**A '~' path in a normal environment.**

- For '~', '~/…' and '~\…', CPython's `ntpath.expanduser` puts USERPROFILE in front of the path
  whenever it is set, and Windows sets it in every user session. The result starts with the home
  folder, so the branch cannot raise.
- The exception is the '~user' form in a session whose profile folder name differs from USERNAME.
  There the path comes back unchanged and now raises (finding 2). The outcome is a block, which is the
  same outcome a matching session gives, and no path in the repository starts with '~'.

**The change can only add blocks.** Where `_tool_path` does not raise, it returns the same value as at
910069f (`git diff 910069f 6c0f138`). In an environment without a home folder, these '~' paths are
now blocked:

- an agent's Read, Grep or Glob path;
- any actor's write path, including an orchestrator write. At 910069f such a write was judged as an
  unprotected name inside the repository and allowed.

The orchestrator's own reads never reach `_tool_path` (guard.py:374), so they are unaffected.

## Criterion 3: the test

- **It passes with the change.** Observed above.
- **It fails without the change (by reading).** At 910069f, `_tool_path` returned
  `os.path.expanduser(text)` for a '~' path.
  - Case 1 drops USERPROFILE, HOMEDRIVE, HOMEPATH and HOME, so CPython returns `~/AppData` unchanged.
  - Case 2 drops USERNAME and keeps USERPROFILE. CPython returns `~x/AppData` unchanged, because no
    USERNAME is left to match against the profile folder.
  - `common.repo_relative` (common.py:185-197) then joins either path to the root of the temporary
    repository, which `CLAUDE_PROJECT_DIR` names (test_guard.py:575). It returns `~/AppData` or
    `~x/AppData`, a name inside the repository.
  - `_decide_read` allows that name and the hook exits 0, so `assertEqual(…, 2)` fails.

  The temporary repository carries a copy of agent-scopes.json (helpers.py:33-36), and
  `test_allowed_call_exits_0` passes. So exit 2 is not an artefact of a missing scopes file. The caveat
  in finding 1 applies: the test checks the exit code only.
- **Nothing was weakened, skipped or deleted.**
  - test_guard.py is +20/-1. The one removed line is `def run_hook(self, stdin_text):`. Its
    replacement, `def run_hook(self, stdin_text, drop=()):`, removes no variables by default, so the
    three existing callers behave as before.
  - guard.py's two removed lines are the old docstring line and the old one-line return.
  - No test was removed or skipped.

## Criterion 4: evidence

EVD-01M5CT4WP4TFNRCZMNQ0W6C3BP is well-formed E3 evidence:

- producer `tools/governance/run_tests.py`;
- command `python -m unittest discover -s tools/governance/tests -t .`;
- exit 0, result `pass`, 167 tests.

Its `head` is 910069f, the parent, and `clean` is false. Both are expected for a run captured while
the change was uncommitted.

`run_tests.py` computes the `tree` field from a temporary index after `git add -A`
(run_tests.py:31-47), so it includes uncommitted changes. `git diff --stat 4429fc1 6c0f138` shows only
the evidence file. The code that the evidence tested is therefore byte-identical to the committed code.
`recorded_at` (14:06:20Z) comes before the commit time of 19:36:33 +0530 (14:06:33Z). My own run of
the suite on the committed tree gave the same count and result. I cannot run `run_tests.py` or
re-derive `output_sha256`, because the output is not stored and contains timings.

## Conformance

- The commit is made under the orchestrator identity with an `Agent: orchestrator` trailer and an
  `Evidence:` line, as `docs/governance/conventions.md` requires.
- The new evidence record is added, not edited.
- The guard's module docstring states the new rule (guard.py:20).
- RISK-003 (risk-register.yaml:39-40) and the operating model (agent-operating-model.md:42-43) do not
  mention the new rule, but they remain accurate.

## Criterion 5: severity and verdict

All four findings are non-blocking. The change is a narrow, genuine tightening. It fails closed and it
cannot loosen any decision. The findings concern test precision, an accurate but stricter outcome with
a misleading message, premises that are reasoned rather than observed, and a residual that sits
outside the guard's threat model. **Verdict: non-blocking-findings.** No Gate 0 escalation condition is
met. The human reviewer decides.
