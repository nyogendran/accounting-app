---
id: REV-01M5W2PMREVQFW5TCYYJQ1K1D6
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: 428a0a5cd6f66ec665a524fe062e4f2acdf5df86
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [R-reread is still incomplete. A wider, sub-section-based search is needed before step 7] The new
      category is honest about its scope: it covers only clauses already named in section 4 or the old
      section 3.3 item 4. Its 45 and 27 references are counted correctly. But the bound leaves out
      references whose meaning V2.2 changes for the same reasons. (a) S1-2.12.1-c05 and c06, the fixed
      asset and payroll agreement rows. Section 6.4 "What remains" item 3 itself relies on them, and
      the "must be nil" reasoning that puts c01 in Part 1 applies equally to them. Five phasing
      references (lines 1499, 1500, 1567, 1614, 1629) and two in Q-029 are counted as purely
      mechanical. (b) S1-2.2.1-c18, now S7-2.2.1-c50: "A single group chart of accounts applies across
      all [No.] entities". V2.2 now lets an entity run on "Its own chart — independent" with the check
      "That entity only" (S7-2.2.2-c17, p.29), chosen "at entity set-up by [role]" (c21). Phasing R-03
      (line 1740) rests on the c18 sentence as its mitigation, and workbook value 27 cites it. Both are
      in the 108 as renumbered, but neither is flagged for re-reading. (c) S1-2.2.1-c03, the five
      classes, against the new "spare range is reserved outside the five classes" (S7-2.2.1-c30, p.25).
      The glossary cites it once. (d) S1-2.16.2-c01, the migration scope: workbook 1 and phasing 6
      (lines 120, 1424, 1430, 1433, 1689, 1758). Its meaning changes with bank at Enforced and with
      S7-2.2.1-c36. (e) S1-2.15.8-c01, the governance panel: actors 2, glossary 1, phasing 1 (D-2.15.8,
      line 1682). Its scope widens with the four clauses that now report to the panel. Recommended
      method: flag for re-reading every reference to an S1 clause in a sub-section that gained or
      changed clauses (2.1.7, 2.1.8, 2.1.10, 2.2.1, 2.2.2, 2.2.4, 2.4.1, 2.4.3, 2.4.6, 2.4.8, 2.11.4,
      2.15.8, 2.16.1, 3). Add every sub-section that a new or changed S7 clause cites by number: list
      the "in 2.x.y", "per 2.x.y" and "under 2.x.y" strings in the 298 new and 19 changed or successor
      clauses, which reaches 2.3, 2.12.1, 2.16.2, 2.2.9, 2.6.1 and 2.7.2 among others. The orchestrator
      can do this by script from the crosswalk and the index. The flagged set is then a defined
      superset, not the analyst's list. It must be done before step 7. Steps 3 to 6 may proceed with
      items (a) to (e) added by hand.
    citation: >-
      GOV-IMPACT-SRC007 v2 @428a0a5 sections 2 ("Re-read references") and 6.0 (R-reread Parts 1 and 2);
      release-phasing.yaml v3 lines 1499-1629, 1682, 1736-1740; SRC-007 p.27 line 1118 (S7-2.2.1-c50),
      p.29 lines 1205-1219 (S7-2.2.2-c16, c17, c21), p.25 lines 1059-1060 (S7-2.2.1-c30)
  - severity: non-blocking
    text: >-
      [Two V2.2 contradictions still missing from section 4. Both were present in v1 and I missed them in
      REV-01M5W1AAYEP3761509T5F5D6NW] (a) Single group chart against own chart. S7-2.2.1-c50 says "A
      single group chart of accounts applies across all [No.] entities". S7-2.2.2-c16 to c21 provide for
      an entity on its own chart, where "Two independent entities may each use the same code for
      different accounts". This bears on R-03 and on Tiqri's planned second entity (A-03). (b)
      Renumbering. When an independent entity joins a group chart, "the clash is resolved by mapping or
      by renumbering" (S7-2.2.2-c22, p.29). Against that stand "No account is renumbered to make room. A
      code issued is a code kept" (S7-2.2.1-c31, p.25) and "The account code itself can never be
      changed" (S7-2.2.2-c50, p.30). Also, PQ-11 frames the spare range only as an SRC-008 question. But
      c30 against c03 is a tension inside V2.2 itself: c03 says the class is the "First digit 1 assets
      ... 5 expense" and "determines the natural balance and the statement". Fix: add section 4 items
      and PQs. Deciding roles: product-owner, with qualified-accountant.
    citation: >-
      SRC-007 p.24 lines 993-994 (S7-2.2.1-c03); p.25 lines 1059-1062 (c30, c31); p.27 line 1118 (c50);
      p.29 lines 1208-1222 (S7-2.2.2-c17, c21, c22); p.30 line 1285 (S7-2.2.2-c50)
  - severity: non-blocking
    text: >-
      [Section 7 misstates the blocking finding and creates a circular dependency] Section 7 says "The
      D-INT-1 rewrite in step 7 and the decision brief in step 8 need the answers to PQ-01 and PQ-02
      first (the review's blocking finding)", and step 7 says "(after PQ-01 and PQ-02)". The finding
      asked for the analysis to be corrected before steps 7 and 8. It did not ask for the questions to
      be answered first. The decision brief is how PQ-01 and PQ-02 reach the product owner, so it cannot
      wait for their answers. Fix: the brief presents PQ-01 and PQ-02 as preconditions of Q-029, using
      the "PQ-02 in full" block. The D-INT-1 text in phasing v4 is written conditionally, as section 6.4
      already shows. Neither waits for an answer.
    citation: >-
      GOV-IMPACT-SRC007 v2 @428a0a5 section 7 (step 7 and the closing paragraph);
      REV-01M5W1AAYEP3761509T5F5D6NW finding 1 ("This blocks re-base step 7 ... and step 8")
  - severity: non-blocking
    text: >-
      [Minor] (a) PQ-02 and section 6.4 say "All countries defined in the template" "lists five
      jurisdictions". The library rows are five regional groupings: Sri Lanka; "EU member states, UK";
      "UAE, Saudi Arabia, GCC"; India; United States. They cover many countries. That supports the
      multinational reading more strongly, not less. (b) Section 3.4 says "2 successors move or split".
      S1-2.11.4-c05 is also a split (to c05 and c06), so the count is 3. Neither changes a
      recommendation.
    citation: >-
      developer-information-pack 'Invoice template library' r6-r20; crosswalk-successors.yaml v1 line
      13; GOV-IMPACT-SRC007 v2 sections 3.4, 6.4, 6.6
created_at: "2026-10-26"
---

# Re-review of GOV-IMPACT-SRC007 v2 at 428a0a5

Independent E4 re-review for WF-01M5VHRCEQP734DHRKE29J5YET step 7. The subject is
`docs/requirements/impact/GOV-IMPACT-SRC007.md` v2 at commit
`428a0a5cd6f66ec665a524fe062e4f2acdf5df86`. It responds to REV-01M5W1AAYEP3761509T5F5D6NW, which is
not edited here. `git diff --stat 51dc996 428a0a5` shows only the analysis and that review changed.
The normative hash is not given because my shell profile refuses `approvals.py hash`, so the subject is
named by commit.

**Verdict: non-blocking-findings.** The blocking finding is resolved. The re-base may proceed with steps
3 to 6. Before step 7, the wider re-read search in finding 1 should be run, and the section 7 sequencing
in finding 3 corrected.

## Finding 1 of the earlier review (blocking): resolved

- The defaults table is now presented as keyed by organisation, with all four rows (c58 to c61). I
  checked the quotes against lines 1138-1148.
- The evidence (Q-003 v2, A-03, SRC-008 profile D) is stated as evidence. It points to Enforced.
- The set-up-versus-lowering ambiguity is sub-question (b), and the dependency on 2.15.8 is
  sub-question (c).
- Section 1, sections 6.4 A(i) and A(ii), and the income tax interim are all conditional on PQ-01 and
  PQ-02. Section 6.4 says plainly that "Advisory is not to be presented as the starting position".
- **Could the product owner still be misled on Q-029?** Not by the analysis, provided the decision
  brief carries the "PQ-02 in full" block and PQ-01 ahead of Q-029, not after it (finding 3). The
  remaining risk is in the phasing's R-03 (finding 1(b) and finding 2(a)). It bears on the group chart,
  not on the Q-029 options.

## Earlier non-blocking findings 2 to 9

| # | Status | Evidence |
| --- | --- | --- |
| 2 Over-reach | Resolved | Section 6.4 lines 1110-1118 and 1161-1163 are now conditional |
| 3 c67 against c47 and c51 | Resolved | Section 4.8 and PQ-25. The quotes match lines 1159, 1279 and 1287-1288 |
| 4 Governance panel | Resolved | The new subsection quotes c64, c68, S7-2.4.3-c68 and S7-2.4.8-c06 correctly. c36 is cited for PQ-16 |
| 5 Crosswalk v2 | Resolved | Counts match the crosswalk v2 counts block. I cross-summed the per-status table from the per-artifact lists: renumbered 6+6+5+0+24+18 = 59, successor 20+0+1+4+4+6 = 35, changed 10+4 = 14. The Q row (18, 6, 4) also matches my own per-question derivation from Q-014 to Q-029 |
| 6 Re-read category | Partly resolved | The category exists, and its counts are right. By Grep I recounted all 12 Part 1 clauses (4, 14, 2, 4, 2, 3, 4, 2, 2, 2, 4, 2 = 45) and confirmed Part 2 (27). Its scope is too narrow (finding 1) |
| 7 Q-025, Q-018 | Resolved | Q-025 is "Partly answered", with both halves of the question stated. The Q-018 inference is "weak and is not relied on" |
| 8 Ownership | Resolved | PQ-18 is now "product-owner, with qualified-accountant". PQ-24 is recast as a matrix gap. There are 21 PQs (20 + PQ-25). PQ-02 and PQ-25 are in step 2 |
| 9 Minor | Resolved | 16 measures (r38 checked). The r41-r48 scope is narrowed. Values 74-76 are a steward's choice. The heading change is listed, and phasing line 633 reads "heading: Mandatory content" |

## Is the R-reread method adequate?

It is adequate for what it claims, and section 2 says plainly that it "is not a proof that no other
unchanged clause has changed meaning". It is not adequate as the basis of a re-base. A list built by
the analyst from its own section 4 inherits every gap in section 4. Two contradictions are missing from
section 4 (finding 2), and their clauses are missing from R-reread. The re-read flag should instead be
derived mechanically, from sub-section membership and from cross-references (finding 1). That makes the
set a checkable superset.

## New citations checked (23)

All 23 resolved and quoted correctly:

1. S7-2.2.1-c67.
2. S7-2.2.2-c47.
3. S7-2.2.2-c51, including the reclassification sentence.
4. S7-2.2.1-c64.
5. c68's "is refused without approval and, once approved, appears on the governance panel".
6. S7-2.4.3-c68.
7. S7-2.4.8-c06.
8. S7-2.2.1-c36: "Opening balances load against it under 2.16.2" (p.26).
9. c60, with its reason text.
10. The table header, line 1138.
11. c62, "held per entity and per control type".
12. c54.
13. Q-003 v2's three quotes (lines 20-23).
14. A-03.
15. 'Setup options' r9.
16. 'Volume and capacity' r38.
17. "SI-2026-07-001188" (library p.5).
18. "TCN-2026-07-0033" (library p.6).
19. The library p.5 quotes in Q-018.
20. SRC-001 line 1962 against SRC-007 line 2343 (the 2.4.3 heading).
21. Phasing line 633.
22. The crosswalk v2 counts block.
23. The R-reread line references: phasing 193, 1266, 1410 and 1423; workbook 213, 214 and 227.

Also checked: the Q-025 question text and S1-2.4.1-c05's "Debit note DN-…" (SRC-001 line 1924).

## What the revision introduced

- The section 7 sequencing sentence (finding 3) is the only new defect.
- The new content is otherwise accurate: section 4.8, PQ-02 in full, the governance-panel subsection,
  the per-status table and R-reread.
- Sections 3.3 and 3.5 now reconcile with crosswalk v2. The 298 group counts add up (6, 47, 35, 51, 96,
  2, 34, 27).

## Verification (observed)

- `git rev-parse 428a0a5`: `428a0a5cd6f66ec665a524fe062e4f2acdf5df86`.
- `git diff --stat 51dc996 428a0a5`: the analysis and REV-01M5W1AAYEP3761509T5F5D6NW only.
- `git status --short`: empty before this record was written.
- The result of `python tools/governance/check.py` after writing is in the handoff report.
