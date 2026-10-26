---
id: REV-01M5W540WHZ64H999EKPQBSX6S
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: 3fab900cc08085435d8e1e8514151c880d1ff4a0
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [The governance panel's reach is understated; it was there before v3, and I missed it twice] The
      brief's item 3 says the panel "reports lowered control levels and changed bank details printed on
      invoices. Is it in release 1?". The pack names three items. In V2.2 many release-1 sub-sections
      also report to the panel "without anyone being asked to report them": numbering changes
      (S7-2.1.10-c41, p.23); credit limit changes, overrides, write-offs and reallocations
      (S7-2.3.16-c11, p.53); payables bank detail changes, large payments and manual journals to the
      payables control (S7-2.5.17-c12, p.70); failed and pending auto postings (S7-2.6.11-c11, p.77);
      bank account and signatory changes and reopened reconciliations (S7-2.6.16-c12, p.80); tax
      configuration changes (S7-2.7.8-c13, p.87). A product owner told only of two or three items may
      leave the panel out without seeing that most release-1 modules would lose a reporting duty. The
      decision stays with her and can be revisited at the phasing re-base, so this does not block
      sending. The pack's definition of the panel ("reports configuration changes") is general enough.
      Fix, one sentence in brief item 3 and the pack's matching item: "Numbering, receivables,
      payables, bank, auto-posting and tax changes also report to it (2.1.10, 2.3.16, 2.5.17, 2.6.11,
      2.6.16, 2.7.8)." GOV-IMPACT-SRC007 lists only four clauses; correct that at its next revision.
    citation: >-
      GOV-BRIEF-R1-SCOPE v3 @3fab900 "Also needed" item 3; GOV-QPACK-L1 v3 Part 1 "The governance panel
      (2.15.8)"; SRC-007 extraction lines 970, 2263-2264, 3016-3018, 3312-3313, 3411-3412, 3710-3711;
      GOV-IMPACT-SRC007 v2 section 6.4 "Governance-panel dependencies"
  - severity: non-blocking
    text: >-
      [Minor, introduced by the fix] (a) The recommendation says that under reading (1) "C lowers no
      control", directly below the new paragraph that says corporate income tax raises the
      control-account question "under B and C as well". Row B was corrected to "No payroll or asset
      control issue". Say the same in the recommendation: "C lowers no payroll or asset control". (b)
      "C lowers no control" and "keeps release 1 well below B" are presented as "the V1 reasons". The
      V1 review gave A's control cost, depreciation having no interim route, and B roughly doubling
      release 1 (REV-01M5EP1W4DYPM707EB79AYEYV1, line 75). The paraphrase is close enough not to
      mislead.
    citation: >-
      GOV-BRIEF-R1-SCOPE v3 @3fab900 lines 83-102; REV-01M5EP1W4DYPM707EB79AYEYV1 lines 73-79
created_at: "2026-10-26"
---

# Delta re-review of the brief v3, the pack v3 and Q-029 v5 at 3fab900

Independent E4 delta re-review for WF-01M5VHRCEQP734DHRKE29J5YET step 9. The subject is commit
`3fab900cc08085435d8e1e8514151c880d1ff4a0`. It responds to REV-01M5W4F011JE50FZ3VMWD039DG, which is
not edited here. `git diff --stat 1cca839 3fab900` shows only GOV-BRIEF-R1-SCOPE, GOV-QPACK-L1 and
Q-029 changed. The normative hash is not given because my shell profile refuses `approvals.py hash`.

**Verdict: non-blocking-findings. The brief and the pack may be sent to Shifan Cader and Rifaz
Hajirin.** Both blocking findings are resolved. The two one-line fixes below are recommended before
sending, but neither blocks it.

## Earlier findings

| # | Status | Evidence |
| --- | --- | --- |
| 1 Option C (blocking) | Resolved | Brief row C and Q-029 v5 option C give reading (1), "takes its place and feeds TIQACC" (p.11), and reading (2), with Rifaz choosing with Shifan. Step 1 now quotes "Only the owning sub-ledger posts to it" (p.27). The V1 advice is restated with its condition, which is mapped to reading (1). Reading (2) is said to give C "a control cost like A". Row A says its cost "Depends on Step 1". No reading is chosen. |
| 2 Corporate income tax (blocking) | Resolved | A new paragraph in the brief and in Q-029 v5 covers corporate income tax under every option, citing p.84 and p.24 (S7-2.7.6-c07, c08; S7-2.2.1-c06). It also covers the levy entry c10 with Q-042. Row B reads "No payroll or asset control issue". D-2.7.6 is named for the tax specialist with Rifaz. Q-029 v5 restores the full D-INT-1 scope. Release 2 reads "corporate income tax (unless it moves to release 1)". |
| 3 Q-033 | Resolved | All four default rows are shown. Sub-question (a) is in plain words in the brief, the pack and Q-029. The lowering is asked, not asserted. The pack item gives the Enforced evidence. Advisory is not presented as the start. |
| 4 Statuses | Resolved | Q-004 "[R1, partly settled]"; Q-015 "changed by the same clauses; one answer can cover both"; Q-024 marked changed. |
| 5 Completeness and owners | Resolved | The two-year search test and the template designer are added. Q-047 is a precondition in the brief Step 1, Q-029 "Answer these first" and "How to answer". Owners are added for Q-005, Q-016 and Q-053, and for corporate income tax ("With Rifaz"). |
| 6 Readers | Resolved | Q-036 gives V1's wording. Q-037 offers a mapping for a yes or no, which matches p.31 lines 1308-1323. The capacity question names the ceiling, the multinational figures and the single-entity scale. Terms are explained. Dates are 2026-10-26. Naming a tax specialist is routed to Yogi. |

## Spot checks (observed)

All match the SRC-007 extraction:

- "Only the owning sub-ledger posts to it", p.27, line 1136;
- "the external system takes its place and feeds TIQACC through this interface", p.11, line 476;
- the corporate income tax entries, p.84, lines 3592-3593, and "Turnover levy accrued" (c10);
- "a two-year-old supplier invoice", p.11, line 444;
- the four default rows, lines 1139-1146;
- the S7-2.2.2-c61 acceptance text against the Q-037 mapping.

## Verification (observed)

- `git rev-parse 3fab900`: the hash above.
- `git diff 1cca839 3fab900`: three files changed.
- `git status --short`: empty before this record was written.
- The result of `python tools/governance/check.py` after writing is in the handoff report.
