---
id: REV-01M64FW5EQK3D8VZT2NB6GH9CM
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - id: ADR-0002
    hash: sha256:037c709b38e27c1776f6511f2dbc57d8f16416b15168317571185b1ef5d39955
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [V2-B1, the platform store, the one cross-tenant read, has no database-level control] I-11 makes
      the platform store the only cross-tenant read (I-3). It holds every tenant's catalogue entry, user
      identities and every membership, so it holds which client organisations each firm keeps the books
      of. That is confidential across tenants. The restriction to "the signed-in user's own memberships
      and the target tenant's database" is stated only as the behaviour of an application component.
      No invariant names the identity the component connects under or that identity's permissions, and
      nothing says whether the tenant application identity can query the platform store directly.
      Nothing in the database narrows a read to one user. Verification (2) tests the I-11 audit
      entries, but not that one user cannot read another user's memberships or other tenants' catalogue
      rows. This is what remains of v1 B5: the class now exists, but its control is application-only,
      while the ADR's own premise (I-4) is that application-only enforcement is not enough. Fix: add to
      I-11 (a) a separate platform identity with its own deny-by-default allow-list, and no access to
      the platform store for the tenant application identity; (b) reads only through procedures that
      take the authenticated user's identifier, or Row-Level Security on memberships keyed on a
      read-only user value in SESSION_CONTEXT; (c) verification (1) checks that identity's permissions,
      and verification (2) shows that user X cannot list user Y's memberships or a tenant's catalogue
      row X has no membership for.
    citation: >-
      ADR-0002 v2 normative.invariants I-3, I-11; normative.verification (1), (2) ("the audit entries of
      I-7, I-8 and I-11")
  - severity: blocking
    text: >-
      [V2-B2, I-5's allow-list can be bypassed through procedures, undetected] I-5 grants "EXECUTE on
      named procedures". A procedure created WITH EXECUTE AS OWNER (dbo owns the schema), or signed with
      a certificate whose user holds extra permissions, runs with permissions the application identity
      does not hold. If it contains dynamic SQL built from input, an injection becomes ALTER SECURITY
      POLICY or a DROP. Verification (1) checks only the permissions granted to the application identity,
      so it passes while this path exists. Fix: add to I-5 that procedures the application may execute
      run as caller (no EXECUTE AS other than CALLER, no module signing that adds permissions) and
      contain no dynamic SQL, unless the security owner has accepted a named exception. Add to
      verification (1) a scan of sys.sql_modules and the signature catalogue that fails on any
      exception not accepted.
    citation: >-
      ADR-0002 v2 normative.invariants I-5; normative.verification (1) ("the application identity holds
      any permission outside the I-5 allow-list")
  - severity: non-blocking
    text: >-
      [V2-NF1, platform allow-list, reference data, I-5 and I-9 do not agree] The decision names two
      classes, tenant data and platform data, and I-11 puts platform data in "a separate database". Yet
      I-1 keeps "the reviewed allow-list of platform tables" as the exception to the tenant-table rule
      inside tenant databases. Shared reference data that is neither (ISO currencies, countries,
      delivered templates) has no stated home. If such tables sit in tenant databases on the allow-list:
      (a) I-5 grants the application no SELECT on them, so it cannot read them; (b) a foreign key from a
      tenant table to one cannot be composite, which I-9 allows ("between tenant tables"), but
      verification (1) fails it ("any primary, unique or foreign key on a tenant table does not include
      the tenant identifier"). Fix: say whether tenant databases may hold allow-listed tables and of
      which class. If they may, grant SELECT only on them in I-5, and limit the verification (1) key
      rule to keys between tenant tables, as I-9 does.
    citation: >-
      ADR-0002 v2 normative.decision (two classes); I-1; I-5; I-9; I-11; verification (1)
  - severity: non-blocking
    text: >-
      [V2-NF2, I-5 grants more than the ledger may allow, and omits sequences and inherited permissions]
      (a) "SELECT, INSERT, UPDATE and DELETE on tenant tables" includes the tenant's audit log and posted
      entries. S7-2.1.2 says "no role can amend or delete the audit log" (p.9, line 367), and SEC-3 is
      open. State the list as a ceiling ("at most"), which the data-access and audit designs narrow per
      table. (b) If keys or numbers use SEQUENCE objects, the application needs UPDATE on them, which
      the allow-list omits. A sequence shared across tenants also lets one tenant infer others'
      activity from gaps in the values; prefer per-tenant numbering or keys that cannot be guessed. (c)
      The verification (1) permission check must include permissions inherited through the public role,
      database roles and Microsoft Entra group membership, not only direct grants.
    citation: >-
      ADR-0002 v2 normative.invariants I-5; GOV-SCOPE-INCR-001 v6 SEC-3; SRC-007 p.9 (S7-2.1.2, line
      367)
  - severity: non-blocking
    text: >-
      [V2-NF3, temporal history tables against the schema test] I-1 gives history tables "their own
      predicate", and the Microsoft quote supports a filter on them. But verification (1) fails any
      table not on the allow-list that lacks "any of the four block predicates". History tables refuse
      direct writes while versioning is on, and this reviewer could not confirm that a block predicate
      can be bound to one. If it cannot, the test either fails always or is satisfied by allow-listing
      history tables, which would drop their filter from the check. Fix: in verification (1), require a
      filter predicate (and no block predicate) on history tables, and add history-table reads (FOR
      SYSTEM_TIME) to the cross-tenant suite. History tables carry no keys, so I-9 is not affected.
    citation: >-
      ADR-0002 v2 I-1; verification (1); Evidence ("security predicates on the current table aren't
      automatically replicated to the history table")
  - severity: non-blocking
    text: >-
      [V2-NF4, I-4 (e) "without type conversions" cannot be met literally] SESSION_CONTEXT returns
      sql_variant, so the predicate must convert the session value once to compare it with the column.
      The Microsoft advice is about conversions that defeat index use. Fix: "no conversion applied to
      the tenant column; the session value converted once, explicitly, to the column's type".
    citation: >-
      ADR-0002 v2 I-4 (e); Evidence ("Avoid type conversions in predicate functions")
  - severity: non-blocking
    text: >-
      [V2-NF5, the policy can be off at run time, which CI does not see] Verification (1) checks STATE =
      ON in CI only. Data migrations run under the deployment identity, which can switch a policy off or
      work around it, and I-4 (b) permits no exemption. So a migration touching tenant data must either
      run per tenant with the session value set, or turn the policy off, which is an I-8 event. Fix:
      say which, and add a check in each deployed environment (at start-up and after each deployment)
      that refuses traffic if any tenant table's policy is off or missing.
    citation: >-
      ADR-0002 v2 I-4 (b), I-5 ("data migrations run under a separate deployment identity"), I-8;
      verification (1)
  - severity: non-blocking
    text: >-
      [V2-NF6, residual verification gaps] Verification is much stronger and no longer passes
      vacuously. Remaining points: (a) the endpoint list comes from "the application's own route and job
      registry"; handlers mapped outside it (file download, webhook, real-time hub) escape. Compare the
      registry with the running application's endpoint list and fail on any difference. (b) I-4 (b) (no
      exemption) and (e) (separate schema, SCHEMABINDING) are not checked; have the schema test compare
      each predicate function with one approved template. (c) I-6's rule on logs and telemetry (tenant
      tag, no field or parameter values) is not tested. (d) "Changes to the allow-list are reviewed by
      the security owner" has no mechanism before F2 (code owners). Name the interim control.
    citation: >-
      ADR-0002 v2 normative.verification (1), (2); I-4 (b), (e); I-6
  - severity: non-blocking
    text: >-
      [V2-NF7, Microsoft Learn quotes not verified by this reviewer] The ADR quotes two Microsoft Learn
      pages verbatim, with page git commits d0b41be05c89ea95874c19ddcbf4a115cdb89602 and
      2ceb7c07640735a9c49dbb6ff1de511aceead449, read 2026-10-29. This reviewer has no web access and has
      not verified any of these quotes or the page commits. They rest on the orchestrator's reading and
      are not registered sources; the ADR says so itself. They support I-4 (c) to (e), I-1, I-6, I-8,
      I-9, I-10 and I-11. Registering them, or keeping a captured copy, is open with the governance
      owner.
    citation: >-
      ADR-0002 v2 Evidence and assumptions, first two bullets
created_at: "2026-10-29"
---

# Delta review of ADR-0002 v2, tenant isolation (commit 53278ce)

An E4 security delta review. It follows REV-01M64CE9TQR7XK2B9WD3HNP5QA, the v1 review (committed at
f2ec84f), which is not edited here. `trace.py explain ADR-0002` reports version 2, tier 1, status
Proposed, no approval, and the normative hash
`sha256:037c709b38e27c1776f6511f2dbc57d8f16416b15168317571185b1ef5d39955`. That matches the brief. It
marks the v1 review stale (older hash). `created_at` gives the date only.

**Verdict: blocking-findings.** v2 resolves all six v1 blocking findings, B5 only in part, and NF1 to
NF6. Two blocking findings remain, both narrow:

- the platform store is controlled only by application code (V2-B1, the rest of B5);
- procedures can carry permissions past I-5's allow-list without the schema test seeing it (V2-B2).

The non-blocking findings are corrections of precision.

## Status of the v1 findings

| v1 | Status | Reason |
| --- | --- | --- |
| B1 | Resolved | Firm access and operator access are now PR-1 and PR-2, each "Not decided here", with owners, and listed in the scope. I-7 keeps only the mechanism (one membership per tenant, audit under the user's identity). I-8 describes the identities that exist and leaves operator use open (Q-056, SEC-2). |
| B2 | Resolved | I-4 (a) fails closed; (b) forbids exemptions; (c) names all four block predicates and denies UPDATE on the tenant column; (d) one connection component sets the value on every open; (e) SCHEMABINDING and a separate schema. Wording point: V2-NF4. |
| B3 | Resolved | I-9 makes keys tenant-led and foreign keys composite. Verification (1) checks it, and (2) tests re-pointing a foreign key. The CAP-13 note is correct: an entity belongs to one tenant. |
| B4 | Resolved, with a residual (V2-B2, V2-NF2) | I-5 is a deny-by-default allow-list with named denials. I-8 names the privileged identities and sends their use to database auditing outside the database. Verification (1) checks the application identity's permissions. |
| B5 | Partly resolved (V2-B1, V2-NF1) | Platform data is its own class (I-11). I-2 checks membership on every request; I-3 exempts only platform reads. The control on that read is application-only. |
| B6 | Resolved, with residuals (V2-NF3, V2-NF5, V2-NF6) | Default-deny table set, a generated endpoint list, both tenants holding data of every kind, positive controls, identical responses for missing identifiers, and the missing cases added. |
| NF1 | Resolved | I-6 covers whole-database artefacts (privileged path only), logs and telemetry without values, and change data capture. |
| NF2 | Resolved | I-10. |
| NF3 | Resolved | P-1 cites Q-028 for the owner and Q-003 for the countries. Q-003 is linked. |
| NF4 | Resolved | Prose alternatives with for and against, including blast radius, noisy neighbours, keys and cost. The recommendation is conditional on AS-1 and AS-2. The c25 consequence is dropped. |
| NF5 | Resolved | AS-4 (job identity and audit, security owner), AS-5 (sandbox copy, security and product owners), and P-2 keeps the audit log and number series. |
| NF6 | Partly resolved (V2-NF7) | The request is cited to GOV-STATE (line 102, "asked that day that tenant isolation be considered from the initial design"), which resolves. The web quotes carry page commits, but are unregistered and not verified by this reviewer. |

## New material in v2

- **I-4 (d), "every time a connection is opened or taken from the pool".** This is the right rule.
  Taking a pooled connection is an open, and the reset on reuse clears the earlier value. The rule
  also covers reopening after a retry. With (a), a failure to set the value leaves a connection that
  reads nothing, which is fail-closed. No finding.
- **I-11.** See V2-B1 and V2-NF1.
- **I-5 completeness.**
  - Procedures: V2-B2.
  - Sequences and inherited permissions: V2-NF2.
  - Temporal history tables count as tenant tables under I-1. Their DML grants are harmless while
    versioning is on, because the engine refuses direct writes. Their schema check is V2-NF3.
- **I-9 against temporal history and the allow-list.** History tables have no keys, so there is no
  conflict. The conflict with the allow-list is V2-NF1.
- **PR-1, PR-2, AS-4, AS-5.** Each is labelled, names its owner and says it is not decided. AS-4's
  first sentence ("on behalf of the user who started or scheduled them") is a stated assumption with
  its owner, which is acceptable.
- **Citations.** SRC-007 citations are unchanged from v1 and still resolve. S7-2.1.4-c03 ("Login
  identity, not a shared or system account", p.10) is in the clause index.
- **Can the verification still pass trivially?** Not as v1 could. The remaining routes are in V2-B1
  (platform store untested), V2-B2 (procedure permissions) and V2-NF6.
