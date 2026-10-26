---
id: REV-01M5W4F011JE50FZ3VMWD039DG
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: 3cd2c72807d4516c7b1fa821f5228a973bfbda7c
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [Option C and the recommendation overstate what V2.2 says about interface postings] The brief's
      Step 2 row C says "Interface postings are not manual journals, so the levels do not affect them",
      and the recommendation says "C lowers no control" and that "V2.2 does not change" the V1
      reviewer's reasons. V2.2 does not say this. The Enforced level is wider than a block on manual
      journals: "A manual journal to a control account is refused. Only the owning sub-ledger posts to
      it, and the balance is reproducible from that sub-ledger at any past date" (S7-2.2.1-c57, p.27).
      Under C there is no payroll module in TIQACC. Two readings follow. (R1) The external system "takes
      its place" (S7-2.1.6-c14, p.11), so it counts as the owning sub-ledger and C works at Enforced.
      (R2) Only TIQACC's payroll module owns the payroll control account, so at Enforced interface
      postings are refused or the balance is not "reproducible from that sub-ledger", and C needs the
      payroll control type lowered (with c64's approval and governance-panel report) or set to Not
      applied. S7-2.1.6-c15 ("updates the relevant module as though it had been entered in it", p.11)
      does not settle which, because under C the module is not active. Q-029 v4 itself lists "whether
      interface postings (S7-2.1.6-c15) count as sub-ledger postings" as open, and the V1 reviewer made
      C conditional on the qualified accountant confirming exactly that ("needs the qualified accountant
      to confirm that interface postings into payroll control accounts count as sub-ledger postings",
      REV-01M5EP1W4DYPM707EB79AYEYV1). The brief drops that condition from row C and from the
      recommendation, and so presents the recommended option as free of the very issue Step 1 is
      about. Also, the V1 reasons do change under V2.2: A's control-account cost now depends on Q-032
      and Q-033, as the brief's own row A says. I passed the same sentence in GOV-IMPACT-SRC007 v2
      section 6.4 item 8 and in Q-029 v4 option C; that was my miss in REV-01M5W2PMREVQFW5TCYYJQ1K1D6.
      Fix: (1) in row C, replace the sentence with both readings and add "Rifaz confirms whether an
      interface posting counts as the owning sub-ledger at Enforced"; (2) in the recommendation, state
      the V1 advice as it was given (consider C for payroll if a current payroll system exists, subject
      to Q-022 and that confirmation) and say its control-account reason now depends on Step 1; (3) in
      Q-029 option C, replace "so the enforcement level does not touch them" with the two readings. The
      orchestrator should also correct section 6.4 item 8 when the analysis is next revised. Deciding
      roles: qualified-accountant with product-owner. Agents do not choose a reading.
    citation: >-
      GOV-BRIEF-R1-SCOPE v2 @3cd2c72 Step 2 table row C and "Recommendation"; Q-029 v4 @4bead46 option
      C; SRC-007 p.27 extraction lines 1136-1137 (S7-2.2.1-c57); p.11 lines 475-480 (S7-2.1.6-c14,
      c15); REV-01M5EP1W4DYPM707EB79AYEYV1 finding on Q-029 (lines 73-79) and section 2 table (line
      398); GOV-IMPACT-SRC007 v2 line 1160
  - severity: blocking
    text: >-
      [Rows B and C omit the corporate income tax interim, so "No control issue" is not true on the
      brief's own release plan] The brief's release table puts corporate income tax in release 2. The
      2.7.6 entries "Current tax charge for the period Dr Income tax expense · Cr Income tax payable" and
      "Instalment or payment on account Dr Income tax payable · Cr Bank" (S7-2.7.6-c07, c08, p.84) post
      to income tax payable, and "tax" is a control type (S7-2.2.1-c06, p.24). If the tax control type
      runs at Enforced, which the brief calls probable, those entries cannot be keyed as journals in
      release 1 under any option, including B ("No control issue") and C ("C lowers no control"). The
      impact analysis says so: the corporate income tax interim "could post to a tax control account at
      Advisory ... only if PQ-01 resolves for the levels and PQ-02 gives Advisory or an approved
      lowering. Otherwise V1's block applies to it" (section 6.4 item 8). D-INT-1 scope also covers
      payroll returns and opening fixed-asset and payroll balances (release-phasing v3 lines 1465-1485).
      Q-029 v4 narrows the question to payroll and depreciation and drops these. Also, V2.2 places the
      levy entry "Turnover levy accrued" in 2.7.6 (S7-2.7.6-c10, p.84), while Q-042 treats levies as
      release 1, so deferring "corporate income tax" as a whole may defer a release-1 entry. Fix: add
      one line under Step 2: "Under every option, if corporate income tax waits for release 2, its charge
      and instalments meet the same control question (Q-032, Q-033), unless the tax specialist brings it
      into release 1." Change row B's cost to name it. In Q-029, restore the D-INT-1 scope or link
      D-2.7.6. Deciding roles: tax-specialist with qualified-accountant (D-2.7.6), product-owner (scope).
    citation: >-
      GOV-BRIEF-R1-SCOPE v2 @3cd2c72 Step 2 rows B and C, "Proposed releases" row 2; Q-029 v4 @4bead46;
      SRC-007 p.84 extraction lines 3592-3595 (S7-2.7.6-c07, c08, c10); p.24 lines 999-1000
      (S7-2.2.1-c06); GOV-IMPACT-SRC007 v2 lines 1161-1163; release-phasing.yaml v3 lines 1465-1485,
      1669-1675
  - severity: non-blocking
    text: >-
      [Q-033 in the brief and the pack] (a) The brief's two-row table drops c58 ("Single entity, general
      ledger only": Not applied) and merges c60 and c61 into "Group, or multi-currency". The merge is
      fair; the dropped row should stay, as I asked in REV-01M5W2PMREVQFW5TCYYJQ1K1D6, because Not
      applied is a real starting level. (b) Neither the brief nor the pack item asks sub-question (a) of
      Q-033: is the table read against Tiqri or against each entity? The level "is held per entity and
      per control type" (p.27, note 1). Read per entity, the first Sri Lanka entity is a "Single entity
      running sub-ledgers" and its default is Advisory. That is the reading on which option A turns. (c)
      The brief states "Running lower needs an approved, reasoned lowering" as a fact, then asks whether
      a lower level may be chosen at set-up. V2.2 does not say whether a set-up choice is a lowering
      (c54). Reword as a question. (d) The pack's Part 3 item gives Advisory first and does not say that
      the evidence points to Enforced. The brief and the Q-033 record do. Rifaz may read the pack alone.
      Advisory is not presented as the start in the brief, so this does not block. Fix: restore c58;
      add sub-question (a) in plain words ("Is the level decided for Tiqri as a whole, or for each
      company separately?"); add the evidence sentence to the pack item.
    citation: >-
      GOV-BRIEF-R1-SCOPE v2 Step 1, Q-033 bullet; GOV-QPACK-L1 v2 Part 3, Q-033; Q-033 v1 "Open";
      SRC-007 p.27 extraction lines 1128, 1138-1150 (S7-2.2.1-c54, c58 to c62)
  - severity: non-blocking
    text: >-
      [Status of existing questions] (a) The pack marks Q-004 "[closed]". Its record is Proposed v1 and
      its open items (the bracketed values, the sign-off) remain; the pack itself asks who signs. The
      impact analysis says "No longer applies as written" and proposes a successor question, which was
      not created. Mark it "[R1, changed]" or create the successor. (b) The pack says Q-035 "Replaces
      V1's Q-015". Q-015 is still Proposed v1 and unlinked from the pack's text otherwise; the impact
      analysis treats Q-015 as "Changed; partly answered for Sri Lanka", not replaced. Either supersede
      Q-015 in its own record or say "Q-035 and Q-015 together". (c) Q-024 is "Changed (wider)" in section
      6.5 but not marked Changed in the pack. Other statuses I checked match section 6.5: Q-005, Q-016,
      Q-018, Q-021 and Q-025 partly answered; Q-020 changed.
    citation: >-
      GOV-QPACK-L1 v2 Part 1 (Q-004, Q-024), Part 2 (Q-035); Q-004 v1; Q-015 v1; GOV-IMPACT-SRC007 v2
      section 6.5 rows Q-004, Q-015, Q-024
  - severity: non-blocking
    text: >-
      [Completeness and owners] Every question in section 6.5, every PQ in section 6.6 except PQ-24 (kept
      with Q-028, as the brief says) and both of my contradictions (Q-052, Q-053) are in the pack.
      Missing or thin: (a) D-2.1.5-c17, how the "two-year-old supplier invoice" acceptance test is run
      if no history is migrated; the clause is unchanged in V2.2 (extraction line 444, p.11). (b) The
      invoice template designer (S7-2.4.3-c79 to c87), "release 1 or later, for the product owner"
      (section 6.4). (c) Q-047 is a precondition of option A as much as Q-032 to Q-034: if "must be nil"
      governs, Advisory journals still breach it. List it in Q-029's "Answer these first" and in the
      brief's Step 1. (d) Owners: Q-053 is filed under Rifaz only; my finding gave product-owner with
      qualified-accountant, and Tier-1 accounting policy needs both (matrix condition 1); add "With
      Shifan". Q-016 omits the qualified accountant on treatment, Q-005 the qualified accountant and tax
      specialist, and D-2.7.6 its "with: qualified-accountant".
    citation: >-
      release-phasing.yaml v3 lines 1652-1654, 1669-1671; GOV-IMPACT-SRC007 v2 lines 1025, 1188, 1193,
      1228; authority-matrix.yaml v2 conditions; REV-01M5W2PMREVQFW5TCYYJQ1K1D6 finding 2
  - severity: non-blocking
    text: >-
      [The readers] Most items can be answered without the specification. Exceptions: (a) Q-037 asks
      which module each acceptance test accepts; Shifan cannot answer without p.31. Offer the proposed
      mapping for a yes or no. (b) Q-036 asks for "Finance's correction" but the pack item omits V1's
      wording, which the record gives; add it so the answer can be "confirm". (c) The brief's capacity
      item asks "tested to that, or to a single-entity scale?"; "that" can mean the multinational column
      or the ceiling. V2.2 says the ceiling is proved; SRC-008 says build against the multinational
      column. Name both. The figures are right (p.133, lines 5646 and 5652). (d) "Governance panel" and
      "D-2.15.8" are used in the brief without a one-line explanation; say "the management panel that
      shows control changes (2.15.8)". (e) The brief and pack are dated 2026-10-27, a day after this
      review; check the date. (f) Asking Shifan "Who is the tax specialist for the other countries?" is
      fine as input, but naming one is an authority-matrix change for Yogi (pack Part 4 says so); the
      brief should say the same.
    citation: >-
      GOV-QPACK-L1 v2 Q-036, Q-037; Q-036 v1; GOV-BRIEF-R1-SCOPE v2 "Also needed" items 1, 3 and 4;
      SRC-007 p.133 extraction lines 5643-5660; SRC-008 'Volume and capacity' r3
created_at: "2026-10-26"
---

# Review of the release-1 decision brief, the question pack and Q-029 to Q-053 at 3cd2c72

Independent E4 review for WF-01M5VHRCEQP734DHRKE29J5YET step 8. Subjects: GOV-BRIEF-R1-SCOPE v2,
GOV-QPACK-L1 v2, Q-029 v4 and Q-032 to Q-053 v1, at commit
`3cd2c72807d4516c7b1fa821f5228a973bfbda7c` (with `4bead46efd2494616fa7af0676df001ce405c20a`). The
normative hash is not given because my shell profile refuses `approvals.py hash`, so the subject is named
by commit.

**Verdict: blocking-findings. Do not send as it stands.** Both blocking findings are in the one place the
product owner is asked to choose: the Q-029 options table and the recommendation. Each is a short text
fix. Everything else may go as it is once the non-blocking fixes the orchestrator accepts are made.

## Why this is blocking

The brief recommends C and tells the product owner that C "lowers no control" and B has "No control
issue". On V2.2's own words, neither is established:

- At Enforced only "the owning sub-ledger" posts to a control account (S7-2.2.1-c57). Whether an external
  payroll feed is that sub-ledger is open. Q-029 v4 lists this as open, and the V1 reviewer made C depend
  on it.
- Corporate income tax is in release 2 under every option. Its charge and instalments post to a tax control
  account.

A product owner could choose C, or B, believing Step 1 does not matter to it. If Rifaz then reads the
interface postings as not owned (R2), or the tax control type is Enforced, release 1 changes after the
decision. That is the escalation condition in the brief.

## Acceptance criteria

| Criterion | Result |
| --- | --- |
| Q-033 and Step 1: defaults by organisation; Advisory not the start | Keyed by organisation; Advisory is not presented as the start in the brief. c58 dropped, sub-question (a) missing, pack item lacks the evidence (finding 3) |
| Q-029 v4 options A, B, C | A is faithful and conditional. B and C overstate (findings 1 and 2) |
| V1 reviewer's advice for C still holds | Overstated: its condition is dropped, and A's cost now depends on Step 1 (finding 1) |
| Capacity figures | Correct: 2,000 entities and 25,000,000 lines; ceiling 10,000 and 100,000,000 (p.133). Wording of the question ambiguous (finding 6c) |
| Status of existing questions | Q-004, Q-015, Q-024 (finding 4); others match section 6.5 |
| Completeness | All of 6.5, 6.6 (less PQ-24, by design) and Q-052, Q-053 are carried. D-2.1.5-c17 and the designer are missing (finding 5) |
| Readers | Answerable in the main; Q-037, Q-036 and the capacity item need rewording (finding 6) |
| PQ-01 and PQ-02 as preconditions of Q-029 | Done: Step 1 precedes Step 2, and "How to answer" orders them. My earlier finding 3 is resolved |

## Spot checks (the orchestrator's scripted quote check was not repeated wholesale)

All correct against the SRC-007 extraction:

1. S7-2.2.1-c06, p.24 line 1000.
2. c52, p.27 line 1122.
3. c56 and c57, lines 1134-1137.
4. c58 to c61 and the table header, lines 1138-1148.
5. c64 and c67, lines 1153-1159.
6. "No user journal is acceptable as a substitute", line 319.
7. "Payroll processing", line 201.
8. "A third-party payroll product synchronising by file transfer is not acceptable", line 4415.
9. "takes its place and feeds TIQACC", line 476.
10. The receivables "no balance in it exists without a document behind it", line 1933.
11. "Customers 25,000", line 817, and "Legal entities 1 Numbering series", line 5539.
12. The capacity table, lines 5643-5660.
13. "Every clause is answered in Annexure A", line 253.
14. "First digit 1 assets ...", line 993.
15. The naming standard, line 997.
16. SRC-008 'Read me' r3 ("version 1.1"), r8, and 'Volume and capacity' r3 and r27 (25,000).

Owners checked against authority-matrix.yaml v2. The question records' owners match section 6.6, with
Q-053 the one departure (finding 5).

## Verification (observed)

- `git rev-parse 3cd2c72 4bead46`: the hashes above.
- `git diff --stat 86a16d1 3cd2c72`: the brief, the pack, Q-029 and Q-032 to Q-053 only (25 files).
- `git status --short`: empty before this record was written.
- The result of `python tools/governance/check.py` after writing is in the handoff report.
