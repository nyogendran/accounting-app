---
id: REV-01M5CPZDD4BGSK5HJG00SY8TRH
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 67a91d4b3c7b6f1ac0cee96d733afe27e639eaa9
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      Finding-3 evidence (REV-01M5C6QDYWRZJC39SDZ1FBJEKY) resolves only to commit-message prose, and
      the artifact that is meant to hold it does not exist yet. The gate-review skill and RISK-003 now
      instruct re-running and recording "the tool-path probe in GOV-F0-VALIDATION" at each gate, but no
      artifact with id GOV-F0-VALIDATION exists (a repository search finds the id only in those two
      prose mentions; the defined GOV artifacts are GOV-OPERATING-MODEL, GOV-CONVENTIONS, GOV-STATE,
      GOV-METHOD). The probe results, the pattern sweep and the in-memory mutation run live only in the
      commit message of 67a91d4. The brief states this is by design: the F0 validation report is
      written when the workflow ends. I accept the handling as planned, but two consequences remain for
      the human reviewer: (a) Gate 0 must not close until GOV-F0-VALIDATION actually records the probe,
      the sweep and the mutation run, because a commit message is not a resolvable evidence artifact and
      is not re-runnable; (b) if a gate review follows the skill before that artifact exists, step 2's
      instruction to re-run "the tool-path probe in GOV-F0-VALIDATION" cannot be carried out literally.
      The checker does not flag this, because it validates front-matter links, not prose IDs, and
      check.py reports 0 errors.
    citation: >-
      .claude/skills/gate-review/SKILL.md:15-17 and docs/governance/risk-register.yaml:51 at 67a91d4
      (the two GOV-F0-VALIDATION mentions); message of commit 67a91d4 (finding-3 disposition and the
      "In-memory mutation run" / "28 new cases" claims); Grep for "GOV-F0-VALIDATION|^id: GOV-" over the
      repository at 67a91d4 returned only agent-operating-model.md:2, conventions.md:2,
      project-state.md:2, methodology.md:2 and the two prose mentions
  - severity: non-blocking
    text: >-
      The guard still resolves a few path forms differently from the tool, but every residual I found is
      fail-safe (the guard is stricter, or the tool reads nothing), so none is a bypass. (a) The guard
      expands the '~user' form through os.path.expanduser for every path argument (guard.py:236-239),
      whereas the tool, observed, expands only a leading '~/' or bare '~' (Read probe of
      '~x/../CLAUDE.md' and '~\\..\\CLAUDE.md' returned the repository's own CLAUDE.md, i.e. '~x' was
      taken literally; Grep and Glob of '~x/../docs/governance' were blocked with the guard-expanded
      'C:\\Users\\x/../docs/governance'). In every case the guard either blocks (the home area is outside
      the repository) or agrees with the tool inside the repository; it never allows a '~'-leading path
      that the tool reads outside. (b) PADDING trims a superset of the tool's trim: Python '\\s' plus
      U+FEFF covers space, tab, CR, LF, FF, VT, U+FEFF and more (U+001C-001F, U+0085), and it trims
      trailing as well as leading whitespace (guard.py:67). The tool, observed, trims only a leading
      space or BOM. Trimming more, or trimming the trailing end (which Windows strips from filenames
      anyway), can only make the guard judge a cleaner path than the tool; it cannot turn an outside
      absolute path into an inside one. (c) The guard expands '~' for Write, Edit and Glob too, though
      the probe confirmed '~' expansion only for Read and Grep; if the tool does not expand '~' there,
      the guard over-blocks a '~'-leading write, which is fail-safe. All three are reasoned from the
      code plus the live probe; none yields a read or write outside the repository. Recommendation:
      record (a)-(c) in GOV-F0-VALIDATION so a later Claude Code version that changes '~user' or trim
      behaviour is caught by the gate probe.
    citation: >-
      .claude/hooks/guard.py:67 (PADDING), :236-239 (_tool_path / expanduser), :272-274, :282, :284-287
      (_decide_read trims pattern, glob and candidates) and :243 (_decide_write trims the write path) at
      67a91d4; live-probe calls 1-5 and four extra Read/Grep/Glob calls on '~x/..' and '~\\..' paths
      (reported in the handoff)
  - severity: non-blocking
    text: >-
      The change adds fail-safe over-blocks, none of which an agent or the orchestrator needs in this
      repository. Agent Glob patterns and Grep glob-filters that contain '$', a single or double quote,
      or a backtick are now refused by GLOB_SYNTAX_ESCAPE (guard.py:62), and a folder segment of a dot
      and a wildcard ('.*/', '.?/', '.[..]/', '.{..}/') is refused (guard.py:61). Legitimate dotfile
      patterns are unaffected because the dot-wildcard rule requires a wildcard immediately after the
      dot and a following slash, so '**/.*', '**/.git*', '**/.*.md', 'docs/**/.gitkeep', '.claude/**',
      '.githooks/*' all still pass (test_guard.py:364-366). No file in the repository has '$', a quote or
      a backtick in its name, and Grep's content 'pattern' (the regex) is not subject to this rule, only
      its 'glob' filter is, so the practical false-positive surface is empty here. The guard is a
      guardrail, not a security boundary, so I accept these over-blocks as fail-safe, consistent with
      REV-01M5C56YPY0TASJC9E84X1PWYS and REV-01M5C6QDYWRZJC39SDZ1FBJEKY.
    citation: >-
      .claude/hooks/guard.py:54-64 (GLOB_SYNTAX_PARTS; :61 dot-wildcard segment, :62 shell chars) and
      tools/governance/tests/test_guard.py:345-366 at 67a91d4
  - severity: non-blocking
    text: >-
      Two commit-message claims I could not run, both reconciled by reading. The "In-memory mutation run"
      is not reproducible here (the mutation harness is not in the repository, and my shell runs no ad
      hoc Python), but by reading guard.py:54-64 each input in test_agent_glob_rule_alternatives_each_pinned
      is refused by exactly one alternative (',,' by {x,,y}/..; the backslash half of the bracket rule by
      [\\]..; "two dots anywhere" by *..*/x, which GLOB_ESCAPE's delimited '..' does not match; '.]' by
      [x.]/..; '{,' by {,x}/..; the four extglob prefixes by @(.)/, *(x)/, ?(x)/, !(x)/; the colon rule
      by */C:/..), which matches the claim and its one stated exception. The "28 new cases failed before
      the change" also reconciles by reading git show 32e75b8:.claude/hooks/guard.py: 12 cases in
      test_agent_glob_leading_dot_wildcards_and_shell_syntax_blocked, 10 in
      test_agent_padded_or_home_paths_are_judged_as_the_tool_resolves_them, and 6 of the 9 in
      test_padded_paths_to_protected_files_and_records_blocked (the three trailing-space cases were
      already blocked at the parent because the path is absolute and Windows strips the trailing space)
      sum to 28; the 10 cases in test_agent_glob_rule_alternatives_each_pinned were already blocked at
      the parent, so they are regression pins, not new-behaviour cases. Nothing was weakened: the test
      file is +75/-0.
    citation: >-
      message of commit 67a91d4; git show 32e75b8:.claude/hooks/guard.py (parent, no _tool_path/PADDING
      and old GLOB_SYNTAX_ESCAPE); tools/governance/tests/test_guard.py:345-418 at 67a91d4; git diff
      --numstat 32e75b8 67a91d4 (test_guard.py 75/0)
created_at: "2026-10-20"
---

# Gate 0 review of commit 67a91d4 (fix for the padded/'~' path bypass; answer to REV-01M5C6QDYWRZJC39SDZ1FBJEKY)

Independent E4 review for WF-01M5BJDGB5536WYT96GNTQWH4K step 13. I reviewed `git show 67a91d4`
against its parent 32e75b8. HEAD was 67a91d4 and the working tree was clean, so the `path:line`
citations are valid at 67a91d4. The subject is the full hash
`67a91d4b3c7b6f1ac0cee96d733afe27e639eaa9`.

**Decision: the fix closes the probed bypass. For every path argument of every matched tool (Read,
Write, Edit, MultiEdit, NotebookEdit, Grep, Glob) the guard now trims leading and trailing whitespace
and a byte-order mark and expands a leading '~' before judging the path, via `_tool_path` and
`PADDING`, so it judges the path the tool uses. I confirmed with five live-probe calls and the new
tests that padded and '~'-leading reads outside the repository are blocked, a padded read inside the
repository is still allowed, and padded orchestrator writes to protected paths and existing records
are blocked. The change is strictly tighter than its parent for these cases and fails closed; the
only relaxations are fail-safe (dotfile patterns such as `**/.*` still pass). The residual
tool/guard differences I found (the '~user' form, a superset whitespace trim) are all stricter on the
guard side, so none is a bypass. REV-01M5C6QDYWRZJC39SDZ1FBJEKY findings 1-4 are handled as the brief
describes; the one caveat is that finding-3 evidence is still only in the commit message and the
GOV-F0-VALIDATION artifact it points to does not exist yet (finding 1 below). Verdict:
non-blocking-findings.** No Gate 0 escalation condition is met: I confirmed no agent read or write
outside the repository, no write outside scope and no write to a protected path; no test or control
was weakened; and the commit touches no approval, decision record or registered source. The human
reviewer still decides.

## Verification (observed)

- `python tools/governance/check.py`: `check: 0 error(s), 0 warning(s)`.
- `python -m unittest discover -s tools/governance/tests -t .`: `Ran 166 tests in 39.877s` and `OK`.
  This matches the commit message ("166 tests pass") and EVD-01M5CPYWK1BAFQV5QWJ07F12KH (`tests_run`
  166).
- `python -m unittest tools.governance.tests.test_guard -v -k padded -k glob`: `Ran 7 tests` and `OK`;
  the four new tests
  (`test_agent_glob_leading_dot_wildcards_and_shell_syntax_blocked`,
  `test_agent_glob_rule_alternatives_each_pinned`,
  `test_agent_padded_or_home_paths_are_judged_as_the_tool_resolves_them`,
  `test_padded_paths_to_protected_files_and_records_blocked`) each reported `ok`.
- `git show --stat 67a91d4`: six files, 151 insertions, 24 deletions. `git diff --numstat 32e75b8
  67a91d4`: guard.py 32/11, SKILL.md 3/0, agent-operating-model.md 5/2, risk-register.yaml 18/11, the
  new evidence record 18/0, test_guard.py 75/0.
- Evidence tree: EVD-01M5CPYWK1BAFQV5QWJ07F12KH records `tree`
  `abf7fc49547357ebcce5d2339a8c92097e6acb91`. `git diff --stat abf7fc4 67a91d4` shows only
  `ledger/evidence/EVD-01M5CPYWK1BAFQV5QWJ07F12KH.json` (18 insertions). So the code the evidence
  tested is byte-identical to the committed code; the two trees differ only by the evidence file
  itself. `head` is 32e75b8 (the parent) and `clean: false`, both expected for an E3 run captured
  with the change uncommitted.
- Five live-probe calls (the guard reads guard.py on every call, so the fix was live):
  1. Read, `file_path` = a space + the outside marker: **blocked** - "agent 'code-security-reviewer'
     may read only inside the repository, not C:\\Users\\ynr\\AppData\\...\\outside-marker.txt". The
     message shows the trimmed path, confirming `_tool_path` removed the leading space.
  2. Read, `file_path` = `~/AppData/.../outside-marker.txt`: **blocked** - same message with
     `C:\\Users\\ynr\\AppData\\...`, confirming '~' expanded to the home folder.
  3. Grep, pattern `outside`, `path` = a space + the outside folder: **blocked** - "may read only
     inside the repository, not C:\\Users\\ynr\\AppData\\...\\globprobe".
  4. Read, `file_path` = a space + `C:\\yogi\\tiq-accounting-app\\CLAUDE.md`: **allowed**, returned
     CLAUDE.md. A padded path inside the repository is not over-blocked.
  5. Glob, `path` `docs\\governance`, pattern `.*/*.md`: **blocked** - "pattern .*/*.md names a root,
     drive or home folder, has '..', or uses glob syntax that could form one of them."

Limits and extra calls: my shell runs no ad hoc Python and cannot check out the parent, so verdicts
on the parent, the 28-case count and the mutation run are reasoned from
`git show 32e75b8:.claude/hooks/guard.py` and marked "by reading". Beyond the five probe calls I made
four more Read/Grep/Glob calls to study '~user' handling: Read of `~x/../CLAUDE.md` and
`~\..\CLAUDE.md` each returned the repository's own CLAUDE.md (both resolve inside the repository), and
Grep and Glob of `~x/../docs/governance` were both blocked by the guard (nothing outside the
repository was read). I report them for transparency; none read content outside the repository.

## Criterion 2: does the guard now judge the path the tool uses?

`decide()` routes each tool to a decision function (guard.py:366-375). The path arguments and their
handling:

- **Write / Edit / MultiEdit (`file_path`) and NotebookEdit (`notebook_path`):** `decide()` picks
  `file_path or notebook_path or path` and `_decide_write` applies `_tool_path` first (guard.py:243),
  so the write path is trimmed and '~'-expanded before the protected-path, record and scope checks.
- **Read (`file_path`), Grep (`path`), Glob (`path`):** built into `candidates` with `_tool_path`
  (guard.py:282).
- **Grep `glob` filter and Glob `pattern`:** PADDING-trimmed before the GLOB_ESCAPE / GLOB_SYNTAX
  checks (guard.py:272-274), so a leading space or BOM can no longer hide an absolute or escaping
  pattern. This closes the leading-U+FEFF-before-slash gap I raised in REV-01M5C6QDYWRZJC39SDZ1FBJEKY;
  `\ufeff/Windows/*` is now trimmed to `/Windows/*` and blocked (test_guard.py:401).
- **Glob literal prefix:** taken from the trimmed pattern, with the base taken from the '~'-expanded
  `path` (guard.py:284-287).
- **Grep content `pattern`:** a regex, not a path, and correctly not treated as one.

`_tool_path` (guard.py:236-239) trims `^[\s\ufeff]+|[\s\ufeff]+$` and, if the result starts with '~',
calls `os.path.expanduser`. A byte-order mark in the middle of a path is preserved by both PADDING
(which anchors on the ends) and the tool (the brief notes a middle BOM made the tool report "File
does not exist"), so the two agree there too. I found no path argument of a matched tool that the
guard reads differently from the tool in a way that permits a read or write outside the repository.
The residual differences I did find ('~user', the superset trim, '~' expansion for
Write/Edit/Glob) are all stricter on the guard side and are detailed in finding 2 above; each either
blocks or agrees inside the repository, so none is a bypass.

## Criterion 3: REV-01M5C6QDYWRZJC39SDZ1FBJEKY findings 1-4

- **Finding 1 (leading-dot-wildcard segments and shell word syntax passed):** accepted. Two new
  alternatives in GLOB_SYNTAX_PARTS refuse a folder segment of a dot and a wildcard
  (`(?:^|[/\\{,])\.[?*\[{@+!(][^/\\]*[/\\]`, guard.py:61) and a pattern containing `$`, a quote or a
  backtick (`[$'\"`]`, guard.py:62). Every input my earlier finding listed (`.?/*.md`, `.*/*.md`,
  `.[!a]/*.md`, `.[x.y]/*.md`, `.{?,x}/*.md`, `$HOME/**`, `${HOME}/**`, `''/Windows/*`,
  `'.''.'/*.md`, `$'\x2e\x2e'/*.md`) is now refused, and the pins live in test_guard.py:345-366. The
  guard refuses these even though the orchestrator's probe found the Glob tool itself did not climb
  with them; that is defence in depth and I accept it. The rule is carefully scoped so ordinary
  dotfile patterns still pass (finding 3 above).
- **Finding 2 (docs claimed more than the guard did):** accepted. RISK-003
  (risk-register.yaml:39-53) and the operating model (agent-operating-model.md:38-43) now enumerate
  exactly what is refused - absolute forms, `..`, `$`, quotes, backticks, and the named constructs
  (a dot next to a brace/comma/bracket/backslash, an empty brace alternative, an extglob group, a
  bracket that starts with a slash, a dot-and-wildcard segment) - and state the tool-path handling.
  This matches the code.
- **Finding 3 (probe, sweep and mutation unrecorded):** accepted as designed, with the caveat in
  finding 1 above - the evidence is in the commit message now and is to be written into
  GOV-F0-VALIDATION when the workflow ends; that artifact does not exist yet, so Gate 0 must not
  close until it records the probe, the sweep and the mutation run.
- **Finding 4 (untested rule alternatives):** accepted. `test_agent_glob_rule_alternatives_each_pinned`
  (test_guard.py:368-384) pins `,,`, the backslash half of the bracket rule, "two dots anywhere"
  (via `*..*/x`, which GLOB_ESCAPE's delimited `..` does not catch), `.]`, `{,`, the four remaining
  extglob prefixes and the colon rule. Each is refused by one alternative only (verified by reading);
  the one acknowledged exception is the delimited `..` of GLOB_ESCAPE, a subset of "two dots
  anywhere", which cannot be pinned alone.

## Criterion 5: tests and the gate-review skill

- **The new tests fail without the change.** At 32e75b8, `_decide_read` neither PADDING-trimmed the
  pattern nor `_tool_path`-resolved the candidates, `_decide_write` did not `_tool_path` the write
  path, and GLOB_SYNTAX_ESCAPE lacked the two new alternatives
  (`git show 32e75b8:.claude/hooks/guard.py`). Reasoning each case through the parent (finding 4
  above) gives 28 new-behaviour cases that were allowed there and are blocked now, which matches the
  commit's "28 new cases failed before the change". I did not re-run at the parent (my profile cannot
  check it out).
- **Nothing was weakened, skipped or deleted.** `git show --stat 67a91d4` and `git diff --numstat`
  show test_guard.py +75/-0; the 11 deletions in guard.py are the single old GLOB_SYNTAX_ESCAPE line
  and the `_decide_read`/`_decide_write` lines that the refactor replaces with strictly wider logic.
  The only `skipTest` in the suite (test_guard.py:442, 8.3 short names) is pre-existing and unrelated.
- **The gate-review skill change is sound.** Adding a step to re-run the tool-path probe with the
  current Claude Code version and record it (SKILL.md:15-17) is the right control for a guard whose
  correctness depends on observed tool behaviour that a version upgrade could change. Its only weak
  point is the forward reference to GOV-F0-VALIDATION (finding 1).

## Criterion 6: evidence

EVD-01M5CPYWK1BAFQV5QWJ07F12KH is well-formed E3 (producer run_tests.py, command
`python -m unittest discover -s tools/governance/tests -t .`, exit 0, result pass, 166 tests). Its
`tree` abf7fc4 differs from the commit tree (677bf5c) only by the evidence file, so the tested code
equals the committed code. I cannot run run_tests.py (orchestrator-only), but the full suite of 166
tests passing on the committed tree corroborates the record.

## Criterion 7: severity and verdict

All four findings are non-blocking. The commit is a genuine control improvement: it closes a bypass
that existed at the parent (confirmed live for padded and '~'-leading agent reads outside the
repository and for padded orchestrator writes to protected paths). No finding confirms a read or
write outside the repository, a write outside scope, a write to a protected path, a weakened control,
or a touch of approvals, decision records or registered sources. The findings are an evidence
forward-reference, fail-safe residual differences, fail-safe over-blocks and two
reasoned-not-run commit-message claims. Verdict: non-blocking-findings. No Gate 0 escalation
condition is met; the human reviewer decides.
