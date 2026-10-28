---
id: REV-01M61PXHZBS8N3YVQX2XDJHHWH
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:329d893ebf3350eac38b01bae1fdbada7c265204b24b7cd89796f52945878f6e
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [NF1, CAP-06 settles the open question Q-057 while saying it is open; B3 is only partly resolved]
      CAP-06 says "Which role may change a tenant's figure, the tenant's own administrator or the
      operator, is open (Q-057, EXC-29)". The same sentence then says "the permission to do so is an
      ordinary permission under CAP-03". Under CAP-03, "Roles are built by the entity's administrator",
      and INCR-001 has no operator role, because EXC-01 and EXC-27 exclude operator access. So the only
      people who could hold that permission are the tenant's own users. In effect, the tenant
      administrator raises its own share of a shared platform: the self-service reading of
      S7-2.16.1-c34. That is the security owner's open point in Q-057 ("Who may raise a figure is the
      security owner's"), and the scope says "no security assumption is made". The warning has the same
      problem: it names "the holder of the permission above".
      A second inconsistency: CAP-06's first bullet states as fact that no figure "is ... a limit the
      software enforces against the entity", while EXC-29 holds open "warn only, or refuse".
      Fix (the requirements engineer chooses which):
      (a) hold the change of a figure out with EXC-29. Until Q-057 is answered, figures are set only
      through the non-production route that the security owner accepts.
      (b) label the change as a working assumption pending the security owner and the product owner.
      In either case, quote c33 in CAP-06 as V2.2's text, not as a settled behaviour, or remove "refuse"
      from EXC-29 and say so under D-2.
    citation: >-
      GOV-SCOPE-INCR-001 v2 CAP-06 first, third and fourth bullets; EXC-29; EXC-01; EXC-27; CAP-03 first
      bullet; security_points note; Q-057 v1 "Open"; "An entity that outgrows a delivered default raises
      it itself" (SRC-007 p.134, S7-2.16.1-c34)
  - severity: non-blocking
    text: >-
      [NF2: correcting an error found after a close is undefined now that only reversal remains] CAP-12
      allows "a reversal of a posted journal in an open period", dated "in the current open period".
      EXC-28 holds out "correction of an entry in a closed period". CAP-14 allows a closed period to be
      reopened. The scope does not say:
      (a) whether reopening a period, then reversing, is the intended route for an error found after
      close. If it is, the reported figures of that period are restated, which is what S7-2.2.6-c12
      exists to prevent;
      (b) which date a reversal takes when the original's period has been reopened and a later period is
      also open. "Current open period" is ambiguous once more than one period is open;
      (c) at which rate a foreign-currency reversal is translated. A "mechanical inverse" uses the
      original rate, while S7-2.2.9-c21 converts "at the rate in force on the document date".
      Fix: add (a) and (b) to AP-10 or to a new point, and (c) to AP-10, all for the qualified accountant
      with the product owner. State the consequence under D-7: until Q-055 is answered, an error found
      after close can be corrected only by reopening.
    citation: >-
      "The correction is dated in the current open period, so figures already reported for a closed
      period are never restated behind the reader's back" (SRC-007 p.38, S7-2.2.6-c12); "converted at the
      rate in force on the document date" (p.44, S7-2.2.9-c21); GOV-SCOPE-INCR-001 v2 CAP-12 sixth bullet,
      CAP-14 fourth bullet, EXC-28, AP-10, D-7
  - severity: non-blocking
    text: >-
      [NF3: the EXC-27 test-route proposal sits inside the block the product owner approves] The text
      labels itself clearly: "PROPOSAL for the security owner, not a decision, and not a production
      route". It does not decide a security matter. But it sits in `normative.exclusions`, and D-1 asks
      the product owner to "Approve the scope below as proposed". An approval of the scope could
      therefore be read as approving a security arrangement, including "fixed test credentials", which
      is not the product owner's to approve. Also, testing CAP-01 to CAP-05 depends on the security
      owner accepting some test route, and the scope does not state this dependency. Fix: say in D-1 or
      D-2 that approving the scope does not approve test_route_proposal, which is decided under Q-056,
      or move the proposal to the body. Then state the test dependency, as CAP-05 does for SEC-1.
    citation: >-
      GOV-SCOPE-INCR-001 v2 EXC-27 test_route_proposal; D-1; D-2; Q-056 v1 "Open"; authority-matrix.yaml
      v2 (security owner)
  - severity: non-blocking
    text: >-
      [NF4: what follows from opening one financial year] The D-3 limit is coherent: no posting crosses a
      year end, and CAP-15 shows no balance across one. It has consequences the scope does not state.
      (a) If INCR-001 carries live books, posting stops at the entity's first year end until year-end
      close arrives. D-3 should say whether INCR-001 is meant for production use.
      (b) Two behaviours cannot be exercised within one year: CAP-13's reset rule "annually at the
      financial year end", and audit lock, which V2.2 applies "once the audit of that year is
      finalised". State these as testability limits, as CAP-05 does.
    citation: >-
      GOV-SCOPE-INCR-001 v2 CAP-14 second bullet, CAP-13 second bullet, D-3, DEP-5; "Applied once the
      audit of that year is finalised" (SRC-007 p.41, S7-2.2.8-c12); "Reset rule | Never, annually at
      the financial year end, or at the start of each period" (p.22, S7-2.1.10-c18)
  - severity: non-blocking
    text: >-
      [NF5: the departures are confirmed by the product owner alone] D-1 asks the product owner to
      confirm DEP-1 to DEP-8 one by one. Several are not hers alone. DEP-5 needs "a retained-earnings
      policy (qualified accountant and product owner)". DEP-6 needs Q-033, which the qualified accountant
      owns. DEP-7 rests on WA-10, which is pending the qualified accountant. DEP-8 is tax, which belongs
      to the tax specialist. DEC-0010 condition 5 requires the qualified accountant for accounting
      policy. D-3, D-6 and D-7 already name the qualified accountant; D-1 does not. Fix: give each DEP an
      owners field, as the AP items have.
    citation: >-
      DEC-0010 v1 condition 5; GOV-SCOPE-INCR-001 v2 D-1, DEP-5 to DEP-8, WA-10
  - severity: non-blocking
    text: >-
      [NF6: stale and inconsistent text left by the revision]
      (a) normative.statement still reads "the classification of every question Q-001 to Q-054". This is
      normative text, and the classification now covers Q-001 to Q-057.
      (b) The body section "Not claimed" still says "The assurance review is a later step
      (REV-01M61MRRKX52P8XHG3NZXSPCZJ is reserved for it)".
      (c) "Two reads I had to make" omits WA-09, WA-10 and AP-10 to AP-12.
      (d) tier_proposal.approval_consequence opens with a garbled "Authority-matrix (the product owner's
      approval ...".
      (e) bracketed_values item 6 gives c07 as the source of "the [role] with approval that audit-locks a
      period". c07's brackets are the override and the reopening approval; the audit-lock role is c12,
      which item 7 already lists.
      (f) CAP-04's reading of S7-2.1.11-c01 (it applies only where the rule is set to block) is a
      reasonable reconciliation with c13, but it is a reading and is not labelled as one. Label it, with
      the product owner as owner.
    citation: >-
      GOV-SCOPE-INCR-001 v2 normative.statement, body "Not claimed" and "Things to know before
      approving", tier_proposal, bracketed_values items 6 and 7, CAP-04 fifth bullet; SRC-007 p.41 lines
      1734-1736 and 1747-1749
created_at: "2026-10-28"
---

# Delta review of GOV-SCOPE-INCR-001 v2 (commit 160acb1)

This is an E4 delta review for WF-01M61MRRKX52P8XHG3NZXSPCZH, step 4. It follows
REV-01M61MRRKX52P8XHG3NZXSPCZJ, which this record does not edit.

The subject is `docs/requirements/increments/GOV-SCOPE-INCR-001.md` v2 at commit
`160acb1d62478c496d4e11ac713cbbf73844d406`. `python tools/governance/trace.py explain
GOV-SCOPE-INCR-001` reports version 2, tier 1, no approval, and the normative hash
`sha256:329d893ebf3350eac38b01bae1fdbada7c265204b24b7cd89796f52945878f6e`. That matches the brief.
`git diff c88927d 160acb1 --stat` shows changes to the subject, Q-055 to Q-057, and the earlier review
record. I judged the v2 file itself, not its change table.

`created_at` gives the date only, because my shell profile refuses `date`.

**Verdict: blocking-findings, one blocking finding.** The revision fixes B1, B2 and 13 of the 14
non-blocking findings fully or in part. One new blocking problem remains: CAP-06 settles the security
point that Q-057 holds open (NF1). The other new findings are small. A v3 that fixes NF1 and the stale
normative statement (NF6 a) should be reviewable as a short delta.

## Earlier findings

| Finding | Status | Evidence in v2 |
| --- | --- | --- |
| B1 tenant bootstrap | Resolved | EXC-27 and Q-056 (blocking, owner security owner) hold out the production route. CAP-01 states that no production route creates a tenant. The test route is marked as a proposal; see NF3 for where it sits. |
| B2 adjustment journal | Resolved | EXC-28 and Q-055 (blocking, owner qualified accountant). CAP-12 now covers manual journals corrected by reversal; CAP-14 drops the two adjustment periods. S7-2.2.5-c05 and S7-2.2.6-c16 are removed from CAP-12, and EXC-28 cites c05, c16, S7-2.2.8-c04, c05 and c35. Journals and periods remain coherent, apart from NF2. |
| B3 capacity versus licensing | Partly resolved | The licensing wording in EXC-21 is gone, CAP-06 cites c33 and S7-2.16.5-c23, and EXC-29 and Q-057 hold out the behaviour at a limit and who raises it. But CAP-06 makes changing a figure "an ordinary permission under CAP-03", which settles Q-057 (NF1). |
| Departures from plain text | Resolved | DEP-1 to DEP-8 are listed. D-1 no longer approves the departures in bulk. CAP-09 quotes c44 with the duplicate check. The EXC-15 reason is replaced. See NF5 on who confirms each departure. |
| Statement-line master | Resolved | CAP-08 adds the statement lines, notes and cash-flow categories as entity data, with the approval route proposed under AP-5 (qualified accountant and product owner). It cites S7-2.2.1-c47. |
| Year boundary | Resolved | CAP-14 proposes one financial year per entity, CAP-15 shows no balance across a year end, D-3 names the qualified accountant, and DEP-5 is listed. See NF4 for the consequences. |
| Pending journals at close | Partly resolved | Approving a journal into a closed period is refused under S7-2.2.8-c13. Whether a period may close while journals in it are pending is left open as AP-12, with no interim behaviour, so that requirement still cannot be written. A labelled interim assumption would finish this. |
| Reversal semantics | Resolved | CAP-12 defines the reversal as a system-generated mechanical inverse. It is not the scheduled reversing type. The series is AP-10. See NF2 for the rate and date. |
| Numbering location | Resolved | CAP-13 proposes not using the location element in journal series. AP-11 names the qualified accountant and the product owner. |
| Journal fields | Resolved | CAP-12 gives a field list taken from S7-2.2.4-c37 to c56, labelled WA-09. The decimal places come from the currency, not the template's [2]. I checked c37, c38, c39, c41, c42, c43, c48 and c49 against the extraction. |
| Dimension column | Resolved | WA-10 (pending the qualified accountant) and DEP-7. |
| Trace links (a) to (f) | Partly resolved | (a) EXC-01 no longer cites c27. (b) S7-2.1.11-c01 is in CAP-04. (d) c05 is in bracketed_values. (e) EXC-08 names reserved codes. (f) c35 is cited, and EXC-07 adds c21. (c) is corrected for c12, but item 6 still gives c07 as the source of the audit-lock role (NF6 e). |
| CAP-07 | Resolved | The period lock state is stored. c09 and c23 are cited as partly built. A Gate B input is added to stack_dependencies. |
| Over-wide exclusions | Resolved | CAP-07 keeps the first sentence of c18. EXC-10 is narrowed, and a flag change on an account with no transactions and no balance stays in CAP-09 (S7-2.2.1-c67). |
| Policy owners | Resolved | AP-8 names the product owner. AP-9 states the Finance manager as "Set by" (c09 to c11). |
| CAP-05 testability | Resolved | Fifth bullet of CAP-05. |
| Q-007 before Gate B | Not resolved, reason accepted | The body puts it to the orchestrator. It is a recommendation outside the scope, so leaving the scope unchanged is acceptable. |

## The areas the brief asked about

- **EXC-27.** It decides nothing: the text says "PROPOSAL ... not a decision". Its place in the
  normative block is the only issue (NF3).
- **CAP-12 with reversal only, and EXC-28.** Journals and periods are coherent and testable: manual
  journals, second-user approval, reversal in an open period, and four period states without the
  adjustment periods. What is missing is a route for errors found after close (NF2).
- **CAP-06.** The setting, the audit record and the warning are sound, except for the permission and
  the enforcement wording (NF1).
- **CAP-08 statement-line master.** Sound. The route is a proposal with owners (AP-5).
- **D-3 year boundary.** Sound, with the consequences in NF4.
- **WA-09, WA-10 and AP-10 to AP-12.** Each is labelled, with the qualified accountant and the product
  owner as owners. Nothing is invented: WA-09 adopts V2.2's own template rules, and WA-10 is a reading
  of c02 to c09. CAP-04's reading of S7-2.1.11-c01 is the one reading left unlabelled (NF6 f).
- **Questions.** The classification lists 57 entries; a grep counts 57, Q-001 to Q-057, each once. Of
  these, 8 are blocking and 49 not-blocking, which matches the summary. Each blocking question has a
  matching exclusion: Q-007 EXC-11, Q-013 EXC-12, Q-014 EXC-09, Q-031 EXC-01, Q-034 EXC-10, Q-055
  EXC-28, Q-056 EXC-27, Q-057 EXC-29. The owners of Q-055 (qualified accountant), Q-056 (security
  owner) and Q-057 (product owner) match the question records. I would not re-classify any question.
- **Consistency.** The capabilities, EXC-01 to EXC-29, DEP-1 to DEP-8 and D-1 to D-7 agree with one
  another, except for NF1 (CAP-06 against EXC-29), NF5 (DEP owners) and the stale text in NF6.

## Clauses checked

**Against the rendered PDF: none.** I tried p.134 again, and the Read tool returned "pdftoppm is not
installed". The pages that B2, B3 and NF1 rest on (pp.37, 38, 40 to 42, 133 to 136) still need to be
checked on the PDF before an owner decides.

**Against the extraction only**, in this delta:
- S7-2.2.4-c37, c38, c39 (p.34, lines 1459-1470);
- S7-2.2.4-c41, c42, c43, c48, c49 (pp.34-35);
- S7-2.2.6-c11, c12, c16 (p.38);
- S7-2.2.9-c21 (p.44);
- S7-2.2.8-c07, c12 (p.41);
- S7-2.1.10-c18 (p.22);
- S7-2.16.1-c33, c34 (p.134);
- S7-2.16.5-c23 (p.136);
- S7-2.2.1-c67 (p.27).

The earlier review's checks are listed in REV-01M61MRRKX52P8XHG3NZXSPCZJ.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above. The earlier review
  is shown as against an older hash (stale).
- `git log -2`: the subject commit 160acb1 and the questions commit e4b9215.
- The output of `python tools/governance/check.py` with this record in place is in the handoff report.
