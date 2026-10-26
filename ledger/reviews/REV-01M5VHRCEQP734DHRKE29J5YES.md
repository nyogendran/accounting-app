---
id: REV-01M5VHRCEQP734DHRKE29J5YES
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 5358393950bb636c84bd91b8060ccf7ee6b32343
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [Control fails open; code and convention disagree] A clause link that is absent from an
      existing clause index produces only a warning. The convention this change revises says
      otherwise: "Every linked ID must exist, except clause IDs (`S1-…`) before the clause index
      exists, which produce a warning." The S1 index exists now (docs/requirements/clause-index.yaml),
      so under the convention a link to an S1 ID that is not in it should be an error. The code warns
      before this change and after it. For S1 the gap is pre-existing. The change keeps the gap for
      S1, extends it to S7, and raises the convention to v2 without fixing line 66, which still names
      only `S1-…`. Effect: check.py exits 0 on a broken clause link (line 543 returns 1 only on
      errors). The pre-commit hook runs with --quiet, so it prints only the warning count and lets
      the commit through. The gate-review skill's "no errors allowed" test also passes. The warning
      is visible, so the link does not pass silently in a full run, but nothing blocks it. The change
      also weakens one case. At HEAD a well-formed `S7-…` link matched no ID pattern and failed with
      "no such ID" (an error). Now it is a warning, and it stays a warning even after the S7 index
      exists. No artifact links an S7 ID today (rg finds `S7-` only in conventions.md), so nothing
      currently in the repository is hidden. The full check reports 0 warnings today, so turning
      "index exists, ID absent" into an error would break nothing now. Fix, decided by the governance
      owner in the DEC that follows: either (a) make it an error when the index file exists and the
      ID is absent, keep the warning when the file is missing, and test both cases for both kinds; or
      (b) state in conventions.md lines 64-66 that a clause link absent from an existing index is a
      warning by design, and name S7 there. Until one of these is chosen, code and convention
      disagree.
    citation: >-
      docs/governance/conventions.md lines 64-66 (working tree, sha256 aeeddb78...14a2e4d, text
      unchanged from HEAD); tools/governance/check.py lines 82-87, 127-133, 540-543 (sha256
      ec4bd795...d6f7ef86 prefix ec4bd7951d10, full hash in the body); .githooks/pre-commit line 4
      ("check.py --pre-commit --quiet"); .claude/skills/gate-review/SKILL.md line 12;
      `python tools/governance/check.py` -> "check: 0 error(s), 0 warning(s)"
  - severity: non-blocking
    text: >-
      [Tests do not prove each kind uses its own index] test_each_clause_kind_is_checked_against_its_own_index
      creates only the S7 index, and the S1 ID it uses is in no index. Two wrong implementations
      would still pass: looking every kind up in the S7 set, and looking every kind up in the union
      of all sets. In both, S7-2.2.1-c01 is found, S7-2.2.1-c02 is not, and S1-2.2.1-c01 is found
      nowhere. The message would still name clause-index.yaml, because the message reads
      CLAUSE_INDEXES[clause_kind] independently of the set that was looked up. Also untested: an S1
      ID present in the S1 index gives no warning (the S1 positive path has never been tested); an S7
      link with the S7 index missing gives a warning, not an error; a malformed clause ID such as
      S7-2.2.1-c1 is still an error ("no such ID"); and test_invalid_ids has no clause-shaped
      negatives. Recommendation: write both indexes, put S1-2.2.1-c01 in the S1 index and
      S7-2.2.1-c02 only in the S1 index, then assert that S1-2.2.1-c01 gives no warning and that
      S7-2.2.1-c02 still warns and names clause-index-src007.yaml. Add the malformed-ID case and
      the missing-S7-index case. The name test_clause_links_warn_until_clause_index_exists also no
      longer describes what it asserts.
    citation: >-
      tools/governance/tests/test_check.py lines 66-86 (sha256 278d92ee...2a3a0b);
      tools/governance/tests/test_common.py lines 113-138 (sha256 06ec81ef...366287);
      tools/governance/check.py lines 91, 129-132
  - severity: non-blocking
    text: >-
      [Guidance drift] .claude/skills/governance-check/SKILL.md line 14 says "Clause warnings
      disappear once the clause index exists." That is wrong for a link absent from an existing
      index, and there are now two indexes. .claude/agents/requirements-engineer.md (lines 3 and
      18-19) describes only the SRC-001 index and `S1-` IDs, although the brief says that agent is
      building the SRC-007 index. Neither file is in this change. Both should be aligned when finding
      1 is decided.
    citation: >-
      .claude/skills/governance-check/SKILL.md line 14; .claude/agents/requirements-engineer.md
      lines 3, 18-19
  - severity: non-blocking
    text: >-
      [Index robustness, low] _clause_ids accepts any YAML. A file whose `clauses` key is missing or
      is not a list gives an empty set, so every link of that kind warns rather than reporting a
      malformed index. An ID of the wrong kind in an index (an S1 ID in the S7 index) is ignored
      without comment. A YAML syntax error raises and stops check.py, which fails closed. The index
      paths are constants and parsing uses yaml.safe_load, so there is no path-injection or
      unsafe-parsing risk. Recommendation: report an index whose clause IDs do not match its kind,
      or whose `clauses` key is not a list.
    citation: >-
      tools/governance/check.py lines 82-87; tools/governance/common.py lines 108-112, 271-272
      (sha256 12bed95f...a3bfc5)
created_at: "2026-10-26"
---

# Review of the S7 clause-kind change (uncommitted)

This is an independent E4 review for WF-01M5VHRCEQP734DHRKE29J5YET step 1. The subject is the
uncommitted working-tree change against HEAD `5358393950bb636c84bd91b8060ccf7ee6b32343`, as the
brief names it. During the review HEAD moved to `43adce947915fda2f5de86995876627a4f4e1fae`, which
changes only `docs/governance/project-state.md` (`git show --stat 43adce9`), so the reviewed files are
the same against either commit. This record covers these files only at these hashes:

| File | sha256 |
| --- | --- |
| `docs/governance/conventions.md` | `aeeddb78b7300e9f58bffc701ac8cbac8bffc307d4ca65125cc35ba7014a2e4d` |
| `tools/governance/check.py` | `ec4bd7951d109f92f20093b04fbc5121b5fa1b7839ec2094b97a72d22eb7508b` |
| `tools/governance/common.py` | `12bed95f813f5b2ccfdd31f082558ce2d45742b91529e8d5168a8de42a30bfc5` |
| `tools/governance/tests/test_check.py` | `278d92ee761ae8db995a2ee8825bd6f7ef86f01fb8d9f8a2dcbfcf4fc42a3a0b` |
| `tools/governance/tests/test_common.py` | `06ec81ef02f2b80835384da04e3c586e10a0521fb3ca90a5970ac6309d366287` |

**Verdict: blocking-findings.** The code does what its diff says. S7 IDs classify correctly, each
kind looks up its own index, and a missing index still warns. However, the change revises the
conventions and leaves them contradicting the checker: a clause link absent from an existing index
passes with a warning, where the convention requires an error. For S7 this turns a previous error
into a permanent warning. Finding 1 needs the governance owner's decision on which side to change.
The fix is small either way. The other three findings are non-blocking.

## Acceptance criteria

| Criterion | Result |
| --- | --- |
| 1. Other code that treats S1 specially | None missed. In `tools/`, `.claude/hooks/` and `.githooks/`, only `check.py` gave S1 special treatment (`rg "S1\|clause-index\|id_kind"`). `trace.py` treats links as opaque strings (lines 98-103). Approval hashing sorts link targets as strings (`common.py` `normative_payload`), so S7 links hash like any other ID. The guard has no ID logic. Two text files have drifted (finding 3). |
| 1. Classification and collisions | Correct. `S7-\d+(?:\.\d+)*-c\d{2,3}`, anchored by `_COMPILED`, starts with `S7-`. No other pattern starts with `S7-`; the nearest are `S1-`, `SRC-` and `SCN-`. The test covers `S7-2.2.1-c112`. |
| 1. Missing index means a warning | Kept: `_clause_ids` returns an empty set when the file is missing, and the branch at lines 130-133 only warns. This is tested for S1 only (finding 2). |
| 2. Behaviour change | The new text "is not in <index path>" is more accurate. The old text claimed the link "cannot be checked until the clause index exists" even when the index existed. For S1 nothing that was reported before is now hidden: same condition, same level. For S7, a well-formed link went from an error to a warning (finding 1). Whether a link absent from an existing index should only warn is not acceptable as it stands, because the convention says it should be an error (finding 1). |
| 3. Tests | They prove that S7 uses the S7 index and that the warning message names the right path. They do not prove that S1 uses its own index, or that the indexes are kept separate (finding 2). |
| 4. Verdict | blocking-findings: one blocking finding and three non-blocking. |

## Verification (observed)

- `git status --short`: five modified files, the ones listed above.
- `git rev-parse HEAD`: `5358393950bb636c84bd91b8060ccf7ee6b32343` at the start of the review, and
  `43adce947915fda2f5de86995876627a4f4e1fae` later (only project-state.md changed).
- `git diff`: read in full.
- `sha256sum` of the five files: the values in the table above.
- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`.
- `python -m unittest tools.governance.tests.test_check`: `Ran 54 tests ... OK`.
- `python -m unittest tools.governance.tests.test_common`: `Ran 17 tests ... OK`. The guard refused
  the brief's single command naming both modules, so I ran them one at a time.
- `git grep` at HEAD was refused by the guard. The HEAD behaviour cited in finding 1 comes from the
  `-` lines of `git diff`.
- I did not read or wait for `docs/requirements/clause-index-src007.yaml`.
