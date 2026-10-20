---
id: REV-01M5C6QDYWRZJC39SDZ1FBJEKY
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 8aad2142273b588fd161fcb551c85ba19efd58a0
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      Residual of the same class as finding 1 of REV-01M5C56YPY0TASJC9E84X1PWYS, narrower, and
      unconfirmed. Two kinds of input pass both GLOB_ESCAPE and GLOB_SYNTAX_ESCAPE, and their literal
      prefix resolves inside the repository, so the guard allows them (by reading: the brief limited the
      live probe to three inputs, and my shell cannot run ad hoc Python). Each could form '..' or a root
      in bash. (a) A segment that begins with a literal dot followed by a wildcard, by a bracket
      expression whose dot is not next to '[' or ']', or by a brace whose alternative starts with a
      wildcard: .?/*.md, .*/*.md, .[!a]/*.md, .[x.y]/*.md and .{?,x}/*.md. Bash lets a segment that
      begins with '.' match '..' unless the globskipdots option is on, as it is by default from bash 5.2.
      The new test refuses .[.]/*.txt, which is the same case. (b) Shell word syntax, which the guard
      already refuses in the form '~': $HOME/** and ${HOME}/** (the home folder), ''/Windows/* (the root
      after quote removal), and '.''.'/*.md and $'\x2e\x2e'/*.md (the parent). By my knowledge,
      node-glob, fast-glob and Python glob never list '.' or '..' and perform none of (b), and ripgrep's
      glob only filters what it finds under the search path; the orchestrator's probe, which is not
      recorded (finding 3), found that the Glob tool did not climb from relative patterns. If confirmed,
      the exposure is file names outside the repository, not their contents. Recommendation: refuse a
      segment that begins with '.' followed by '?', '*', '[' or '{' when another segment follows it, and
      refuse '$' and quotes, or allow only a fixed set of pattern characters; add a test for each that
      fails first. Otherwise narrow the documented rule (finding 2).
    citation: >-
      .claude/hooks/guard.py:48 (GLOB_ESCAPE), :53 (GLOB_SYNTAX_ESCAPE) and :254-276 (the two text
      checks, then the literal prefix, which is '.' or a relative name for every input above), and
      tools/governance/common.py:185-197 (a relative candidate is taken from the root), at 8aad214;
      tools/governance/tests/test_guard.py:305 (.[.]/*.txt refused) at 8aad214; GNU Bash Reference
      Manual, "Filename Expansion" and the shopt option globskipdots (external; not opened in this
      review)
  - severity: non-blocking
    text: >-
      The documented rule claims more than the guard does. RISK-003 now says that a Glob pattern or Grep
      filter that "uses glob syntax that could form either is refused", and the operating model says
      patterns must be "without glob syntax next to a dot that could form `..` or a root". Finding 1
      lists inputs that pass. The operating-model sentence is also inexact the other way: '*.{md,yaml}'
      and '*.[ch]' put glob syntax next to a dot and are allowed, as intended, while the refused root
      forms '{x,}/Windows/*' and '[/]Windows/*' have no dot. RISK-003 still does not name the textual
      residual of the pattern check, which finding 4 of REV-01M5C56YPY0TASJC9E84X1PWYS asked to record.
      Recommendation: before the Gate 0 brief cites RISK-003, state what the guard refuses (absolute
      forms, '..' and the listed constructs) and name what it does not, or close finding 1 first.
    citation: >-
      docs/governance/risk-register.yaml:36-38 and :43-46, and
      docs/governance/agent-operating-model.md:38-40, at 8aad214
  - severity: non-blocking
    text: >-
      Three claims in the commit message do not resolve to an artifact: "18 everyday patterns were
      checked" (no list exists; the tests pin nine allowed patterns), "A guard mutated in memory without
      the root rule fails the pinned test" (no test or recorded run), and the live probe of the Glob tool
      with its "nine glob-syntax variants" (inputs and outputs not recorded). Each is consistent with the
      code by reading. The probe is the only evidence of how the Glob tool treats relative patterns,
      which the severity of finding 1 relies on, and my three probe calls reached only the guard.
      Recommendation: record the patterns, the mutation and the probe's inputs and observed outputs in
      the workflow record or the F0 validation report, adding .?/x, .*/x and $HOME/x to the probe, or
      mark the claims as unrecorded.
    citation: >-
      message of commit 8aad2142273b588fd161fcb551c85ba19efd58a0; tools/governance/tests/test_guard.py:273,
      :293-295 and :321-325 at 8aad214 (the nine allowed patterns); a repository search at 8aad214 for
      the probe found only version notes
      (docs/sources/SRC-006-bootstrap-plan/bootstrap-plan-2026-10-19.md:16 and
      docs/sources/SRC-005-framework-review/framework-review-2026-10-20.md:830), and there is no
      ledger/workflows/ folder
  - severity: non-blocking
    text: >-
      Some alternatives of GLOB_SYNTAX_ESCAPE have no test that fails without them. ',,' (an empty middle
      brace alternative) and the '[\' half of the bracket rule are not tested. '..' anywhere and '{,' are
      tested only with inputs that another rule also refuses. Of the five extglob prefixes only '+(' is
      tested. A later edit could drop any of these without a failing test. These inputs are each refused
      by one rule only and would pin them: {x,,y}/Windows/*, [\]Windows/*, ..*/*.md, {,x}/Windows/* and
      @(.)/x. No test was weakened, skipped or deleted.
    citation: >-
      .claude/hooks/guard.py:53 and tools/governance/tests/test_guard.py:300-343 at 8aad214; `git diff
      --numstat 76fc69f 8aad214` (test_guard.py 45 insertions, 0 deletions); `git blame` of
      test_guard.py:367 (its one skipTest dates from d0d422d)
created_at: "2026-10-20"
---

# Gate 0 review of commit 8aad214 (fix for REV-01M5C56YPY0TASJC9E84X1PWYS, finding 1)

This is an independent E4 review for WF-01M5BJDGB5536WYT96GNTQWH4K step 12. I reviewed
`git show 8aad214` against its parent 76fc69f. HEAD was 8aad214 and the working tree was clean, so
the `path:line` citations below are valid at 8aad214.

**Decision: every construct that finding 1 of REV-01M5C56YPY0TASJC9E84X1PWYS named is now refused,
and so is the empty brace alternative before a slash. For node-glob, fast-glob, Python glob and
ripgrep's glob filter I found no input that passes the guard and climbs out or starts at a root. The
change only adds a condition to an existing block, so it is strictly tighter than its parent and fails
closed. Two kinds of input still pass that could form `..` or a root in bash (finding 1). Neither is
confirmed against the Glob tool, but the new wording in RISK-003 and the operating model claims more
than the guard does (finding 2). Verdict: non-blocking-findings.** No Gate 0 escalation condition is
confirmed. The human reviewer still decides.

## Verification (observed)

- `python tools/governance/check.py`, before this record was written: `check: 0 error(s), 0 warning(s)`.
- `python -m unittest discover -s tools/governance/tests -t .`: `Ran 162 tests in 26.044s` and `OK`.
  This matches the commit message and EVD-01M5C6PHB4XEH6YRCG12XCCY0F.
- `python -m unittest tools.governance.tests.test_guard -v -k glob`: `Ran 3 tests` and `OK`;
  `test_agent_glob_patterns_and_grep_filters_stay_inside_repository`,
  `test_agent_glob_root_drive_and_network_forms_blocked` and
  `test_agent_glob_syntax_that_could_form_an_escape_is_blocked` each gave `ok`.
- `git show --stat 8aad214`: five files, 88 insertions, 12 deletions. `git diff --numstat 76fc69f
  8aad214`: guard.py 11 and 2, agent-operating-model.md 3 and 1, risk-register.yaml 11 and 9, the
  evidence record 18 and 0, test_guard.py 45 and 0.
- `git diff --stat 41f1dc1ef0447248bba662087db433a791216e58 8aad214`, the evidence's `tree` against the
  commit: only `ledger/evidence/EVD-01M5C6PHB4XEH6YRCG12XCCY0F.json` (18 insertions).
- Live probe, the three calls in the brief. The guard reads guard.py on every call, so the new rule
  was live.
  1. Glob, `path` `C:\yogi\tiq-accounting-app\docs\governance`, pattern `{.,x}./*.md`: blocked, with
     "Blocked by the TIQACC governance guard: agent 'code-security-reviewer' may read only inside the
     repository; pattern {.,x}./*.md names a root, drive or home folder, has '..', or uses glob syntax
     that could form one of them. Use a relative pattern and the path argument".
  2. The same `path`, pattern `[.][.]/*.md`: blocked, with the same message naming that pattern.
  3. Pattern `docs/**/*.{md,yaml}`, no `path`: allowed. It listed 29 files under `docs/`, both `.md`
     and `.yaml`.

Limits: my shell cannot run ad hoc Python, and the brief limited the live probe to those three inputs.
Verdicts on inputs that no test contains come from reading guard.py:48, :53 and :249-276, and are
marked "by reading". What I say about bash, node-glob, fast-glob, picomatch and Python glob comes from
my knowledge of those tools, not from runs in this review. Calls 1 and 2 stopped at the guard, so they
show nothing about how the Glob tool itself expands a pattern.

## How the change works

`_decide_read` now refuses a Glob `pattern` or Grep `glob` if `GLOB_ESCAPE` matches it with
backslashes turned into slashes, as before, or if the new `GLOB_SYNTAX_ESCAPE` matches it as written
(guard.py:254-260). The candidate checks of `path`, `file_path` and the Glob literal prefix are
unchanged (:261-276). I label the alternatives of the new expression (:53) in order:

- D1: `..` anywhere;
- D2: a dot after `{`, `,`, `[` or `\`;
- D3: a dot before `}`, `,` or `]`;
- D4, D5, D6: an empty brace alternative, `{,`, `,,` or `,}`;
- D7: an extglob group, `@(`, `+(`, `*(`, `?(` or `!(`;
- D8: a bracket that starts with `/` or `\`.

A, B and C label `GLOB_ESCAPE` (:48) as in REV-01M5C56YPY0TASJC9E84X1PWYS: A, a root, home folder or
drive at the start or after `{` or `,`; B, any colon; C, a delimited `..`. The new condition is joined
with `or`, so nothing the parent refused is now allowed. `re.search` on a string does not raise, so
there is no new exception path, and any exception still exits 2 (:358-365). Read tools still reach
`_decide_read` only for agents (:349).

## Finding 1 of REV-01M5C56YPY0TASJC9E84X1PWYS: the named constructs

| Construct | Inputs | Refused by | Test |
| --- | --- | --- | --- |
| Brace alternative joined to a dot | `{.,x}./*.txt`, `.{.,x}/*.txt`, `{x,.}./*.txt` | D2, D3 | test_guard.py:306-308, :315 |
| Bracket expression | `[.][.]/*.txt`, `.[.]/*.txt` | D2, D3 | :304-305, :316 |
| Backslash escape | `.\./*.txt` | D2 | :309 |
| Extglob | `+(.)/*.txt` | D7 | :310 |
| Extglob, other prefixes | `@(.)/x`, `*(.)/x`, `?(.)/x`, `!(x)/x` | D7 | by reading |
| Empty brace alternative before a slash | `{,}/Windows/*`, `{x,}/Windows/*`, `{{,},x}/Windows/*` | D4, D6 | :311-313 |
| The same, other positions | `{,x}/Windows/*`; `{x,,y}/Windows/*` | D4; D5 | by reading |
| Bracket that starts at a root | `[/]Windows/*`; `[\]Windows/*` | D8 | :314; by reading |
| Brace sequence | `{a..c}` | D1 | by reading |

A brace alternative joins a dot to the text beside it only when the dot is the first or last character
of the alternative, and such a dot always sits next to `{`, `,` or `}`, which D2 and D3 cover. That
fails only if a matcher trimmed whitespace inside alternatives (`{ . ,x}./*.md` passes); to my
knowledge none of bash, minimatch's brace expansion, picomatch or ripgrep's globset does.

## Other constructs that could form `..` or a root

- **node-glob (minimatch), fast-glob (picomatch) and Python glob** list folders with calls that never
  return `.` or `..` (`fs.readdir`, `os.scandir`). They climb only through a literal `..` segment
  after brace expansion and escapes, and D1 to D3 and C refuse every spelling of one I found. They
  start at a root only when the pattern, after brace expansion, begins with `/`, `\`, a drive or a
  network prefix, which A, B and D4 to D6 refuse. I found no input that passes and climbs or starts at
  a root in these three.
- **ripgrep** (the Grep tool's `glob`): `rg --help` (ripgrep 14.1.1, lines 586-588, observed) says
  "-g GLOB, --glob=GLOB Include or exclude files and directories for searching that match the given
  glob". It filters what ripgrep finds under the search path, so no glob syntax moves the search; the
  checks there are defence in depth.
- **bash** (finding 1):
  - a segment that begins with a literal `.` followed by `?`, `*`, a bracket expression whose dot is
    not next to `[` or `]`, or a brace whose alternative starts with a wildcard. Bash lists `.` and
    `..`, and a segment that begins with `.` can match them unless `globskipdots` is on, which is the
    default from bash 5.2. The new test refuses `.[.]/*.txt`, which is the same case;
  - shell word syntax. The guard refuses `~` but not `$`, quotes or ANSI-C quoting. As a bash word,
    `$HOME/**` and `${HOME}/**` name the home folder, `''/Windows/*` names the root after quote
    removal, and `'.''.'/*.md` and `$'\x2e\x2e'/*.md` name the parent. None of the libraries above
    performs these expansions.
- **picomatch regex groups**: `(.|x)./*.md` and `(|x)/Windows/*` pass both text checks. picomatch reads
  `(a|b)` as an alternation, but fast-glob takes its base folder from the pattern's text and never
  lists `..`, so they do not climb or start at a root there, and I do not count them. On Windows the
  later prefix check may refuse them anyway, since `|` is not a valid file-name character.
- **A leading U+FEFF** before `/` passes: Python's `\s` does not match it, while JavaScript's `trim()`
  removes it. This matters only if the Glob tool trimmed its input before deciding that a pattern is
  absolute, which I could not check. I do not count it.

These inputs pass both text checks and have a literal prefix that resolves inside the repository, so
the guard allows them (by reading; the last two have the `|` caveat):

```text
.?/*.md
.*/*.md
.[!a]/*.md
.[x.y]/*.md
.{?,x}/*.md
$HOME/**
${HOME}/**
''/Windows/*
'.''.'/*.md
$'\x2e\x2e'/*.md
(.|x)./*.md
(|x)/Windows/*
```

## Ordinary patterns (false positives)

Still allowed: `docs/**/*.{md,yaml}` (probe call 3), `*.{md,yaml}`, `{README,CHANGELOG}.md`,
`**/*.[ch]`, `ledger/reviews/REV-*[0-9A-Z].md` and `.claude/**/*.md` (test_guard.py:321-325), and,
by reading, these:

```text
**/.gitkeep
.githooks/*
.\docs\*.md
tools/governance/tests/test_*.py
**/.git{ignore,attributes}
```

Refused, although they stay inside the repository (by reading):

```text
{.claude,.githooks}/**
**/*{.md,.yaml}
**/{.gitignore,.gitattributes}
**\.gitkeep
docs/v{1..3}/*.md
*.{md,}
**/*(1).pdf
```

Dotted names inside brace alternatives (D2, D3) are the ones an agent is most likely to write; I
would use the first to review `.claude/` and `.githooks/` together. Each has a simple form that
passes, for example two calls, `**/*.{md,yaml}`, `**/.git{ignore,attributes}` or `**/.gitkeep`. The
block message says what to do. I accept these as fail-safe over-blocks and raise no finding.

## Tests

- **The 13 new block cases fail without the change (by reading).** At 76fc69f, `_decide_read` ran
  `GLOB_ESCAPE` and then the same candidate checks (`git show 76fc69f:.claude/hooks/guard.py`, lines
  244-267). `GLOB_ESCAPE` matches none of the 13. Seven Glob cases start with `{` or `[`, so their
  literal prefix is empty and adds no candidate. The prefixes of the other four, `.`, `.`, `.\./` and
  `+(.)/`, resolve to the root or below it, because `repo_relative` takes a relative path from the root
  (common.py:185-197). The two Grep cases have no candidate. So each was allowed at the parent, and its
  subtest fails there. The five allowed cases pass with either version. I did not re-run the tests at
  the parent, because my profile cannot check it out.
- **The pinned forms are meaningful.** test_guard.py:330-343 pins the five forms that finding 3 of
  REV-01M5C56YPY0TASJC9E84X1PWYS named and the climb inside the repository from its finding 2. Each
  was refused at the parent by A, B or C, which matches "passed before and after". Without A,
  `\\server\share\**`, `\Windows\**` and `{ /x,docs}/**` match no other rule, so the claim that a guard
  mutated without the root rule fails the test is consistent by reading. `c:x*` and the repository's
  own absolute path on Windows are also caught by B.
- **Nothing was weakened, skipped or deleted.** test_guard.py is +45 -0. The two lines deleted from
  guard.py are the old condition and message, replaced by a strictly wider condition. The only
  `skipTest` under tools/governance/tests (test_guard.py:367) dates from d0d422d (`git blame`).
- **Gaps** (finding 4). Each of these inputs is refused by one rule only, so a test with them would pin
  D5, D8's backslash half, D1, D4 and a second extglob prefix:

```text
{x,,y}/Windows/*
[\]Windows/*
..*/*.md
{,x}/Windows/*
@(.)/x
```

## Claims in the commit message and evidence

- "162 tests pass": observed (above).
- EVD-01M5C6PHB4XEH6YRCG12XCCY0F: `tests_run` 162, `result` pass, `exit_code` 0. Its `head` is
  76fc69f, the parent, as expected for evidence captured before the commit, and `clean: false` is
  expected because the change was not yet committed. It was recorded at 08:26:27Z, 21 seconds before
  the commit time of 13:56:48 +0530. Its `tree` differs from 8aad214 only by the evidence file itself,
  so the code it tested is the committed code.
- "the 13 new block cases failed before the change; the ordinary patterns and the pinned forms passed
  before and after": consistent by reading (Tests, above).
- "'*.{md,yaml}', '{a,b}.md', '*.[ch]' and '*[0-9].md' still pass": consistent by reading. The tests
  pin `*.{md,yaml}` and close forms of the other three (test_guard.py:321-325).
- "18 everyday patterns were checked", the mutated guard, and the live probe of the Glob tool: no
  artifact at 8aad214 records them (finding 3).
- Conformance: the `[F0-6]` tag and the `Evidence:` and `Agent: orchestrator` trailers are present;
  one authoring agent, one commit. Neither changed governance file has a normative block, and no
  approval request or decision exists yet (nothing under `ledger/approval-*`), so no approval is
  voided.

## Dispositions of REV-01M5C56YPY0TASJC9E84X1PWYS findings 2 to 4

- **Finding 2** (absolute patterns inside the repository refused, with a misleading message):
  accepted. The block stays, which fails safe. The message no longer says the pattern "leaves" the
  repository and tells the agent to use a relative pattern and the `path` argument (guard.py:256-260).
  The behaviour is pinned (test_guard.py:338 and :342-343) and documented
  (agent-operating-model.md:38-40).
- **Finding 3** (untested forms): accepted. All five forms and the climb inside the repository are
  pinned (test_guard.py:330-343). The new rule's own gaps are finding 4 here.
- **Finding 4** (dispositions not recorded): accepted as planned, and partly done. RISK-003 now names
  the glued-option residual (risk-register.yaml:45-46). The dispositions of findings 3 (`$` blocked
  for agents) and 4 (an orchestrator over-block) of REV-01M5C44F4G2E9W08D7YH4587J3 are not recorded at
  8aad214, and there is no `ledger/workflows/` folder; the brief says the workflow record and the F0
  validation report will record them after this review. RISK-003 still does not name the textual
  residual of the pattern check, and now claims the opposite (finding 2 here).

## Severity and verdict

Finding 1 is non-blocking. The guard is a guardrail, not a security boundary (guard.py:19-21,
RISK-003). No input in it is confirmed against the Glob tool: the libraries that tool could plausibly
use do not climb with them, and the orchestrator's probe saw no climb from relative patterns. If one
were confirmed, the exposure would be file names outside the repository, not their contents. Findings
2 to 4 are documentation, evidence and test gaps. Nothing weakens a control: the change is strictly
tighter than its parent. Verdict: non-blocking-findings.

## Gate 0 escalation conditions

None is confirmed. I ran no input that reads or writes outside the repository or an agent's scope,
and no test or control was weakened. The commit does not touch approvals, decision records or
registered sources: its five files are the guard, its tests, the risk register, the operating model
and a new evidence record.
