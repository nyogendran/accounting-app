---
id: ADR-0001
type: adr
title: Application stack baseline - React frontend, .NET backend, Azure with Azure SQL Database
status: Proposed
version: 1
owner: orchestrator
tier: 2
normative:
  decision: >-
    TIQACC is built as a browser application with a React frontend and a .NET backend, hosted on
    Microsoft Azure, with its data in Azure SQL Database. Versions: the backend targets .NET 10, the
    current long-term-support release (released 11 November 2025, supported to 10 November 2028); the
    frontend uses React 19, pinned to the latest 19.x patch confirmed on the npm registry when the
    project is first scaffolded (19.3.1 at the time of writing). Every dependency is pinned to an
    exact version in source control, never a range or "latest".
  scope: >-
    This ADR fixes only the four choices above and the version policy. It does not decide the data
    access approach, the tenant isolation mechanism, identity and sign-in, the frontend component
    library or design system, the API style, the hosting topology or the Azure regions. Each of those
    is its own ADR, listed under follow_on_decisions.
  version_policy: >-
    The backend stays on long-term-support releases of .NET; a short-term-support release (such as
    .NET 11, expected November 2026) is not adopted. A move to the next long-term-support release is a
    change to this ADR. Security patches within the pinned major version are applied as they are
    released.
  follow_on_decisions:
    - Tenant isolation mechanism in Azure SQL Database (Q-031, Q-056; Tier 1, security owner with tech lead).
    - Data access approach over Azure SQL Database.
    - Identity, sign-in and multi-factor authentication (SEC-1 in GOV-SCOPE-INCR-001; security owner).
    - Frontend component library, design system and accessibility standard (with the L4 UX specification).
    - API style between frontend and backend.
    - Azure hosting topology, environments, and the regions that hold data and backups per country (Q-028, S7-2.1.3-c04).
  constraints:
    - "Cloud-hosted, multi-tenant or single-tenant, accessed through a current browser with no local installation and no browser plug-in (SRC-007 p.8, S7-2.1.1-c01)."
    - "Q-054 v2: the governance owner's answer as tech lead of 2026-10-28 (Azure, Azure SQL Database; React and .NET at their latest stable versions; a highly intuitive UI)."
  verification: >-
    The tech lead reviews the scaffolded repository at INCR-001 Gate B: the backend project files
    target net10.0; package manifests pin React and every other dependency to exact versions; no
    dependency is a range or "latest". From F4, CI fails a build that declares a dependency range.
links:
  derives_from: [Q-054]
  related: [DEC-0010, GOV-SCOPE-INCR-001, Q-028, Q-031, Q-056, S7-2.1.1-c01, S7-2.1.3-c04]
---

# ADR-0001: Application stack baseline

- **Motivating requirements or constraints:** SRC-007 asks for a cloud-hosted, browser-based system
  with no local installation (p.8, S7-2.1.1-c01). The governance owner, as tech lead, chose Azure and
  Azure SQL Database, and React and .NET at their latest stable versions, on 2026-10-28 (Q-054 v2).
  DEC-0010 puts the stack ADR in INCR-001's Gate B.

- **Alternatives considered:**
  - *Backend on .NET 11 when it ships (November 2026).* It would be "latest" for a few weeks, but it is
    a short-term-support release. Not proposed: a finance system needs the longer support window, and
    a move every year adds upgrade work to Tier-1 code.
  - *Backend on .NET 10 (long-term support).* Proposed. It is the latest stable long-term-support
    release, with security updates to 10 November 2028. The next long-term-support release, expected
    November 2027, is a planned upgrade under this ADR's version policy.
  - *Frontend on React 19.x.* Proposed, as chosen. No React 20 exists at the time of writing.
  - *Other frontend or backend frameworks.* Not considered: the tech lead named React and .NET.

- **Evidence and assumptions:**
  - .NET release and support dates: Microsoft's .NET blog and lifecycle page, read 2026-10-29 (.NET 10
    released 11 November 2025 and supported to 10 November 2028; .NET 8 and .NET 9 end support on
    10 November 2026; .NET 11 expected November 2026 as short-term support). Sources:
    https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/,
    https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/,
    https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core.
  - React 19.3.1, released 14 October 2026: the React GitHub releases page and Wikipedia, read
    2026-10-29. react.dev could not be reached to confirm it. **Labelled assumption:** the exact patch
    is confirmed on the npm registry at scaffolding, and that confirmation is recorded with the pin.
  - The "highly intuitive" UI goal in Q-054 v2 is a usability requirement. It goes to the L4 UX
    specification and the design-system ADR, not to this one.

- **Decision owner and approval status:** the tech lead (authority matrix v2, "Architecture and
  technology stack"), who escalates to the product owner where cost or scope is affected. Status:
  Proposed. Tier 2: the stack choice itself is not posting, numbering, isolation or money; the Tier-1
  parts, tenant isolation above all, are separate ADRs. No approval request has been raised yet.

- **Consequences:**
  - Positive: one supported platform from database to browser; security updates for the backend to
    November 2028; the follow-on design work in INCR-001 can start from a fixed base.
  - Negative: a planned upgrade to the next long-term-support .NET release before November 2028.
    Choosing Azure SQL Database ties tenant isolation to what that database offers, which the
    isolation ADR must settle.
  - Nothing here may be built before Gate C (CLAUDE.md rule 1). This ADR only fixes the base that the
    INCR-001 designs build on.
