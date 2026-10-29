---
id: ADR-0002
type: adr
title: Tenant isolation in Azure SQL Database - one tenant per request, enforced in the database
status: Proposed
version: 1
owner: orchestrator
tier: 1
normative:
  decision: >-
    Tenant isolation is designed in from the first data model, not added later. The tenant (one
    organisation, Q-031 v3) is the isolation boundary; legal entities inside a tenant are separated
    by role scoping (S7-2.1.2), not by this mechanism. Proposed placement: a hybrid. A tenant's data
    sits either in a shared database with other tenants or in a database of its own, chosen per tenant
    and recorded in a tenant catalogue. The schema and the application code are the same in both
    places: every tenant-owned table carries a tenant identifier, and Row-Level Security filters and
    blocks by it in every database, shared or dedicated. New tenants start in a shared database unless
    a placement rule below puts them in their own.
  invariants:
    - "I-1. Every row of tenant-owned data carries its tenant identifier, in every table, in every database, including dedicated ones."
    - "I-2. The tenant of a request is taken on the server from the authenticated identity and the tenant the user has selected and is entitled to. It is never taken from a value the browser sends without that check."
    - "I-3. A request, a background job and a report run act in exactly one tenant. No query reads or writes two tenants' data."
    - "I-4. Isolation is enforced in the database, not only in application code: a Row-Level Security filter predicate on reads and a block predicate on inserts and updates, keyed on a tenant value set in SESSION_CONTEXT with @read_only = 1 when the connection is opened for the request."
    - "I-5. The application connects as a database user that cannot alter or bypass the security policy. Schema changes run under a separate deployment identity, never the application's."
    - "I-6. Everything that holds tenant data outside the tables is scoped by tenant in the same way: files and attachments, caches, search indexes, queues, exports, logs and backups. A cache key or storage path always includes the tenant."
    - "I-7. Access from one tenant into another (a firm keeping a client's books, Q-031 v3 reading (a)) exists only as an explicit grant recorded in the client's tenant, which the client can see and withdraw; the firm's user then works inside the client's tenant under I-3, and every action is written to the client's audit log under the user's own identity (S7-2.1.4). Who grants and withdraws it is open (Q-031)."
    - "I-8. Tiqri's staff, as operator, have no standing access to any tenant's books. Any operator access is time-limited, has a recorded reason, and is written to the tenant's audit log. Whether and when it is allowed is open (Q-056, SEC-2)."
  placement_rules:
    - "P-1. A tenant whose country's law requires its data in that country (S7-2.1.3-c04) is placed in a database in a region that satisfies it. Which countries require it is open (Q-028)."
    - "P-2. A tenant whose volumes approach the share of a shared database set in the hosting ADR moves to a database of its own; the move is a planned, tested operation."
    - "P-3. Whether a subscriber may buy a dedicated database is a product decision (product owner, Q-039)."
  scope: >-
    This ADR decides the isolation boundary, the invariants and the placement model. It does not
    decide: the identity provider and sign-in (SEC-1); encryption standard and key management,
    including whether keys are per tenant (SEC-1, S7-2.1.3-c03); the Azure regions and elastic-pool
    sizing (hosting ADR); the data-access library (data-access ADR); how a firm's access is granted
    (Q-031); operator access (Q-056, SEC-2); or the release-1 tenant count (Q-038).
  verification: >-
    (1) A schema test, run in CI from F4, fails the build if any table holding tenant-owned data lacks
    the tenant column or is not covered by the security policy. (2) An automated cross-tenant test
    suite, run in CI for every change, signs in as a user of tenant A and tries every endpoint, report
    and export against tenant B's data, by identifier, by search and by direct database call under the
    application identity; every attempt must return nothing or be refused, and is a Tier-1 test that
    may not be weakened or skipped (CLAUDE.md rule 8). (3) The same suite runs against a shared and a
    dedicated database. (4) The security owner reviews the design at INCR-001 Gate B and a penetration
    test covers cross-tenant access before Gate D.
links:
  derives_from: [ADR-0001, Q-031]
  related: [Q-028, Q-038, Q-039, Q-056, Q-057, DEC-0010, GOV-SCOPE-INCR-001, S7-2.1.1-c01, S7-2.1.3-c03, S7-2.1.3-c04, S7-2.16.1-c25]
---

# ADR-0002: Tenant isolation

- **Motivating requirements or constraints:**
  - SRC-007 allows a "Cloud-hosted, multi-tenant or single-tenant" system (p.8, S7-2.1.1-c01) and
    requires "Data residency in each jurisdiction whose law requires it; the vendor states where data
    and backups physically sit" (p.10, S7-2.1.3-c04).
  - "Limits are set per tenant and per entity, never globally, so one group raising a limit does not
    alter any other" (p.133, S7-2.16.1-c25).
  - Q-031 v3 (working answer): a tenant is one organisation; a firm (Tiqri, an audit firm or a client)
    keeps the books of client organisations, each its own tenant. So the platform holds many tenants,
    many of them small, and some users work across several tenants.
  - Q-038 v3 (working answer): release 1 is one entity, 125 named users, 50 at peak and 200,000
    journal lines a month, per tenant. SRC-007's tested ceiling is far larger: 10,000 legal entities,
    500,000 named users and 100,000,000 journal lines a month (p.133).
  - ADR-0001 fixes Azure SQL Database. The governance owner asked on 2026-10-29 that isolation be
    decided from the initial design.
  - GOV-SCOPE-INCR-001 v6 names isolation as a security point (SEC-2).

- **Why now.** Isolation shapes every table, key, index, query, cache and test. Retrofitting a tenant
  column or a database split onto a built ledger is a migration of posted, audit-locked data, which
  is the costliest kind of change in this system. It is decided before the data model and the
  data-access ADR.

- **Alternatives considered:**

  | Option | Isolation | Fits many small client tenants (Q-031) | Residency (c04) | Per-tenant restore | Cost and operations |
  | --- | --- | --- | --- | --- | --- |
  | A. Database per tenant (elastic pools) | Strongest: a separate database | Poorly at large numbers: one database, one schema migration and one backup set per tenant | Natural: place each database in its region | Native point-in-time restore | Highest; schema changes roll out across every database |
  | B. Shared database, tenant column and Row-Level Security | Logical: relies on the predicate and on the application identity being unable to bypass it | Well | Only by running a shared database per region | Needs a per-tenant export and restore procedure | Lowest; one schema |
  | C. Schema per tenant | Between A and B | Poorly: many schemas in one database, same migration burden as A | As B | Awkward | Not proposed: costs of A without its isolation |
  | **D. Hybrid of A and B, same schema everywhere (proposed)** | B by default; A where placement requires; Row-Level Security in both | Well | Shared database per region, or a dedicated one | B or A by placement | Moderate: one schema, a tenant catalogue, a tested move between placements |

  Microsoft describes these patterns, and the hybrid of shared and single-tenant databases, for Azure
  SQL Database (see Evidence). D is proposed because Q-031 implies many small tenants (which favours
  B), while residency and the tested ceiling require some tenants in their own place (which favours
  A). Keeping the tenant column and the security policy even in a dedicated database means one code
  path, one test suite, and a tenant can move without a schema change.

- **Evidence and assumptions:**
  - Microsoft Learn, "Multitenant SaaS patterns - Azure SQL Database" (read 2026-10-29): describes
    database-per-tenant, multitenant databases and hybrids, and states that a multitenant database
    gives up some isolation, with Row-Level Security available to scope queries to one tenant.
    https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns?view=azuresql
  - Microsoft Learn, "Row-Level Security" (read 2026-10-29): filter and block predicates; setting
    SESSION_CONTEXT with @read_only = 1 stops the value changing until the connection is closed or
    returned to the pool; predicate functions created WITH SCHEMABINDING.
    https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17
  - **Labelled assumptions** (orchestrator, each to be confirmed by the security owner or tech lead):
    - AS-1: many tenants will be small (a firm's clients). From Q-031 v3; the release-1 tenant count
      is open (Q-038).
    - AS-2: Row-Level Security with a non-bypassing application identity, plus the cross-tenant test
      suite, is acceptable isolation for a shared database. Security owner.
    - AS-3: a firm's cross-tenant work needs no query that spans tenants; a firm-wide view across its
      clients, if wanted, would be built from per-tenant results the firm is entitled to, under I-3.
      Product owner, with Q-031.
  - No evidence was found in SRC-007 for which countries require in-country data (Q-028 open).

- **Decision owner and approval status:**
  - Deciders: the security owner (isolation guarantee, I-7, I-8) and the tech lead (placement model).
    Both are held by the governance owner (authority matrix v2). The product owner is consulted on
    P-3 and AS-3, where cost or scope is affected.
  - Tier 1: isolation is in the Tier-1 list. Stage 0 approvals do not count for Tier 1, so no approval
    request is raised until F2 (GitHub) is in place.
  - The authority matrix's small-team fallback says Tier-1 policy approvals "still need a second
    named person, external if necessary", and one person holds both deciding roles here. Whether a
    Tier-1 ADR needs that second person is for the governance owner to say.
  - Status: Proposed.

- **Consequences:**
  - Positive: isolation enforced by the database as well as by code; one schema and one test suite;
    residency handled by placement; a tenant can move from shared to dedicated as it grows; capacity
    figures stay per tenant (S7-2.16.1-c25).
  - Negative:
    - Every table, index and unique key includes the tenant identifier, including gapless number
      series (CAP-13), which are per tenant and per entity.
    - A shared database cannot restore one tenant by point-in-time restore. A per-tenant export and
      restore procedure is needed, and tested against the backup objectives (RPO [4] hours, RTO [8]
      hours, p.132).
    - The test or sandbox environment "refreshed from production on request" (p.8, S7-2.1.1-c02)
      copies one tenant's data. That copy must keep the tenant's isolation and residency, and who may
      request it is the security owner's.
    - A tenant catalogue (which tenant is in which database) becomes a critical component with its
      own availability and audit.
    - Row-Level Security adds a predicate to every query; the tenant column leads the relevant indexes.
  - Open items that change this ADR if answered differently: Q-031 (firm access), Q-056 and SEC-2
    (operator and provisioning reach), Q-028 (residency), Q-038 (platform tenant count), SEC-1 (keys).
  - Nothing here may be built before Gate C (CLAUDE.md rule 1).
