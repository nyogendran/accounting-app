---
id: GOV-F0-VALIDATION
type: governance
title: F0 validation report
status: Proposed
version: 1
owner: orchestrator
links:
  related: [GATE-0, DEC-0001, WF-01M5BJDGB5536WYT96GNTQWH4K]
---

# F0 validation report

What was checked for F0 (SRC-005, section F), how, and what remains unverified. Every result below
was observed in a session; agents' claims were checked against files, commits or guard probes before
they were relied on.

## F0 acceptance criteria

| Criterion (SRC-005, F0) | Result | Evidence |
| --- | --- | --- |
| Tool tests pass | Met | EVD-01M5CT4WP4TFNRCZMNQ0W6C3BP: E3, 167 tests, pass; its tree equals commit 6c0f138 without the evidence file |
| Hook tests cover allow, block, Windows paths, shell writes and fail-closed | Met | `test_guard.py` (55 tests: scopes; protected paths; 8.3 short names, `\\?\`, network and Git Bash paths; tool paths padded with whitespace or a byte-order mark or starting with `~`, and a `~` that cannot be expanded; shell writes; quoted and escaped options; substitution and expansion; reads outside the repository, including glob syntax that could form `..` or a root; orchestrator blocked patterns; exit code 2 on internal error), `test_capture_hook.py` (5); live checks below |
| An agent's attempt to write a decision record is blocked | Met | Unit tests for every actor; pre-commit rejects decisions the capture hook did not write. Live: the code-security-reviewer's write to `ledger/approval-decisions/` was refused (by the permission deny rule, which acts before the guard) |
| A synthetic requirement goes through drafting, two reviews and a hook-captured approval, and a normative edit then voids it | Met on synthetic data | `test_dry_run`: drafted; reviewed by requirements-assurance and accounting-domain-expert at its current hash (readiness needs both); approved by running the real capture hook script on the exact phrase; marked Approved; edited normatively. The approval becomes void, both reviews and readiness are lost, and the checker rejects the Approved status. A mutated copy with a wrong approval code failed. The live hook in a real session is first exercised by the Gate 0 decision |

## Agent smoke tests and live probe (WF-01M5BJDGB5536WYT96GNTQWH4K)

Each agent ran a fixed brief and reported each step as observed; the orchestrator then checked the
files on disk and `git status`.

| Agent | CLAUDE.md in context | Write in scope | Blocked |
| --- | --- | --- | --- |
| requirements-engineer | Yes: quoted rule 7 without opening the file | `docs/requirements/` | `docs/governance/`, outside the repository, the denied `docs/requirements/assurance/`, `python -c`, `git log --output` |
| requirements-assurance | Yes | `docs/requirements/assurance/` | `docs/governance/`, outside the repository, `python -c`, `git log --output` |
| accounting-domain-expert | Yes | `docs/accounting/` | `docs/governance/`, outside the repository, `python -c`, `git log --output` |
| code-security-reviewer | Yes | Its review records (seven, committed) | `docs/governance/`, a decision record, outside the repository, `run_tests.py`, `python -c`, `git log --output` |

Live probe after the guard fix (step 10, requirements-assurance at e1f1bbe): blocked `git log` with a
quoted `--output`, `git diff --no-index` on a file outside the repository, and Read and Grep outside
the repository; allowed Read and `git log` inside it. The new Read, Grep and Glob hook matcher was
active in the same session.

The smoke files were never committed. They were deleted after the checker, extended in fa9a669,
reported each of them as a Markdown file without front matter.

| Finding from the smoke tests and probes | Disposition |
| --- | --- |
| P1 (high; the orchestrator's tool-path probe, step 12a): Grep's and Glob's `path` reach the hook as typed. Both tools trim a leading space or byte-order mark, and Grep expands a leading `~`. The guard read `' C:\...'` and `~/...` as names inside the repository, so any agent could search or list any folder the OS account can read, and Grep prints matching lines. Read and Write trim the same way. But Claude Code hands Read's `file_path` to the hook already resolved, as the step 13 review's calls showed, so the Read form was not live. For Write it was not observed | Confirmed; fixed in 67a91d4: the guard judges every tool path as the tool resolves it. The 67a91d4 commit message overstates the Read form |
| OQ-1: the checker silently skipped Markdown under `docs/` without front matter | Fixed in fa9a669; the conventions now say which files are governed. You decide this convention at Gate 0 |
| R2: a block by a deny pattern cited only the agent's scope | Fixed in fa9a669 |
| F1 (high): quoted or escaped options (`git log "--output=<path>"`, `find "-delete"`) passed the agent deny list, letting any agent write any file | Confirmed by probe; fixed in e1f1bbe |
| F2: `rg --hostname-bin` runs a program | Fixed in e1f1bbe |
| Q2: agents could read any file the OS account can read (`cat ~/...`, `git diff --no-index`, the Read tool), and the web-research agent could send it out | Fixed in e1f1bbe, 0272342, 8aad214, 67a91d4 (P1) and 6c0f138: agents read only inside the repository |
| R1 and R-1: parallel agents share one working tree | Process: parallel only with non-overlapping scopes; files staged by exact path |
| R3: the narrower scope named in a brief is not enforced | Limitation: the guard enforces each agent's standing scope; the orchestrator's `git status` review of every handoff checks the brief's scope |
| F3: a session runs agent definitions as loaded at its start | Limitation: the reviewer's runs here used its definition from before c449dc1; the guard enforced the current scopes throughout |
| R4: subagents' environment header says "Is a git repository: false" | Observation only |

## Independent review

Every change to framework code was reviewed by an agent that did not write it (E4). Your review as a
person (E1) is part of the Gate 0 decision.

| Review | Subject | Verdict | Outcome |
| --- | --- | --- | --- |
| First independent review (general-purpose agent; its findings are listed in the d0d422d commit message, because review records could not yet name commits) | f02ec5c | Two critical, one high, three medium, two low, one concern | All fixed test-first in d0d422d, with four further gaps found while fixing |
| REV-01M5C0YAD8BAMX6HNTM9H4WC1E | fa9a669 (covering d0d422d, 658ed21, fa9a669) | Non-blocking, four findings | 1 fixed in c449dc1; 2 to 4 recorded below |
| REV-01M5C2545W1VGNTXKY5DWSCZQV | c449dc1 | Non-blocking, three findings | The dry run now also checks readiness. Its statement that no agent profile still allowed a write outside the agent's scope was wrong: the parallel smoke test found F1 |
| REV-01M5C44F4G2E9W08D7YH4587J3 | e1f1bbe | Non-blocking, four findings | 1 fixed in 0272342; 2 to 4 recorded below |
| REV-01M5C56YPY0TASJC9E84X1PWYS | 0272342 | Non-blocking, four findings | 1 (glob syntax could form `..` or a root without the text showing it; unconfirmed) probed live, see "Tool-path probe", then closed by construction in 8aad214; 2 (absolute patterns inside the repository are refused) recorded as an over-block; 3 (untested forms) pinned by a test in 8aad214; 4 (dispositions not yet recorded) recorded in RISK-003, this report and the workflow record |
| REV-01M5C6QDYWRZJC39SDZ1FBJEKY | 8aad214 | Non-blocking, four findings | 1 (a leading-dot wildcard segment and shell syntax pass; they form `..` or a root only in bash) probed: the Glob tool did neither (see "Tool-path probe"); refused anyway in 67a91d4. 2 (RISK-003 and the operating model claimed more than the guard did) reworded exactly in 67a91d4. 3 (claims without an artifact) recorded under "Tool-path probe". 4 (rule alternatives without a failing test) pinned in 67a91d4 and checked by a mutation run |
| REV-01M5CPZDD4BGSK5HJG00SY8TRH | 67a91d4 | Non-blocking, four findings | 1 (the probe record must be in this report before Gate 0 closes) done, under "Tool-path probe". 2 (the guard and the tool still resolve some forms differently, always stricter on the guard side) recorded there; while validating it, the orchestrator found that the guard failed open when the environment names no home folder, fixed in 6c0f138. 3 (fail-safe over-blocks) recorded below. 4 (two claims reconciled by reading) the mutation run's output is recorded under "Tool-path probe" |
| REV-01M5CT5C97V1T7W6ZHY99DQHJM | 6c0f138 | Non-blocking, four findings | Recorded, not fixed before Gate 0 (see the limitations). 1 (the test pins the exit code, not the branch) and 2 (a `~user` path can raise with a misleading message, still as a block) are carried to the next change of the guard. 3 (premises reasoned or imprecise: CPython needs `HOMEPATH`, not `HOMEDRIVE`) is corrected in this report. 4 (the `USERPROFILE` assumption) is recorded under "Tool-path probe" |

An agent review is evidence, not proof. One review missed a high-severity gap that a smoke test found
by reading the same code. The most serious gap of the workflow, P1, was found by the orchestrator's
live probe after five agent reviews of the read check; the probe followed up a remark in the step 12
review about a byte-order mark. Every bypass an agent claimed was probed against the guard before it
was accepted or fixed; one claimed example turned out to be blocked already.

## Other checks performed

| Check | Observed result |
| --- | --- |
| `python tools/governance/check.py` on the repository | 0 errors, 0 warnings |
| Source fingerprints (SRC-001 to SRC-006) | All match the register (checked by `check.py`) |
| Specification extraction | Deterministic: two runs gave SHA-256 `31b2220f…`; 121 page markers; header bound to the PDF's SHA-256 |
| Copies of SRC-003 and SRC-004 | Byte-identical to the originals in `c:\yogi\tiqacc-documents` |
| Red phase before implementation | Observed for every rule added, including each review fix |
| Evidence records | Each E3 record's tree equals its commit without the evidence file, except EVD-01M5BESNRA44FFY24C4RPMYWQK (below) |
| Git option abbreviations | Git 2.50.1 rejects shortened `--output` options (tested in a scratch repository), so the deny rule for the full name is enough |
| How Claude Code's tools resolve paths and patterns | See "Tool-path probe" below |
| `.claude/settings.json` against the published schema | One error: `onFailure` is unknown to the schema, which lags Claude Code; the field is documented (2.1.295 or later) and `claude doctor` (2.1.304) reports no issues |
| Git hooks, live | Rejected: an agent commit without an `Agent:` trailer; a human commit claiming an agent (again in step 11, when a review commit was first attempted under the person's own git identity); a commit editing a committed evidence record. Both hooks ran and passed on every commit made in this session |
| Guard hook, live | Blocked agents outside their scopes (four smoke tests) and the bypasses of step 10; blocked the orchestrator's own commands near registered sources, including a here-document that only named them (step 11a), and a pipeline whose quoted regex contained `\|` (a known over-block). The step 12 review's live calls: `{.,x}./*.md` and `[.][.]/*.md` blocked, `docs/**/*.{md,yaml}` allowed. The step 13 review's live calls: a padded read and a `~` read outside the repository, a padded Grep path outside it, and the pattern `.*/*.md` blocked; a padded read of CLAUDE.md allowed |
| Validate hook, live | Flagged a dangling link in this report the moment it was written |
| Skills | The six project skills load; `delegate` was used for the agent tasks of this workflow |
| Terminal CLI | Updated from 2.1.227 to 2.1.304 (DEC-0005) |

## Tool-path probe

The guard judges tool inputs the way Claude Code was observed to resolve them, so this probe is
re-run at each gate with the then-current version (gate-review skill; RISK-003).

**Procedure.** The orchestrator runs it, because the guard does not restrict the orchestrator's
reads. It uses a scratch folder outside the repository: `globprobe/` holds `outside-marker.txt`
(text: `outside`), and `globprobe/inner/` holds `inside.txt` and `sub/deeper.txt`. Make each call
below and compare the result. "Space +" means a single leading space.

**Results.** Claude Code 2.1.301 (VS Code extension, native binary), 2026-10-20:

| Tool and argument | Input | Observed |
| --- | --- | --- |
| Glob, `path` `inner` | `*.txt`; `**/*.txt` | `inside.txt` and `sub/deeper.txt` (control) |
| Glob, `path` `inner` | `../*.txt`; `sub/../*.txt` | nothing |
| Glob, `path` `inner` | `[.][.]/*.txt`, `.[.]/*.txt`, `{.,x}./*.txt`, `.{.,x}/*.txt`, `.\./*.txt`, `@(..)/*.txt`, `+(.)/*.txt`, `{.}{.}/*.txt`, `?(.)./*.txt` | nothing |
| Glob, `path` `inner` | `.?/*.txt`, `.*/*.txt`, `.[!a]/*.txt`, `.{?,x}/*.txt`, `(.\|x)./*.txt` | nothing |
| Glob, `path` `inner` | `''inside.txt`, `${NOPE}inside.txt`, `$'\x69'nside.txt`, `$HOME/*` | nothing: no shell processing |
| Glob, `path` `inner` | `C:/…/globprobe/*.txt`; `/Users/…/globprobe/*.txt` | all three files, including `outside-marker.txt`: an absolute pattern replaces the search folder |
| Glob, `path` `inner` | the root-relative pattern after a space or a byte-order mark | nothing: patterns are not trimmed |
| Glob | `*.txt`, `path` space + `…\globprobe` | all three files: `path` is trimmed |
| Read | space + the absolute path of `outside-marker.txt`; a byte-order mark + the same | `outside`: trimmed |
| Read | the same path with a byte-order mark after `C:\Users\ynr\` | "File does not exist": the character reaches the tool |
| Read | `~/AppData/…/outside-marker.txt` | `outside`: `~` expanded |
| Read | `$HOME/…`; `%USERPROFILE%\…`; `file:///C:/…`; the path in double quotes | "File does not exist" each time |
| Grep, pattern `outside` | `path` space + `…\globprobe`; `path` `~/AppData/…/globprobe` | `outside-marker.txt`: trimmed, `~` expanded |
| Write | space + an absolute path in `globprobe` | the file was created at the trimmed path |
| WebFetch | `file:///C:/…/outside-marker.txt` | "Invalid URL" |

**What the hook receives.** The guard's block messages name the path it judged, and the step 13
review's calls show the difference:

- **Grep and Glob `path`: as typed.** `~x/../docs/governance` was blocked as
  `C:\Users\x/../docs/governance`, which is the guard's own `~` expansion.
- **Read `file_path`: already resolved.** The block message for `~/AppData/…` names the path with
  backslashes throughout; the guard's own expansion would have mixed the slashes. `~x/../CLAUDE.md`
  and `~\..\CLAUDE.md` were allowed and returned the repository's CLAUDE.md, so the tool takes
  `~x` and `~\` literally.

**Remaining differences between guard and tool**, all stricter on the guard side:

- the guard expands `~user` and `~\`, which the tool takes literally;
- the guard also trims trailing whitespace, and more characters than the probe showed the tool
  trimming;
- the guard expands `~` for Write, Edit and Glob, which the probe confirmed only for Read and Grep;
- the guard expands `~` from `USERPROFILE`, or else from `HOMEPATH` (with `HOMEDRIVE` if set), as
  Python's `expanduser` does. With neither `USERPROFILE` nor `HOMEPATH` set, it fails closed
  (6c0f138). Before that commit it judged `~/...` as a name inside the repository, which was
  observed by running the hook without them. The commit message of 6c0f138 names `HOMEDRIVE` as
  required; it is not;
- the guard assumes that `USERPROFILE`, which Windows sets in every user session, names the same
  folder that Claude Code expands `~` to. Without `USERPROFILE`, Python falls back to `HOMEPATH`,
  which can name another folder (for example a network home). Changing Claude Code's environment
  needs the same access as replacing the program that runs the hook (RISK-003).

**Guard decisions** for the padded inputs, before and after 67a91d4 (`decide()` with an agent, or
without one for the orchestrator, given the input as typed):

| Input | Before | After |
| --- | --- | --- |
| Agent Read: space, byte-order mark or tab + an outside path | allowed | blocked |
| Agent Grep or Glob: `path` space + an outside folder | allowed | blocked |
| Agent Read with a trailing space | blocked | blocked |
| Agent Write: space + a path inside its scope | blocked (scope check) | allowed: the tool writes the trimmed path, which is in scope |
| Orchestrator Write: space + `ledger/approval-decisions/…`; byte-order mark + `requirement-doc/…` | allowed | blocked (protected) |
| Orchestrator Edit: space + an existing record | allowed | blocked (record) |
| Agent Grep: `path` `~/AppData` in an environment with no home folder (hook run without `USERPROFILE` and `HOMEPATH`) | allowed until 6c0f138 | blocked (fails closed) |

**Pattern sweep.** These 22 everyday agent patterns pass at 67a91d4: `**/*.md`, `docs/**/*.md`,
`**/*.py`, `**/REV-*.md`, `tools/**/test_*.py`, `*.json`, `ledger/**/*.yaml`,
`**/*.{md,yaml,yml,json}`, `docs/sources/SRC-00[1-6]*/**`, `**/*-v1*`, `.claude/**`,
`.claude/agents/*.md`, `requirement-doc/*.pdf`, `docs/**/README.md`, `**/*.test.ts`,
`src/**/*.{ts,tsx}`, `**/__tests__/**`, `docs/requirements/REQ-GL-*.md`, `**/.*`, `**/.git*`,
`docs/**/.gitkeep` and `**/*.{md,yaml}`. These are refused, as fail-safe over-blocks: `[!.]*`,
`**\.claude\**`, `@(a|b).md`, `*.{md,}`, `{.claude,.githooks}/**`, `.*/x`, `docs/$x/*.md`,
`docs/'a'/*.md` and the repository's own absolute path with `docs/**/*.md`.

**Mutation run.** Each alternative of the agent pattern rules, and the tool-path normalisation, was
removed in turn from an in-memory copy of the guard, and the eight read and glob tests were run.

| Removed | Failing subtests |
| --- | --- |
| Root, home or drive at a start | 3 |
| Any colon | 1 |
| Delimited `..` | 0: a subset of "two dots anywhere", so it cannot be pinned on its own |
| Two dots anywhere | 1 |
| Dot after an opening brace, comma, bracket or backslash | 1 |
| Dot before a closing brace, comma or bracket | 1 |
| Empty brace alternative | 5 |
| Extglob group | 5 |
| Bracket that starts with a slash | 2 |
| Folder segment of a dot and a wildcard | 6 |
| `$`, quotes and backticks | 6 |
| Trimming and `~` expansion of tool paths | 15 |
| Trimming alone | 12 |

The unmutated copy fails none.

## Not verified, and limitations

- **Tool-path handling follows observed behaviour:** the guard judges tool paths as Claude Code
  2.1.301 resolved them (trimmed, `~` expanded). A later version could resolve them differently, so
  the tool-path probe above is re-run at each gate (RISK-003).
- **Review findings carried forward** (non-blocking; for the next change to the guard):
  REV-01M5CT5C97V1T7W6ZHY99DQHJM finding 1, where the new fail-closed test checks only the exit
  code (assert the message, and add a write-tool case), and finding 2, where a `~user` path raises
  with "no home folder" in a session whose profile folder is named differently from `USERNAME`.
  The second still blocks.
- **Live approval capture:** the capture hook script is tested and was run on synthetic data, but
  Claude Code has not yet invoked it on a real approval; the Gate 0 decision is the first. If no
  decision record appears after the phrase is typed, Gate 0 stays pending.
- **Stage 0 identity:** agents and the person share one OS account until a git host exists, so the
  attestation is best effort (RISK-003, DEC-0003).
- **The guard analyses command text.** It is a guardrail against mistakes and casual misuse, not a
  security boundary (RISK-003). Known residuals for the orchestrator: a path assembled inside a shell
  variable, a full-path command name such as `/bin/rm`, and a recursive command on a folder that
  contains protected paths (`find docs/sources -delete`). Commit-time checks and git history are the
  backstop.
- **Agent identification:** a subagent call carrying neither `agent_type` nor `agent_id` would be
  treated as the orchestrator. Claude Code supplied `agent_type` in every live run here.
- **Agent shell limits that fail safe:** `$` is blocked, including regex end-anchors (agents use the
  Grep tool instead); `>` is blocked even inside quotes; an option glued to a path (`-f<path>`) is not
  path-checked, but no allowed command prints outside content through it.
- **Known over-blocks (fail safe):** `core.hooksPath` anywhere in an orchestrator command;
  `git update-index --force-remove`; a quoted `\|` in a pattern next to a protected path is read as
  a pipe; a backslash-spelled tool path next to a protected path. For agents: a Glob pattern written
  as an absolute path inside the repository, or with a `..` that stays inside it; a pattern with
  one of the refused constructs although it would stay inside, such as `[!.]*`, `**\.claude\**`,
  `{.claude,.githooks}/**`, `.*/x`, an extglob group, `$` or a quote. The block message tells the
  agent to use a relative pattern and the `path` argument.
- **Unattributed evidence:** EVD-01M5C45W5N8QMJ9J82DP8WVR16 (pass, 159 tests, tree equal to commit
  e1f1bbe) appeared during step 10 from a `run_tests.py` run that no Claude session transcript
  shows. Its content is accurate, but its author is unknown, so it was not committed; it is held
  outside the repository for you.
- **FileChanged hook:** SRC-005 A7 proposed it to flag writes to decision records. It watches named
  files only, so it cannot watch for new records; replaced by the pre-commit attestation check and a
  protected capture log.
- **Evidence record EVD-01M5BESNRA44FFY24C4RPMYWQK** (107 tests) records tree `f39945a`, which differs
  from commit f02ec5c only in the executable bit of the two git hook scripts. Fixed in 8e6a69a.
- **Not built in F0, by design:** the knowledge base (F1), git-host approvals (F2), defect and
  change-impact workflows with `trace impact` (F3), CI evidence (F4), chat (F5) and deployment
  evidence (F6); and six of the ten agents, created at Gate A and Gate B (DEC-0002).
