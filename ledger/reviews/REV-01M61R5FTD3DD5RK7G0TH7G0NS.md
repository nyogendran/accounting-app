---
id: REV-01M61R5FTD3DD5RK7G0TH7G0NS
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:3c1ffb4b780312cba90a212e851968558355e43cec548523a6d82a31ad52b98e
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [NF10: WA-14 treats as settled a point that Q-056 v2 still lists as open] WA-14 says "no tenant is
      created by an unattended sign-up", and CAP-01 repeats it. The governance owner's quoted answer does
      not say this. It says: "There should be an owner or tenant administrator who should be able to
      manage tenants (provisioning/onboarding clients)." The words "tenants are not created by an
      unattended sign-up" are the recorder's gloss in the first bullet under the answer. The same record
      then keeps the point open twice. Under "Still open": "Whether provisioning is Tiqri's service or
      self-service for subscribers is the product owner's". Under "Open": "Whether Tiqri provisions
      tenants, or customers sign up themselves, is the product owner's". EXC-27 correctly lists "Tiqri's
      service or self-service" as open, so WA-14 and EXC-27 pull in different directions. The practical
      effect on INCR-001 is nil, because no production provisioning route is built. But D-2 asks the
      product owner to confirm WA-14 as if the governance owner had said it.
      Fix for the requirements engineer: keep in WA-14 only "a named administrative role provisions
      tenants and onboards clients". Move "no unattended sign-up" to EXC-27's open list, or label it as
      a reading of the answer pending the product owner.
      Fix for the orchestrator: reconcile Q-056 v2's first bullet with its "Open" section at the next
      version.
    citation: >-
      Q-056 v2 "Answer so far", first bullet, "Still open" and "Open"; GOV-SCOPE-INCR-001 v4 WA-14,
      CAP-01 third bullet, EXC-27 what, D-2
  - severity: non-blocking
    text: >-
      [NF11: who holds the permission to raise figures is not defined] CAP-03 says "The tenant's
      administrator role holds the permission to raise capacity figures", and CAP-06 grants the raise to
      "the tenant's administrator role". INCR-001 has no tenant-level role. Roles are "built by the
      entity's administrator" and "assigned per entity" (S7-2.1.2-c01, c08). The starting set has one
      "Administrator" ("Configuration, user and role maintenance", S7-2.1.2-c26). Figures are "set per
      tenant and per entity" (S7-2.16.1-c25). Two readers could build this differently:
      (a) Is the "tenant's administrator role" the starting-set Administrator of each entity, or a role
      held at tenant level? Does an entity's administrator raise only that entity's figures, or the
      tenant's too?
      (b) Is the raise a granular permission that any administrator may add to other roles? V2.2 says
      permissions "are not bundled into fixed packages that the entity cannot take apart"
      (S7-2.1.2-c02). Or is it fixed to one role, which would depart from c02?
      This is authorisation (Tier 1), and it touches Q-056's open point on how the first administrator
      is named. The answer belongs to the security owner, with the product owner, and is not the
      requirements engineer's to make. Fix: in CAP-03 and CAP-06, say that the holder is the
      administrator role as Q-056 and Q-057 will define it. State in the meantime whether the raise is an
      ordinary, re-assignable permission under c02, as a labelled interim assumption with the security
      owner as owner.
    citation: >-
      GOV-SCOPE-INCR-001 v4 CAP-03 sixth bullet, CAP-06 second, third and seventh bullets, WA-13; "Roles
      are built by the entity's administrator, not fixed by the vendor" (SRC-007 p.8, S7-2.1.2-c01);
      "Permissions are not bundled into fixed packages that the entity cannot take apart" (p.8,
      S7-2.1.2-c02); "Limits are set per tenant and per entity, never globally" (p.133, S7-2.16.1-c25)
  - severity: non-blocking
    text: >-
      [NF12: raises have no upper bound in INCR-001] CAP-06 says "INCR-001 builds no ceiling check",
      and the tenant's administrator may raise any figure (WA-13). In INCR-001, then, a tenant
      administrator can raise a figure without limit on a shared platform. The scope states this openly
      and holds the platform ceiling out (EXC-29), so it settles nothing. But the consequence is not
      named for the tech lead, who owns the ceiling question in Q-057 v2, and D-2 lists "a platform
      ceiling" only as leaving the increment. A related point: CAP-06's statement that "Initial default
      values are loaded by the test route" sits in a capability, yet it relies on test_route_proposal,
      which nobody has approved. Fix: add the unbounded raise to D-2 or stack_dependencies as a point for
      the tech lead. Phrase the initial load as dependent on the route the security owner accepts, as
      EXC-27 test_dependency already does.
    citation: >-
      GOV-SCOPE-INCR-001 v4 CAP-06 fourth and fifth bullets, EXC-27 test_dependency and approval_note,
      EXC-29, D-2; Q-057 v2 "Still open" (platform ceiling, tech lead)
created_at: "2026-10-28"
---

# Delta review of GOV-SCOPE-INCR-001 v4 (commit ee20ce5)

This is an E4 delta review for WF-01M61MRRKX52P8XHG3NZXSPCZH, step 8. It follows
REV-01M61QHQX58WSCVFQMT2EPXSRD, which is not edited here.

The subject is `docs/requirements/increments/GOV-SCOPE-INCR-001.md` v4 at commit
`ee20ce5e50be3d0a6af9f0bf7878ddbd4bf7ed13`. `python tools/governance/trace.py explain
GOV-SCOPE-INCR-001` reports version 4, tier 1, no approval, and the normative hash
`sha256:3c1ffb4b780312cba90a212e851968558355e43cec548523a6d82a31ad52b98e`. That matches the brief.
I checked it against Q-056 v2 and Q-057 v2 as committed at ead697d. I read the changed sections of the
file directly.

`created_at` gives the date only, because my shell profile refuses `date`.

**Verdict: non-blocking-findings.** WA-13 matches what Q-057 v2 settles. WA-14 matches what Q-056 v2
settles, with one exception: it carries "no unattended sign-up", which the record itself still lists
as open (NF10). Readings (a) and (b) of Q-056 remain unchosen. Q-056 and Q-057 are rightly still
blocking, and EXC-27 and EXC-29 match what stays open. NF7 to NF9 are resolved. The three new findings
are about wording and labelling, and none needs a decision before the scope is sent. Approval still
needs F2 (Tier 1).

## Findings from REV-01M61QHQX58WSCVFQMT2EPXSRD (v3)

| Finding | Status | Evidence in v4 |
| --- | --- | --- |
| NF7 CAP-06 loose end | Resolved | The question is overtaken by WA-13. The setting is now "editable by the tenant's administrator for a raise only", with c23 cited. The test route loads the initial figures under a service identity. CAP-06 states which parts of c29 can be tested and that the load-test part cannot (EXC-22). Who holds the permission is a new point (NF11). |
| NF8 AP-10 and AP-13 without an interim position | Resolved | D-7 makes AP-10 and AP-13 preconditions of INCR-001 Gate A, owned by the qualified accountant with the product owner. It says which reversals each one holds up: "the series point (AP-10) holds up every reversal". AP-13 now states the matter of fact and leaves only acceptability open. |
| NF9 (a) D-5 owners | Resolved | "Product owner with the qualified accountant (DEP-3 names both)". |
| NF9 (b) duplicate bullet in CAP-14 | Resolved | One pending-journals bullet remains (WA-12). |
| NF9 (c) override role in item 6 | Resolved | Item 6 is now "[role] approving a reopening" (c07) only. |

Earlier findings that were already resolved stay resolved. Q-007 before Gate B remains "not resolved,
reason accepted", as before.

## What the brief asked to check

1. **WA-13 against Q-057 v2.** WA-13 matches. The record settles only that the "Tenant admin should
   be able to increase the cap limit". WA-13 says "the tenant's own administrator may raise a capacity
   figure", and lists warn or refuse, lowering, platform ceiling and licensing as still open. It is
   labelled "governance owner's answer of 2026-10-28 (as security owner and tech lead), pending the
   product owner", and the product owner owns Q-057, as DEC-0010 condition 3 requires. Nothing the
   record leaves open is treated as settled. "INCR-001 offers raising only" and "builds no ceiling
   check" are hold-outs, not choices (see NF12 on the consequence).
   **WA-14 against Q-056 v2.** "A named administrative role provisions tenants and onboards clients"
   matches the quoted answer. "No unattended sign-up" does not (NF10). WA-14 is labelled "(as security
   owner), pending the product owner". **Readings (a) and (b) are still unchosen**: EXC-27 lists both
   "or both", CAP-01 lists them as open, and SEC-2 is narrowed to reach.
2. **Still blocking.** This is correct for both. EXC-27 matches Q-056 v2's open list: which reading
   applies, how the first administrator is named, what the provisioning role can reach, and whether
   provisioning is a Tiqri service or self-service. EXC-29 matches Q-057 v2's: warn or refuse,
   lowering, platform ceiling, licensing (with EXC-21).
3. **NF7 to NF9.** See the table above.
4. **New problems.**
   - CAP-03: the holder of the raise permission is undefined (NF11).
   - CAP-06: unbounded raises, and reliance on an unapproved route (NF12).
   - D-2 asks the owners to confirm WA-13 and WA-14. That is consistent, apart from NF10.
   - D-7 is consistent with CAP-12, AP-10 and AP-13.
   - The test-route proposal, now extended to load the initial figures, is still marked "PROPOSAL ...
     not a decision", with `approval_note` and the D-1 exclusion, so it decides nothing.
5. **Questions.** There are 57 classification entries (grep count), Q-001 to Q-057, once each. Eight
   are blocking (lines 390, 396, 397, 414, 417, 438, 439, 440: Q-007, Q-013, Q-014, Q-031, Q-034,
   Q-055, Q-056, Q-057), and each names its exclusion: EXC-11, EXC-12, EXC-09, EXC-01, EXC-10, EXC-28,
   EXC-27, EXC-29.

## Clauses checked

**Against the rendered PDF: none.** `pdftoppm` is still not installed; this was observed in the
earlier delta reviews and nothing in the environment has changed. The pages that B2, B3 and Q-055 to
Q-057 rest on (pp.37, 38, 40 to 42, 133 to 136) still need to be checked on the PDF before an owner
decides.

**Against the extraction only**, in this delta: S7-2.1.2-c01 and c02 (p.8, lines 332-336);
S7-2.1.2-c26 (p.9, lines 388-389); S7-2.16.1-c25 (p.133, line 5666); S7-2.16.1-c34 (p.134, lines
5691-5692). The earlier clause lists are in the earlier records.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above. All three earlier
  reviews are shown as against an older hash (stale).
- `git log -4`: ee20ce5 (scope v4), 70d7f06 (the v3 review), ead697d (Q-056 and Q-057 answers),
  efb9ff3.
- The output of `python tools/governance/check.py` with this record in place is in the handoff report.
