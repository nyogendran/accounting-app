---
id: REV-01M5VJJW4XDTK3F6EKJ9M0GNWF
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: 43adce947915fda2f5de86995876627a4f4e1fae
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [Missing index still means a warning, so removing an index weakens the check] An index file
      that is absent turns every clause error of its kind back into a warning. The rule is
      intended, but the checker cannot tell "not built yet" from "deleted" or "not committed". Two
      consequences follow. (a) Deleting or renaming a committed clause-index.yaml turns every broken
      S1 link from an error into a warning, and the pre-commit hook (--quiet) lets that commit
      through. (b) Artifact checks read the working tree, not the staged tree (run_checks; only
      check_staged reads the index). An artifact that links S7 IDs can therefore be committed while
      clause-index-src007.yaml is only in the working tree. A clean checkout of that commit then
      warns instead of erroring. Neither case is new: (a) and the working-tree basis predate this
      change. Recommendation: once an index has been committed (or registered), make its absence an
      error. For example, check `git ls-files` or list the index in the source register.
    citation: >-
      tools/governance/check.py lines 82-88, 131-137, 500-514 (sha256
      b59ad1726091c48eee86af9b28a5f5a02c4d517df1d5e92da2d454b465f85b57); .githooks/pre-commit line 4
  - severity: non-blocking
    text: >-
      [Index robustness, carried over from REV-01M5VHRCEQP734DHRKE29J5YES finding 4, not addressed]
      A partly written index fails closed. Every link to an ID not yet in it is an error, which is the
      intended behaviour. No artifact links an S7 ID today, so the index being built in parallel
      breaks nothing (check: 0 errors). A truncated file with a YAML syntax error, or a file whose top
      level is not a mapping (data.get on a list raises AttributeError), stops check.py with a
      traceback instead of reporting a finding. A file whose `clauses` value is not a list gives an
      empty set, so every link of that kind becomes an error, with no message that the index itself
      is malformed. An ID of the wrong kind in an index is ignored without comment. The new
      test_each_kind_is_checked_against_its_own_index_only relies on that, which is correct for the
      lookup but leaves a misplaced ID unreported. No security impact: the paths are constants and
      parsing uses yaml.safe_load.
    citation: >-
      tools/governance/check.py lines 82-88; tools/governance/common.py lines 271-272 (sha256
      12bed95f813f5b2ccfdd31f082558ce2d45742b91529e8d5168a8de42a30bfc5)
  - severity: non-blocking
    text: >-
      [Minor test note] test_malformed_clause_id_is_an_error uses S7-2.2.1-x01, which fails the
      pattern at the "c". A near miss such as S7-2.2.1-c1 (one digit) would also exercise the
      \d{2,3} bound. It goes through the same code path (id_kind returns None, then "no such ID"), so
      this is optional.
    citation: >-
      tools/governance/tests/test_check.py lines 112-115 (sha256
      c0a0689c22fc4f1bf192cb41a07bacbe822dcb7eaf0d7ebb141b7e1a5cd599d7); tools/governance/common.py
      line 80
created_at: "2026-10-26"
---

# Re-review of the S7 clause-kind change after REV-01M5VHRCEQP734DHRKE29J5YES (uncommitted)

This is an independent E4 re-review for WF-01M5VHRCEQP734DHRKE29J5YET step 3. The subject is the
uncommitted working-tree change on HEAD `43adce947915fda2f5de86995876627a4f4e1fae`. It covers these
files only at these hashes. If any of them changes before commit, this review does not cover it.

| File | sha256 |
| --- | --- |
| `docs/governance/conventions.md` | `435dcd142259f290990d58e5d32c724f3b996e4722d407c02c0fe6b683978b6f` |
| `tools/governance/check.py` | `b59ad1726091c48eee86af9b28a5f5a02c4d517df1d5e92da2d454b465f85b57` |
| `tools/governance/common.py` | `12bed95f813f5b2ccfdd31f082558ce2d45742b91529e8d5168a8de42a30bfc5` |
| `tools/governance/tests/test_check.py` | `c0a0689c22fc4f1bf192cb41a07bacbe822dcb7eaf0d7ebb141b7e1a5cd599d7` |
| `tools/governance/tests/test_common.py` | `06ec81ef02f2b80835384da04e3c586e10a0521fb3ca90a5970ac6309d366287` |
| `.claude/skills/governance-check/SKILL.md` | `e52d3fdf8c2d0564c2924b8f75b569daeb9c9dee12e0203255a38cbe2ba8d1b6` |
| `.claude/agents/requirements-engineer.md` | `ed1bde883c0a7780c644a2b5e43ad48b1b66f360d2cbef41eac1df4de6f89c38` |

These hashes match the prefixes in the orchestrator's re-review request.

**Verdict: non-blocking-findings.** The blocking finding is resolved, and the test gaps and
guidance drift are closed. The three remaining findings are non-blocking.

## Status of the earlier findings

| Earlier finding | Status |
| --- | --- |
| 1, blocking: a clause link absent from an existing index only warned, against the convention | **Resolved.** `_clause_ids` returns `None` only when the file is missing (check.py lines 82-88). The branch at lines 131-137 warns only when its own kind's index is `None`, and otherwise reports an error: "link <type> -> <id>: not in <index>". The convention text (conventions.md, link rule) now names `S1-…` and `S7-…` and says the same thing, so code and convention agree. S7 is no longer weaker than at HEAD: an S7 link absent from an existing index is an error, as an unknown S7 ID was before. Missing indexes still warn per kind (S1: the test at line 66; S7: `test_missing_s7_index_warns`). |
| 2: the tests did not prove that each kind uses its own index | **Closed.** `test_each_kind_is_checked_against_its_own_index_only` puts each linked ID only in the other kind's index. Checking the wrong index or the union of both would find both IDs and raise no error, so the test would fail; I traced both by hand. The S1 and S7 positive paths (`test_clause_in_its_own_index_passes_silently`), errors for both kinds, the missing S7 index and a malformed S7 ID are all covered. The test count went from 54 to 58: one test replaced by five. |
| 3: guidance drift | **Adequately handled.** Governance-check step 3 now states the warn-versus-error rule and both index paths. `requirements-engineer.md` names both sources, ID forms and index paths. `docs/sources/SRC-007-spec-v2.2/extracted/spec-v2.2.txt` exists (`ls`). The other SRC-001 mentions are deferred until DEC-0008 is approved. That is reasonable, because DEC-0008 is still Proposed. |
| 4: index robustness | Not addressed, still non-blocking (finding 2 above). |

## Defects introduced by the fix

None that fail open. A partly written index fails closed: links to IDs not yet in it become errors.
This blocks only artifacts that already cite S7 IDs, and there are none today. A truncated index
crashes check.py instead of producing a finding, which is still fail-closed (finding 2). The remaining
weakness is that the warning on a missing index cannot tell "not yet built" from "removed" (finding
1). It predates this change.

## Verification (observed)

- `git rev-parse HEAD`: `43adce947915fda2f5de86995876627a4f4e1fae`.
- `git status --short`: the seven files above are modified. Untracked:
  `docs/requirements/clause-index-src007.yaml` (not read),
  `ledger/evidence/EVD-01M5VJJMZ19QHQ5HEQ5KZ8HY5H.json` and
  `ledger/reviews/REV-01M5VHRCEQP734DHRKE29J5YES.md`.
- `git diff` of the five changed paths: read in full.
- `sha256sum` of the seven files: the values in the table above.
- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`.
- `python -m unittest tools.governance.tests.test_check`: `Ran 58 tests in 22.042s OK`.
- `python -m unittest tools.governance.tests.test_common`: `Ran 17 tests in 0.020s OK`.
- I did not open EVD-01M5VJJMZ19QHQ5HEQ5KZ8HY5H, and I did not observe the 172-test run.
