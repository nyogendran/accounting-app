---
id: REV-01M61MRRKX52P8XHG3NZXSPCZJ
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:c6c15494a21468d8e3c9dd79acc97e662111fa197cc7425df2d74e1ac35db412
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [B1, omission: no tenant or first administrator can come into existence] CAP-01 defines the tenant
      as the organisation boundary. CAP-03 has roles "built by the entity's administrator", and CAP-04
      has the administrator keeping the segregation matrix. No capability says how a tenant, its first
      entity and its first administrator are created, or by whom. EXC-01 excludes "vendor or operator
      support access", and Q-031 v3 leaves open reading (c), "Tiqri, as the operator of the product,
      administers its customers' tenants (set-up, support, subscriptions under 2.16.5)". Without that
      start state, CAP-01 to CAP-04 cannot be specified or tested end to end. Whoever creates a tenant
      can also reach into it, which is SEC-2 ("what an operator of the product may reach in a tenant").
      So this is a security and product decision, not an editorial fix. Fix: add a capability or a named
      exclusion for tenant provisioning and the first administrator (the bootstrap), and name its owners:
      the security owner with the product owner. If it is excluded, state how INCR-001 test tenants are
      created, and that this route is not a production route.
    citation: >-
      GOV-SCOPE-INCR-001 v1 CAP-01, CAP-03, EXC-01, SEC-2; Q-031 v3 "Answer so far" reading (c) and
      "Open" first bullet; "Roles are built by the entity's administrator, not fixed by the vendor"
      (SRC-007 p.8, S7-2.1.2-c01)
  - severity: blocking
    text: >-
      [B2, SRC-007 contradicts itself on journals, and no question record covers it: escalate] CAP-12
      adopts two rules for the adjustment journal that cannot both hold. (1) "An adjustment journal is
      raised in the period's adjustment period and approved by the Finance manager role", from 2.2.5.
      (2) "A correction is a new entry (a reversal or an adjustment journal) ... dated in the current
      open period ... approved by someone other than the person raising it", and "An entry in a closed
      period is corrected by a dated adjustment journal in the current open period", from 2.2.6. Section
      2.2.8 defines one adjustment period per year, "dated at the year end, outside the twelve, for
      closing and audit adjustments". Reading R1: the 2.2.6 "adjustment journal" is the 2.2.5 type. Then
      a correction of a closed-period entry can only go into the year-end adjustment period, which
      contradicts "dated in the current open period" for every month but the last, and the Finance
      manager approves it. Reading R2: the 2.2.6 "adjustment journal" is a generic correcting entry in
      any open period, approved by any second user, and the 2.2.5 type is reserved for year-end closing
      and audit entries. That type is then idle in INCR-001, because year-end close is excluded (EXC-13).
      The two readings differ on the period, the approving role, the numbering series ("Journal, by
      journal type", S7-2.1.10-c04) and the separate and prior-period reporting. A grep of
      docs/governance/questions for "adjustment period" or "adjustment journal" finds only Q-011, which
      is about depreciation. This is accounting policy. Owner: the qualified accountant, with the product
      owner (DEC-0010 condition 5). Recommended resolution, for the owner to decide: raise a question,
      and until it is answered narrow CAP-12's correction route to a reversal approved by a second user,
      holding the adjustment journal type out of INCR-001 as an exclusion. The alternative is to state R2
      as a labelled working assumption pending the qualified accountant. Either way, CAP-14's "adjustment
      period" and "special audit adjustment period" need a stated use in INCR-001, or they go with EXC-13.
    citation: >-
      "Adjustment | Raised in the period's adjustment period for closing or audit adjustments,
      reportable separately | Finance manager" (SRC-007 p.37, S7-2.2.5-c05); "Entry in a closed period |
      Dated adjustment journal in the current open period, reported as a prior-period item" (p.38,
      S7-2.2.6-c16); "approved by someone other than the person raising it" (p.38, S7-2.2.6-c11); "An
      additional period dated at the year end, outside the twelve, for closing and audit adjustments"
      (p.40, S7-2.2.8-c04); "Year-end adjustment journals are raised in the adjustment period" (p.42,
      S7-2.2.8-c35); GOV-SCOPE-INCR-001 v1 CAP-12 includes, second and fifth bullets
  - severity: blocking
    text: >-
      [B3, capacity limits conflated with licensing, and the behaviour at a limit is undefined] EXC-21
      says "INCR-001 counts named users against a configurable limit only (CAP-06)", and CAP-01 makes
      "the number of entities a tenant may hold" a CAP-06 limit. V2.2 says the 2.16.1 figures are
      technical capacity, not entitlement. It says they are not limits enforced against the entity, and
      that the entity raises them itself. Read that way, a CAP-06 limit cannot cap users or entities
      commercially, and S7-2.1.3-c05 named-user licensing belongs to 2.16.5, which is excluded (Q-039).
      CAP-06 also does not say what happens at 100% of a limit. S7-2.16.1-c26 only rules out failing
      "without stating which limit was reached", and c33 says no figure is "a limit the software enforces
      against the entity". Nor does CAP-06 say whose administrator raises a limit: the tenant's own, as
      c34 reads, or the operator's, which matters on a shared multi-tenant platform whose total is open
      in Q-038. Two teams would build different things, a hard cap or a warning only, and acceptance
      criteria cannot be written without guessing. No question record covers this; Q-038 and Q-039 do
      not. Owners: the product owner, with the tech lead; the security owner for who may raise a
      tenant's limit. Fix: delete the licensing wording in EXC-21. State in CAP-06 the V2.2 reading
      (warn at the threshold, never refuse silently, not a licence cap, raised by the entity's
      administrator) as a labelled working assumption with those owners, or raise a question and hold
      the at-limit behaviour out.
    citation: >-
      "The figures in 2.16.1 are technical capacity, not commercial entitlement ... none of them is a
      licence cap" (SRC-007 p.136, S7-2.16.5-c23); "No figure in this section is a licence cap, a tier
      boundary or a limit the software enforces against the entity that bought it" (p.134,
      S7-2.16.1-c33); "An entity that outgrows a delivered default raises it itself" (p.134,
      S7-2.16.1-c34); "It does not fail silently, truncate a run, or reject a posting without stating
      which limit was reached" (p.133, S7-2.16.1-c26); GOV-SCOPE-INCR-001 v1 EXC-21, CAP-01 fourth
      bullet, CAP-06
  - severity: non-blocking
    text: >-
      [Departures from plain V2.2 text are not shown to the product owner one by one] D-1 asks for
      approval of "the narrowings" in general. Several exclusions remove rules that V2.2 states plainly,
      without a bracket or a question, and the scope does not say so. (a) EXC-08 removes the duplicate
      check, but c44 makes it a step of the only route ("follows the request, duplicate check, review and
      approval process ... There is no second route"). CAP-09 cites c44 and paraphrases it as "request,
      review and approval", dropping that step. (b) EXC-08 removes the ranked alternatives, but "A
      refusal is always accompanied by alternatives, ranked". (c) EXC-06 and D-5 contradict "An entity
      never begins with an empty chart" (c33). (d) EXC-15 removes the approver's amendment on the ground
      of "a threshold the specification leaves open". V2.2 makes the threshold "configurable", which is
      the kind of setting DEC-0010 admits, so the stated reason is weak. A product-owner choice is a
      valid reason. Fix: list each departure under D-1 or D-5 with the clause it sets aside. Fix CAP-09's
      paraphrase of c44.
    citation: >-
      S7-2.2.1-c44 (p.26); "A refusal is always accompanied by alternatives, ranked" (p.29,
      S7-2.2.2-c25); "An entity never begins with an empty chart" (p.26, S7-2.2.1-c33); "An amendment by
      the approver beyond a configurable threshold" (p.38, S7-2.2.6-c08); GOV-SCOPE-INCR-001 v1 CAP-09
      first bullet, EXC-06, EXC-08, EXC-15, D-1, D-5
  - severity: non-blocking
    text: >-
      [No account can be approved without a statement-line master that no capability builds] V2.2 lets
      no unmapped account be approved, and every route must carry the statement mapping before approval.
      CAP-08 says the statement lines, notes and cash-flow classifications are "data held by Finance",
      and AP-5 leaves their content open. No capability creates or maintains that data, or says who may
      change it and under what approval. So CAP-09 cannot approve its first account. Fix: add to CAP-08
      the maintenance of statement lines, notes and cash-flow categories as entity data, with its
      approval route, and cite S7-2.2.1-c47, which is currently uncited. The content stays AP-5's
      (qualified accountant, product owner).
    citation: >-
      "Statement line and note | Yes | An unmapped account cannot be approved" (SRC-007 p.30,
      S7-2.2.2-c44); "every account carries its statement mapping before it can be approved" (p.26,
      S7-2.2.1-c47); GOV-SCOPE-INCR-001 v1 CAP-08 sixth bullet, AP-5
  - severity: non-blocking
    text: >-
      [The year-end exclusion leaves the year boundary undefined] EXC-13 rests on "INCR-001 can run
      inside a financial year". But CAP-14 creates future periods and financial years. Audit lock is
      "Applied once the audit of that year is finalised". V2.2 allows the new year to be "opened and
      transacted in before the prior year is closed". And CAP-15 shows an account balance "for any period
      or date range". The scope does not say whether posting into a second financial year is allowed in
      INCR-001, or how income and expense balances are shown across a year end with no roll-up. Fix:
      state the limit (for example, no second year is opened in INCR-001) or the enquiry behaviour, as
      part of D-3, with the qualified accountant.
    citation: >-
      "The new financial year can be opened and transacted in before the prior year is closed" (SRC-007
      p.42, S7-2.2.8-c37); "Applied once the audit of that year is finalised" (p.41, S7-2.2.8-c12);
      GOV-SCOPE-INCR-001 v1 EXC-13, CAP-14 first bullet, CAP-15 second bullet
  - severity: non-blocking
    text: >-
      [Close behaviour that CAP-12 relies on is missing] EXC-14 removes the period-end checklist, whose
      tasks include "completion of journal approvals". CAP-14 does not say whether a period can be
      soft-closed or hard-closed while journals dated in it are still pending, or what happens when such
      a journal is approved after the close: refused under S7-2.2.8-c13, or redated, and by whom. Two
      readers will build this differently. Fix: state the behaviour, or name it as a question for the
      qualified accountant.
    citation: >-
      "completion of journal approvals" (SRC-007 p.42, S7-2.2.8-c40); "Posting is blocked into a closed
      period" (p.41, S7-2.2.8-c13); GOV-SCOPE-INCR-001 v1 EXC-14, CAP-14
  - severity: non-blocking
    text: >-
      [Testability: what a "reversal" is, and its series] CAP-12 names "a reversal" as a correction
      route. EXC-15 excludes "reversing on a schedule". V2.2's reversing journal type "Auto-reverses on
      the first day of the next period, or on a stated date". Numbering is separated "by journal type".
      The scope does not say whether a correction reversal is that type, a manual journal with the signs
      swapped, or a system-generated entry from the original, nor which series it draws from. Fix: define
      it in CAP-12 (for example, a system-generated reversal of the original, dated in the current open
      period, approved by a second user, in a named series). The choice is the qualified accountant's if
      it goes beyond a mechanical inverse.
    citation: >-
      "Reversing | Auto-reverses on the first day of the next period, or on a stated date | Second user"
      (SRC-007 p.37, S7-2.2.5-c04); "Journal, by journal type — manual, recurring, reversing,
      adjustment" (p.21, S7-2.1.10-c04); GOV-SCOPE-INCR-001 v1 CAP-12 fifth bullet, EXC-15
  - severity: non-blocking
    text: >-
      [Testability: the location element of a journal number] CAP-13 builds the series from, among other
      things, a "location code", which V2.2 takes "From the location the document is raised at".
      Location is a line-level dimension that V2.2 also uses for "document numbering series". A manual
      journal whose lines carry different locations has no single location. Fix: say where a journal's
      location for numbering comes from (a header value, the user's location, or not used for journals),
      or name it for the qualified accountant.
    citation: >-
      "Branch or location code | From the location the document is raised at" (SRC-007 p.21,
      S7-2.1.10-c13); "Location ... Branch and warehouse performance, document numbering series" (p.31,
      S7-2.2.3-c06); "Dimensions are carried at line level" (p.31, S7-2.2.3-c01)
  - severity: non-blocking
    text: >-
      [Testability: screen journal fields are undefined] CAP-12 gives no field list for a manual journal.
      The only field rules in V2.2 are the upload template's, and EXC-15 excludes upload: journal
      description mandatory, line description mandatory and "Not defaulted from the header", one
      currency per journal, an entity code the user may post to. AP-4 already uses the one-currency rule.
      Fix: either adopt the template's header and line rules for screen entry (cite S7-2.2.4-c37 to c56),
      or list the fields CAP-12 needs.
    citation: >-
      "Every line of one journal carries the same currency" (SRC-007 p.34, S7-2.2.4-c42); "Line
      description | Yes | Text | ... Not defaulted from the header" (p.35, S7-2.2.4-c48); "Journal
      description | Yes" (p.34, S7-2.2.4-c41)
  - severity: non-blocking
    text: >-
      [Unlabelled reading: the dimension "Mandatory on" column] CAP-10 applies the "Mandatory on" column
      "through the per-account rules, as data" and builds "no hard-coded mandatory rule per dimension".
      For cost centre, profit centre and department, V2.2 states the column plainly ("All income and
      expense lines"), and it also lets any dimension be set "mandatory, optional or blocked per account"
      (c09). Reading the column as a default that the account overrides, rather than a floor, is a
      reading. Q-044 covers location only. Fix: label it as a working assumption pending the qualified
      accountant, or extend Q-044.
    citation: >-
      "Cost centre | [CC-nn] | All income and expense lines" (SRC-007 p.31, S7-2.2.3-c02); "Any
      dimension can be made mandatory, optional or blocked per account" (p.32, S7-2.2.3-c09); Q-044 v1;
      GOV-SCOPE-INCR-001 v1 CAP-10 fourth bullet
  - severity: non-blocking
    text: >-
      [Trace link errors] (a) S7-2.1.2-c27 (Auditor) is cited both in CAP-04 (in scope) and in EXC-01
      (excluded). (b) S7-2.1.11-c01 is linked but appears in no capability or exclusion. It also conflicts
      with S7-2.1.2-c13, under which the system "warns or blocks, as the administrator sets per rule".
      CAP-04 should cite it, with the reading that it applies where a rule is set to block. (c)
      bracketed_values cites S7-2.2.8-c11 for "[role] reopening and audit locking". The hard-closed row
      c11 has no bracket. The brackets are in the state diagram (c07, "override by [role] only", "reopen —
      approval by [role]") and in the audit-locked row (c12, "[role], with approval"). (d) The "[role]"
      that may key a code (S7-2.2.2-c05), which CAP-09 relies on, is missing from bracketed_values. (e)
      EXC-08 cites S7-2.2.2-c12 (reserved code or range), which matches nothing in its "what", so
      reserved codes are neither in scope nor excluded by name. (f) Name uniqueness within a group,
      which EXC-09 says "stays in CAP-08", is S7-2.2.2-c35, and it is not cited.
    citation: >-
      GOV-SCOPE-INCR-001 v1 CAP-04 and EXC-01 clause lists, links (S7-2.1.11-c01), bracketed_values item
      6, EXC-08; SRC-007 p.9 lines 361-362 and p.23 line 980; p.41 lines 1734-1736 and 1747-1749; p.28
      line 1178; p.30 line 1250
  - severity: non-blocking
    text: >-
      [CAP-07 cites more than it builds; future constraint] CAP-07 cites c09 and c23, which store the
      reporting-currency amount and the "period lock state at posting" on the transaction, "not derived
      later". CAP-07 stores only the transaction and functional amounts and omits the lock state. If
      groups arrive later (release 3), the reporting amount on every INCR-001 transaction would have to
      be derived afterwards, which c23 forbids. The tax code on journal lines (S7-2.2.4-c57, EXC-19) is
      a similar later addition to posted lines. This is an architectural concern for Gate B, not a scope
      error. Fix: name both in stack_dependencies or as a Gate B design input (tech lead), and either cite
      c09 and c23 as partial or store the lock state.
    citation: >-
      "All three are stored on the transaction, not derived later" (SRC-007 p.44, S7-2.2.9-c23); "period
      lock state at posting" (p.43, S7-2.2.9-c09); GOV-SCOPE-INCR-001 v1 CAP-07, EXC-17
  - severity: non-blocking
    text: >-
      [Over-wide exclusions] (a) EXC-17 excludes all of S7-2.2.9-c18. Its first sentence, "Rates for a
      closed or locked accounting period cannot be changed", is plain, and both manual rates (CAP-07) and
      period close (CAP-14) are in scope. Keep that sentence, and exclude only the rate-table lock and
      unlock. (b) EXC-10 removes every change to the control flag. But c67, c47 and c51 agree that an
      account with no transactions and no balance can change through the 2.2.2 approval; Q-034 is
      contested only once history exists. The uncontested part could stay.
    citation: >-
      SRC-007 p.44 line 1865 (S7-2.2.9-c18); p.27 line 1159 (S7-2.2.1-c67); p.30 lines 1279 and 1287
      (S7-2.2.2-c47, c51); Q-034 v1
  - severity: non-blocking
    text: >-
      [Policy owners and stated values] (a) AP-8 names only the qualified accountant. DEC-0010 condition
      5 and the scope's own note require the qualified accountant and the product owner for accounting
      policy. (b) AP-9 presents as open who may open and close periods, but V2.2's "Set by" column names
      the "Finance manager" for Open, Soft closed and Hard closed. Only reopening approval and audit lock
      are bracketed. Fix both, citing c09 to c12.
    citation: >-
      DEC-0010 v1 condition 5; SRC-007 p.41 lines 1738-1749 (S7-2.2.8-c09 to c12); GOV-SCOPE-INCR-001 v1
      AP-8, AP-9
  - severity: non-blocking
    text: >-
      [CAP-05 cites acceptance that INCR-001 cannot exercise] CAP-05 cites S7-2.1.11-c02, "An amended
      posted document shows a complete before-and-after entry". INCR-001 allows no amendment of a posted
      entry (CAP-12, EXC-11), so this can only be tested on master data. CAP-05's login and failed-login
      events depend on the authentication mechanism that EXC-02 excludes, so they are testable only
      after SEC-1. Fix: state both dependencies.
    citation: >-
      SRC-007 p.23 line 981 (S7-2.1.11-c02); p.10 line 412 (S7-2.1.4-c04); GOV-SCOPE-INCR-001 v1 CAP-05,
      EXC-02, EXC-11
  - severity: non-blocking
    text: >-
      [Q-007 is correctly blocking, but excluding it fixes the data model] Q-007 itself says "Whether
      posted lines can ever change in place is an early data-model decision". Excluding it means
      INCR-001's posted-line model is designed before the answer. Reading (B), which allows in-place
      edits, would then be a data-model change request. Recommendation for the orchestrator: ask the
      qualified accountant to answer Q-007 before INCR-001 Gate B, even though INCR-001 Gate A does not
      need it.
    citation: >-
      Q-007 v1 "Why it matters" and readings (A) to (C); GOV-SCOPE-INCR-001 v1 EXC-11
created_at: "2026-10-28"
---

# Independent review of GOV-SCOPE-INCR-001 v1 (commit c88927d)

E4 review for WF-01M61MRRKX52P8XHG3NZXSPCZH step 2, as required by DEC-0010 condition 1. The subject is
`docs/requirements/increments/GOV-SCOPE-INCR-001.md` at commit
`c88927d31401c80b141932fd0b79b1dba6b1c691`. My shell profile refuses `approvals.py hash`. `python
tools/governance/trace.py explain GOV-SCOPE-INCR-001` reports the normative hash as
`sha256:c6c15494a21468d8e3c9dd79acc97e662111fa197cc7425df2d74e1ac35db412`, which matches the brief.
`created_at` gives the date only, because the shell profile also refuses `date`. The review was written
after the subject commit (2026-10-28T16:29:43Z).

**Verdict: blocking-findings. The scope is not yet sound for the product owner to decide on.** Most of
it holds up. The cut is disciplined. No in-scope capability posts from a sub-ledger. The five blocking
questions are each matched by a named exclusion. Every working answer from the governance owner is
labelled. But three points need fixing first:

- B1: there is no way to create a tenant or its first administrator, and that is a security decision.
- B2: SRC-007 contradicts itself on the adjustment journal inside CAP-12, and no question record covers
  it. This is escalated.
- B3: the capacity limits are confused with licensing, and the behaviour at a limit is undefined.

Findings: 3 blocking, 14 non-blocking.

## The eight challenge areas

1. **Independence (DEC-0010).** No capability depends on Q-029. I checked each capability's
   `independence` statement against the clauses: CAP-11 builds the three levels without choosing an
   option in Q-029, and CAP-12 has no sub-ledger posting. Q-032 is rightly not-blocking: Enforced
   behaves the same under both readings, and the scope states that a contrary answer removes Not applied
   and Advisory by change request. Q-033 is rightly not-blocking: D-6 removes the delivered defaults, so
   no set-up level is a lowering "from Enforced". Note, though, that V2.2's own default for a "Single
   entity, general ledger only" is Not applied (S7-2.2.1-c58, p.27), not the Advisory of WA-03.
   **Re-classifications: none of Q-001 to Q-054.** Three matters are blocking for the capability they
   touch, but no question record exists for them: tenant provisioning (B1, which partly overlaps Q-031
   reading (c)), the adjustment journal (B2), and limit enforcement (B3). I recommend that the
   orchestrator raise B2 and B3 as questions, and B1 if the security owner wants one.
2. **Traceability.** I sampled at least two clauses per capability against the extraction; the list
   is below. Every sampled clause supports what the capability claims, with these exceptions: CAP-09's
   paraphrase of S7-2.2.1-c44, CAP-07's citations of c09 and c23, CAP-05's citation of S7-2.1.11-c02,
   and the link errors in the trace-link finding (S7-2.1.2-c27, S7-2.1.11-c01, S7-2.2.8-c11, S7-2.2.2-c12, the missing c05 bracket
   and c35). Clauses missing from foundation capabilities: S7-2.2.1-c47, S7-2.2.2-c35,
   S7-2.2.2-c21 (the chart an entity runs on is set at set-up by [role] and shown on the chart screen),
   and S7-2.1.11-c01. Q-007, Q-013 and Q-014 still cite S1 clauses. I checked the scope's S7 mapping
   against the S1 text they quote: S7-2.2.6-c10 and c14 (p.38), S7-2.2.8-c30 (p.42), S7-2.2.1-c05 (p.24)
   and S7-2.2.2-c43 (p.30) carry the same words. No error.
3. **Exclusions.** EXC-02 to EXC-05, EXC-07, EXC-09, EXC-11, EXC-12, EXC-16, EXC-18 to EXC-20 and
   EXC-22 to EXC-26 are justified as written. The following leave a capability incomplete or depart
   from plain text without saying so: EXC-01 (B1); EXC-13 (the year-end boundary finding); EXC-14 (the
   pending-journals-at-close finding); EXC-06, EXC-08 and EXC-15 (the departures-from-plain-text
   finding); EXC-10 and EXC-17 (the over-wide-exclusions finding); EXC-21 (B3).
4. **Working assumptions.** WA-01 to WA-08 are labelled, each with its pending owner, as DEC-0010
   condition 3 requires. There are three unlabelled readings: the dimension "Mandatory on" column (the
   dimension-column finding), the meaning of the "adjustment journal" (B2), and the at-limit behaviour
   and who may raise a limit (B3).
5. **Invention.** The scope adopts no accounting policy, tax treatment or security assumption as its
   own. Every point names an owner role (AP-1 to AP-9, SEC-1 to SEC-3), except that AP-8 lacks the
   product owner. The EXC-03 constraint (no production tenant data where residency is required until
   Q-028 is settled) is a precaution under Q-028's owner, not an invented rule. B1 and B3 are the places
   where a security or product decision is missing rather than assumed.
6. **Testability.** CAP-02, CAP-03, CAP-04, CAP-08, CAP-11 and CAP-15 are bounded enough to write
   requirements from. The others need the fixes named in the findings: CAP-01 (B1); CAP-06 (B3); CAP-12
   (B2, and the reversal and journal-field findings); CAP-13 (the numbering-location finding); CAP-14
   (the year-end and pending-journal findings); CAP-09 (the statement-line finding); CAP-10 (the
   dimension-column finding); CAP-05 (its own finding).
7. **Tier and process.** Tier 1 is correct: the scope covers posting, numbering, periods, audit,
   authorisation, isolation, money and rounding (methodology.md, risk tiers). The approval consequence
   is stated correctly. authority-matrix.yaml has `stage0.allowed_tiers: [2, 3]`, so a Stage 0 (E1-op)
   approval cannot count, and approval needs F2 with Shifan Cader's own identity. DEC-0010 is Approved
   (APR-01M61ME5F96WP1KB4TVNBAH65X, valid). One process note: D-3 (year-end) and the B2 resolution touch
   accounting policy. Under DEC-0010 condition 5 they need the qualified accountant as well as the
   product owner, but the D-list asks only the product owner.
8. **Internal consistency.** The question-classification summary (5 blocking, 49 not-blocking) matches
   the entries. The five blocking questions match EXC-01 and EXC-09 to EXC-12. D-1 to D-6 match their
   exclusions. The body agrees with the normative block. The inconsistencies found are S7-2.1.2-c27,
   cited both in scope and excluded; the two incompatible adjustment-journal rules inside CAP-12 (B2);
   and EXC-09's claim that name uniqueness "stays in CAP-08" without the clause that states it (c35).

## Clauses checked

**Against the rendered PDF: none.** The Read tool could not render the PDF because `pdftoppm` is not
installed. No rendered pages are stored under `docs/sources/SRC-007-spec-v2.2/`. Every check below is
against the extraction `docs/sources/SRC-007-spec-v2.2/extracted/spec-v2.2.txt` through the clause
index. The pages that B2 and B3 rest on should be confirmed on the PDF before an owner decides: p.37
(the 2.2.5 table, whose three columns are flattened in the extraction), pp.40 to 42, pp.133 to 136.

**Against the extraction (text and page via the index):**

- CAP-01: S7-2.1.1-c01; S7-2.14.1-c08; S7-2.14.2-c01, c14, c15.
- CAP-02: S7-2.1.3-c05; S7-2.1.4-c03.
- CAP-03: S7-2.1.2-c02, c03, c07, c09, c10, c11.
- CAP-04: S7-2.1.2-c13, c14, c16, c17, c18, c19, c26, c27; S7-2.1.11-c01.
- CAP-05: S7-2.1.4-c01, c04, c07, c08; S7-2.1.11-c02.
- CAP-06: S7-2.16.1-c07, c14, c21, c22, c23, c24, c25, c26, c33, c34, c39.
- CAP-07: S7-2.2.9-c02, c03, c04, c06, c09, c11, c12, c15, c17, c18, c21, c23, c37.
- CAP-08: S7-2.2.1-c02, c03, c04, c05, c06, c13, c15, c17, c31, c47, c51, c52; S7-2.2.2-c42 to c49;
  S7-2.2.4-c47.
- CAP-09: S7-2.2.1-c44; S7-2.2.2-c02 to c11, c14, c15, c17, c20, c21, c25, c35, c50, c51, c52, c54.
- CAP-10: S7-2.2.3-c01, c02, c06, c09, c11, c12, c14.
- CAP-11: S7-2.2.1-c52 to c68.
- CAP-12: S7-2.2.4-c01, c16, c41, c42, c48, c57; S7-2.2.5-c01, c04, c05, c08; S7-2.2.6-c01, c03 to
  c16, c22, c28.
- CAP-13: S7-2.1.10-c01, c04, c12, c13, c14, c18, c20, c23, c25, c27, c28, c29, c31, c38, c42.
- CAP-14: S7-2.2.8-c02 to c15, c25 to c28, c30, c35, c37, c40, c44 to c48; S7-2.14.2-c19.
- CAP-15: S7-2.2.4-c01, c77.
- Exclusions and cross-checks: S7-2.2.1-c33; S7-2.16.5-c18 to c23; S7-2.2.2-c25, c47, c51.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above, status Proposed, v1,
  tier 1, no approval.
- `python tools/governance/trace.py explain DEC-0010`: Approved, approval valid.
- `git log -3`: the subject commit is c88927d31401c80b141932fd0b79b1dba6b1c691.
- The result of `python tools/governance/check.py` with this record in place is in the handoff report.
