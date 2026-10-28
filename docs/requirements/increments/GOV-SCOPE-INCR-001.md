---
id: GOV-SCOPE-INCR-001
type: governance
title: "Scope proposal for the foundation increment (INCR-001)"
status: Proposed
version: 2
owner: requirements-engineer
tier: 1
revised_after_review: [REV-01M61MRRKX52P8XHG3NZXSPCZJ]
links:
  governed_by: [DEC-0010]
  related: [DEC-0007, DEC-0008, GOV-IMPACT-SRC007, GOV-BRIEF-R1-SCOPE, GOV-QPACK-L1, REV-01M61MRRKX52P8XHG3NZXSPCZJ,
    Q-055, Q-056, Q-057,
    S7-2.2.4-c37, S7-2.2.4-c38, S7-2.2.4-c39, S7-2.2.4-c40, S7-2.2.4-c41, S7-2.2.4-c42, S7-2.2.4-c43, S7-2.2.4-c49, S7-2.2.4-c50,
    S7-2.2.4-c51, S7-2.2.4-c52, S7-2.2.4-c53, S7-2.2.4-c54, S7-2.2.4-c55, S7-2.2.4-c56,
    S7-2.2.1-c47, S7-2.2.2-c21, S7-2.2.2-c35, S7-2.16.1-c33, S7-2.16.1-c34, S7-2.16.5-c23, S7-2.2.2-c25,
    Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010, Q-011, Q-012, Q-013, Q-014, Q-015, Q-016, Q-017, Q-018, Q-019, Q-020,
    Q-021, Q-022, Q-023, Q-024, Q-025, Q-026, Q-027, Q-028, Q-029, Q-030, Q-031, Q-032, Q-033, Q-034, Q-035, Q-036, Q-037, Q-038, Q-039, Q-040,
    Q-041, Q-042, Q-043, Q-044, Q-045, Q-046, Q-047, Q-048, Q-049, Q-050, Q-051, Q-052, Q-053, Q-054,
    S7-2.1.1-c01, S7-2.1.1-c04,
    S7-2.1.2-c01, S7-2.1.2-c02, S7-2.1.2-c03, S7-2.1.2-c05, S7-2.1.2-c06, S7-2.1.2-c07, S7-2.1.2-c08, S7-2.1.2-c09, S7-2.1.2-c10,
    S7-2.1.2-c12, S7-2.1.2-c13, S7-2.1.2-c14, S7-2.1.2-c15, S7-2.1.2-c16, S7-2.1.2-c17, S7-2.1.2-c18, S7-2.1.2-c19, S7-2.1.2-c24, S7-2.1.2-c25, S7-2.1.2-c26, S7-2.1.2-c27,
    S7-2.1.3-c05,
    S7-2.1.4-c01, S7-2.1.4-c02, S7-2.1.4-c03, S7-2.1.4-c04, S7-2.1.4-c05, S7-2.1.4-c06, S7-2.1.4-c07, S7-2.1.4-c08,
    S7-2.1.10-c01, S7-2.1.10-c04, S7-2.1.10-c11, S7-2.1.10-c12, S7-2.1.10-c13, S7-2.1.10-c14, S7-2.1.10-c15, S7-2.1.10-c16, S7-2.1.10-c17, S7-2.1.10-c18, S7-2.1.10-c19,
    S7-2.1.10-c20, S7-2.1.10-c21, S7-2.1.10-c22, S7-2.1.10-c23, S7-2.1.10-c24, S7-2.1.10-c25, S7-2.1.10-c26, S7-2.1.10-c27, S7-2.1.10-c28, S7-2.1.10-c29, S7-2.1.10-c31,
    S7-2.1.10-c38, S7-2.1.10-c39, S7-2.1.10-c40, S7-2.1.10-c42, S7-2.1.10-c43,
    S7-2.1.11-c01, S7-2.1.11-c02,
    S7-2.2.1-c01, S7-2.2.1-c02, S7-2.2.1-c03, S7-2.2.1-c04, S7-2.2.1-c05, S7-2.2.1-c06, S7-2.2.1-c07, S7-2.2.1-c08, S7-2.2.1-c10, S7-2.2.1-c11, S7-2.2.1-c12, S7-2.2.1-c13,
    S7-2.2.1-c15, S7-2.2.1-c17, S7-2.2.1-c31, S7-2.2.1-c44, S7-2.2.1-c48, S7-2.2.1-c51, S7-2.2.1-c52, S7-2.2.1-c53, S7-2.2.1-c54, S7-2.2.1-c55, S7-2.2.1-c56, S7-2.2.1-c57,
    S7-2.2.1-c62, S7-2.2.1-c64, S7-2.2.1-c66,
    S7-2.2.2-c01, S7-2.2.2-c02, S7-2.2.2-c04, S7-2.2.2-c05, S7-2.2.2-c06, S7-2.2.2-c07, S7-2.2.2-c08, S7-2.2.2-c09, S7-2.2.2-c10, S7-2.2.2-c11, S7-2.2.2-c14, S7-2.2.2-c15,
    S7-2.2.2-c17, S7-2.2.2-c20, S7-2.2.2-c42, S7-2.2.2-c43, S7-2.2.2-c44, S7-2.2.2-c45, S7-2.2.2-c46, S7-2.2.2-c48, S7-2.2.2-c49, S7-2.2.2-c50, S7-2.2.2-c52, S7-2.2.2-c54,
    S7-2.2.3-c01, S7-2.2.3-c02, S7-2.2.3-c03, S7-2.2.3-c04, S7-2.2.3-c05, S7-2.2.3-c06, S7-2.2.3-c07, S7-2.2.3-c08, S7-2.2.3-c09, S7-2.2.3-c11, S7-2.2.3-c12, S7-2.2.3-c14, S7-2.2.3-c16,
    S7-2.2.4-c01, S7-2.2.4-c16, S7-2.2.4-c47, S7-2.2.4-c77,
    S7-2.2.5-c01, S7-2.2.5-c05, S7-2.2.5-c08,
    S7-2.2.6-c01, S7-2.2.6-c03, S7-2.2.6-c04, S7-2.2.6-c05, S7-2.2.6-c06, S7-2.2.6-c09, S7-2.2.6-c10, S7-2.2.6-c11, S7-2.2.6-c12, S7-2.2.6-c13, S7-2.2.6-c15, S7-2.2.6-c16,
    S7-2.2.6-c22, S7-2.2.6-c23, S7-2.2.6-c24, S7-2.2.6-c25, S7-2.2.6-c26, S7-2.2.6-c28,
    S7-2.2.8-c01, S7-2.2.8-c02, S7-2.2.8-c03, S7-2.2.8-c04, S7-2.2.8-c05, S7-2.2.8-c06, S7-2.2.8-c07, S7-2.2.8-c08, S7-2.2.8-c09, S7-2.2.8-c10, S7-2.2.8-c11, S7-2.2.8-c12,
    S7-2.2.8-c13, S7-2.2.8-c14, S7-2.2.8-c15, S7-2.2.8-c17, S7-2.2.8-c25, S7-2.2.8-c26, S7-2.2.8-c27, S7-2.2.8-c28, S7-2.2.8-c44, S7-2.2.8-c45, S7-2.2.8-c47, S7-2.2.8-c48,
    S7-2.2.9-c01, S7-2.2.9-c02, S7-2.2.9-c03, S7-2.2.9-c04, S7-2.2.9-c05, S7-2.2.9-c06, S7-2.2.9-c09, S7-2.2.9-c11, S7-2.2.9-c12, S7-2.2.9-c15, S7-2.2.9-c17,
    S7-2.2.9-c20, S7-2.2.9-c21, S7-2.2.9-c23, S7-2.2.9-c37,
    S7-2.2.11-c01, S7-2.2.11-c02,
    S7-2.14.1-c08, S7-2.14.2-c01, S7-2.14.2-c04, S7-2.14.2-c05, S7-2.14.2-c10, S7-2.14.2-c14, S7-2.14.2-c15, S7-2.14.2-c19,
    S7-2.16.1-c08, S7-2.16.1-c14, S7-2.16.1-c21, S7-2.16.1-c22, S7-2.16.1-c23, S7-2.16.1-c24, S7-2.16.1-c25, S7-2.16.1-c26, S7-2.16.1-c39,
    S7-2.1.3-c01, S7-2.1.3-c02, S7-2.1.3-c03, S7-2.1.3-c04, S7-2.1.1-c02, S7-2.1.1-c03, S7-2.1.1-c05,
    S7-2.1.5-c01, S7-2.1.6-c01, S7-2.1.7-c01, S7-2.1.8-c01, S7-2.1.9-c01,
    S7-2.1.2-c04, S7-2.1.2-c11, S7-2.1.2-c20, S7-2.1.2-c21, S7-2.1.2-c22, S7-2.1.2-c23,
    S7-2.2.1-c09, S7-2.2.1-c14, S7-2.2.1-c16, S7-2.2.1-c18, S7-2.2.1-c33, S7-2.2.1-c34, S7-2.2.1-c35, S7-2.2.1-c36, S7-2.2.1-c46, S7-2.2.1-c50, S7-2.2.1-c63, S7-2.2.1-c65, S7-2.2.1-c67,
    S7-2.2.2-c03, S7-2.2.2-c12, S7-2.2.2-c13, S7-2.2.2-c47, S7-2.2.2-c51, S7-2.2.2-c53, S7-2.2.2-c55,
    S7-2.2.4-c19, S7-2.2.4-c57, S7-2.2.5-c02, S7-2.2.5-c03, S7-2.2.5-c04, S7-2.2.5-c06, S7-2.2.5-c07, S7-2.2.5-c09, S7-2.2.5-c10, S7-2.2.6-c07, S7-2.2.6-c08, S7-2.2.6-c14, S7-2.2.6-c27,
    S7-2.2.7-c01, S7-2.2.8-c16, S7-2.2.8-c30, S7-2.2.8-c31, S7-2.2.8-c32, S7-2.2.8-c33, S7-2.2.8-c34, S7-2.2.8-c39, S7-2.2.8-c46,
    S7-2.2.9-c07, S7-2.2.9-c10, S7-2.2.9-c16, S7-2.2.9-c18, S7-2.2.9-c24, S7-2.2.10-c01,
    S7-2.1.10-c30, S7-2.1.10-c32, S7-2.1.10-c41, S7-2.3-c01, S7-2.4-c01, S7-2.5-c01, S7-2.6-c01, S7-2.7-c01, S7-2.8-c01, S7-2.9-c01, S7-2.10-c01,
    S7-2.11-c01, S7-2.12-c01, S7-2.13-c01, S7-2.14.1-c01, S7-2.14.3-c01, S7-2.15.8-c01, S7-2.16.2-c01, S7-2.16.5-c01]
normative:
  statement: >-
    Proposed scope of the foundation increment INCR-001 under DEC-0010. It lists the capabilities in
    scope with their S7 clauses, the explicit exclusions with reasons, the classification of every
    question Q-001 to Q-054 as blocking or not-blocking for the foundation, the working assumptions the
    scope relies on, the accounting-policy points it names without deciding, and the decisions asked of
    the product owner. It is a proposal. No requirement, story or acceptance criterion is written here.
  basis:
    - "DEC-0010 v1 (Approved), normative.decision and conditions 1 to 5."
    - "SRC-007 (V2.2) is the baseline (DEC-0008). Clause text was read from the extraction of SRC-007; the PDF is authoritative if the extraction looks garbled."
    - "No in-scope capability posts from a sub-ledger, so none depends on Q-029 (release-1 scope). Each capability states its own independence."

  decisions_requested_of_product_owner:
    - id: D-1
      text: "Approve the scope below as proposed, including the narrowings and extensions of DEC-0010's first list (section changes_to_dec0010_list). Each departure from plain V2.2 text is its own item in departures_from_plain_text (DEP-1 to DEP-8) and is confirmed or rejected one by one; approving the scope does not approve a departure unless it is confirmed there."
    - id: D-2
      text: "Confirm that a firm's access to its clients' tenants (EXC-01), the production tenant bootstrap (EXC-27, Q-056) and the behaviour at a capacity limit (EXC-29, Q-057) leave INCR-001 until their owners answer."
    - id: D-3
      text: "Product owner with the qualified accountant (DEC-0010 condition 5): confirm that year-end close and retained-earnings roll-up are not in INCR-001 (EXC-13), and the proposed limit that INCR-001 opens one financial year per entity and shows no balance across a year end (CAP-14, CAP-15)."
    - id: D-4
      text: "Confirm that the governance panel (2.15.8) is not in INCR-001: events it would report are recorded in the audit log and the reporting surface waits (EXC-18). This is phasing decision D-2.15.8."
    - id: D-5
      text: "Confirm that no delivered standard chart, industry variant, chart upload or group chart is in INCR-001 (EXC-06, EXC-07, DEP-3): accounts are created one request at a time through the approval route."
    - id: D-6
      text: "Product owner with the qualified accountant: confirm that the V2.2 delivered-defaults table for control levels (S7-2.2.1-c58 to c61) is not built in INCR-001: levels are set explicitly per entity and per control type (see CAP-11, Q-033 and DEP-6)."
    - id: D-7
      text: "Product owner with the qualified accountant: confirm that INCR-001 journals are manual journals only, and that the adjustment type, closed-period correction and the adjustment periods wait for Q-055 (EXC-28)."

  departures_from_plain_text:
    note: "Each item sets aside a rule V2.2 states plainly, with no bracket and no open question. Each is for the product owner to confirm or reject on its own."
    items:
      - {id: DEP-1, sets_aside: "The duplicate check as a step of the only route for adding an account (S7-2.2.1-c44, S7-2.2.2-c03).", reason: "It protects chart quality, not the ledger; keeps the first increment's Tier-1 surface small. A product-owner choice."}
      - {id: DEP-2, sets_aside: "Ranked alternatives with every refused code (S7-2.2.2-c25).", reason: "The refusal still names what holds the code. A product-owner choice."}
      - {id: DEP-3, sets_aside: "'An entity never begins with an empty chart' (S7-2.2.1-c33): INCR-001 delivers no standard chart and an entity starts empty.", reason: "The delivered chart is Finance's data and unconfirmed (Q-005). A product-owner choice."}
      - {id: DEP-4, sets_aside: "An approver may amend a pending entry within a configurable threshold (S7-2.2.6-c07, c08).", reason: "A product-owner choice to hold it for a later increment. The threshold being configurable is not the reason: V2.2 does admit it as a setting."}
      - {id: DEP-5, sets_aside: "Year-end close, and a new year opened and transacted in before the prior year is closed (S7-2.2.8-c34, c37).", reason: "Needs a retained-earnings policy (qualified accountant and product owner). INCR-001 opens one financial year per entity (D-3)."}
      - {id: DEP-6, sets_aside: "The delivered default control level by organisation type (S7-2.2.1-c58 to c61).", reason: "Needs the answer to Q-033. Levels are set explicitly at entity set-up."}
      - {id: DEP-7, sets_aside: "The 'Mandatory on' column of the dimension table read as a floor (S7-2.2.3-c02 to c07).", reason: "Read as a default the per-account rule (c09) can override; see WA-10, pending the qualified accountant."}
      - {id: DEP-8, sets_aside: "A tax code on journal lines and a default tax code on accounts (S7-2.2.4-c57, S7-2.2.1-c09).", reason: "Tax is the tax specialist's and excluded (EXC-19)."}

  changes_to_dec0010_list:
    - {item: "tenants as organisations", change: "confirmed, with an entity register added; the production route that creates a tenant, its first entity and its first administrator leaves (EXC-27, Q-056)", why: "V2.2 makes the entity a mandatory attribute of every transaction (S7-2.14.2-c14) and holds periods, numbering, control levels and roles per entity, so the entity must exist from the start. Who creates a tenant can also reach into it, which is a security decision."}
    - {item: "a firm's access to its clients' tenants", change: "narrowed: leaves the increment", why: "Q-031 v3 leaves open who owns a client's data, who grants and withdraws a firm's access, how it is logged and under which roles. Those are security and product decisions (blocking, EXC-01)."}
    - {item: "users, roles", change: "confirmed, extended with segregation of duties and delegation", why: "S7-2.1.2 builds roles with a segregation-of-duties matrix and names two controls the system enforces by itself (c16): approval of one's own document and the audit log. Journal approval (second user) cannot be specified without them."}
    - {item: "audit log", change: "confirmed", why: "S7-2.1.4 states it plainly."}
    - {item: "double-entry journals, immutable once posted, corrected by reversal", change: "confirmed and narrowed to manual journals and their correction by reversal", why: "Template, recurring, accrual, intercompany, year-end and upload routes need schedules, groups, year-end policy or the upload mapping engine (EXC-15). The adjustment type is held out pending Q-055 (EXC-28). Post-approval dimension or narrative changes are held back by Q-007 (EXC-11)."}
    - {item: "periods opened and closed", change: "confirmed and extended to all four states, narrowed to the general-ledger period of an entity", why: "S7-2.2.8 defines open, soft closed (optional), hard closed and audit locked as one set. The override route (Q-013), year-end close, close checklist, module period states and the adjustment and special audit adjustment periods leave (EXC-12, EXC-13, EXC-14, EXC-28)."}
    - {item: "gapless numbering series as configuration", change: "confirmed, narrowed to series for journals; formats prescribed by a tax authority leave", why: "Authority-prescribed formats and ranges belong to the tax specialist (Q-035, Q-046, Q-015) and to tax documents that do not exist yet (EXC-19)."}
    - {item: "chart of accounts with control flags and enforcement levels as settings", change: "confirmed and narrowed; extended with controlled account creation and dimension rules", why: "Posting is blocked to accounts whose dimension rules are not satisfied (S7-2.2.1-c52), and V2.2 allows no second route by which an account appears (S7-2.2.1-c44, S7-2.2.2-c54). Delivered chart, upload, group chart, duplicate check and the naming standard leave (EXC-06 to EXC-09). Changing a flag after creation leaves (Q-034, EXC-10)."}
    - {item: "currencies with decimal places from currency configuration", change: "confirmed and extended with manually entered rates and the stored transaction and functional amounts", why: "A foreign-currency journal cannot be specified without a rate and its source (S7-2.2.5-c08, S7-2.2.9-c37). Rate feeds, revaluation and translation leave (EXC-17)."}
    - {item: "not in DEC-0010's list", change: "added: capacity limits as configuration (CAP-06) and ledger enquiry (CAP-15)", why: "V2.2 forbids a limit written as a constant (S7-2.16.1-c23, c39), which shapes every capability from the first line of design. A ledger that cannot be queried back to its journals cannot be tested (S7-2.2.4-c77)."}

  capabilities:
    - id: CAP-01
      title: "Tenant as the organisation boundary, and the entity register"
      includes:
        - "A tenant is one organisation. Its entities, users, roles, configuration and ledger data belong to exactly one tenant."
        - "An entity register holding legal name, registration number, jurisdiction, entity type, functional currency and financial year end. Tax registration numbers and status are left out (EXC-19)."
        - "Every transaction belongs to exactly one entity. Users are assigned to entities and cannot view or post to an entity they are not assigned to, in search results and reports as well as entry screens."
        - "The number of entities, like every capacity figure, is a technical-capacity setting under CAP-06 and is not a licence cap or an enforced limit (S7-2.16.1-c33). What happens at a limit waits on Q-057 (EXC-29). Group structure, ownership and consolidation are excluded (EXC-26)."
        - "No production route creates a tenant, its first entity or its first administrator (EXC-27, Q-056). Test tenants are created by the proposal in EXC-27, which is not a production route."
      clauses: [S7-2.1.1-c01, S7-2.14.1-c08, S7-2.14.2-c01, S7-2.14.2-c14, S7-2.14.2-c15]
      decisions: [DEC-0010]
      relies_on:
        - "working assumption: governance owner's answer of 2026-10-28, pending product owner (Q-031 v3): a tenant is an organisation; a firm keeps the books of client organisations, each its own tenant."
        - "working assumption: governance owner's answer of 2026-10-20, pending product owner (Q-001): TIQACC is Tiqri's own multi-tenant SaaS product."
        - "working assumption: governance owner's answer of 2026-10-28, pending product owner (Q-038 v3): release 1 is one entity per tenant."
        - "working assumption: governance owner's answer of 2026-10-28, pending tech lead's stack decision record at Gate B (Q-054): Azure with Azure SQL Database. The scope does not depend on it; the isolation mechanism does (see stack_dependencies)."
      independence: "Independent of Q-029: no sub-ledger is involved. The blocking questions touching tenants (Q-031, Q-056, Q-057) are removed by excluding firm access (EXC-01), the production bootstrap (EXC-27) and behaviour at a limit (EXC-29); this capability rests only on the part of Q-031 both answers state, the tenant being an organisation."
    - id: CAP-02
      title: "Users"
      includes:
        - "Named users, each identified individually. No shared or system account is used for an interactive action."
        - "A leaver is disabled immediately and the user's transaction history stays intact."
        - "The way a user proves identity (single sign-on provider, multi-factor, password and lockout policy, encryption standard) is a security-owner decision (EXC-02, SEC-1)."
      clauses: [S7-2.1.3-c05, S7-2.1.4-c03, S7-2.14.2-c15]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029 and of every blocking question. Authentication clauses S7-2.1.3-c01 to c03 are not taken into scope, so no security assumption is made here."
    - id: CAP-03
      title: "Roles, permissions and their assignment"
      includes:
        - "A role is a named set of granular permissions, each a module, an object and an action (view, create, amend, approve, post, cancel, export, administer). Roles are built by the entity's administrator: from scratch, copied, or adjusted."
        - "Permissions are scoped to entities and to dimension values. Other scopes named in S7-2.1.2-c03 (bank accounts, document types, locations as master data) arrive with their modules."
        - "A user may hold any number of roles; effective permissions are the union, and an explicit denial overrides a grant. Roles are assigned per entity, effective-dated, with temporary assignment and delegation under the delegate's own login."
        - "A role change takes effect for every user holding it, is effective-dated and is written to the audit log with before and after values."
        - "A screen shows a user's effective permissions and which role grants each, and can be exported."
      clauses: [S7-2.1.2-c01, S7-2.1.2-c02, S7-2.1.2-c03, S7-2.1.2-c05, S7-2.1.2-c06, S7-2.1.2-c07, S7-2.1.2-c08, S7-2.1.2-c09, S7-2.1.2-c10]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029 and of every blocking question. Value limits (S7-2.1.2-c04) and bulk assignment by position (c11) leave with their modules (EXC-24)."
    - id: CAP-04
      title: "Segregation of duties"
      includes:
        - "A segregation-of-duties matrix kept by the administrator, checked when roles are assigned, warning or blocking per rule and naming the conflicting permissions."
        - "A conflict may be accepted as a documented exception, approved by a role the entity names, with an expiry date, a compensating control and a standing exceptions list. A conflict report can be run for all users and entities."
        - "Two controls the system enforces and no role configuration can switch off: a user cannot approve a document they raised, and no role can amend or delete the audit log."
        - "A starting role set supplied as editable data, limited to the roles whose permissions exist in the foundation: Preparer, Approver, Finance manager, Administrator and Auditor, with the default 'must not do' column."
        - "S7-2.1.11-c01 (a user holding an incompatible role pair cannot be saved) is read as applying where the administrator has set the rule to block (S7-2.1.2-c13); where set to warn, the assignment is saved with the warning."
      clauses: [S7-2.1.2-c12, S7-2.1.2-c13, S7-2.1.2-c14, S7-2.1.2-c15, S7-2.1.2-c16, S7-2.1.2-c17, S7-2.1.2-c18, S7-2.1.2-c19, S7-2.1.2-c24, S7-2.1.2-c25, S7-2.1.2-c26, S7-2.1.2-c27, S7-2.1.11-c01]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029 and of every blocking question. The roles for sales, purchases, stores and payroll (S7-2.1.2-c20 to c23) leave with their modules; the auditor's access to individual pay (Q-026) does not arise without payroll."
    - id: CAP-05
      title: "Audit log"
      includes:
        - "Every create, amend, delete, approve, reject, cancel, export and login event, failed logins included, is written to a log that no user or administrator can edit."
        - "Each entry records timestamp to the second with time zone, user, action, object, field-level before and after values, and source."
        - "The log is queryable by user, date, module and document and exportable to Excel. It runs alongside, and does not replace, the history held on each transaction."
        - "The application provides no way to purge the log. The retention period [7] years is a bracketed value (see bracketed_values_relied_on); no deletion capability is built, so Q-025 and Q-020 do not block."
        - "Testability limits: the acceptance statement S7-2.1.11-c02 (an amended posted document shows before and after values) can be exercised in INCR-001 on master data only, because no posted entry can be amended (CAP-12, EXC-11). Login and failed-login events can be tested only after the authentication mechanism is decided (SEC-1, EXC-02)."
      clauses: [S7-2.1.4-c01, S7-2.1.4-c02, S7-2.1.4-c03, S7-2.1.4-c04, S7-2.1.4-c05, S7-2.1.4-c06, S7-2.1.4-c07, S7-2.1.4-c08, S7-2.1.11-c02, S7-2.2.6-c28]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029 and of every blocking question."
    - id: CAP-06
      title: "Capacity figures as configuration, with a warning"
      includes:
        - "The 2.16.1 figures are technical capacity. None is a licence cap, a tier boundary or a limit the software enforces against the entity (S7-2.16.1-c33, S7-2.16.5-c23). INCR-001 counts no user or entity against a licence."
        - "No capacity figure is a constant in the source. Each is a configuration value with a default, an administrator-facing setting and an effective date, set per tenant and per entity."
        - "Changing a figure takes effect without a release, redeployment or restart, and is recorded in the audit log with who, from what, to what and when. Which role may change a tenant's figure, the tenant's own administrator or the operator, is open (Q-057, EXC-29); the permission to do so is an ordinary permission under CAP-03."
        - "The system warns at a configurable proportion of a figure ([80]% by default), naming the figure and the current level, and never fails silently (S7-2.16.1-c26). The role named in the warning is the holder of the permission above. What the system does at 100% of a figure is held out (EXC-29)."
        - "No limit is implemented so that it cannot be raised: no fixed-width identifier, no counter that cannot be widened, no key or partition scheme that assumes a maximum."
        - "Defaults for the rows named in the governance owner's working answer: one legal entity, 125 named users, 50 concurrent users at peak, 200,000 journal lines a month. The other rows of the single-entity column are open in Q-038 and are not assumed."
      clauses: [S7-2.16.1-c23, S7-2.16.1-c24, S7-2.16.1-c25, S7-2.16.1-c26, S7-2.16.1-c33, S7-2.16.1-c39, S7-2.16.1-c08, S7-2.16.1-c14, S7-2.16.1-c21, S7-2.16.1-c22, S7-2.16.5-c23]
      decisions: [DEC-0010]
      relies_on:
        - "working assumption: governance owner's answer of 2026-10-28, pending product owner (Q-038 v3): release 1 is one entity, 125 named users, 50 at peak and 200,000 journal lines a month, per tenant."
      independence: "Independent of Q-029. Q-038's open rows change default values only, because every figure is a setting; Q-038 is therefore not-blocking. Behaviour at a limit and who raises a figure are Q-057 (blocking), held out as EXC-29; this capability builds only the setting, the audit record and the warning."
    - id: CAP-07
      title: "Currency master and manually entered rates"
      includes:
        - "All ISO 4217 currencies held with code, numeric code, name, symbol and minor-unit precision. Each entity nominates its functional currency, fixed once transactions exist."
        - "Currencies are activated or deactivated per entity; a currency with history is deactivated, never deleted. An entity that uses one currency sees no currency selection, rate or revaluation."
        - "Rounding and precision follow the currency's minor unit, including zero-decimal and three-decimal currencies. This is the plain text of S7-2.2.9-c06; the number of places is never fixed at two."
        - "Rates entered and maintained by Finance (the manual company rate), each with its rate type, effective date, source and retrieval time. Rates are never overwritten. A transaction stores the rate applied to full precision, its source and type, and, where a user overrode the proposed rate, who, when and why."
        - "Each transaction stores its transaction-currency amount, its functional-currency amount and the period lock state at posting. The reporting-currency amount (S7-2.2.9-c22) is not stored in INCR-001; S7-2.2.9-c23 and c09 are cited as partly built, and the effect on later groups is a Gate B input (stack_dependencies)."
        - "Rates for a closed or locked accounting period cannot be changed (the first sentence of S7-2.2.9-c18). The rate-table lock and unlock is excluded (EXC-17)."
      clauses: [S7-2.2.9-c01, S7-2.2.9-c02, S7-2.2.9-c03, S7-2.2.9-c04, S7-2.2.9-c05, S7-2.2.9-c06, S7-2.2.9-c09, S7-2.2.9-c11, S7-2.2.9-c12, S7-2.2.9-c15, S7-2.2.9-c17, S7-2.2.9-c18, S7-2.2.9-c20, S7-2.2.9-c21, S7-2.2.9-c23, S7-2.2.9-c37, S7-2.14.2-c05]
      decisions: [DEC-0010]
      relies_on:
        - "working assumption: governance owner's answer of 2026-10-28, pending qualified accountant (Q-040 v2): decimal places come from each currency's configuration, not a fixed two."
      policy_points: [AP-3, AP-4]
      independence: "Independent of Q-029 and of every blocking question. Q-040's open part (whether places also govern stored amounts, rounding and tax) is answered for rounding and precision by S7-2.2.9-c06 itself; the upload template is excluded (EXC-15)."
    - id: CAP-08
      title: "Chart of accounts: accounts, groups and their attributes"
      includes:
        - "An entity's own chart. Account code numeric and fixed length ([6] digits by default, settable from four to ten at implementation), class from the first digit (1 assets, 2 liabilities, 3 equity, 4 income, 5 expense). No dimension and no entity or country is encoded in the code."
        - "Groups and sub-groups up to [4] levels; a group never accepts postings. A code issued is a code kept: no account is renumbered."
        - "Attributes: name, control-account flag, statement line and note reference, cash flow classification (for balance-sheet accounts), dimension rules, currency restriction, reconciliation requirement with frequency and owner (stored only; no reconciliation workflow), status (active, blocked, archived). An account with history is blocked, never deleted. The default tax code attribute is excluded (EXC-19)."
        - "Chart changes are effective-dated."
        - "Posting is refused to group and header accounts, blocked accounts, accounts whose dimension rules are not satisfied, and, at the Enforced level, control accounts by manual journal."
        - "Statement lines, notes and cash flow categories are entity data that Finance creates and maintains in the system, so that an account can carry its statement mapping before it is approved (S7-2.2.1-c47, S7-2.2.2-c44). Proposed: they are created and changed through the same maker-checker approval route as accounts (CAP-09); the owners confirm this route (AP-5). No statutory statement structure is delivered in INCR-001; the content is AP-5's."
        - "A name identical to another account's in the same group is refused (S7-2.2.2-c35)."
      clauses: [S7-2.2.2-c35, S7-2.2.1-c47, S7-2.2.1-c01, S7-2.2.1-c02, S7-2.2.1-c03, S7-2.2.1-c04, S7-2.2.1-c05, S7-2.2.1-c06, S7-2.2.1-c07, S7-2.2.1-c08, S7-2.2.1-c10, S7-2.2.1-c11, S7-2.2.1-c12, S7-2.2.1-c13, S7-2.2.1-c15, S7-2.2.1-c17, S7-2.2.1-c31, S7-2.2.1-c48, S7-2.2.1-c51, S7-2.2.1-c52, S7-2.2.2-c42, S7-2.2.2-c43, S7-2.2.2-c44, S7-2.2.2-c45, S7-2.2.2-c46, S7-2.2.2-c48, S7-2.2.2-c49, S7-2.2.2-c50, S7-2.2.2-c52, S7-2.2.4-c47]
      decisions: [DEC-0010]
      relies_on: []
      policy_points: [AP-5]
      independence: "Independent of Q-029. The attribute table's blanket block on control accounts (S7-2.2.1-c06) conflicts with the posting rule (c52): that is Q-032, handled under CAP-11 as a working assumption. The naming-standard part of c05 and c43 is removed (Q-014, EXC-09); the spare range is not provided (Q-041, EXC-07)."
    - id: CAP-09
      title: "Controlled creation, amendment and blocking of accounts"
      includes:
        - "S7-2.2.1-c44 says that once a chart is in use every addition, amendment, reclassification or blocking follows the request, duplicate check, review and approval process, with no second route. INCR-001 builds request, review and approval; the duplicate check is set aside (DEP-1). Maker-checker: created by one user, approved by a role the entity names. The account does not exist and cannot be posted to until approved. There is no second route: no account can be created from a transaction screen."
        - "The system proposes the code. A code keyed by a user is accepted only in the correct range, only by a permitted role and only if free. No two accounts in the entity share a code; the check runs when keyed, when submitted and at approval. A blocked, archived or deleted account keeps its code, and a code on a pending request is reserved. A refusal names the account that holds the code, its status, who created it and when, and has no override."
        - "The check reaches the entity only (an entity running its own chart)."
        - "An account becomes postable from an effective date. The account code never changes; name changes keep the previous version and reason. Class and group cannot change once transactions exist. Blocking an account with a balance is refused."
        - "The control flag and control type of an account with no transactions and no balance may be changed through this same approval (S7-2.2.1-c67). Changing them once transactions or a balance exist is held out (Q-034, EXC-10)."
        - "Every step is written to the audit log (this serves as the chart change record)."
      clauses: [S7-2.2.1-c44, S7-2.2.1-c67, S7-2.2.2-c01, S7-2.2.2-c02, S7-2.2.2-c04, S7-2.2.2-c05, S7-2.2.2-c06, S7-2.2.2-c07, S7-2.2.2-c08, S7-2.2.2-c09, S7-2.2.2-c10, S7-2.2.2-c11, S7-2.2.2-c14, S7-2.2.2-c15, S7-2.2.2-c17, S7-2.2.2-c20, S7-2.2.2-c42, S7-2.2.2-c50, S7-2.2.2-c52, S7-2.2.2-c54]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029. Q-043 (is approval ever optional) is not-blocking because V2.2 states the approval plainly and overrides SRC-008; a different answer is a change request. The duplicate check, ranked alternatives, bulk change and the reclassification tool leave (EXC-08); the naming standard leaves (Q-014, EXC-09); changing the control flag or type once transactions or a balance exist leaves (Q-034, EXC-10)."
    - id: CAP-10
      title: "Dimensions: definitions, values and per-account rules"
      includes:
        - "Dimensions carried at line level on every transaction: cost centre, profit centre, department, business unit, location, project, and entity-defined dimensions. Entity is not a dimension but a mandatory attribute of every transaction."
        - "Any dimension can be made mandatory, optional or blocked per account, and a posting that breaches the rule is refused with the dimension named."
        - "Dimension values can be added, blocked and renamed by the entity, restricted per entity, with history retaining the value in force. A dimension with history is blocked, never deleted."
        - "The 'Mandatory on' column of the dimension table is read as a default that the per-account rule overrides, and is applied as data. INCR-001 builds no hard-coded mandatory rule per dimension. This is a reading, not plain text: working assumption (WA-10), pending the qualified accountant; it is DEP-7. Q-044 covers the location rule only."
      clauses: [S7-2.2.3-c01, S7-2.2.3-c02, S7-2.2.3-c03, S7-2.2.3-c04, S7-2.2.3-c05, S7-2.2.3-c06, S7-2.2.3-c07, S7-2.2.3-c08, S7-2.2.3-c09, S7-2.2.3-c11, S7-2.2.3-c12, S7-2.2.3-c14, S7-2.2.3-c16, S7-2.14.2-c10, S7-2.2.11-c01]
      decisions: [DEC-0010]
      relies_on:
        - "labelled assumption of the requirements engineer, pending qualified accountant (WA-10): the dimension 'Mandatory on' column is a default that a per-account rule overrides."
      independence: "Independent of Q-029. Reports by dimension and default dimension values on customer, supplier and item masters leave (EXC-25). Dimension changes after posting leave (Q-007, EXC-11)."
    - id: CAP-11
      title: "Control accounts: flag, control types and enforcement levels as settings"
      includes:
        - "A control-account flag on the account and a control type from a fixed list: receivables, payables, inventory, payroll, fixed assets, tax and bank. The type is never free text."
        - "An enforcement level per entity and per control type, set by the administrator: Not applied (any account accepts a manual journal), Advisory (allowed with a reason chosen from a configurable list, listed on an exception report to a role the entity names, optionally also approved by a second person) or Enforced (a manual journal is refused, naming the owning sub-ledger)."
        - "Note: V2.2's own default for a single entity running the ledger alone is Not applied (S7-2.2.1-c58), not the Advisory of WA-03; the delivered defaults are not built (DEP-6)."
        - "Lowering a level from Enforced requires approval, a recorded reason and an effective date, and writes a record to the audit log. The reporting surface for management (S7-2.2.1-c64, the 2.15.8 panel) is excluded (EXC-18)."
        - "The exception list of every manual journal posted to a control account in the period, with user, reason, value and approver where one was required. Its review as part of period close is excluded with the close checklist (EXC-14)."
        - "No level is hard-coded. The delivered defaults by organisation type (S7-2.2.1-c58 to c61) are not built (D-6); the level for each control type is set explicitly when the entity is set up."
        - "In INCR-001 no sub-ledger exists, so no posting arrives from an owning sub-ledger. At Enforced every manual journal to a control account is refused."
      clauses: [S7-2.2.1-c06, S7-2.2.1-c52, S7-2.2.1-c53, S7-2.2.1-c54, S7-2.2.1-c55, S7-2.2.1-c56, S7-2.2.1-c57, S7-2.2.1-c62, S7-2.2.1-c64, S7-2.2.1-c66]
      decisions: [DEC-0010]
      relies_on:
        - "working assumption: governance owner's answer of 2026-10-28, pending product owner (Q-032 v3): the enforcement levels govern; the attribute table's blanket block (S7-2.2.1-c06) does not."
        - "working assumption: governance owner's answer of 2026-10-28, pending qualified accountant (Q-033 v2): the first entity's control types, bank included, start at Advisory. The scope builds the setting, not the value; the value is data entered at set-up."
      policy_points: [AP-1, AP-2]
      independence: "Independent of Q-029: the capability supplies the three behaviours and records them; it does not choose option A, B or C. Independent of Q-047 (no sub-ledger agreements exist). If the product owner answers Q-032 that the blanket block governs, the Not applied and Advisory behaviours leave by change request; this is stated, not hidden. Q-034 is blocking and removes the change-after-creation part (EXC-10)."
    - id: CAP-12
      title: "Journals: entry, approval, posting and correction"
      includes:
        - "Manual journals entered on screen. The adjustment type is held out pending Q-055 (EXC-28). Draft or pending entries are editable by the preparer and affect no balance. An entry rejected by an approver returns with a reason. An amendment by the preparer to a submitted entry returns it to the start of the approval chain."
        - "Fields, adopted from the rules of the upload template for screen entry (labelled assumption WA-09): entity the user may post to (S7-2.2.4-c37); journal date, whose period must be open (c38); journal type, from the configured list, which holds manual only (c39); optional reference (c40); journal description, mandatory, a blank or a repeated placeholder refused (c41); one currency for every line of a journal (c42); optional exchange rate, treated as an override when supplied (c43); per line an account that exists, is active and accepts postings (c47), a mandatory line description not defaulted from the header (c48), a debit or a credit but not both (c49, c50), and dimensions as the account's rule requires (c51 to c56). The number of decimal places comes from the currency (Q-040 working assumption), not the template's [2]. Tax, partner entity, document reference, due date, analysis reference and attachment columns are excluded."
        - "A manual journal must balance by entity and by currency and is approved by a second user, always. A foreign-currency journal is converted at the rate in force with the rate and its source retained (CAP-07)."
        - "Validation runs before posting and reports an unbalanced entry, a missing mandatory dimension, a blocked or group account, a closed period and a breach of the segregation matrix. A transaction cannot be partly posted, and a dropped connection must not create a partial or duplicate transaction."
        - "Approval is the boundary. An approved and posted entry is locked: no screen, import, API call or administrator action can change its value, account, date, dimensions or party, and none can delete it."
        - "A correction in INCR-001 is a reversal of a posted journal in an open period. A reversal here is a one-off, system-generated entry, created on request by a permitted user from the original, with the same entity, currency, accounts and dimensions and debit and credit swapped (a mechanical inverse); it references the original, carries its own reason, is dated in the current open period, is approved by someone other than the person raising it, and is linked to the original both ways. It is not the reversing journal type, which reverses on a schedule (EXC-15). The series it draws from is open (AP-10). Correction by an adjustment journal, and correction of an entry in a closed period, wait for Q-055 (EXC-28)."
        - "Each entry carries its history: edits before approval, submission and approval, corrections after approval. History cannot be edited or deleted by any user including an administrator."
      clauses: [S7-2.2.4-c01, S7-2.2.4-c16, S7-2.2.4-c37, S7-2.2.4-c38, S7-2.2.4-c39, S7-2.2.4-c40, S7-2.2.4-c41, S7-2.2.4-c42, S7-2.2.4-c43, S7-2.2.4-c49, S7-2.2.4-c50, S7-2.2.4-c51, S7-2.2.4-c52, S7-2.2.4-c53, S7-2.2.4-c54, S7-2.2.4-c55, S7-2.2.4-c56, S7-2.2.5-c01, S7-2.2.5-c08, S7-2.2.6-c01, S7-2.2.6-c03, S7-2.2.6-c04, S7-2.2.6-c05, S7-2.2.6-c06, S7-2.2.6-c09, S7-2.2.6-c10, S7-2.2.6-c11, S7-2.2.6-c12, S7-2.2.6-c13, S7-2.2.6-c15, S7-2.2.6-c22, S7-2.2.6-c23, S7-2.2.6-c24, S7-2.2.6-c25, S7-2.2.6-c26, S7-2.1.1-c04, S7-2.2.11-c01, S7-2.2.11-c02]
      decisions: [DEC-0010]
      relies_on:
        - "labelled assumption of the requirements engineer, pending qualified accountant (WA-09): the upload template's header and line rules apply to screen entry, including one currency per journal."
        - "labelled assumption of the requirements engineer, pending qualified accountant (WA-08): a journal is issued when approved and posted."
      policy_points: [AP-3, AP-4, AP-6, AP-7, AP-10]
      independence: "Independent of Q-029: only users post in INCR-001; no sub-ledger posts, so the interim-posting question does not arise. Two internal SRC-007 conflicts are removed: S7-2.2.6-c14 against c10 (Q-007, EXC-11), and the two meanings of 'adjustment journal' in S7-2.2.5-c05 and S7-2.2.6-c11 and c16 (Q-055, EXC-28). INCR-001 implements c10 without exception and holds the adjustment type out."
    - id: CAP-13
      title: "Gapless numbering series held as configuration"
      includes:
        - "Every journal carries a number the system generates. No user types, chooses, edits or re-uses a number."
        - "A series is built on a configuration screen from prefix and suffix, entity and country code taken from the entity record, location code, financial year and period, sequence (length, start, increment, padding), separators and custom elements, with a reset rule of never, annually at the financial year end, or at each period. The format is previewed before it is saved."
        - "A separate sequence per entity, per country, per location, per module and document type, and per further attribute where required. The combination of entity, series and number is unique across the system."
        - "The number is generated when the document is issued, never reserved, never on save of a draft. Two users issuing in the same series at the same moment receive consecutive numbers with no gap, duplicate or failure. A number is never reused, renumbered or reassigned."
        - "A series can be marked statutory: gapless by enforcement, with a document issued against it never deletable, and a gap-detection report that must return nil. A statutory series cannot be changed, reset, re-pointed or closed without approval and a recorded reason. The report of a non-nil result to management on the 2.15.8 panel is excluded (EXC-18)."
        - "The location element of a journal number: a journal's lines may carry different locations, so a journal has no single location of its own. Proposed: the location element is not used in journal series in INCR-001 until the owner decides where it comes from (AP-11)."
        - "Creating or amending a series is a separate administrator permission not held by default. Every change records user, time, before and after, reason, approval reference and effective date and cannot be edited or deleted. A format change applies only to documents issued after its effective date. Setting a sequence backwards is refused for every role. One screen lists every series with format, next number, last number, last issue date and whether it is statutory."
      clauses: [S7-2.1.10-c01, S7-2.1.10-c04, S7-2.1.10-c11, S7-2.1.10-c12, S7-2.1.10-c13, S7-2.1.10-c14, S7-2.1.10-c15, S7-2.1.10-c16, S7-2.1.10-c17, S7-2.1.10-c18, S7-2.1.10-c19, S7-2.1.10-c20, S7-2.1.10-c21, S7-2.1.10-c22, S7-2.1.10-c23, S7-2.1.10-c24, S7-2.1.10-c25, S7-2.1.10-c26, S7-2.1.10-c27, S7-2.1.10-c28, S7-2.1.10-c29, S7-2.1.10-c31, S7-2.1.10-c38, S7-2.1.10-c39, S7-2.1.10-c40, S7-2.1.10-c42, S7-2.1.10-c43]
      decisions: [DEC-0010]
      relies_on: []
      policy_points: [AP-6, AP-10, AP-11]
      independence: "Independent of Q-029. Series prescribed by a tax authority, loaded authority ranges and the calendar-year reset (Q-035, Q-046, Q-015) leave with tax documents (EXC-19). Concurrency-safe issue depends on the stack (stack_dependencies)."
    - id: CAP-14
      title: "Financial years and period control"
      includes:
        - "A financial year per entity with its own start and end dates; a short or long first year; entities in one tenant may have different year ends. Fiscal periods generated for the year (monthly, quarterly, half-yearly, annual, or a 4-4-5 calendar), and future periods created in advance but not open. The adjustment period and the special audit adjustment period (S7-2.2.8-c04, c05) are not created in INCR-001: their use is Q-055 (EXC-28)."
        - "Proposed limit, for the product owner with the qualified accountant (D-3): INCR-001 opens one financial year per entity, so no posting crosses a year end and no income and expense roll-up is needed. A second year, and the carry-forward of balances, arrive with year-end close (EXC-13)."
        - "Close with pending journals: approving a journal is a posting, so approval into a closed period is refused under S7-2.2.8-c13. Whether a period may be soft-closed or hard-closed while journals dated in it are still pending is open (AP-12); the period-end checklist that would settle it is excluded (EXC-14)."
        - "Period states open, soft closed (optional, off per entity), hard closed and audit locked. Posting is blocked into a closed period, a future period not yet opened and an audit-locked period, with a message naming the period and its state, from the screen and from every other route. Audit locked is permanent: no reopening by any role. Reopening from soft or hard closed needs management approval, a mandatory reason, an entry on a standing reopened-periods list, and every posting made while reopened is listed separately."
        - "Period state is held per entity for the general ledger. One entity can be closed for a period while another stays open."
        - "Opening, closing, reopening and audit-locking are restricted to named roles assigned per entity. The user who closes a period cannot approve its reopening, unless released as a documented exception under CAP-04."
        - "Every change of state, soft-close posting and blocked attempt is recorded with user, time, state before and after, reason and approval reference, and cannot be edited or deleted."
      clauses: [S7-2.2.8-c01, S7-2.2.8-c02, S7-2.2.8-c03, S7-2.2.8-c06, S7-2.2.8-c07, S7-2.2.8-c08, S7-2.2.8-c09, S7-2.2.8-c10, S7-2.2.8-c11, S7-2.2.8-c12, S7-2.2.8-c13, S7-2.2.8-c14, S7-2.2.8-c15, S7-2.2.8-c17, S7-2.2.8-c25, S7-2.2.8-c26, S7-2.2.8-c27, S7-2.2.8-c28, S7-2.2.8-c44, S7-2.2.8-c45, S7-2.2.8-c47, S7-2.2.8-c48, S7-2.14.2-c04, S7-2.14.2-c19, S7-2.2.11-c02]
      decisions: [DEC-0010]
      relies_on: []
      policy_points: [AP-8, AP-9, AP-12]
      independence: "Independent of Q-029. The adjustment periods leave with Q-055 (EXC-28), consistent with CAP-12. The override route into a hard-closed period leaves (Q-013, EXC-12); the row of S7-2.2.8-c11 that mentions the override is read without it. Year-end close, close checklist, dashboard and module period states leave (EXC-13, EXC-14). Q-008, Q-009 and Q-012 concern reconciliations, which are excluded."
    - id: CAP-15
      title: "Ledger enquiry"
      includes:
        - "The general ledger is the single repository; no module keeps a second set of balances."
        - "From an account balance, for any period or date range within the one financial year INCR-001 opens (CAP-14), a user permitted to see the entity reaches the journals that make it up, and from a journal its approval trail and correction history. No balance is shown across a year end."
        - "No statement, report pack or dashboard is part of INCR-001."
      clauses: [S7-2.2.4-c01, S7-2.2.4-c77]
      decisions: [DEC-0010]
      relies_on: []
      independence: "Independent of Q-029 and of every blocking question. Sub-ledger document links of S7-2.2.4-c78 and c79 wait for their modules."

  stack_dependencies:
    - "Tenant isolation mechanism (CAP-01): the scope states the boundary, not the mechanism."
    - "Concurrency-safe gapless numbering (CAP-13) and atomic posting (CAP-12)."
    - "Tamper resistance of the audit log and of posted entries (CAP-05, CAP-12)."
    - "Money and rounding storage (CAP-07)."
    - "Capacity proof (CAP-06) and what 'built against' means for load tests."
    - "Authentication and encryption (CAP-02), a security-owner decision at Gate B."
    - "Gate B design input for the tech lead (review finding on CAP-07): posted lines must later accept a reporting-currency amount (S7-2.2.9-c22, c23) and a tax code (S7-2.2.4-c57) without rewriting posted entries, which INCR-001 locks without exception. The scope does not say how."
    - "The stack ADR is the tech lead's decision. The scope neither chooses nor assumes a stack; Q-054's working answer is recorded as a working assumption only."

  exclusions:
    - {id: EXC-01, what: "A firm's access to client tenants; vendor or operator support access", reason: "Q-031 v3 leaves open who owns a client's data, who grants and withdraws a firm's access, how it is logged, under which roles a firm's staff act, whether a firm may keep the books of a client it audits (a professional and regulatory question), and how subscriptions apply. Security owner and product owner; the audit-firm question is for the qualified accountant. Returns when Q-031 is answered, as an addition to INCR-001 or in a later increment.", clauses: [S7-2.16.5-c01]}
    - {id: EXC-02, what: "Single sign-on provider, multi-factor authentication, password policy and lockout, encryption standard", reason: "S7-2.1.3-c01 leaves the identity provider as a bracket; c02 and c03 are open security settings. These are security decisions (security owner), taken in the Gate B design. Not decided here (SEC-1).", clauses: [S7-2.1.3-c01, S7-2.1.3-c02, S7-2.1.3-c03]}
    - {id: EXC-03, what: "Data residency and the hosting regions per country", reason: "Depends on the owner of residency rules (Q-028), the countries (Q-003) and the stack decision (Q-054). No production tenant data in a jurisdiction that requires residency may be held before it is decided.", clauses: [S7-2.1.3-c04]}
    - {id: EXC-04, what: "Environments, mobile access, offline behaviour beyond fail-safe posting, session timeout", reason: "Operational and architecture matters for Gate B; the session timeout is a bracketed security value.", clauses: [S7-2.1.1-c02, S7-2.1.1-c03, S7-2.1.1-c05]}
    - {id: EXC-05, what: "Search, integration and API, modular architecture and activation, localisation, assistants", reason: "They sit on modules that INCR-001 does not contain. Languages beyond the default are a product-owner confirmation for release 1.", clauses: [S7-2.1.5-c01, S7-2.1.6-c01, S7-2.1.7-c01, S7-2.1.8-c01, S7-2.1.9-c01]}
    - {id: EXC-06, what: "Delivered standard chart, industry variants, upload and export of a chart, copy of another entity's chart, chart versioning", reason: "The delivered chart is Finance's data (Q-005) and is not confirmed. The upload route needs the mapping engine (EXC-15). Accounts are created one request at a time (D-5).", clauses: [S7-2.2.1-c33, S7-2.2.1-c34, S7-2.2.1-c35, S7-2.2.1-c36, S7-2.2.1-c46]}
    - {id: EXC-07, what: "Group chart, extension accounts, entity and country segments, group-wide code check, choice of which chart an entity runs on at set-up (S7-2.2.2-c21; INCR-001 offers the entity's own chart only), spare range, allocation in steps and chart widening", reason: "INCR-001 gives each entity its own chart. Q-052 (group or own chart), Q-049 (entity inside the code), Q-053 (renumbering on a clash) and Q-041 (spare range) are open and concern groups, which wait for release 3.", clauses: [S7-2.2.1-c16, S7-2.2.1-c18, S7-2.2.1-c50, S7-2.2.2-c13, S7-2.2.2-c21]}
    - {id: EXC-08, what: "Duplicate check (DEP-1), near-duplicate warnings, ranked alternatives (DEP-2), reserved codes and ranges held back by a role, bulk change, reclassification tool, hygiene reports", reason: "They improve chart quality but do not protect the ledger. Keeping the first increment's Tier-1 surface small. A product-owner choice, shown one by one in departures_from_plain_text.", clauses: [S7-2.2.2-c03, S7-2.2.2-c12, S7-2.2.2-c25, S7-2.2.2-c53, S7-2.2.2-c55]}
    - {id: EXC-09, what: "Validation of account names against the naming standard", reason: "Q-014 (blocking): 2.2.2 has no naming standard. Uniqueness of a name inside its group stays in CAP-08. Leaves unless the qualified accountant answers Q-014.", clauses: [S7-2.2.1-c05, S7-2.2.2-c43]}
    - {id: EXC-10, what: "Changing the control flag or the control type on an account that has transactions or a balance", reason: "Q-034 (blocking): S7-2.2.1-c67 allows it by approval; S7-2.2.2-c47 and c51 forbid it once transactions or a balance exist. The three agree for an account with neither, and that case stays in CAP-09. Leaves unless the product owner answers Q-034.", clauses: [S7-2.2.1-c67, S7-2.2.2-c47, S7-2.2.2-c51]}
    - {id: EXC-11, what: "Narrative, internal reference or dimension changes to a posted entry", reason: "Q-007 (blocking): S7-2.2.6-c14 permits them under approval where the entity chooses; c10 allows no change to dimensions. INCR-001 locks posted entries without exception. Leaves unless the qualified accountant answers Q-007.", clauses: [S7-2.2.6-c14, S7-2.2.6-c10]}
    - {id: EXC-12, what: "Override posting into a hard-closed period", reason: "Q-013 (blocking): what the override may be used for is an accounting-policy question. Hard close refuses every posting in INCR-001. Leaves unless the qualified accountant answers Q-013.", clauses: [S7-2.2.8-c30, S7-2.2.8-c31, S7-2.2.8-c32, S7-2.2.8-c33, S7-2.2.8-c46]}
    - {id: EXC-13, what: "Year-end close, retained-earnings roll-up, opening-balance carry-forward, year-end journal type", reason: "Needs a retained-earnings policy and the year ends (Q-003), both for the qualified accountant and product owner. INCR-001 opens one financial year per entity (CAP-14), so no second year and no carry-forward exist; the first year-end falls to a later increment (D-3, DEP-5).", clauses: [S7-2.2.8-c34, S7-2.2.8-c37, S7-2.2.5-c09]}
    - {id: EXC-14, what: "Close dashboard, period-end checklist, close notifications, module period states", reason: "They depend on reconciliations and modules that INCR-001 does not contain (Q-008, Q-009, Q-012). The data model for period state keeps the entity and period as keys so a module state can be added.", clauses: [S7-2.2.8-c16, S7-2.2.8-c39]}
    - {id: EXC-15, what: "Journal routes other than manual: template, recurring, reversing on a schedule, accrual and prepayment, intercompany, year-end, bulk upload and API import; schedules (2.2.7); approver amendment of a pending entry (DEP-4)", reason: "Upload needs the mapping engine; schedules and accruals need accounting policy; intercompany needs groups. Approver amendment is held back by a product-owner choice (DEP-4), not for want of a threshold: V2.2 makes the threshold configurable.", clauses: [S7-2.2.4-c19, S7-2.2.5-c02, S7-2.2.5-c03, S7-2.2.5-c04, S7-2.2.5-c06, S7-2.2.5-c07, S7-2.2.5-c10, S7-2.2.6-c07, S7-2.2.6-c08, S7-2.2.7-c01]}
    - {id: EXC-16, what: "Every module that depends on Q-029 or on sub-ledgers: receivables, invoicing, payables, bank and cash, tax, fixed assets, inventory, payroll, reconciliation, financial statements, consolidation; posting rules engine; sub-ledger postings into control accounts; raising a control level on module activation; the reconciliation schedule", reason: "DEC-0010 admits only capabilities that do not depend on the release-1 scope decision (Q-029). Every one of these needs it or a blocking question.", clauses: [S7-2.3-c01, S7-2.4-c01, S7-2.5-c01, S7-2.6-c01, S7-2.7-c01, S7-2.8-c01, S7-2.9-c01, S7-2.10-c01, S7-2.12-c01, S7-2.13-c01, S7-2.2.1-c63, S7-2.2.1-c65]}
    - {id: EXC-17, what: "Preferred rate source, automatic daily rate synchronisation, the rate-table lock and its unlock by approval (the first sentence of S7-2.2.9-c18 stays in CAP-07), rate enquiry, reporting currency, realised and unrealised exchange differences, revaluation, translation", reason: "A source and its provider are the entity's choice and an integration; exchange differences and revaluation are accounting policy (treatment to profit or loss or to other comprehensive income) needing sub-ledgers and the qualified accountant. The group reporting currency is Q-003.", clauses: [S7-2.2.9-c07, S7-2.2.9-c10, S7-2.2.9-c16, S7-2.2.9-c18, S7-2.2.9-c24]}
    - {id: EXC-18, what: "The governance panel (2.15.8) as a reporting surface", reason: "Phasing decision D-2.15.8 is open. INCR-001 writes the events the panel would report (numbering changes, a statutory gap result, a lowered control level) to the audit log, so none is lost.", clauses: [S7-2.15.8-c01, S7-2.1.10-c41]}
    - {id: EXC-19, what: "Tax: tax register, tax codes on accounts and journal lines, entity tax registrations, default tax code attribute, authority-prescribed number formats and ranges, annual or calendar-year reset, tax documents", reason: "Tax and statutory rules are the tax specialist's. Q-015, Q-016, Q-017, Q-018, Q-019, Q-021, Q-035, Q-042, Q-046, Q-051 are open and each concerns tax documents or levies that INCR-001 does not contain.", clauses: [S7-2.2.1-c09, S7-2.2.4-c57, S7-2.1.10-c30, S7-2.1.10-c32]}
    - {id: EXC-20, what: "Opening balances and data migration", reason: "Q-006 (is data migrated) and Q-045 (opening bank balances where bank is Enforced) are open. Opening balances load through a route that does not exist in INCR-001.", clauses: [S7-2.16.2-c01]}
    - {id: EXC-21, what: "Subscription, user licensing and entitlement", reason: "Q-039 (licensing for Tiqri's own product) and Q-031 (who subscribes for a client tenant) are open. INCR-001 builds no entitlement and counts no user or entity against a licence. The 2.16.1 figures are technical capacity, not commercial entitlement (S7-2.16.5-c23), and are handled only as settings with a warning in CAP-06.", clauses: [S7-2.16.5-c01, S7-2.16.5-c23]}
    - {id: EXC-22, what: "Availability, backup, recovery, support response, performance targets and load proof against the tested ceiling", reason: "Q-024 (service levels) is open and Q-038 leaves open whether the ceiling applies. These are operational targets for Gate B and release readiness. Capacity figures remain configurable (CAP-06).", clauses: [S7-2.16.1-c07]}
    - {id: EXC-23, what: "Supporting documents and attachments on journals, the audit pack", reason: "The supporting-document module (2.11) is not in INCR-001, and file storage is an architecture decision.", clauses: [S7-2.11-c01, S7-2.2.6-c27]}
    - {id: EXC-24, what: "Role features tied to later modules: value limits, scopes to bank accounts and document types, bulk assignment by position, starting roles for sales, purchases, stores and payroll", reason: "The bands are defined with procurement (2.5.5) and the other scopes and roles belong to modules that do not exist yet.", clauses: [S7-2.1.2-c04, S7-2.1.2-c11, S7-2.1.2-c20, S7-2.1.2-c21, S7-2.1.2-c22, S7-2.1.2-c23]}
    - {id: EXC-25, what: "Reporting by dimension and default dimension values on master records", reason: "Reports and masters are not in INCR-001.", clauses: [S7-2.2.3-c10, S7-2.2.3-c13]}
    - {id: EXC-26, what: "Group structure, ownership and control, consolidation, intercompany, group chart mapping, cross-entity reporting and the current-entity switch", reason: "One entity per tenant in release 1 (working assumption, Q-038). Groups wait for release 3.", clauses: [S7-2.14.1-c01, S7-2.14.3-c01, S7-2.2.10-c01]}
    - id: EXC-27
      what: "The production route that creates a tenant, its first entity and its first administrator, and what the creator can reach in the tenant afterwards"
      reason: "Q-056 (blocking, owner security owner with product owner): no clause of V2.2 describes it, and whoever creates a tenant can reach into it (SEC-2, Q-031 reading (c)). Leaves unless Q-056 is answered."
      clauses: [S7-2.1.2-c01]
      test_route_proposal: "PROPOSAL for the security owner, not a decision, and not a production route. INCR-001 test tenants could be created only in a non-production test environment, by a scripted data load run by the tech lead's team, which creates the tenant, one entity and one test administrator account with fixed test credentials, and writes each of these to the audit log. The load would be refused in any production environment. Whether this is acceptable, and how any later production route differs, is for the security owner (Q-056, SEC-2)."
    - id: EXC-28
      what: "The Adjustment journal type; correction by an adjustment journal; correction of an entry in a closed period; the adjustment period and the special audit adjustment period"
      reason: "Q-055 (blocking, owner qualified accountant with product owner): S7-2.2.5-c05 puts the Adjustment type in the year-end adjustment period, approved by the Finance manager; S7-2.2.6-c11, c12 and c16 make an 'adjustment journal' a correction in the current open period, approved by a second user. Leaves unless Q-055 is answered; the two periods go with it because their only use is that type and year-end close (EXC-13)."
      clauses: [S7-2.2.5-c05, S7-2.2.6-c16, S7-2.2.8-c04, S7-2.2.8-c05, S7-2.2.8-c35]
    - id: EXC-29
      what: "What the system does when a tenant reaches 100% of a capacity figure (warn only, or refuse), and which role may change a tenant's figure (the tenant's administrator or the operator)"
      reason: "Q-057 (blocking, owner product owner with tech lead and security owner): S7-2.16.1-c33 and c34 read as a warning and self-service; S7-2.16.5-c23 says capacity is not entitlement; V2.2 does not say who raises a figure on a shared platform. Leaves unless Q-057 is answered. CAP-06 builds the setting, the audit record and the warning only."
      clauses: [S7-2.16.1-c33, S7-2.16.1-c34]

  question_classification:
    summary: "57 questions, all open. Blocking for INCR-001: 8 (Q-007, Q-013, Q-014, Q-031, Q-034, Q-055, Q-056, Q-057). Not-blocking: 49. None is closed or superseded in the records; Q-004's baseline part is settled by DEC-0008 and noted there. A blocking question names the capability that leaves unless its owner answers; eight exclusions (EXC-01, EXC-09 to EXC-12, EXC-27 to EXC-29) already hold those capabilities out."
    entries:
      - {q: Q-001, owner: product-owner, class: not-blocking, reason: "Product intent; the multi-tenant reading is a working assumption (governance owner's answer of 2026-10-20, pending product owner) and fixes nothing beyond CAP-01."}
      - {q: Q-002, owner: product-owner, class: not-blocking, reason: "Release order; DEC-0010 bounds INCR-001 apart from it."}
      - {q: Q-003, owner: qualified-accountant, class: not-blocking, reason: "INCR-001 needs only ISO 4217 currencies, a functional currency, a jurisdiction and a year end per entity, all configuration; the rest waits (see countries_currencies_tax)."}
      - {q: Q-004, owner: product-owner, class: not-blocking, reason: "Baseline part settled by DEC-0008; the bracketed values the foundation relies on are confirmed through the V2.2 workbook before Gate A (bracketed_values_relied_on)."}
      - {q: Q-005, owner: product-owner, class: not-blocking, reason: "Annexure B inputs: the delivered chart and invoice formats are excluded (EXC-06, EXC-19)."}
      - {q: Q-006, owner: product-owner, class: not-blocking, reason: "Data migration is excluded (EXC-20)."}
      - {q: Q-007, owner: qualified-accountant, class: blocking, reason: "S7-2.2.6-c14 conflicts with c10 on post-approval dimension and narrative changes.", leaves_unless_answered: "Post-approval narrative, reference or dimension change (EXC-11); INCR-001 locks posted entries without exception."}
      - {q: Q-008, owner: qualified-accountant, class: not-blocking, reason: "Suspense balance at hard close; no suspense and no close checklist in INCR-001 (EXC-14)."}
      - {q: Q-009, owner: qualified-accountant, class: not-blocking, reason: "Reconciliation separation of duties; no reconciliation in INCR-001. The general released-separation mechanism (S7-2.1.2-c17) is in CAP-04."}
      - {q: Q-010, owner: qualified-accountant, class: not-blocking, reason: "Depreciation day count; fixed assets excluded (EXC-16)."}
      - {q: Q-011, owner: qualified-accountant, class: not-blocking, reason: "Correcting a depreciation run; fixed assets excluded (EXC-16)."}
      - {q: Q-012, owner: qualified-accountant, class: not-blocking, reason: "Hard close with an unapproved bank reconciliation; bank and reconciliation excluded (EXC-14, EXC-16)."}
      - {q: Q-013, owner: qualified-accountant, class: blocking, reason: "What the override into a hard-closed period may be used for is accounting policy.", leaves_unless_answered: "Override posting into a hard-closed period (EXC-12)."}
      - {q: Q-014, owner: qualified-accountant, class: blocking, reason: "2.2.2 contains no naming standard to validate against.", leaves_unless_answered: "Naming-standard validation of account names (EXC-09); name uniqueness stays."}
      - {q: Q-015, owner: tax-specialist, class: not-blocking, reason: "Annual restart of the sales tax invoice series; tax documents excluded (EXC-19)."}
      - {q: Q-016, owner: tax-specialist, class: not-blocking, reason: "Standalone credit and debit notes; invoicing excluded (EXC-16)."}
      - {q: Q-017, owner: tax-specialist, class: not-blocking, reason: "Cancelling an issued invoice; invoicing excluded (EXC-16)."}
      - {q: Q-018, owner: tax-specialist, class: not-blocking, reason: "Tax references for unregistered customers; customers and invoicing excluded (EXC-16, EXC-19)."}
      - {q: Q-019, owner: tax-specialist, class: not-blocking, reason: "Customer registration status; customer master excluded (EXC-16)."}
      - {q: Q-020, owner: tax-specialist, class: not-blocking, reason: "Statutory retention periods; INCR-001 builds no deletion (CAP-05), so no period is applied."}
      - {q: Q-021, owner: tax-specialist, class: not-blocking, reason: "Return forms, e-filing formats and prescribed invoice wording; tax excluded (EXC-19)."}
      - {q: Q-022, owner: product-owner, class: not-blocking, reason: "External payroll by file; payroll excluded (EXC-16)."}
      - {q: Q-023, owner: product-owner, class: not-blocking, reason: "Vendor-addressed clauses; the encryption standard of S7-2.1.3-c03 is a security-owner decision at Gate B (EXC-02), not a scope input."}
      - {q: Q-024, owner: product-owner, class: not-blocking, reason: "Service levels; operational targets excluded (EXC-22)."}
      - {q: Q-025, owner: product-owner, class: not-blocking, reason: "Retention model; INCR-001 has no purge, so it applies no retention period."}
      - {q: Q-026, owner: product-owner, class: not-blocking, reason: "Auditor access to individual pay; payroll excluded (EXC-16)."}
      - {q: Q-027, owner: product-owner, class: not-blocking, reason: "Editorial cross-reference errors; no foundation clause is cited through a wrong reference except S7-2.2.2-c48's 'under 2.10', read as the reconciliation owner, stored only."}
      - {q: Q-028, owner: governance-owner, class: not-blocking, reason: "Owner of residency rules; residency is excluded (EXC-03) but must be settled before any production tenant in a jurisdiction that requires it."}
      - {q: Q-029, owner: product-owner, class: not-blocking, reason: "Release-1 scope decision; DEC-0010 admits only capabilities independent of it. No INCR-001 capability posts from a sub-ledger (EXC-16)."}
      - {q: Q-030, owner: qualified-accountant, class: not-blocking, reason: "Expected credit loss; receivables excluded (EXC-16)."}
      - {q: Q-031, owner: product-owner, class: blocking, reason: "Who owns a client's tenant and data, who grants, withdraws and logs a firm's access, and under which roles, are open; they are security and product decisions.", leaves_unless_answered: "A firm's access to client tenants (EXC-01). The tenant as the organisation boundary stays on the working assumption."}
      - {q: Q-032, owner: product-owner, class: not-blocking, reason: "Working assumption: the levels govern. CAP-11 builds the three behaviours as settings; if the blanket block governs, Not applied and Advisory leave by change request."}
      - {q: Q-033, owner: qualified-accountant, class: not-blocking, reason: "Working assumption: Advisory for every control type, bank included. INCR-001 builds the setting and no default; whether a set-up level is a 'lowering' changes only who approves and what is recorded, by change request."}
      - {q: Q-034, owner: product-owner, class: blocking, reason: "S7-2.2.1-c67 allows a flag change by approval; S7-2.2.2-c47 and c51 forbid it once transactions or a balance exist.", leaves_unless_answered: "Changing the control flag or type on an account that has transactions or a balance (EXC-10); a change on an account with neither stays through the approval route (CAP-09)."}
      - {q: Q-035, owner: tax-specialist, class: not-blocking, reason: "Sales document series restart; authority-prescribed series excluded (EXC-19)."}
      - {q: Q-036, owner: product-owner, class: not-blocking, reason: "Two corrupted rows (p.19 and p.130); neither is a clause INCR-001 cites. The capacity table rows it relies on (p.133) are intact."}
      - {q: Q-037, owner: product-owner, class: not-blocking, reason: "Which sections the 2.2.2 acceptance statement tests; needed when acceptance tests are derived at L4, not to set scope."}
      - {q: Q-038, owner: product-owner, class: not-blocking, reason: "Working assumption for the named rows; every limit is a setting (CAP-06). The platform total of tenants is an input to Gate B sizing (tech lead)."}
      - {q: Q-039, owner: product-owner, class: not-blocking, reason: "Licensing; excluded (EXC-21)."}
      - {q: Q-040, owner: qualified-accountant, class: not-blocking, reason: "Working assumption: places from the currency's configuration. S7-2.2.9-c06 states this for precision and rounding; the upload template is excluded (EXC-15)."}
      - {q: Q-041, owner: qualified-accountant, class: not-blocking, reason: "Accounts in the spare range; the spare range is not provided (EXC-07), so codes outside classes 1 to 5 are not created."}
      - {q: Q-042, owner: tax-specialist, class: not-blocking, reason: "The first entity's industry tax set; tax excluded (EXC-19)."}
      - {q: Q-043, owner: product-owner, class: not-blocking, reason: "V2.2 states the approval plainly and overrides SRC-008; optional approval, if decided, is a change request."}
      - {q: Q-044, owner: qualified-accountant, class: not-blocking, reason: "Location on balance-sheet accounts; INCR-001 ships no chart and builds no hard-coded mandatory rule, so the rule is account data."}
      - {q: Q-045, owner: qualified-accountant, class: not-blocking, reason: "Opening bank balances; opening balances excluded (EXC-20)."}
      - {q: Q-046, owner: tax-specialist, class: not-blocking, reason: "Calendar-year reset; INCR-001 offers the three V2.2 reset rules and prescribed formats are excluded (EXC-19)."}
      - {q: Q-047, owner: product-owner, class: not-blocking, reason: "Manual journals below Enforced against the nil sub-ledger agreement; no sub-ledger agreement exists in INCR-001 (EXC-16)."}
      - {q: Q-048, owner: product-owner, class: not-blocking, reason: "Which specification version SRC-008 was prepared against; SRC-008 supplies no value to INCR-001."}
      - {q: Q-049, owner: product-owner, class: not-blocking, reason: "Entity inside the account code; INCR-001 follows V2.2, which keeps the entity outside the code (EXC-07)."}
      - {q: Q-050, owner: qualified-accountant, class: not-blocking, reason: "Inconsistent SRC-008 specimens; none is used as foundation data."}
      - {q: Q-051, owner: tax-specialist, class: not-blocking, reason: "Who the Sri Lanka non-tax invoice is for; invoicing excluded (EXC-16, EXC-19)."}
      - {q: Q-052, owner: product-owner, class: not-blocking, reason: "Group or own chart; INCR-001 builds the entity's own chart only (EXC-07)."}
      - {q: Q-053, owner: qualified-accountant, class: not-blocking, reason: "Renumbering on a code clash when joining a group chart; group chart excluded (EXC-07)."}
      - {q: Q-054, owner: tech-lead, class: not-blocking, reason: "Working assumption pending the stack decision record at Gate B; the scope states no stack and lists where it depends on one (stack_dependencies)."}
      - {q: Q-055, owner: qualified-accountant, class: blocking, reason: "S7-2.2.5-c05 and S7-2.2.6-c11, c12, c16 give 'adjustment journal' two meanings with different period, approver, series and reporting.", leaves_unless_answered: "The Adjustment journal type, correction by adjustment journal, correction of a closed-period entry, and the adjustment and special audit adjustment periods (EXC-28). INCR-001 journals are manual, corrected by reversal."}
      - {q: Q-056, owner: security-owner, class: blocking, reason: "No clause says who creates a tenant, its first entity and its first administrator, or what the creator can reach afterwards.", leaves_unless_answered: "The production route that creates a tenant, its first entity and first administrator (EXC-27). Test tenants come from the proposal in EXC-27, which is not a production route."}
      - {q: Q-057, owner: product-owner, class: blocking, reason: "V2.2 does not say what happens at a capacity limit or who may raise a tenant's figure; capacity is not a licence cap (S7-2.16.1-c33, S7-2.16.5-c23).", leaves_unless_answered: "Behaviour at 100% of a capacity figure and who may change a tenant's figure (EXC-29). CAP-06 builds the setting, the audit record and the warning."}

  working_assumptions:
    - {id: WA-01, source: "Q-031 v3", text: "A tenant is an organisation; a firm (Tiqri, an audit firm or a client) keeps the books of client organisations, each its own tenant.", label: "working assumption: governance owner's answer of 2026-10-28, pending product owner (with security owner and qualified accountant for the open points)", used_by: [CAP-01]}
    - {id: WA-02, source: "Q-032 v3", text: "The enforcement levels govern manual journals to control accounts, not the attribute table's blanket block.", label: "working assumption: governance owner's answer of 2026-10-28, pending product owner (with qualified accountant)", used_by: [CAP-11]}
    - {id: WA-03, source: "Q-033 v2", text: "Every control type, bank included, starts at Advisory for the first entity.", label: "working assumption: governance owner's answer of 2026-10-28, pending qualified accountant (with product owner)", used_by: [CAP-11]}
    - {id: WA-04, source: "Q-038 v3", text: "Release 1 is one entity, 125 named users, 50 at peak and 200,000 journal lines a month, per tenant.", label: "working assumption: governance owner's answer of 2026-10-28, pending product owner (with tech lead)", used_by: [CAP-01, CAP-06]}
    - {id: WA-05, source: "Q-040 v2", text: "Decimal places come from each currency's configuration.", label: "working assumption: governance owner's answer of 2026-10-28, pending qualified accountant (with tech lead)", used_by: [CAP-07]}
    - {id: WA-06, source: "Q-054", text: "Hosting on Azure with Azure SQL Database.", label: "working assumption: governance owner's answer of 2026-10-28, pending tech lead's stack decision record at Gate B", used_by: [CAP-01]}
    - {id: WA-07, source: "Q-001", text: "TIQACC is Tiqri's own multi-tenant SaaS product.", label: "working assumption: governance owner's answer of 2026-10-20, pending product owner", used_by: [CAP-01]}
    - {id: WA-08, source: "this scope, for AP-6", text: "A journal is 'issued' for numbering (S7-2.1.10-c23) when it is approved and posted, not when a draft is saved. S7-2.2.6-c01 makes approval the point at which an entry becomes a record of account.", label: "labelled assumption of the requirements engineer, pending qualified accountant (with product owner)", used_by: [CAP-12, CAP-13]}
    - {id: WA-09, source: "this scope, review finding on journal fields", text: "The header and line rules of the journal upload template (S7-2.2.4-c37 to c56) apply to entry on screen, including one currency per journal and mandatory descriptions, because V2.2 states no other field rules for journals.", label: "labelled assumption of the requirements engineer, pending qualified accountant (with product owner)", used_by: [CAP-12]}
    - {id: WA-10, source: "this scope, review finding on the dimension column", text: "The 'Mandatory on' column of the dimension table (S7-2.2.3-c02 to c07) is a default that a per-account dimension rule (c09) can override, not a floor.", label: "labelled assumption of the requirements engineer, pending qualified accountant (with product owner)", used_by: [CAP-10]}

  accounting_policy_points:
    note: "Named, not decided. Each needs the qualified accountant and the product owner (DEC-0007 conditions) unless another owner is named. The tax specialist is consulted where tax is touched."
    items:
      - {id: AP-1, point: "The enforcement level per control type for the first entity, and whether a level set at entity set-up is a 'lowering' (Q-033).", owners: [qualified-accountant, product-owner]}
      - {id: AP-2, point: "Who approves a lowering of a level (S7-2.2.1-c64 names no role); the contents of the reason list for an Advisory journal; which role receives the Advisory exception report.", owners: [qualified-accountant, product-owner]}
      - {id: AP-3, point: "The rounding method, and where a functional-currency rounding difference on a balanced foreign-currency journal is posted. S7-2.2.9-c06 fixes the precision, not the method.", owners: [qualified-accountant, product-owner]}
      - {id: AP-4, point: "Which rate applies to a journal date when no manual company rate exists for that date, and who may override a rate. One currency per journal is adopted from the upload template (WA-09), pending the qualified accountant.", owners: [qualified-accountant, product-owner]}
      - {id: AP-5, point: "The content of the statement lines, notes and cash flow categories an account maps to, per accounting framework (Q-003), and the approval route for creating and changing them (proposed: the same maker-checker route as accounts).", owners: [qualified-accountant, product-owner]}
      - {id: AP-6, point: "Which journal series are statutory, and the moment a journal is 'issued' (WA-08).", owners: [qualified-accountant, tax-specialist, product-owner]}
      - {id: AP-7, point: "Journal types in INCR-001: manual only, approved by a second user as V2.2 states it (S7-2.2.5-c01). Confirmation that no other type is needed in the first increment; the Adjustment type waits for Q-055.", owners: [qualified-accountant, product-owner]}
      - {id: AP-8, point: "The financial year end for each entity and the first-year length (Q-003). The adjustment and special audit adjustment periods wait for Q-055 (EXC-28).", owners: [qualified-accountant, product-owner]}
      - {id: AP-9, point: "V2.2 names the Finance manager as 'Set by' for Open, Soft closed and Hard closed (S7-2.2.8-c09, c10, c11); that is stated, not open. Open: who gives the management approval for a reopening (S7-2.2.8-c07, c26), which role audit-locks a period (c12, bracketed), and whether the entity uses soft close (c15).", owners: [qualified-accountant, product-owner]}
      - {id: AP-10, point: "Which number series a correction reversal draws from (the manual journal series, or a series of its own), and whether the mechanical inverse described in CAP-12 is the intended reversal.", owners: [qualified-accountant, product-owner]}
      - {id: AP-11, point: "Where the location element of a journal number comes from, given that a journal's lines may carry different locations (S7-2.1.10-c13, S7-2.2.3-c06). Proposed meanwhile: not used in journal series.", owners: [qualified-accountant, product-owner]}
      - {id: AP-12, point: "Whether a period may be soft-closed or hard-closed while journals dated in it are pending approval.", owners: [qualified-accountant, product-owner]}

  security_points:
    note: "Named for the security owner. Not decided here, and no security assumption is made."
    items:
      - {id: SEC-1, point: "Identity provider, multi-factor policy, password and lockout defaults, encryption standard (S7-2.1.3-c01 to c03).", owner: security-owner}
      - {id: SEC-2, point: "The tenant isolation guarantee and what an operator of the product may reach in a tenant (with Q-031).", owner: security-owner}
      - {id: SEC-3, point: "Whether the audit log and posted entries need tamper evidence beyond 'no user or administrator can edit', which the specification states as a behaviour only (S7-2.1.4-c01, S7-2.2.6-c10).", owner: security-owner}

  points_without_a_question_record:
    note: "The orchestrator may raise these as questions. The requirements engineer cannot create question records."
    items: [SEC-1, SEC-3, AP-2, AP-3, AP-4, AP-5, AP-6, AP-7, AP-9, AP-10, AP-11, AP-12]
    covered_by_questions: "SEC-2 by Q-056 and Q-031; the adjustment journal by Q-055; limits by Q-057."

  countries_currencies_tax:
    foundation_needs:
      - "All ISO 4217 currencies with minor-unit precision, so LKR and any other currency can be activated (S7-2.2.9-c02)."
      - "A functional currency per entity, fixed once transactions exist (S7-2.2.9-c03)."
      - "A jurisdiction recorded on the entity, without a restriction to a list of countries and without any behaviour that depends on it (S7-2.14.1-c08). The country code may appear as an element of a numbering series (S7-2.1.10-c12)."
      - "A financial year per entity with its own start and end dates (S7-2.2.8-c02)."
      - "Manually entered rates (S7-2.2.9-c11)."
    waits_on_q003:
      - "Which countries release 1 supports, Norway and any added country (product owner, qualified accountant)."
      - "A named tax specialist for added countries; an authority-matrix change (governance owner)."
      - "The accounting framework per country and for the group, the year end for each entity, the group reporting currency (qualified accountant)."
      - "Statutory returns, tax documents, tax registrations and levies, and prescribed number formats (tax specialist)."
      - "The statutory statement structure that statement-line mappings point to (AP-5)."
      - "Data-residency regions per country (Q-028)."
    tax_in_scope: "None. INCR-001 holds no tax rule, code, register, registration or document (EXC-19)."

  bracketed_values_relied_on:
    note: "Each is a bracketed value in V2.2. INCR-001 requirements state it as a configurable parameter and cite the bracket; the owning role confirms the value through the V2.2 bracketed-value workbook (Q-004), which is not yet produced."
    items:
      - {value: "[6] digits, four to ten", clause: S7-2.2.1-c17, owner: qualified-accountant}
      - {value: "[4] group levels", clause: S7-2.2.1-c04, owner: qualified-accountant}
      - {value: "[role] approving account creation", clause: S7-2.2.2-c04, owner: qualified-accountant}
      - {value: "[role] receiving the Advisory exception report", clause: S7-2.2.1-c56, owner: qualified-accountant}
      - {value: "[role] approving a segregation-of-duties exception and a released separation", clause: S7-2.1.2-c14, owner: product-owner}
      - {value: "[role] approving a reopening, and the [role] with approval that audit-locks a period", clause: S7-2.2.8-c07, owner: qualified-accountant}
      - {value: "[role] approving the audit lock", clause: S7-2.2.8-c12, owner: qualified-accountant}
      - {value: "[role] allowed to key an account code", clause: S7-2.2.2-c05, owner: qualified-accountant}
      - {value: "[role] receiving a non-nil statutory gap result", clause: S7-2.1.10-c29, owner: product-owner}
      - {value: "[7] years audit log retention", clause: S7-2.1.4-c08, owner: product-owner}
      - {value: "[80]% capacity warning", clause: S7-2.16.1-c26, owner: tech-lead}
      - {value: "[4] custom dimensions and dimension code formats", clause: S7-2.2.3-c08, owner: qualified-accountant}

  tier_proposal:
    tier: 1
    justification: "methodology.md puts posting, numbering, periods, audit, authorisation, isolation, money and rounding in Tier 1. This scope fixes which Tier-1 capabilities are built and which are held back, and DEC-0010 condition 4 states the foundation is Tier 1. The tier is not lowered."
    approval_consequence: "Authority-matrix (the product owner's approval of D-3, D-6 and D-7 also needs the qualified accountant, DEC-0010 condition 5). Authority-matrix stage0.allowed_tiers is [2, 3]: a Stage 0 approval (E1-op) never counts for Tier 1. The product owner's Stage 0 approval of this scope would not count. Approval needs F2 (GitHub, Stage 1, with Shifan Cader's own identity). Until then the scope stays Proposed, and DEC-0010 condition 1 stops requirements being written."
---

# Scope proposal for the foundation increment (INCR-001)

**This body is explanation. It is not normative.** The product owner's approval covers the
`normative` block of the front matter only.

## What this is

DEC-0010 (Approved) lets Gates A and B pass for one increment at a time, starting with a foundation
increment. Its first list of what the foundation holds (tenants and firm access, users, roles, audit
log, journals, periods, numbering, chart with control settings, currencies) was a starting point. This
proposal checks each item against SRC-007 and the question records, and says in `changes_to_dec0010_list`
what it confirms, narrows or extends and why.

I read the clause text from the extraction of SRC-007, not from the PDF. Where it looked garbled I would
have said so; I found nothing garbled in the sections cited. The PDF remains authoritative.

## How the scope was cut

Three tests, applied to every candidate capability:

1. **Is it stated plainly, or a setting?** V2.2 states most ledger controls without a bracket or an open
   question: no edit after approval, audit log, gapless series, period states. Others it makes a setting
   per entity: control levels, soft close, capacity limits.
2. **Does it need a sub-ledger?** Q-029 is about postings from payroll, depreciation and other modules
   before they exist. A capability that only users exercise cannot depend on it. That is why
   INCR-001 contains no module.
3. **Does a blocking question touch it?** Eight do, and the touched part leaves the increment: firm
   access (Q-031), the naming standard (Q-014), changing a control flag once history exists (Q-034),
   post-approval dimension changes (Q-007), the override into a hard-closed period (Q-013), the
   adjustment journal (Q-055), the tenant bootstrap (Q-056) and behaviour at a capacity limit (Q-057).
   Each stays out as a named exclusion, so the rest of its capability can go ahead.

## Where the scope is thin on purpose

- **No tax, no countries beyond a recorded jurisdiction.** Q-003 is open and the added countries have no
  tax specialist. The foundation holds what any country needs: currencies, a functional currency, a year
  end.
- **No year-end close.** It needs a retained-earnings policy. An increment can run inside a financial
  year. This is the largest narrowing; D-3 asks the product owner to confirm it.
- **No delivered chart or chart upload.** The chart is Finance's data and Q-005 is open. Accounts are
  created one request at a time, which is also the route V2.2 insists is the only one.
- **No governance panel.** Several in-scope clauses report to it. The events are written to the audit
  log, so the panel can be built later without losing history (D-4).

## Things to know before approving

- **Approval needs F2.** The scope is Tier 1. A Stage 0 approval would not count, and the scope cannot be
  approved until the git-host identity exists. DEC-0010 condition 1 then holds requirements back. I did
  not lower the tier to avoid this; the orchestrator and the governance owner may want to plan for it.
- **Q-032 and Q-033 are working answers.** If the product owner or the qualified accountant answers
  differently, CAP-11 changes by change request. The scope builds the mechanism and fixes no value.
- **One SRC-007 conflict sits inside CAP-11.** The attribute table (S7-2.2.1-c06) says manual journals to
  control accounts are blocked; the posting rule (c52) blocks them at Enforced only. This is Q-032,
  already recorded, so I did not escalate it as new. The other conflict, c14 against c10 on posted
  entries, is Q-007 and is excluded.
- **Two reads I had to make.** The moment a journal is "issued" for numbering (WA-08), and the approval
  role for lowering a control level, which S7-2.2.1-c64 does not name (AP-2). Both are named for the
  qualified accountant, not decided.
- **The stack.** Several capabilities lean on it (see `stack_dependencies`): concurrency-safe numbering,
  isolation, tamper resistance. The scope states behaviour only.

## Changes from v1 to v2

v2 answers REV-01M61MRRKX52P8XHG3NZXSPCZJ (3 blocking, 14 non-blocking findings). The orchestrator raised
Q-055 to Q-057 from B2, B1 and B3. I answered none of them.

| Change | Finding or question |
| --- | --- |
| Tenant bootstrap held out as EXC-27, with a test-tenant route offered as a proposal to the security owner, marked not a production route. CAP-01 says so. | B1, Q-056 |
| Adjustment journal type, correction by adjustment journal, closed-period correction and the two adjustment periods held out as EXC-28. CAP-12 is manual journals corrected by reversal; CAP-14 drops the two periods. I took the reviewer's recommended narrower option. | B2, Q-055 |
| CAP-06 reworded: capacity is not a licence cap or an enforced limit; it builds the setting, the audit record and the warning. EXC-21 licensing wording deleted. CAP-01's entity limit reworded. Behaviour at a limit and who raises a figure held out as EXC-29. | B3, Q-057 |
| Departures from plain V2.2 text listed one by one (DEP-1 to DEP-8). D-1 no longer approves them in bulk. CAP-09 now quotes c44 in full. EXC-15's weak reason replaced by a product-owner choice. | Departures finding |
| CAP-08 adds maintenance of statement lines, notes and cash flow categories as entity data, proposed under the account approval route; cites c47 and c35. | Statement-line finding |
| One financial year per entity proposed (CAP-14, CAP-15, D-3); no balance across a year end. D-3, D-6, D-7 now also need the qualified accountant. | Year-end finding; review point 7 |
| Pending journals at close named as AP-12; approval into a closed period refused by c13. | Close-behaviour finding |
| Correction reversal defined as a mechanical, system-generated inverse (CAP-12); its series is AP-10. | Reversal finding |
| Location element of a journal number: proposed not used in journal series; AP-11. | Numbering-location finding |
| CAP-12 field list adopted from the upload template's rules (c37 to c56), labelled WA-09. | Journal-fields finding |
| 'Mandatory on' column reading labelled WA-10 and shown as DEP-7. | Dimension-column finding |
| Trace links: c27 removed from EXC-01; c01 of 2.1.11 cited in CAP-04 with its reading; bracket citations corrected to c07 and c12 and the c05 key-code role added; reserved codes named in EXC-08; c35 cited. EXC-07 also cites c21. | Trace-link finding (a) to (f) |
| CAP-07 stores the lock state, cites c09 and c23 as partly built, keeps the first sentence of c18; Gate B input added in stack_dependencies. | CAP-07 finding; over-wide exclusions (a) |
| EXC-10 narrowed: flag change on an account with no history stays in CAP-09. | Over-wide exclusions (b) |
| AP-8 names the product owner. AP-9 rewritten: the Finance manager as 'Set by' for Open, Soft closed and Hard closed is stated (c09 to c11); only the reopening approver, the audit-lock role and use of soft close are open. | Policy-owners finding |
| CAP-05 states that c02 is testable on master data only and login events only after SEC-1. | CAP-05 finding |
| Classification covers Q-001 to Q-057: 8 blocking, 49 not-blocking. | Q-055 to Q-057 |

## Findings not fixed, and why

- **Q-007 and the posted-line data model.** The review recommends the qualified accountant answer Q-007
  before INCR-001 Gate B, because excluding Q-007 fixes the posted-line model before the answer. This is a
  recommendation to the orchestrator, not a scope change. I record it here and leave the scope as it is.
- **WA-03 against V2.2's single-entity default.** The review notes that V2.2's default for a single
  entity running the ledger alone is Not applied, not Advisory. This is unchanged: CAP-11 states the
  difference and builds no default (DEP-6).
- **PDF check.** The review checked clauses against the extraction only. I did not check against the PDF
  either. The pages B2 and B3 rest on (pp.37, 40 to 42, 133 to 136) should be confirmed on the PDF before an
  owner decides.

## Not claimed

No requirement, story or acceptance criterion exists yet. Nothing here is approved, and no working
answer is treated as confirmed. The assurance review is a later step (REV-01M61MRRKX52P8XHG3NZXSPCZJ is reserved for it).
