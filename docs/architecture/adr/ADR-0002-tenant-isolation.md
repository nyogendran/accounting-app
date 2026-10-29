---
id: ADR-0002
type: adr
title: Tenant isolation in Azure SQL Database - one tenant per request, enforced in the database
status: Proposed
version: 2
owner: orchestrator
tier: 1
normative:
  decision: >-
    Tenant isolation is designed in from the first data model, not added later. The tenant (one
    organisation, Q-031 v3) is the isolation boundary; legal entities inside a tenant are separated
    by role scoping (S7-2.1.2), not by this mechanism. Data is in two classes: tenant data (everything
    a tenant owns, including its books, master data, settings and audit log) and platform data (the
    platform store, I-11). Proposed placement for tenant data: a hybrid. A tenant's data sits either in
    a shared database with other tenants or in a database of its own, chosen per tenant and recorded in
    the tenant catalogue. The schema and the application code are the same in both places: every
    tenant table carries a tenant identifier, and Row-Level Security filters and blocks by it in every
    database, shared or dedicated. New tenants start in a shared database unless a placement rule puts
    them in their own. The placement choice holds only while AS-1 holds; if it does not, option A
    (database per tenant) is to be reconsidered.
  invariants:
    - "I-1. Every table is a tenant table unless it is on the reviewed allow-list of platform tables (I-11). Every row of a tenant table carries its tenant identifier, in every database, shared or dedicated, including temporal history tables, which carry their own predicate."
    - "I-2. The tenant of a request is set on the server from the authenticated identity and a tenant membership found in the platform store for that identity (I-11), checked on every request. It is never taken from a value the browser sends without that check."
    - "I-3. A request, a background job and a report run act on tenant data in exactly one tenant. No query reads or writes two tenants' tenant data. Reading the platform store (I-11) is not tenant data and is the only cross-tenant read."
    - "I-4. Isolation is enforced in the database, not only in application code, and fails closed: (a) the predicate admits a row only when a tenant value is present in SESSION_CONTEXT and equals the row's tenant identifier, so a connection with no value, a NULL value or an unknown tenant reads nothing and writes nothing; (b) no predicate contains an exemption for any user, role or identity; (c) every tenant table has a filter predicate and block predicates AFTER INSERT, AFTER UPDATE, BEFORE UPDATE and BEFORE DELETE, and the application identity is denied UPDATE on the tenant identifier column; (d) one connection component, used by every caller including background jobs and bulk loads, sets the value with @read_only = 1 every time a connection is opened or taken from the pool; (e) predicate functions are created WITH SCHEMABINDING, without type conversions, in a separate schema that the application identity cannot alter."
    - "I-5. The application identity holds only an allow-list of permissions: SELECT, INSERT, UPDATE and DELETE on tenant tables (less UPDATE on the tenant column), and EXECUTE on named procedures. It holds no membership of db_owner or db_ddladmin and no CONTROL, ALTER, ALTER ANY SECURITY POLICY, ALTER ANY USER, IMPERSONATE or VIEW DEFINITION on the security schema. Schema changes and data migrations run under a separate deployment identity, never the application's."
    - "I-6. Everything that holds tenant data outside the tables is scoped by tenant: files and attachments, caches, search indexes, queues, exports, logs and telemetry. A cache key, storage path or index partition always includes the tenant. Logs and telemetry are tagged with the tenant and do not record field values or query parameter values. Whole-database artefacts (backups, restores, copies, replicas, Query Store and other diagnostics) hold every tenant in that database and are reached only through the privileged path (I-8). Change data capture is not enabled on a tenant table without the security owner's agreement."
    - "I-7. A user who works in more than one tenant (Q-031 v3: a firm's staff in client tenants) holds one membership per tenant in the platform store (I-11). Under a membership the user acts inside that one tenant under I-3, and every action is written to that tenant's audit log under the user's own identity (S7-2.1.4). Removing a membership takes effect at the user's next request. Who may create and remove a membership into a client's tenant is open (Q-031, security owner with product owner); proposal PR-1 below."
    - "I-8. Identities that can alter or bypass Row-Level Security exist by nature of the platform: the logical server administrator, the Microsoft Entra administrator, the deployment identity and any holder of the permissions I-5 denies the application. Each is held by named people or by the deployment pipeline, never by the application, and every use is recorded by database auditing to an audit store outside the database, whose access and retention the security owner sets (SEC-3). Whether Tiqri as operator may use any path to read a tenant's data, and on what conditions, is open (Q-056, SEC-2); proposal PR-2 below."
    - "I-9. Every primary key, unique key and index enforcing uniqueness on a tenant table leads with the tenant identifier, and every foreign key between tenant tables is composite on (tenant identifier, key), so no row can reference another tenant's row and no insert can collide with another tenant's value."
    - "I-10. No SQL written or shaped by a user is run; every query is parameterised; database error text is not returned to the client; a request for an identifier that belongs to another tenant gets the same response as one that does not exist."
    - "I-11. The platform store is a separate database holding only platform data: the tenant catalogue (tenant, database, region, status), user identities, tenant memberships (I-7) and placement. It holds no ledger, master or settings data of any tenant. It is read on the request path only through a platform component that returns the signed-in user's own memberships and the target tenant's database, and written only by named administrative operations, each recorded in the platform store's own audit log and, where it concerns a tenant, in that tenant's audit log."
  placement_rules:
    - "P-1. A tenant whose data must sit in a given country under that country's law (S7-2.1.3-c04) is placed in a database in a region that satisfies it. Who owns the residency rules is open (Q-028); which countries are served is open (Q-003)."
    - "P-2. A tenant whose volumes approach the share of a shared database set in the hosting ADR moves to a database of its own. The move is a planned, tested operation that takes the tenant offline in the catalogue, keeps its audit log complete and its number series unbroken (CAP-13, SEC-3), and is recorded in its audit log."
    - "P-3. Whether a subscriber may buy a dedicated database is a product decision (product owner, Q-039)."
  proposals_for_owners:
    - "PR-1 (for Q-031; security owner with product owner). A firm's membership in a client's tenant is visible to the client's administrator, who can remove it. Not decided here."
    - "PR-2 (for Q-056 and SEC-2; security owner). Tiqri as operator holds no standing access to a tenant's data; any access is time-limited, carries a recorded reason, and is written to the tenant's audit log as well as the database audit (I-8). Not decided here."
  scope: >-
    This ADR decides the isolation boundary, the data classes, the invariants and the placement model.
    It does not decide: the identity provider and sign-in (SEC-1); the encryption standard and key
    management, including whether keys are per tenant (SEC-1, S7-2.1.3-c03); the Azure regions and
    elastic-pool sizing (hosting ADR); the data-access library (data-access ADR); who grants
    memberships into a client's tenant (Q-031, PR-1); whether and how Tiqri as operator may reach
    tenant data (Q-056, SEC-2, PR-2); the identity under which background jobs run and what their audit
    entries record (AS-4); the release-1 tenant count (Q-038).
  verification: >-
    (1) Schema test, run in CI from F4, which fails the build if: any table not on the platform
    allow-list lacks the tenant column, a filter predicate or any of the four block predicates; any
    security policy is not STATE = ON or not schema-bound; any primary, unique or foreign key on a
    tenant table does not include the tenant identifier (I-9); or the application identity holds any
    permission outside the I-5 allow-list. Changes to the allow-list are reviewed by the security
    owner. (2) Cross-tenant test suite, run in CI on every change, with fixtures in which tenant A and
    tenant B both hold data of every kind. The list of endpoints, reports, exports and jobs under test
    is generated from the application's own route and job registry, and the build fails if any is not
    covered. For each, a positive control (tenant B's user sees B's data) and the attack (tenant A's
    user, by identifier, search and direct call under the application identity, cannot read, write or
    detect B's data, and gets the same response as for a missing identifier). It also covers: a
    connection with no tenant value reads and writes nothing; changing the value after it is set
    fails; insert, update and bulk insert carrying B's identifier under A's value are refused;
    re-pointing a foreign key to a B row is refused; background jobs and report runs; caches, files,
    search and queues (I-6); a membership removed takes effect on the next request (I-7); the audit
    entries of I-7, I-8 and I-11; and the shared-to-dedicated move (P-2). These are Tier-1 tests and
    may not be weakened or skipped (CLAUDE.md rule 8). (3) The suite runs against a shared and a
    dedicated database. (4) The security owner reviews the design at INCR-001 Gate B, and a
    penetration test covers cross-tenant access before Gate D.
links:
  derives_from: [ADR-0001, Q-031]
  related: [REV-01M64CE9TQR7XK2B9WD3HNP5QA, Q-003, Q-028, Q-038, Q-039, Q-056, Q-057, DEC-0010, GOV-SCOPE-INCR-001, S7-2.1.1-c01, S7-2.1.1-c02, S7-2.1.3-c03, S7-2.1.3-c04, S7-2.1.4-c03]
---

# ADR-0002: Tenant isolation

## Version history

- v1 (commit 2865a34): first draft.
- v2: answers REV-01M64CE9TQR7XK2B9WD3HNP5QA. B1: firm access and operator access move out of the
  invariants into proposals PR-1 and PR-2 for their owners. B2: I-4 fails closed and names every
  block predicate. B3: I-9, tenant-led keys. B4: I-5 allow-list and I-8 privileged identities. B5:
  platform data as its own class, I-11. B6: verification rebuilt (default-deny table set, generated
  endpoint list, positive controls, the missing cases). NF1 to NF6 taken in as noted below.

## Motivating requirements or constraints

- SRC-007 allows a "Cloud-hosted, multi-tenant or single-tenant" system (p.8, S7-2.1.1-c01) and
  requires "Data residency in each jurisdiction whose law requires it; the vendor states where data
  and backups physically sit" (p.10, S7-2.1.3-c04).
- Q-031 v3 (working answer): a tenant is one organisation; a firm (Tiqri, an audit firm or a client)
  keeps the books of client organisations, each its own tenant. So the platform may hold many
  tenants, and some users work in several.
- Q-038 v3 (working answer): release 1 is one entity, 125 named users, 50 at peak and 200,000 journal
  lines a month, per tenant. SRC-007's tested ceiling is far larger: 10,000 legal entities, 500,000
  named users and 100,000,000 journal lines a month (p.133).
- ADR-0001 fixes Azure SQL Database.
- GOV-SCOPE-INCR-001 v6 names isolation as a security point (SEC-2).
- The governance owner asked, in the orchestrator session of 2026-10-29, that tenant isolation be
  considered from the initial design; recorded in GOV-STATE of that date.

## Why now

Isolation shapes every table, key, index, query, cache and test. Microsoft: "Your choice of tenancy
model affects application design and management. Switching to a different model later is sometimes
costly." Retrofitting a tenant column or a database split onto a built ledger is a migration of
posted and audit-locked data. It is decided before the data model and the data-access ADR.

## Alternatives considered

- **A. Database per tenant, in elastic pools.**
  - For: the strongest isolation; a defect in one predicate exposes nothing across tenants;
    per-tenant restore is native; performance isolation between tenants; per-tenant encryption keys
    are simplest (SEC-1); residency by placing each database.
  - Against: higher cost per tenant where many tenants are small and mostly idle; one schema
    migration per database. Microsoft states that Azure SQL Database manages "well over 100,000
    databases" and rates the operational complexity "Low-Medium", so scale alone does not rule it out.
- **B. Shared databases only, tenant column and Row-Level Security.**
  - For: the lowest cost per tenant; one schema per database.
  - Against: Microsoft: "A multitenant database necessarily sacrifices tenant isolation"; one
    predicate defect or privileged misuse exposes every tenant in that database; noisy neighbours
    ("the Azure system has no built-in way to monitor or manage the use of these resources by an
    individual tenant"); per-tenant point-in-time restore is not native; residency needs a shared
    database per region.
- **C. Schema per tenant.** Not proposed: the migration burden of A without its isolation.
- **D. Hybrid of A and B, the same schema everywhere (proposed).** Microsoft's "hybrid sharded
  multitenant database model": "all databases have the tenant identifier in their schema", and "at
  any time, you can move a particular tenant to its own multitenant database".
  - For: B's cost for small tenants, A's isolation for tenants that need it, one code path and one
    test suite, a tenant can move without a schema change.
  - Against: the costs of both models plus a catalogue and a move procedure; shared databases keep
    B's blast radius and noisy-neighbour risk for the tenants in them.

**Recommendation and its condition.** D is proposed because Q-031 v3 implies many client tenants,
which Microsoft notes favours shared databases ("Multitenant databases are advantageous when there
are a large number of relatively inactive tenants"), while residency and the tested ceiling need
some tenants on their own. That rests on AS-1, which is unconfirmed. If the release-1 tenant count
(Q-038) turns out small, or the security owner does not accept AS-2, option A is the better choice;
under I-1 and I-9 the schema is the same either way, so A remains open until the hosting ADR.

## Evidence and assumptions

- Microsoft Learn, "Multitenant SaaS Patterns - Azure SQL Database", page git commit
  d0b41be05c89ea95874c19ddcbf4a115cdb89602, read 2026-10-29,
  https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns?view=azuresql.
  Quoted above, and: "The tenant identifier is the leading element in the primary key of all sharded
  tables" (supports I-9); "A catalog is required in which to maintain the mapping between tenants and
  databases" (I-11).
- Microsoft Learn, "Row-Level Security", page git commit 2ceb7c07640735a9c49dbb6ff1de511aceead449,
  read 2026-10-29,
  https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17:
  - "Block predicates explicitly block write operations (AFTER INSERT, AFTER UPDATE, BEFORE UPDATE,
    BEFORE DELETE) that violate the predicate" (I-4 c).
  - "Setting the @read_only parameter to 1 prevents the value from changing again until the
    connection is closed (returned to the connection pool)" (I-4 d: set on every open).
  - "Dbo users can alter or drop security policies however their changes to security policies can be
    audited" (I-8).
  - "It's highly recommended to create a separate schema for the RLS objects" and "Avoid type
    conversions in predicate functions" (I-4 e).
  - "block predicates AFTER INSERT applies to bulk insert operations just as they would regular
    insert operations" (I-4 d, verification).
  - "security predicates on the current table aren't automatically replicated to the history table"
    (I-1).
  - "Change Data Capture (CDC) can leak entire rows that should be filtered to members of db_owner"
    (I-6).
  - "It's possible to cause information leakage by using carefully crafted queries that use errors
    to exfiltrate data" (I-10).
  - "indexed views can't be created on top of tables that have a security policy" (Consequences).
  - The page does not say whether foreign-key checks are filtered by a predicate. I-9 removes the
    dependency; the cross-tenant suite tests it.
  - These are web pages, not registered sources. Registering them as a source is for the governance
    owner; until then the quoted passages and page commits above are the evidence.
- **Labelled assumptions** (orchestrator; each confirmed by its owner before approval):
  - AS-1: many tenants will be small and mostly idle (a firm's clients). From Q-031 v3; the release-1
    tenant count is open (Q-038). Owner: product owner.
  - AS-2: Row-Level Security under I-4, I-5 and I-9, with the verification above, is acceptable
    isolation for a shared database. Owner: security owner.
  - AS-3: a firm's work across clients needs no query that spans tenants' tenant data; a firm-wide
    view, if wanted, is built from per-tenant results under I-3. Owner: product owner, with Q-031.
  - AS-4: background jobs act in one tenant, on behalf of the user who started or scheduled them.
    Under which identity they connect, and what their audit entries record against S7-2.1.4-c03
    ("Login identity, not a shared or system account", p.10), is open. Owner: security owner.
  - AS-5: the test or sandbox environment "refreshed from production on request" (p.8,
    S7-2.1.1-c02) is read here as a per-tenant copy. The clause does not say so, and putting a
    tenant's production books in a test environment is a data-handling question. Owners: security
    owner, product owner.
- No evidence was found in SRC-007 of which countries require data held in-country.

## Decision owner and approval status

- Deciders: the security owner (the isolation guarantee, AS-2, AS-4, I-8, PR-1, PR-2) and the tech
  lead (placement). Both are held by the governance owner (authority matrix v2). The product owner is
  consulted on P-3, AS-1, AS-3 and AS-5, where cost or scope is affected.
- Tier 1: isolation is in the Tier-1 list. Stage 0 approvals do not count for Tier 1, so no approval
  request is raised until F2 (GitHub) is in place.
- The authority matrix's small-team fallback says Tier-1 policy approvals "still need a second named
  person, external if necessary", and one person holds both deciding roles here. Whether a Tier-1 ADR
  needs that second person is for the governance owner to say.
- Status: Proposed. Reviews: REV-01M64CE9TQR7XK2B9WD3HNP5QA on v1 (blocking); v2 to be reviewed.

## Consequences

- Positive: isolation enforced by the database as well as by code, failing closed; one schema and one
  test suite; residency handled by placement; a tenant can move from shared to dedicated as it grows,
  or the whole platform to option A, without a schema change.
- Negative:
  - Every key and unique index on tenant data leads with the tenant identifier (I-9). CAP-13's
    "unique across the system" for entity, series and number is unchanged in meaning, because an
    entity belongs to exactly one tenant.
  - A shared database cannot restore one tenant to a point in time. A per-tenant export and restore
    procedure is needed and tested against the backup objectives (RPO [4] hours, RTO [8] hours,
    p.132).
  - Indexed views cannot be used on tenant tables.
  - The platform store and catalogue (I-11) are critical components with their own availability,
    audit and security review.
  - Row-Level Security adds a predicate to every query; the tenant column leads the relevant indexes.
  - Tenants in a shared database share its performance; tenant-level monitoring is the application's
    to build.
- Open items that change this ADR if answered differently: Q-031 and PR-1, Q-056 and PR-2 with SEC-2,
  Q-028 and Q-003 (residency), Q-038 and AS-1 (tenant count), SEC-1 (keys), AS-4, AS-5.
- Nothing here may be built before Gate C (CLAUDE.md rule 1).
