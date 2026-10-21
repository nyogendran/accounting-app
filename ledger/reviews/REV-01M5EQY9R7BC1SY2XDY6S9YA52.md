---
id: REV-01M5EQY9R7BC1SY2XDY6S9YA52
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: f6bab34d3894857e0b5f4e5c9027f716afb7e16f
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [D-INT-1 option A(ii), steward's claim contradicted in part; fix before D-INT-1 goes to the
      product owner] effect_on_control_account_rule says that under (ii) "SRC-001 prescribes
      'reclassifying the balance by journal, with the working attached' (S1-2.2.2-c16), but a journal
      into the new control accounts is itself blocked (S1-2.2.1-c21), so the balances must arrive
      through the sub-ledger". That settles a tension inside SRC-001 by choosing one reading, and it
      leaves out a clause that bears directly on the point. Reading R1 (the steward's): c21 ("Posting
      is blocked to: ... control accounts by manual journal", p.24) overrides c16, so release 2 must
      load the balances through the sub-ledger. Reading R2: c16 is the specific rule for exactly this
      case. It reads "Class, group and control-account status cannot be changed once transactions
      exist. A misclassified account is corrected by opening the correct account and reclassifying the
      balance by journal" (p.24). Under R1 that route could never be used whenever the correct account
      is a control account. SRC-001 also gives "A controlled reclassification tool [that] can move
      history from one account to another, restricted to [role], requiring approval, posting a visible
      journal rather than rewriting history, and recorded in the audit log" (S1-2.2.2-c18, p.25). A
      journal posted by that tool is arguably not a "manual journal" under c21. Consequence: under R1,
      A(ii) needs a sub-ledger load at release 2. Under R2 it closes with one approved
      reclassification, so A costs less than the file now suggests. Recommended resolution: state both
      readings, add S1-2.2.2-c18 to D-INT-1 (and to Q-029 at its next version), and leave the choice
      to the qualified accountant, who already sets the method. Two precision points in the same
      block. (a) The reason the interim accounts can never be flagged is c16 ("once transactions
      exist"), not c12 ("while the account carries a balance"); c12 alone would allow flagging at a
      nil balance. (b) A(i) cites S1-3-c01, which applies "after signature" (p.121). SRC-001 is
      unsigned until Q-004 is decided, so cite the framework's change control (SRC-005, A3) as well.
      c16 is on p.24 only (clause index lines 1044-1045); "pp.24-25" in against_interim_journals
      repeats an error from my earlier review.
    citation: >-
      docs/requirements/release-phasing.yaml@f6bab34 (decisions_needed D-INT-1, options A
      effect_on_control_account_rule, against_interim_journals); SRC-001 p.24 S1-2.2.1-c21 and
      S1-2.2.2-c16; p.25 S1-2.2.2-c18; p.121 S1-3-c01, all as quoted; Q-004@v1; Q-029@v2
  - severity: non-blocking
    text: >-
      [D-INT-1 option C, steward's claim confirmed but its effects incomplete] The claim that the
      qualified accountant must confirm whether interface postings count as sub-ledger postings is
      confirmed. S1-2.1.6-c14 lets the external system "take its place and feeds TIQACC through this
      interface" where a module is not activated (p.11). But S1-2.1.6-c15 has a received transaction
      update "the relevant module as though it had been entered in it ... and raises its ledger entries
      through the posting rules in 2.6.10" (p.11), and under C there is no active payroll module for it
      to update. So whether the payroll control accounts have a sub-ledger at all in release 1 is
      genuinely open. Two effects of C are not stated, though the matching effect is stated for A.
      (a) The payroll row of the sub-ledger agreement ("Net pay, withholding tax and fund contribution
      payables | Payroll run totals not yet remitted", S1-2.12.1-c06, p.101) has no in-system run
      totals to agree to in release 1. (b) The entries the interface raises are configured on the
      interface ("field mapping, value translation, posting rules ... set up without development",
      S1-2.1.6-c16, p.11), so it is unstated whether the payroll entry table S1-2.10.10-c01 to c08
      governs them before 2.10.10 is delivered. Recommend adding both to C's
      effect_on_control_account_rule.
    citation: >-
      release-phasing.yaml@f6bab34 (D-INT-1 option C; option A effect_on_control_account_rule, last
      sentence); SRC-001 p.11 S1-2.1.6-c14, c15, c16; p.101 S1-2.12.1-c06, as quoted
  - severity: non-blocking
    text: >-
      [variants B and C, completeness] The lists match the counts: 23 and 10 sub-sections, and the
      release-2 totals of 26, 3 and 16 add up. Under each option the payroll and fixed asset sections,
      their acceptance parts, introductions and dependent recommendations move together. Three gaps.
      (a) Both B and C put 2.8.2 in release 1. 2.8.2 has the row "Purchase order and goods receipt |
      Receipt of an asset item creates the asset record at receipt, per 2.9.1" (S1-2.8.2-c02, p.76),
      and capital-item orders are release 1 ("Any value, capital items ... Requisition and purchase
      order", S1-2.5.5-c04, p.51). Yet "Fixed asset item | Capitalised on receipt and passed to the
      asset register under 2.8.2" (S1-2.9.1-c08, p.84) stays in release 5, with only "the product owner
      may bring c08 forward". Each variant should either move c08 or state which rule covers
      S1-2.8.2-c02 for a service entity. (b) Under B, payroll and attendance (2.10.4) move to release
      1. The 2.1.6 reason for leaving out "[attendance device, where used]" ("because attendance
      belongs to payroll") then no longer holds, so variants.B recommendations_that_change should list
      workbook value 19. (c) Option A's effect_on_release_1 says "plus the release-1 parts of 20
      splits", but 2.8.16 and 2.15.11 have no release-1 part, so it is 18.
    citation: >-
      release-phasing.yaml@f6bab34 (variants B and C; 2.1.6 release-1 reason; 2.9.1 release-5 part;
      D-INT-1 option A effect_on_release_1); SRC-001 p.51 S1-2.5.5-c04, p.76 S1-2.8.2-c02, p.84
      S1-2.9.1-c08, as quoted
  - severity: non-blocking
    text: >-
      [2.10.1 split and D-2.10.1, steward's claim partly contradicted] The claim "SRC-001's employee
      master has no field for the employee's manager" is true of the field table (p.91). But SRC-001
      puts the reporting line in the employee master: "A manager sees only their own reporting line,
      and the hierarchy is maintained in the employee master rather than assumed from the department"
      (S1-2.10.11-c08, p.96). So the approver of an expense claim ("approved by the manager",
      S1-2.5.2-c07) has a source in SRC-001. That source is not in the release-1 part of 2.10.1, and
      D-2.10.1 should cite it rather than say the master has no manager. Two more gaps in the
      release-1 employee record. (a) SRC-001's employee route for raising a claim is self-service,
      "Claim and reimbursement submission with attachment" (S1-2.10.11-c04, p.96), which is in release
      2. D-2.10.1 does not say how a claim is "Raised by an employee" in release 1: as a named user
      (S1-2.1.3-c05), or keyed by Finance on the employee's behalf. That choice affects licensing and
      segregation. (b) The record deferred to release 2 includes fields SRC-001 marks mandatory
      ("Yes": c03 to c06, c08, c10, c11, p.91). The split should say that those validations apply
      from payroll activation, so that a release-1 record is valid without them.
    citation: >-
      release-phasing.yaml@f6bab34 (2.5.2 reason; 2.10.1 split; D-2.10.1); SRC-001 p.49 S1-2.5.2-c07,
      p.91 S1-2.10.1 field table, p.96 S1-2.10.11-c04 and c08, as quoted
  - severity: non-blocking
    text: >-
      [2.1.7 needs-decision part, minor] The reason for D-2.1.7-c84 lists the parts of c84 deferred to
      releases 3 and 5. It omits "activating a second module later leaves the first unchanged and
      requires no migration" (S1-2.1.7-c84, p.17). Release 2 exercises that part when payroll or fixed
      assets are activated, and the release-2 loading task (R-06) stands against it. Recommend naming
      that part and its release in the partial-acceptance recommendation.
    citation: >-
      release-phasing.yaml@f6bab34 (2.1.7 needs-decision part; releases[1].loading_task; R-06);
      SRC-001 p.17 S1-2.1.7-c84 as quoted
created_at: "2026-10-21"
---

# Re-review of commit f6bab34, the steward's revision after REV-01M5EP1W4DYPM707EB79AYEYV1

Independent E4 re-review for WF-01M5D0SE8MMS39CTPTXH8ME1HT step 7 (L1 discovery). The subject is
`git diff f3b3b4c f6bab34 -- docs/requirements/`, which covers `release-phasing.yaml` v2,
`actors.yaml` v2, `glossary.yaml` v2, BO-02 v2, BO-03 v2, BO-05 v2 and the new BO-08 v1. The working
tree at HEAD (e0b9420) differs from f6bab34 only in `docs/governance/questions/Q-031.md`, so the
subject files I read are the committed ones.

**Verdict: non-blocking-findings.** Finding 1 of the earlier review, the blocking one, is closed.
D-INT-1 now presents options A (with branches (i) and (ii)), B and C, gives each one's effect on the
control-account rule (S1-2.2.1-c06, c21; S1-2.2.2-c12, c16), and has `chosen: none`. All 14 earlier
findings are closed. Five new findings are non-blocking. One should be fixed before D-INT-1 goes to
the product owner: the A(ii) claim takes one side of a tension within SRC-001 and leaves out
S1-2.2.2-c18. Nothing is invented, and the steward decides no business rule and no option. Every
new indicator, quote and bracketed value I checked traces to SRC-001.

## Status of the 14 earlier findings

| # | Earlier finding | Status | Evidence at f6bab34 |
| --- | --- | --- | --- |
| 1 | D-INT-1 premise (blocking) | Closed | D-INT-1 `against_interim_journals` quotes S1-2.2.1-c06 ("manual journals to them are blocked", p.23), c21 (p.24), S1-2.2.2-c12, c16 and S1-2.12.1-c05, c06. Option A states branches (i) and (ii) and names the qualified accountant. R-01 is rewritten, and Q-029 is at v2. New finding 1 qualifies the (ii) text |
| 2 | D-INT-1 scope | Closed | D-INT-1 `scope` adds S1-2.7.5-c04, c05 with S1-2.7.7-c20 ("uploaded where prepared outside it", p.73); S1-2.7.6-c07, c08, with the c12 question for the tax specialist; leases (S1-2.8.13-c13 to c15); and opening balances. `with` adds the tax specialist. 2.7.7 quotes the illustrative rows "EPF — employee and employer", "ETF", "Payroll income tax" and "Corporate income tax — instalment" (p.72). All verified |
| 3 | Q-029 readings | Closed | `for_interim_journals`, `against_interim_journals` and `for_a_module_not_yet_active` give the evidence on both sides, quoted correctly. `assurance_view` records my recommendation as advisory. New findings 1 and 2 refine A and C |
| 4 | Item master dependency | Closed | The 2.9.1 split assigns c02, c03, c10, c13, c14, c20, c24, c25 and c26 to release 1, exactly as recommended. The "Tax class Yes Standard, zero, exempt; drives 2.4" quote and S1-2.1.7-c70 are verified (pp.84, 16) |
| 5 | Expense claims need the employee master | Closed (new finding 4) | The 2.10.1 split gives release 1 c01, c02, c07 and c09, and D-2.10.1 offers the alternative of deferring. "Cr Employee payable" is verified as S1-2.5.13-c13 (p.55) |
| 6 | 2.16.2 fallback | Closed | The reason now says opening by manual journal is blocked (S1-2.2.1-c06, c21; S1-2.3-c01). The recommendation is release 1 for any entity with balances, and the method is for the qualified accountant. The release-2 `loading_task` and R-06 are recorded |
| 7 | 2.1.8 data-model clauses | Closed | c20, c22, c34, c42 and c43 are release 1 under the new `design-constraints` rule; quotes verified (pp.18-19). A-02 notes that Sinhala and Tamil are outside c52 to c56. R-02 is rewritten |
| 8 | Acceptance timing | Closed (new finding 5) | (a) S1-2.5.18-c01 is moved to release 5, quoting S1-2.5.6-c07. (b) c84 is needs-decision, with D-2.1.7-c84. (c) S1-2.1.5-c17 is needs-decision, with D-2.1.5-c17, and 2.11.2 notes the text-recognition point. (d) c57 is moved to release 1 with S1-2.7.2-c02 |
| 9 | Accuracy | Closed | (a) S1-2.1.7-c25 is cited "only for this description", in the rationale and in 2.1.2, 2.1.4 and 2.1.10. (b) 2.1.6 quotes all four bracketed entries of c17 and workbook values 17 to 20, which I verified in bracketed-values.yaml (n 17, 18). (c) R-01 now states the stock-issue part of BO-01's second indicator correctly |
| 10 | BO-03 faithfulness | Closed | The statement now admits entries raised from a rule or schedule. Each quote is verified: S1-2.6.5-c06, c08 (p.61), S1-2.6.16-c08 (p.67), S1-2.6.12-c01 (p.65), S1-2.2.7-c01, c11, c12 (p.30). "value, account, date and party ... never deleted" is common ground between S1-2.2.6-c10 and c14 (p.29). Q-007 is linked |
| 11 | Objectives coverage | Closed | (a) BO-08 is new. (b) BO-05 has an open item, and D-2.15.8 restates it. (c) BO-02 drops the duplicate indicator and adds S1-2.1.11-c02 and S1-2.11.7-c05, verified (pp.22, 100), with the bracket "[25]" kept as workbook value 161 |
| 12 | Entity and tenant | Closed | The glossary note on Entity and actors.yaml `notes[0]` no longer equate entity and tenant. OI-TENANT records the reading as one to decide, with product-owner, tech-lead and security-owner. "SRC-001 does not use the word tenant except ... (S1-2.1.1-c01)" is verified by search: only p.8 line 325. R-05 is added |
| 13 | Signatories | Closed | src001-signatories adds "(open: to be recorded as a decision, Q-004)" and quotes CLAUDE.md |
| 14 | Glossary | Closed | Retention is split into two terms. The records sense is `defined: false`, with S1-2.1.4-c08 and S1-2.11.4-c05 quotes verified (pp.10, 100). System-generated reversal is now `defined: false`, `paraphrased` |

## Focus items in the brief

**D-INT-1.** The three options are each complete in form: description, effect on release 1, effect
on the control-account rule, other effects, and dependencies. No option is preferred: the
`how_to_read_options` note says that writing the marks under A "is a convention of presentation, not a
recommendation", and `variants.basis` repeats it.

The two claims the brief asked me to test:

- **A(ii): "reclassification by journal is itself blocked by S1-2.2.1-c21".** Contradicted in part,
  as an unqualified statement. SRC-001 supports it only on one reading, and it omits S1-2.2.2-c18
  (new finding 1).
- **C: "the qualified accountant must confirm that interface postings (S1-2.1.6-c15) count as
  sub-ledger postings".** Confirmed, because c15 presupposes a module that C leaves inactive. Two of
  C's effects are unstated (new finding 2).

**Variants.** I recounted from the subsection marks. Under A, release 2 holds 26 sub-sections: 2.5.3,
2.8.1 to 2.8.7, 2.8.13 to 2.8.15, 2.10.2 to 2.10.12, 2.10.14, 2.10.15, 2.13.2 and 2.13.4. B moves 23
of them, which leaves 3. C moves 10, which leaves 16. The release-1 totals of 112 and 99 follow.

The dependencies respected are:

- the 2.8 and 2.10 introductions;
- the release-2 parts of 2.7.5, 2.8.16 and 2.10.1;
- the S1-2.1.6-c09 integration row under C;
- the changed recommendations for 2.8.8 and 2.7.6;
- 2.10.13 and 2.8.9 to 2.8.12 kept at their releases.

The three gaps are in new finding 3.

**New splits.**

- **2.9.1:** sound, as recommended.
- **2.10.1:** sound in principle, with the gaps in new finding 4.
- **2.1.5:** sound. c01 to c16 are release 1, and c17 alone is needs-decision, with an honest reason.
- **2.1.8:** sound. The new `design-constraints` rule limits release-1 acceptance "to what release 1
  data exercises", which is testable.

**New decisions.**

- **D-2.10.1:** the right owner, but its premise about the manager is partly contradicted (new
  finding 4).
- **D-2.1.5-c17:** well-formed.
- **D-2.1.7-c84:** well-formed, but its reason omits one part of c84 (new finding 5).

**BO-08.** All four indicators are SRC-001's own, and each `basis` matches the extraction word for
word:

- S1-2.1.11-c03, p.22;
- S1-2.14.14-c13, p.112, line 4814;
- S1-2.16.1-c03 and c04, p.119.

The brackets are kept, and the workbook values are 175 to 177. The open items name no identity
provider, encryption standard, hosting location or tenant model. The tenant-isolation gap is left open
for the product owner, the tech lead and the security owner, with no indicator proposed. The value
rationale fits S1-0-c01 ("accessed through a browser from any location with no local installation",
p.4). Nothing in BO-08 is invented.

**Invented content or decided business rules.** None found. The nearest are:

- the A(ii) mechanics, which take one side of an SRC-001 tension but route the method to the
  qualified accountant (new finding 1);
- the "no manager field" premise (new finding 4).

Neither is invented, and neither decides a rule. The c57 move and the design constraints are marks
in a proposal that the product owner decides.

## Outside this commit (note only)

- BO-07 cites S1-2.1.7-c84, which is now needs-decision (D-2.1.7-c84).
- Workbook value 4 says "per tenant". Q-031 is new.
- Q-031 (e0b9420) now exists, but actors.yaml OI-TENANT, phasing R-05 and the open item in BO-08
  still point only to OI-TENANT. They should cross-reference Q-031 at their next version.
- Q-029 v2 (0194386) lists S1-2.2.1-c06 and S1-2.2.2-c12 in `related`, but not c21, c16 or c18. Its
  option C does not carry the qualified-accountant dependency that D-INT-1 states. Align it with
  D-INT-1 when new finding 1 is fixed.

## Method

- **Reading.** I read the full diff of the four YAML and four objective files. I read
  release-phasing.yaml v2 in full: lines 1 to 1739, all 187 sub-sections and the variants.
- **Quotes.** I checked every new or changed quote against
  `docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt` by Grep, or by reading pp.4, 8, 10-11, 13,
  16-19, 22-25, 29-30, 49, 51, 55, 61, 65, 67, 69, 71-73, 75-77, 81-82, 84, 91, 96, 98-101, 106, 112,
  119 and 121. The only differences are line wraps.
- **Clause mapping.** I checked against `clause-index.yaml` the clause-to-text mapping for the
  clauses the new text leans on: S1-2.1.6-c08 to c16, S1-2.1.7-c02, c55 to c58, c79 to c84,
  S1-2.1.8-c20 to c22, c34, c42, c43, S1-2.2.2-c15 to c19, all of S1-2.9.1, all of S1-2.10.1,
  S1-2.10.11-c01 to c09, S1-2.8.13-c01 to c15, S1-2.12.1-c05, c06 and S1-2.7.7-c20.
- **Counts.** I made the counts by reading; my shell profile runs no ad hoc scripts.
- **Not repeated.** I did not repeat the checks the brief says the orchestrator has done: YAML
  parsing, the existence of every clause ID, the sub-section coverage, and check.py.

## Verification (observed)

- `git rev-parse f6bab34`: `f6bab34d3894857e0b5f4e5c9027f716afb7e16f`.
- `git diff --stat f6bab34 HEAD`: `docs/governance/questions/Q-031.md` only.
- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`.
  The result after writing it is in the handoff report.
