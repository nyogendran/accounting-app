---
id: REV-01M61QHQX58WSCVFQMT2EPXSRD
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:8bd453cc3846cdf9a85db05327f429657e5c597fcf4ae19b8019f8769b1401cc
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [NF7: CAP-06 still has a loose end, with no role granted and nothing settled] CAP-06's second
      bullet keeps V2.2's phrase "an administrator-facing setting" (S7-2.16.1-c23). Its third bullet
      says "INCR-001 grants no role the right to change a figure". Read side by side, a builder could
      still put an editable screen in front of the tenant administrator. The phrase is V2.2's own text,
      and the third bullet governs, so this does not settle Q-057. Three related gaps remain:
      (a) EXC-29 says figures "are set only through the test route the security owner accepts". But
      the EXC-27 test_route_proposal creates only "the tenant, one entity and one test administrator";
      it does not cover setting figures.
      (b) V2.2's acceptance for this, "an administrator raises a limit and the new level takes effect
      without a release, a redeployment or a restart" (S7-2.16.1-c29), cannot be run as written in
      INCR-001. Unlike CAP-05, CAP-13 and CAP-14, CAP-06 does not state this as a testability limit.
      (c) "Who" in the audit record of a scripted change will be a service identity, not a user.
      Fix: say in CAP-06 that in INCR-001 the setting is not editable by any tenant role (or not shown
      at all); add the setting of figures to the test route the security owner is asked to accept; and
      state the c29 testability limit.
    citation: >-
      GOV-SCOPE-INCR-001 v3 CAP-06 second and third bullets; EXC-27 test_route_proposal; EXC-29 reason;
      "Each is a configuration value with a default, an administrator-facing setting and an effective
      date" (SRC-007 p.133, S7-2.16.1-c23); "an administrator raises a limit and the new level takes
      effect without a release, a redeployment or a restart" (p.133, S7-2.16.1-c29)
  - severity: non-blocking
    text: >-
      [NF8: AP-10 and AP-13 have no interim position] v3 gives AP-12 an interim working assumption
      (WA-12), so its requirement can be written. AP-10 and AP-13 have none. AP-10 covers the
      reversal's series and, for a foreign-currency original, its rate. AP-13 covers the reversal's date
      when a reopened period and a later period are both open. So the CAP-12 requirements for those
      cases cannot be written until the owners answer. The scope makes this explicit ("open (AP-10)",
      "open (AP-13)"), so nothing is hidden or invented. But D-7 does not say whether these must be
      answered before INCR-001 Gate A, or whether the requirement may be written without them. Part of
      AP-13 is also a matter of fact rather than policy. A reversal dated in a reopened period does
      change that period's reported figures; the open point is whether that is acceptable, and the
      wording could say so. Fix: either give labelled interim assumptions, as with WA-12, or state in
      D-7 that AP-10 and AP-13 are preconditions of INCR-001 Gate A, for the qualified accountant with
      the product owner.
    citation: >-
      GOV-SCOPE-INCR-001 v3 CAP-12 sixth and seventh bullets, AP-10, AP-12, AP-13, WA-12, D-7; "The
      correction is dated in the current open period, so figures already reported for a closed period
      are never restated behind the reader's back" (SRC-007 p.38, S7-2.2.6-c12)
  - severity: non-blocking
    text: >-
      [NF9: small inconsistencies] (a) D-5 asks only the product owner to confirm EXC-06, EXC-07 and
      DEP-3. DEP-3's owners are the product owner and the qualified accountant, and D-1 requires "every
      role named in its owners field". D-5 should name the qualified accountant, as D-3, D-6 and D-7 do.
      (b) CAP-14's third and fourth bullets state the pending-journals-at-close rule twice. The two are
      consistent, but one should go. (c) bracketed_values item 6 lists the override [role] at
      S7-2.2.8-c07, but the override is excluded (EXC-12), so INCR-001 does not rely on that value.
    citation: >-
      GOV-SCOPE-INCR-001 v3 D-1, D-5, DEP-3 owners; CAP-14 third and fourth bullets; bracketed_values
      item 6; EXC-12
created_at: "2026-10-28"
---

# Delta review of GOV-SCOPE-INCR-001 v3 (commit efb9ff3)

This is an E4 delta review for WF-01M61MRRKX52P8XHG3NZXSPCZH, step 6. It follows
REV-01M61PXHZBS8N3YVQX2XDJHHWH and REV-01M61MRRKX52P8XHG3NZXSPCZJ, neither of which is edited here.

The subject is `docs/requirements/increments/GOV-SCOPE-INCR-001.md` v3 at commit
`efb9ff344c76580703ee9837c18a8abef63b6aa6`. `python tools/governance/trace.py explain
GOV-SCOPE-INCR-001` reports version 3, tier 1, no approval, and the normative hash
`sha256:8bd453cc3846cdf9a85db05327f429657e5c597fcf4ae19b8019f8769b1401cc`. That matches the brief.

I judged the v3 file itself. `git diff 160acb1 efb9ff3` was too large to display, and the guard would
not let me read the saved output, so I read the changed sections of the file directly.

`created_at` gives the date only, because my shell profile refuses `date`.

**Verdict: non-blocking-findings. On scope, v3 is sound for the product owner, with the qualified
accountant where named, to decide on.** It still needs F2 before any approval counts (Tier 1;
`stage0.allowed_tiers: [2, 3]`). Every blocking finding from both earlier reviews is resolved. The
three new findings are clarity fixes and none needs a decision. NF8 and NF9 (a) affect what the
decision-makers are told, so they are worth fixing before the scope is sent.

## Findings from REV-01M61PXHZBS8N3YVQX2XDJHHWH (v2)

| Finding | Status | Evidence in v3 |
| --- | --- | --- |
| NF1 CAP-06 settles Q-057 (blocking) | Resolved | CAP-06 now says "INCR-001 grants no role the right to change a figure: it is not an ordinary CAP-03 permission". It quotes c33 as "V2.2's text, not a settled behaviour". "Whether the system warns only, or refuses at a figure, is open", which matches EXC-29. The warning "names none until it is answered". The "administrator-facing setting" phrase is a remaining loose end (NF7). |
| NF2 errors found after close | Resolved | CAP-12's seventh bullet sets out (a) correction only by reopening, and none in an audit-locked period, (b) the date when several periods are open, and (c) the rate. AP-10 now covers the rate, AP-13 the date and restatement, and D-7 states the consequence. There is no interim position (NF8). |
| NF3 EXC-27 test route in the normative block | Resolved | EXC-27 has `approval_note` and `test_dependency`. D-1 says approving the scope "does not approve EXC-27's test_route_proposal". D-2 states the test dependency. The proposal still decides nothing. |
| NF4 one financial year | Resolved | D-3 asks whether INCR-001 is meant for production. CAP-13 and CAP-14 state the testability limits of the annual reset and the audit-lock trigger. |
| NF5 owners of the departures | Resolved | Each of DEP-1 to DEP-8 now has an `owners` field. DEP-1 to DEP-7 include the qualified accountant, as DEC-0010 condition 5 requires, and DEP-8 the tax specialist. D-1 requires "every role named in its owners field", and approval_consequence agrees. D-5 is the exception (NF9 a). |
| NF6 (a) normative statement | Resolved | "Q-001 to Q-057". |
| NF6 (b), (c) stale body | Resolved | "Not claimed" names both reviews and says v3 needs its own review. "Things to know before approving" lists WA-08 to WA-12 and AP-10 to AP-13. |
| NF6 (d) approval_consequence | Resolved | Rewritten; it reads correctly. |
| NF6 (e) bracket item 6 | Resolved | Item 6 is c07 (reopening and override) and item 7 is c12 (audit lock). See NF9 (c). |
| NF6 (f) S7-2.1.11-c01 reading | Resolved | Labelled WA-11, "labelled reading of the requirements engineer, pending product owner". It is cited in CAP-04's `relies_on`. |

## Findings marked partly resolved in the earlier reviews

| Finding | Status | Evidence in v3 |
| --- | --- | --- |
| B3 capacity versus licensing | Resolved | Through NF1 above. EXC-21 and CAP-06 count nothing against a licence. |
| Pending journals at close | Resolved | WA-12 adopts no close-blocking check, and approval into a closed period is refused under S7-2.2.8-c13 "until the period is reopened". It is labelled "an interim assumption, not a policy", pending the qualified accountant with the product owner, and AP-12 says "The owners may replace it". It holds a labelled interim position and does not settle policy. |
| Trace links (c) | Resolved | See NF6 (e). |
| Q-007 before Gate B | Not resolved; the reason is accepted, as before | The body puts it to the orchestrator. |

## What the brief asked to check

- **CAP-06.** No wording grants a role the right to change a figure, and "warn or refuse" is not
  settled. The "administrator-facing setting" phrase is V2.2's own text, and the third bullet
  overrides it, but it should say so (NF7).
- **Reversal-only correction (CAP-12, CAP-14, AP-13).** This is coherent and matches V2.2's
  correction table. A posted journal in an open period is reversed "in the current period"
  (S7-2.2.6-c15, p.38), and the closed-period route, the adjustment journal (c16), is held out with
  Q-055. "Cannot be corrected at all in an audit-locked period" follows from S7-2.2.8-c12. The gap is
  only that AP-10 and AP-13 have no interim position (NF8).
- **WA-11 and WA-12.** Each is labelled with its owner: WA-11 pending the product owner, and WA-12
  pending the qualified accountant with the product owner. WA-11 reconciles S7-2.1.11-c01 with
  S7-2.1.2-c13 without choosing between them. WA-12 is the least restrictive interim build and says
  so. Neither decides policy.
- **DEP owners against DEC-0010 condition 5.** These are correct; see NF5 above.
- **D-1 to D-7.** They agree with the capabilities and exclusions, except that D-5 omits the qualified
  accountant (NF9 a).
- **Questions.** A grep lists Q-001 to Q-057 at lines 376 to 432, once each. Eight are blocking, and
  each `leaves_unless_answered` names its exclusion: Q-007 EXC-11, Q-013 EXC-12, Q-014 EXC-09, Q-031
  EXC-01, Q-034 EXC-10, Q-055 EXC-28, Q-056 EXC-27, Q-057 EXC-29.

## Clauses checked

**Against the rendered PDF: none.** In the earlier delta the Read tool returned "pdftoppm is not
installed", and nothing has changed in this environment. I did not try again. The pages that B2, B3
and Q-055 to Q-057 rest on (pp.37, 38, 40 to 42, 133 to 136) still need to be checked on the PDF
before an owner decides.

**Against the extraction only**, in this delta:
- S7-2.16.1-c23 (p.133, line 5662-5663);
- S7-2.16.1-c29 (p.133, lines 5673-5676);
- S7-2.2.6-c12 and c15 (p.38);
- S7-2.2.8-c12 and c13 (p.41).

The earlier clause lists are in the two earlier records.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above. Both earlier reviews
  are shown as against an older hash (stale).
- `git log -2`: efb9ff3 (scope v3), then 2f0221b (the v2 delta review).
- The output of `python tools/governance/check.py` with this record in place is in the handoff report.
