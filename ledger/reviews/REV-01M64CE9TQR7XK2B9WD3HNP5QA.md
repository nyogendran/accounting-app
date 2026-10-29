---
id: REV-01M64CE9TQR7XK2B9WD3HNP5QA
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - id: ADR-0002
    hash: sha256:884a429febab7d23a77f82d007b7806ffb7008615c2c36736d2ac58ff3503543
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [B1, decides what it calls open] The scope field says the ADR does not decide "how a firm's access
      is granted (Q-031); operator access (Q-056, SEC-2)". The invariants decide parts of both. I-8
      states "Tiqri's staff, as operator, have no standing access to any tenant's books. Any operator
      access is time-limited, has a recorded reason, and is written to the tenant's audit log". That is
      the SEC-2 question ("what an operator or provisioning role may reach in a tenant after creating
      it"), which Q-056 v3 holds open with the security owner. Q-031 v3 reading (c) ("without access to
      their books") is one of three readings, not an answer. I-7 says the grant is one "which the client
      can see and withdraw". Q-031 v3 holds open "who grants and withdraws the firm's access". The
      closing "Whether and when it is allowed is open" in I-8 and "Who grants and withdraws it is open"
      in I-7 contradict the sentences before them. Fix, either way: (a) move the I-7 and I-8 policy
      content out of the invariants into a labelled proposal for the security owner (and the product
      owner for I-7), leaving only "operator access and firm access, when decided, act inside one
      tenant under I-3 and are audited under S7-2.1.4"; or (b) state openly that this ADR proposes
      answers to SEC-2 and part of Q-031, remove them from the "does not decide" list, and have the
      orchestrator record them against Q-056 and Q-031 for their owners.
    citation: >-
      ADR-0002 v1 normative.invariants I-7, I-8 and normative.scope; Q-031 v3 "Open" first bullet;
      Q-056 v3 "Still open ... what the provisioning role can reach inside a tenant after creating it";
      GOV-SCOPE-INCR-001 v6 security_points SEC-2
  - severity: blocking
    text: >-
      [B2, I-4 does not fail closed] I-4 keys every predicate on a SESSION_CONTEXT value but never says
      what happens when the value is absent, NULL, of the wrong type or names a tenant that is not in
      the catalogue. A predicate written as "tenant_id = SESSION_CONTEXT(...)" happens to return no rows
      on NULL, but a common variant adds an exemption ("OR the caller is dbo / a support role / a job
      account"), and nothing in I-1 to I-8 forbids it. I-4 also says "a block predicate on inserts and
      updates" without naming the operations. Without AFTER UPDATE, a tenant-A session can update a
      visible row's tenant identifier to B and push it into tenant B. "When the connection is opened for
      the request" assumes one opening path; .NET data access can open and close a pooled connection
      several times in one request, and background jobs, raw ADO.NET and bulk-copy paths open their own.
      Fix: add to I-4 (1) the predicate admits a row only when the session value is present and equals
      the row's tenant, so no value means no rows and no writes; (2) no exemption clause in any
      predicate, and every operator path goes through I-8; (3) block predicates AFTER INSERT and AFTER
      UPDATE on every tenant-owned table, with BEFORE UPDATE and BEFORE DELETE if the filter does not
      already cover them; (4) a single connection-opening component sets the value with @read_only = 1
      on every open, for every caller, including jobs and bulk loads; (5) predicate functions WITH
      SCHEMABINDING in a schema the application identity cannot alter.
    citation: >-
      ADR-0002 v1 normative.invariants I-4; ADR-0002 v1 Evidence, the Microsoft Learn "Row-Level
      Security" entry (filter and block predicates, SCHEMABINDING, read_only)
  - severity: blocking
    text: >-
      [B3, cross-tenant references and key collisions are not invariants] I-1 requires a tenant column,
      but no invariant requires tenant-scoped keys. (a) Foreign keys: referential-integrity checks are
      not filtered by the tenant predicate (to be confirmed by a test). A tenant-A row could then
      reference a tenant-B parent by its identifier and pass the block predicate, which checks only the
      child's own tenant. That allows both a cross-tenant link in the ledger and an existence probe on
      tenant B's identifiers. (b) Unique keys: a unique index without the tenant identifier refuses
      tenant A's insert because tenant B holds the value. That leaks the existence of B's data (for
      example a document number, a customer code or a tax ID) and couples tenants' numbering. The
      Consequences say "Every table, index and unique key includes the tenant identifier", but only as
      a cost, not as a normative rule, and foreign keys are not mentioned. Fix: add an invariant that
      every primary, unique and foreign key on tenant-owned data includes the tenant identifier
      (composite foreign keys on (tenant, id)), and make the schema test in verification (1) check it.
      This also makes CAP-13's "unique across the system" a tenant-scoped uniqueness.
    citation: >-
      ADR-0002 v1 normative.invariants I-1, I-4; Consequences, Negative, first bullet;
      GOV-SCOPE-INCR-001 v6 CAP-13 ("The combination of entity, series and number is unique across the
      system")
  - severity: blocking
    text: >-
      [B4, I-5 does not name the bypass paths or the people who hold them] Row-Level Security does not
      stop anyone who can change it. I-5 says the application user "cannot alter or bypass the security
      policy" but does not say what that means in permissions, and it covers the application identity
      only. Bypass paths not addressed: (a) membership of db_owner, or CONTROL, ALTER ANY SECURITY
      POLICY, ALTER on the predicate function's schema, ALTER ANY USER or IMPERSONATE (EXECUTE AS a less
      restricted principal); (b) human and privileged identities: the logical server administrator, the
      Microsoft Entra administrator, the deployment identity in I-5, and any group granted db_owner for
      support. These read all tenants of a shared database by changing or dropping the policy, and that
      is a standing operator path that I-8 says does not exist; (c) data migrations and backfills run by
      the deployment identity; (d) query tools on the database (portal query editor, management tools).
      AS-2 ("a non-bypassing application identity ... is acceptable isolation") is labelled and owned,
      which is correct, but the ADR gives the security owner no list to accept. Fix: state the
      application identity's permission set as a deny-by-default allow-list (DML on tenant tables,
      EXECUTE on named procedures, nothing else); state which identities can alter the policy and that
      each such use is an I-8 event, written to an audit trail outside the tenant's control (database
      auditing); add a permission test to verification (1) that fails if the application user holds
      any permission outside the list.
    citation: >-
      ADR-0002 v1 normative.invariants I-5, I-8; Evidence, labelled assumption AS-2
  - severity: blocking
    text: >-
      [B5, I-2, I-3 and I-7 cannot all hold as written] I-2 takes the tenant from "the tenant the user
      has selected and is entitled to". To know which tenants a firm's user is entitled to, and to
      offer a choice, the server must read entitlements across tenants. I-7 records each grant "in the
      client's tenant", which is under Row-Level Security, and I-3 says "No query reads or writes two
      tenants' data". The tenant catalogue ("which tenant is in which database") is cross-tenant too, as
      is user identity, because one login spans several tenants (Q-031 v3). The ADR has no class of
      platform-level data, and gives that data no owner, identity, protection or audit. Fix: define a
      platform store (catalogue, user-to-tenant membership or grant index, placement), exempt from I-3
      only for the entitlement lookup; state which identity reads and writes it, that it holds no
      ledger data, how a grant in the client's tenant and its index entry stay consistent (the client's
      withdrawal must take effect at once), and that changes to it are audited. Add it to
      verification.
    citation: >-
      ADR-0002 v1 normative.invariants I-2, I-3, I-7; Consequences, Negative, fourth bullet (tenant
      catalogue); Q-031 v3 second answer ("the firm's users work across those tenants")
  - severity: blocking
    text: >-
      [B6, the verification can be satisfied trivially] (1) The schema test checks tables "holding
      tenant-owned data", but nothing defines that set. If it is an annotation or a list, an
      unannotated table passes. Use default-deny: every table is tenant-owned unless it is on a
      reviewed allow-list of platform tables (B5). Also check policy STATE = ON, both predicate kinds,
      SCHEMABINDING, composite keys (B3) and the application user's permissions (B4). (2) "Tries every
      endpoint" does not say how "every" is enumerated. Generate the list from the application's route
      and report registry, and fail when one is not covered. "Must return nothing or be refused" passes
      vacuously if tenant B's fixture is empty or the call fails for another reason. Add a positive
      control: the same call as a tenant-B user returns B's data, and the A-side response does not tell
      "exists in B" from "does not exist". Missing cases: a connection with no session value returns
      and writes nothing; changing the value after it is set fails; insert or update with B's
      identifier under A's session is blocked; re-pointing a foreign key to a B parent is refused; bulk
      insert under A's session with B's identifier; a background job and a report run; caches, files,
      search and queues (I-6); the I-7 and I-8 audit entries; and the shared-to-dedicated move (P-2).
      (3) and (4) are fine as stated.
    citation: >-
      ADR-0002 v1 normative.verification (1) to (4)
  - severity: non-blocking
    text: >-
      [NF1, I-6 is unsatisfiable for backups and omits stores] "Backups ... scoped by tenant in the same
      way" cannot hold for a shared database: its backups, point-in-time restores, copies, exports and
      geo or readable replicas hold every tenant in it. The ADR itself says a shared database "cannot
      restore one tenant". I-6 also omits application telemetry and exception traces (query text and
      parameter values), Query Store and other database diagnostics that keep query text and
      parameters, change data capture or change tracking, and analytics copies or mirroring. Fix: say
      that whole-database artefacts hold all their tenants and are reached only by the operator path
      (I-8); list telemetry, diagnostics and analytics copies under I-6; and tag every log and
      telemetry entry with the tenant without recording field values.
    citation: >-
      ADR-0002 v1 normative.invariants I-6; Consequences, Negative, second bullet
  - severity: non-blocking
    text: >-
      [NF2, side channels] Row-Level Security leaks through crafted queries that raise errors or vary
      in timing according to a hidden row's value. That matters only if user input can shape SQL,
      through dynamic SQL, a report builder or ad-hoc filters. Database error text returned to the
      client, and a different response for "not yours" than for "not found", leak existence. Fix: add
      an invariant that no user-authored SQL runs, every query is parameterised, database errors are
      not returned to clients, and cross-tenant identifiers get the same response as missing ones.
    citation: >-
      ADR-0002 v1 normative.invariants I-4; verification (2) "return nothing or be refused"
  - severity: non-blocking
    text: >-
      [NF3, Q-028 misrepresented] P-1 says "Which countries require it is open (Q-028)". Q-028 v1 asks
      "Which role owns the statutory data-residency rules for each country?". It is the owner question,
      not the country list. The countries are Q-003, and GOV-SCOPE-INCR-001 EXC-03 cites Q-028, Q-003
      and Q-054 together. Fix: "Who owns the rule is open (Q-028); which countries are served is open
      (Q-003)", and add Q-003 to links.related.
    citation: >-
      ADR-0002 v1 placement_rules P-1; Q-028 v1 Question; GOV-SCOPE-INCR-001 v6 EXC-03
  - severity: non-blocking
    text: >-
      [NF4, alternatives table leans to D] The table omits criteria on which A is stronger: per-tenant
      encryption keys (SEC-1, S7-2.1.3-c03), noisy-neighbour performance isolation, the blast radius of
      one predicate defect (all tenants of a shared database), and the running cost of two placement
      models plus a move procedure. "Poorly at large numbers" for A and "Moderate" for D carry no
      evidence. The case for D rests on AS-1 (many small tenants), which is unconfirmed, and Q-038's
      platform tenant count is open. S7-2.16.1-c25 concerns configured limits ("one group raising a
      limit does not alter any other"), not resource isolation, so "capacity figures stay per tenant"
      is not a consequence of choosing D. Fix: add these columns; state that the recommendation holds
      only if AS-1 holds; and drop or re-word the c25 consequence. The recommendation is reasonable
      once qualified this way.
    citation: >-
      ADR-0002 v1 Alternatives table; Evidence AS-1; Consequences, Positive; S7-2.16.1-c25 (p.133)
  - severity: non-blocking
    text: >-
      [NF5, unlabelled points and owners] (a) I-3 has background jobs act in one tenant but does not say
      under which identity, or what the audit log records. S7-2.1.4-c03 requires "Login identity, not a
      shared or system account", and the scope already notes a service identity in an audit entry. Label
      it open with the security owner. (b) "copies one tenant's data" reads S7-2.1.1-c02 ("test or
      sandbox refreshed from production on request") as per tenant. The clause does not say so, and
      putting production books in a test environment is a data-handling question. Label it as an
      assumption with its owner (security owner, product owner). (c) P-2's move must keep audit-log
      integrity and number series (SEC-3, CAP-13); say so.
    citation: >-
      ADR-0002 v1 I-3, Consequences, Negative, third bullet, P-2; S7-2.1.1-c02 (p.8); S7-2.1.4-c03
      (p.10); GOV-SCOPE-INCR-001 v6 CAP-06 ("the audit entry of that load would name a service
      identity")
  - severity: non-blocking
    text: >-
      [NF6, evidence that does not resolve in the repository] The two Microsoft Learn pages are web
      sources "read 2026-10-29", not registered sources, and no copy is kept. The ADR relies on the
      read_only and pool-return behaviour; this reviewer could not re-check it from the repository.
      "The governance owner asked on 2026-10-29" cites no record. Fix: register the pages (or capture
      the quoted passages) as a source, and cite the workflow or question record that holds the
      request.
    citation: >-
      ADR-0002 v1 Evidence, first two bullets; Motivating requirements, sixth bullet
created_at: "2026-10-29"
---

# Review of ADR-0002 v1, tenant isolation (commit 2865a34)

An E4 security and architecture review. The subject is
`docs/architecture/adr/ADR-0002-tenant-isolation.md` at commit
`2865a34212b8be4a707d6e1eb68d6ce7577ca510`, with a clean working tree. The guard blocked
`approvals.py hash` for this reviewer, so the hash was read from `trace.py explain ADR-0002`. It
reported version 1, tier 1, status Proposed, no approval and
`sha256:884a429febab7d23a77f82d007b7806ffb7008615c2c36736d2ac58ff3503543`. That matches the brief.
`created_at` gives the date only.

**Verdict: blocking-findings.** The direction (a tenant column everywhere, enforcement in the database
and the same schema in shared and dedicated databases) is sound and fits Azure SQL Database. Six points
need fixing before the security owner is asked to accept AS-2:

- the ADR decides what it calls open (B1);
- I-4 does not fail closed (B2);
- tenant-scoped keys and foreign keys are not invariants (B3);
- the bypass identities are not named (B4);
- the invariants conflict over platform-level data (B5);
- the verification can pass trivially (B6).

## What checks out

- **Clause IDs.** Every clause ID resolves in `docs/requirements/clause-index-src007.yaml`:
  S7-2.1.1-c01 (p.8), S7-2.1.1-c02 (p.8), S7-2.1.3-c03 (p.9), S7-2.1.3-c04 (p.10), S7-2.1.4-c03
  (p.10) and S7-2.16.1-c25 (p.133).
- **Quotes.** The quotes match the extracted text and pages:
  - "Cloud-hosted, multi-tenant or single-tenant" (line 323, p.8);
  - "refreshed from production on request" (line 324, p.8);
  - "Data residency in each jurisdiction whose law requires it; the vendor states where data and
    backups physically sit" (line 404, p.10);
  - "Limits are set per tenant and per entity, never globally, so one group raising a limit does not
    alter any other" (line 5666, p.133);
  - RPO [4] hours and RTO [8] hours (line 5633, p.132);
  - the ceiling figures of 10,000 legal entities, 500,000 named users and 100,000,000 journal lines
    (lines 5646, 5652 and 5659, p.133).
- **Working answers.** Q-031 v3 and Q-038 v3 are stated faithfully as working answers. AS-1 is
  labelled as an inference. SEC-1 (identity, keys) is left undecided.
- **Tier and approval.** Tier 1 is correct (methodology.md lists isolation). No approval request is
  raised before F2. The small-team fallback is quoted correctly from the authority matrix and put to
  the governance owner rather than assumed.

## Notes for the author

B2 to B6 are design and test gaps for a Tier-1 control. The fixes add precision; they do not change the
chosen option. B1 is a governance point: whatever the ADR says about firm access and operator access
must reach Q-031 and Q-056 as proposals for their owners, not as invariants.
