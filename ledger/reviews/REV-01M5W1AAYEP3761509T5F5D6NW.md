---
id: REV-01M5W1AAYEP3761509T5F5D6NW
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: 51dc99625262c79fa88f2d304468f8ff125a26c9
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [Section 6.4 and PQ-02: the first entity's default enforcement level is framed too narrowly, and
      the framing favours Advisory] This blocks re-base step 7 (the D-INT-1 rewrite in phasing v4) and
      step 8 (the decision brief). It does not block steps 3 to 6. The summary says the conflict
      "shrinks", and section 6.4 builds options A(i) and A(ii) on "Advisory, and Enforced for bank"
      (S7-2.2.1-c59). Item 5 then asks only whether the first entity is c59 or c61. Four points are
      missing. (a) The defaults table is keyed by organisation, not by entity: its header is
      "Organisation Delivered default Reason" (SRC-007 p.27, extraction line 1138). (b) The analysis
      leaves out the row "Multi-entity group or consolidated reporting Enforced" (S7-2.2.1-c60). (c)
      Tiqri as an organisation is multi-country. Q-003 v2 records "Multiple countries: Sri Lanka, and
      other countries such as Norway" and, on 2026-10-26, "All countries defined in the template". A-03
      plans a second entity in release 3. On either c60 or c61 the delivered default is Enforced, and on
      c61 SRC-008's profile D fits as well ("several countries, several currencies, high transaction
      volume", 'Setup options' r9). (d) Leaving Enforced is a governed act: "Lowering a level from
      Enforced requires approval, a recorded reason and an effective date, and is reported to
      management on the governance panel in 2.15.8" (S7-2.2.1-c64, p.27). The phasing marks 2.15.8
      needs-decision (D-2.15.8), so option A at Advisory has an unrecorded release-1 dependency on the
      governance panel. SRC-007 also does not say whether setting a level below the delivered default
      at entity set-up counts as a "lowering" under c64. c54 says only that the level "is set per entity
      and per control type by the administrator". Consequence: a product owner reading section 6.4
      could take Advisory to be the starting position. The repository evidence points to Enforced, plus
      an approved and reported lowering for each control type. Fix: in a v2 of the analysis, restate
      PQ-02 with all three rows (c59, c60, c61), the organisation-versus-entity reading, Q-003 v2's
      answers, the set-up-versus-lowering ambiguity, and the c64 dependency on 2.15.8. Make the summary
      bullet conditional on PQ-01 and PQ-02. Deciding roles: qualified-accountant and product-owner,
      both needed for Tier-1 accounting control (authority matrix v2, conditions).
    citation: >-
      GOV-IMPACT-SRC007 v1 @51dc996 (section 1 summary; section 6.4 "What V2.2 removes" and item 5;
      PQ-02); SRC-007 p.27, extraction lines 1128-1154 (S7-2.2.1-c54, c58 to c61, c64); Q-003 v2 (lines
      20-23); release-phasing.yaml v3 (A-03; section 2.15.8 needs-decision; D-2.15.8);
      developer-information-pack 'Setup options' r9, r16
  - severity: non-blocking
    text: >-
      [Section 6.4: over-reach, presenting conditional outcomes as settled] Section 6.4 states without
      condition that "A(ii), interim non-control accounts, is no longer needed. The payroll, fixed asset
      and tax accounts can be flagged from release 1 at Advisory. So the flag-immutability trap ... fall
      away", and that "The corporate income tax interim (D-2.7.6) now posts to a tax control account at
      Advisory rather than into a block". Both hold only if PQ-01 resolves for the enforcement levels
      over S7-2.2.1-c06, and if PQ-02 yields Advisory or an approved lowering. The same section later
      says, correctly, that A(ii) becomes moot "if c52 governs". Fix: add the same condition to every
      statement of this kind. Deciding role: product-owner, with qualified-accountant.
    citation: >-
      GOV-IMPACT-SRC007 v1 @51dc996, section 6.4 (bullets under "What V2.2 removes"; "What remains" item
      6; "Effect on the D-INT-1 text")
  - severity: non-blocking
    text: >-
      [Section 4: one internal contradiction is missing] V2.2 says "Changing the flag or the type on an
      account is a change to the chart and passes the approval in 2.2.2 like any other" (S7-2.2.1-c67,
      p.27). Unchanged V1 text in 2.2.2 says "Control account flag Yes Once set, cannot be changed while
      the account carries a balance" (S7-2.2.2-c47, p.30) and "Class, group and control-account status
      cannot be changed once transactions exist" (S7-2.2.2-c51, p.30). Section 3.3 item 4 and section 5
      item 8 mention c47 and c51, but neither sets them against c67. This bears on D-INT-1. Under option
      A, any account not flagged in release 1 still cannot be flagged at release 2 under c51, whatever
      c67 says. Fix: add a section 4 item and a PQ. Deciding role: product-owner, with
      qualified-accountant.
    citation: >-
      SRC-007 p.27 line 1159 (S7-2.2.1-c67); p.30 lines 1279 and 1287-1288 (S7-2.2.2-c47, c51)
  - severity: non-blocking
    text: >-
      [Section 6.4: governance-panel dependencies missing from the release-1 proposals] Several new
      clauses proposed for release 1 report on the governance panel in 2.15.8, which the phasing marks
      needs-decision. They are: remittance changes, "reported to [role] and on the governance panel in
      2.15.8" (S7-2.4.3-c68, p.58), with the acceptance test "appears in the audit log ... and on the
      governance panel" (S7-2.4.8-c06, p.61); lowering an enforcement level (S7-2.2.1-c64, and the
      acceptance test c68 "appears on the governance panel", p.28). Section 6.4 proposes remittance
      details and c53 to c68 for release 1 and does not mention this. Also, S7-2.2.1-c36 ("Opening
      balances load against it under 2.16.2", p.26) is new support for the migration route proposed
      under PQ-16, and section 6.4 does not cite it. Fix: add these to D-2.15.8 and the 2.4.3 and 2.2.1
      proposals. Deciding role: product-owner.
    citation: >-
      SRC-007 pp.26-28, 58, 61 (S7-2.2.1-c36, c64, c68; S7-2.4.3-c68; S7-2.4.8-c06);
      release-phasing.yaml v3 (2.15.8, D-2.15.8)
  - severity: non-blocking
    text: >-
      [Stale against crosswalk v2] The analysis was written against crosswalk v1 (commit 7f6a7ae). It
      reports 10 changed, 7 removed and 307 new clauses. It gives the rule "R-successor ... use the
      successor in section 3.2 (not the crosswalk)" and calls the removed entries "the escalation point".
      Crosswalk v2 at 51dc996 counts "changed: 9", "successor_s1: 8", "successor_rows: 10", "removed: 0"
      and "new: 298". S1-2.4.1-c05 moved from changed to a two-row successor. The successor map now
      agrees with section 3.2 and with the one-to-two split in section 3.3 item 2. The 1,812 and 108
      totals still hold, but S1-2.4.1-c05 moves from R-changed to R-successor. Fix: in v2 of the
      analysis, cite crosswalk v2 and point R-changed and R-successor at its status values.
    citation: >-
      docs/requirements/crosswalk-src001-to-src007.yaml v2 @51dc996 (counts block lines 20-29; pairs at
      lines 3299-3306); GOV-IMPACT-SRC007 v1 sections 1, 2, 3.1 to 3.3 and 6.0
  - severity: non-blocking
    text: >-
      [Section 6.0: "mechanical" understates the re-reading needed] References to clauses whose text is
      the same but whose meaning has changed are counted as mechanical. Section 3.3 item 4 says a re-base
      "must not treat them as unaffected". Examples: S1-2.12.1-c01 in BO-01 indicator 1, which section 6.2
      itself calls "at risk"; S1-2.2.1-c06, quoted in the glossary's "Control account" entry, which
      section 6.3 calls wrong, and in the phasing's D-INT-1 and R-01; S1-2.4.1-c06 (now c08); the six
      "[7] years" clauses; S1-2.3-c01; and S1-2.16.1-c01. A re-base that applies only R-same to these
      carries the old reading forward silently. Fix: add a third category, "same text, re-read", that
      lists these clause IDs, with counts per artifact.
    citation: >-
      GOV-IMPACT-SRC007 v1 sections 3.3 item 4, 6.0, 6.2 (BO-01), 6.3 (glossary); BO-01 v1 (S1-2.12.1-c01
      in indicators)
  - severity: non-blocking
    text: >-
      [Section 6.5: two question statuses overstated] (a) Q-025, "Largely answered by V2.2", and the
      summary. Q-025 asks two things: what retention policy a new tenant starts with, and "does one model
      (the longer of policy and statute) apply to all records, including those with a fixed '[7] years'?"
      V2.2 answers the first (S7-2.11.4-c05, c06). It leaves the second open, because it keeps all six
      "[7] years" clauses, as section 4.3 itself shows. "Partly answered" is accurate. (b) Q-018. The
      claim that SL-NTX-01 "prints a company number and no supplier TIN ..., which suggests reading (B)"
      rests on a specimen of an exempt supply ("Exempt supply under the First Schedule", library p.5).
      The template is also "for suppliers not registered for VAT" (library p.5). So the missing TIN does
      not show what the test forbids for an unregistered customer. Fix: restate (a) as partly answered,
      and drop the inference in (b) or mark it weak. Deciding roles: product-owner (Q-025) and
      tax-specialist (Q-018).
    citation: >-
      Q-025 v1 (question text); SRC-007 p.113 (S7-2.11.4-c05, c06); GOV-IMPACT-SRC007 v1 section 4.3;
      invoice-template-library extraction lines 171-205 (p.5)
  - severity: non-blocking
    text: >-
      [Ownership and the PQ list] (a) PQ-18 is owned by "qualified-accountant" in the section 6.6 table,
      but section 4.1 gives the same point to "the product owner, with the qualified accountant for the
      accounting effect". Which clause governs is a scope decision for the product owner. (b) PQ-24 gives
      privacy-law erasure to the governance owner. The authority matrix v2 names no role for privacy or
      data-protection law, so this is a matrix gap, as for Q-028, and should be stated as one rather
      than as an owner. (c) The analysis proposes 20 PQs (PQ-01 to PQ-24, less 04, 07, 13 and 20), not
      19. (d) Step 2 of section 7 sends PQ-01, 03, 05, 06, 08 and 19 first but leaves out PQ-02, on which
      step 7 depends (see finding 1). All other owner roles match the authority matrix v2. No PQ hands
      an accounting, tax or security decision to an agent.
    citation: >-
      GOV-IMPACT-SRC007 v1 sections 4.1, 6.6 and 7; docs/governance/authority-matrix.yaml v2; Q-028 v1
  - severity: non-blocking
    text: >-
      [Minor accuracy] (a) Section 5 says SRC-008 has "13 measures not in V2.2", then lists 15. SRC-008
      also has a 16th, "Years of data held online" ('Volume and capacity' r38). (b) Section 6.1 says
      SRC-008 r41 to r48 bear on values "62 to 76 and 190 to 192". Those rows prescribe only the tax
      invoice serial. SRC-008's other specimens use other numbers ("SI-2026-07-001188" on SL-NTX-01,
      "TCN-2026-07-0033" on SL-TCN-01). (c) Sections 6.1 and 6.0 present the V1 debit-note values 74 to
      76 as "now sit[ting] under the non-tax debit note S7-2.4.1-c06". V1's single row was "Debit note
      DN-[location]-[YY]-[nnnnnn] Additional charge against an issued invoice" (S1-2.4.1-c05, p.45), and
      crosswalk v2 splits it to both c05 and c06. Which successor keeps the numbers 74 to 76 is the
      steward's numbering choice; the values belong to the tax specialist either way. (d) The 2.4.3
      sub-section heading changed from "Mandatory content" to "Mandatory content and document
      templates". The phasing's heading field needs updating, and the analysis does not list this.
    citation: >-
      developer-information-pack 'Volume and capacity' r8 to r40, 'SL tax invoice field map' r41-r48;
      invoice-template-library pp.5-6; SRC-001 line 1924 and line 1962; SRC-007 lines 2299-2302 and 2343
created_at: "2026-10-26"
---

# Review of GOV-IMPACT-SRC007 v1 at 51dc996

Independent E4 review for WF-01M5VHRCEQP734DHRKE29J5YET step 5. The subject is
`docs/requirements/impact/GOV-IMPACT-SRC007.md` v1 at commit
`51dc99625262c79fa88f2d304468f8ff125a26c9`. `git status --short` and `git diff --stat 51dc996 HEAD`
were both empty. The normative hash could not be taken: my shell profile refuses
`approvals.py hash`, so the subject is named by commit.

**Decision.** The analysis is careful and faithful. Its citations resolve, its quotes are accurate, and
its counts reconcile. Its section 4 contradictions are real, and its arithmetic is correct. It
consistently treats SRC-008 as proposed data. One finding is blocking, and only for the D-INT-1
rewrite and the decision brief. The analysis frames the first entity's control-enforcement default
around "Single entity running sub-ledgers" (Advisory). It leaves out the multi-entity row and the
organisation-level reading. Together with Q-003 v2's answer ("All countries defined in the template"),
these point to Enforced, with a lowering that must be reported on a governance panel that is not yet in
release 1. The mechanical re-base (steps 3 to 6 of section 7) may proceed.

## Method and counts

The shell profile runs no scripts, so every count was made by Grep and by reading.

- **Citations, acceptance criterion 1.** I checked 125 S7 citations against the S7 index (ID, page,
  line range) and the extraction text. They come from every section of the analysis: 3.1-3.5, 4.1-4.7,
  5, 6.1-6.6. By sub-section: 2.2.1 (26), 2.2.2 (11), 2.2.4 (10), 2.2.3 (1), sections 0, 2, 2.3, 2.8,
  2.8.3, 2.11.5, 2.12.1 and 2.12.3 (11), 2.1.10 (5), 2.4.1 and 2.4.4 (6), 2.4.3 (12), 2.11.4 (5), the
  seven "[7]" clauses (7), 2.16.1 (13), 2.16.5 (12), section 3 (3), and 2.1.7, 2.1.8 and 2.15.8 (3).
  I also checked 52 SRC-008 citations across 'Read me', 'Setup options', 'Volume and capacity', 'Code
  structure', 'Chart of accounts', 'Entity in the code', 'Journal upload template', 'SL tax invoice
  field map' and library pp.2-8, 14, 16 and 18. **All 177 resolved, and every quote matched**, apart
  from line wraps. The only errors are the count and attribution points in finding 9. The 15
  single-entity, multinational and ceiling rows of SRC-008 agree with S7-2.16.1-c08 to c22, except
  customers (5,000 against 25,000), as the analysis says. I recomputed the levy example (S7-2.4.3-c25),
  SL-VAT-03, SL-TCN-01, SL-TDN-01, RCT-01 and SOA-01, and the analysis's arithmetic is correct.
- **Section 6.1, bracketed values.** Grep counted the lines containing "[": 159 in S7 and 144 in S1. I
  read every line with two or more brackets and added the extra occurrences (+34 in S7, +37 in S1). The
  totals are S7 193 and S1 181, as the analysis says. 193 - 181 = 12 = 17 new - 5 gone. I located each
  of the 17 new tokens (2.2.1-c17, c27, c46, c56; 2.2.2-c12, c21; 2.2.4-c28, c40, c49, c50, c58;
  2.4.1-c05 ×3; 2.4.3-c68; 2.16.1-c26; 2.16.5-c15) and the 5 gone (S1-2.11.4-c05; S1-2.16.1-c02 ×4).
  **Confirmed:** 173 survive, 17 are new, 5 are answered. "Answered" means replaced by V2.2 text. Each
  still needs the owner's confirmation, as the analysis says.
- **Section 6.0, the 1,812 references.** The per-artifact rows add to 1,812 and 108. Using only-matching
  Grep, I recounted BO-01 to BO-08 (14, 28, 33, 14, 17, 15, 21, 30) and Q-015, Q-016, Q-020, Q-023,
  Q-025 and Q-029 (6, 6, 8, 18, 4, 20). All 234 match, and so do the non-mechanical counts for those
  artifacts. I did not recount the workbook (238), actors (177), glossary (147) or phasing (903).
- **Acceptance criterion 3, crosswalk v2.** All 8 successors are right. Each S7 clause sits at the S1
  clause's place and restates or replaces it. S1-2.1.8-c36 is the same table row (lines 815 and 817),
  and S1-2.2.2-c26's text appears in S7-2.2.2-c61. All 9 changed pairs are right: I read S1-0-c13,
  2.2.1-c15, c16, c19, c21, 2.2.4-c20, c22, 2.11.4-c06 and 2.15.8-c22 in both extractions or indexes.
  I spot-checked 35 same pairs, 7 of them against the full text. They include all 7 of 2.1.10-c32 to
  c38, 2.2.1-c17, c18 and c20, 2.2.2-c07 to c13, c16 and c18, 2.2.4-c21, c23, c24 and c32, 2.4.1-c06 to
  c10, 2.4.8-c01 to c05, 2.11.4-c07, and 2.1.8-c35 and c37. **I found no remaining mis-mapping.** The
  tool keeps brackets when it normalises text (crosswalk_clauses.py line 47), so a lost bracket cannot
  hide inside a same pair. The 2.4.3 box clauses are matched on their anchors only. I compared that box
  in full (S1 lines 1967-1980; S7 lines 2348-2361), and it is unchanged. The sub-section heading count
  rises by one (326 to 327), which is 2.16.5.
- **Acceptance criterion 4, completeness.** Every group in the crosswalk's new list, and every changed
  pair, appears in section 3.5 or 3.1, and the group counts add to 307. The material omissions are in
  findings 1, 3 and 4.

## Section 4: is each contradiction real?

| Item | Real | Note |
| --- | --- | --- |
| 4.1 c06 against c52 and c54-c57; Advisory against "must be nil" and S7-2.3-c01 | Yes | c54 "What the flag causes is not fixed" can be read as qualifying c06. That reading should be put to the owner too |
| 4.2 c08 against 2.1.10-c36 and c37; no calendar-year reset | Yes | 2.1.10 itself also says "every format shown elsewhere in this document is illustrative" (line 916). That covers formats only, not c08's restart |
| 4.3 "[7] years" against no retention figure | Yes, as a tension | Reading the figure as a floor reconciles them, as the analysis says |
| 4.4 c61 tests 2.2.4 and 2.2.1 | Yes, editorial | The splice is visible at lines 1314-1315 |
| 4.5 cross-references | Yes, for the four checked | 2.5.3 is "Supplier invoice capture by email"; 2.11.6 is "Audit access and pack"; c48 says "under 2.10". The 2.16.5-c22 case is rightly marked lower confidence |
| 4.6 corruptions | Yes in the extraction (lines 817, 5539) | I did not render the PDF; the analysis relies on the orchestrator's check |
| 4.7 decimals, widening, lowering | First two yes. Third is redundancy, not contradiction | c64 reports every lowering, so c61's "lowering it is reported" adds nothing |

## Over-reach, acceptance criterion 5

Section 8's "It decides nothing" holds almost everywhere. Every SRC-008 value is "proposed" and sent to
a named owner. The section 4.6 cause is labelled a hypothesis. The phasing marks are labelled proposals.
The exceptions are the unconditional statements in finding 2. Section 6.4 should also not present the
first entity's starting level as known (finding 1). The PQ owners match the authority matrix v2, apart
from finding 8.

## Escalation

Finding 1 is reported for escalation under the brief, because it bears on the product owner's
release-1 decision (Q-029). Resolving it needs the qualified accountant and the product owner. I have
not chosen a reading.
