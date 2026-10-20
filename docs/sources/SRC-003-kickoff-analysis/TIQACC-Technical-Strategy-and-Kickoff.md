**TIQACC: technical strategy, requirement analysis, and kickoff**

Prepared 19 October 2026. Intended use: both an internal group finance platform and a commercial SaaS product, as confirmed by the requirements owner.

Source reviewed: [the 121-page requirement specification](../../requirement-doc/TIQACC-Cloud-Accounting-Requirement%20-%20V1.pdf). Page references below are the printed PDF page numbers. Document content is treated as requirements to assess, not as instructions to this analysis. Statements labelled recommendations, hypotheses, or proposed scope are additions to the specification and require the appropriate product or finance decision.

**1. The central recommendation is to build one controlled finance product, prove it inside your group, and validate it with external customers before expanding the ERP scope.**

The strongest product direction is a finance platform in which a user can understand a financial result, inspect its evidence, resolve the work preventing sign-off, and reproduce the result later on the same accounting basis. A useful positioning hypothesis is: **"Finance you can prove."**

The architecture should combine a reliable accounting kernel, versioned configuration, evidence attached to transactions, an excellent exception workspace, and a shared reporting model. AI should make that system easier to inspect and operate. It must not become the authority for balances or approvals.

Use your group as the first design partner and first production tenant. Give internal users the same permission boundaries, configuration mechanisms, upgrade process, and export capabilities that paying customers receive. An internal-only database shortcut, hard-coded company rule, or separate customer branch will become a commercial liability.

Two or three external design partners should participate before the product is called market-ready. Internal success demonstrates operational usefulness; external adoption tests whether the problem, onboarding effort, configuration model, and pricing generalize.

This recommendation is conditional on being able to agree a narrower release baseline. Page 6 explicitly says every module must be delivered and that activation is not scope deferral. A phased build is a proposed change to delivery scope, not an interpretation that the current specification already excludes difficult modules.

**2. This is an enterprise finance and ERP specification, rather than a conventional small-business accounting application.**

The document is strong on source-to-ledger posting, maker-checker controls, evidence retention, historical reporting, and acceptance examples. Its accounting flow on pages 4-7 is a sound organizing principle: source transaction, approval, deterministic posting, ledger, report, evidence.

However, the combined scope includes several substantial products:

| Capability family | Document coverage | Delivery implication |
|---|---|---|
| Accounting foundation | GL, chart governance, dimensions, periods, currencies; pp23-36 | Build the financial rules and integrity controls before attractive dashboards. |
| Operational finance | AR, invoicing, AP, banking and treasury; pp36-67 | Complete end-to-end flows, including corrections and settlement, are required. |
| Jurisdiction compliance | Tax, returns, statutory outputs; pp68-75 | Each supported country needs maintained rules, examples, output formats, and an accountable owner. |
| Asset accounting | Multiple books, six depreciation methods, revaluation, impairment, leases; pp75-83 | This is substantially larger than an asset list and depreciation button. |
| Supply chain and production | Warehouses, batches, serials, costing, landed cost, BOMs, WIP and MRP; pp83-90 | Manufacturing and costing form a separate delivery program. |
| Workforce and payroll | Country rules, employment rules, leave, benefits, payroll and self-service; pp90-98 | Payroll localization is a continuing product and compliance commitment. |
| Evidence and close | Supporting documents, working papers, reconciliation, audit packs; pp98-102 | This can become a particularly coherent user experience and entry offering. |
| Reporting and group finance | Report builder, language-driven reports, consolidation, ownership, NCI, group dashboards; pp102-119 | Requires governed metrics and reproducible reporting bases, not isolated dashboard calculations. |
| Commercial platform | Standalone modules, activation, localization, integration; pp8-22 | SaaS tenancy, entitlements, provisioning, billing, support access and upgrades need additional specification. |

The 13 industry templates on page 16, minimum 15 languages on page 20, standalone products on pages 13-17, and global payroll/tax ambition multiply the scope. They cannot be reduced to feature flags.

The document also resembles a vendor procurement specification. Its S/C/X/N vendor response matrix and Annexures A and B are referenced on pages 5 and 121, but the actual completed matrix, operational volumes, chart, and existing invoice examples are not included in the supplied PDF. Those missing inputs matter for build-versus-buy and capacity decisions.

**3. Competitive differentiation needs a specific buyer and a measured workflow advantage.**

The closer enterprise peers are NetSuite OneWorld, Dynamics 365 Business Central, and Sage Intacct. Smaller customers will also compare Xero, QuickBooks, and Zoho Books.

Official product documentation already covers much of the proposed category:

| Existing baseline | Implication |
|---|---|
| [NetSuite OneWorld](https://www.netsuite.com/portal/products/global-business-management.shtml) describes multi-entity, currency, language and consolidated operations. | "One platform for every entity" is a positioning foundation, not sufficient differentiation. |
| [NetSuite Financial Close](https://www.netsuite.com/portal/products/erp/financial-management/finance-accounting/financial-close-management.shtml) markets reconciliation, matching and AI financial exception monitoring. | Close control and exception detection need a demonstrably better workflow. |
| [Business Central AI documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/ai-in-bc) describes conversational analysis, reconciliation assistance, invoice matching and payables automation. | Chat, OCR, AI matching and an assistant are established competitive capabilities. |
| [Sage Copilot](https://www.sage.com/en-us/sage-copilot/) markets proactive issue detection and continuous close. | "Continuous close" alone is not an unoccupied market position. |
| [Xero reconciliation](https://www.xero.com/us/accounting-software/reconcile-bank-transactions/) and [Zoho Books features](https://www.zoho.com/us/books/accounting-software-features/) cover automation and core accounting controls. | A broad feature list is unlikely to win against mature products and ecosystems. |

These are vendors' documented claims, not independent performance measurements. Availability varies by country, subscription and rollout status. The table does not establish that competitors lack any capability proposed below.

A sensible initial customer hypothesis is a lean finance team in a service-based group with several entities, fragmented evidence, spreadsheet reconciliations and a slow close. Start in one confirmed jurisdiction. The services profile on pages 16-17 explicitly permits operation without inventory, making it a useful first deployment profile.

Three connected product bets are worth validating:

- **Reproducible financial results.** From a KPI, show the contributing entries, source documents, rule version, exchange-rate basis, approval chain, reporting definition and consolidation basis. Let an authorized reviewer reproduce an issued result after the configuration has changed.
- **Governed configuration changes.** Preview a proposed posting rule against historical transactions, as required on page 64. Extend this carefully into reporting-impact previews for mappings, dimensions and account structures. The broader impact simulation is a product proposal beyond the literal requirement.
- **Work that gets completed.** Bring missing evidence, unmatched payments, rejected imports, intercompany differences, approvals and close tasks into one workspace with owner, amount at risk, deadline, reason and next action.

The claim to test is not "we have these features." It is: "This particular finance team can complete this recurring job more quickly, with less implementation effort and a stronger explanation of the result."

**4. Internal operations and commercial SaaS need separate success criteria within the same product.**

For the internal group, success means accurate accounts, controlled operation, a reconciled parallel run, usable evidence and a dependable close. For the SaaS business, success additionally means repeatable onboarding, isolation between customers, supported configuration, sustainable support costs, commercial packaging and willingness to pay.

Maintain one product roadmap. Internal requests should pass the same product review as external requests. Record whether a change is:

- A core accounting or security capability.
- A reusable configuration option.
- A maintained jurisdiction or industry pack.
- A connector.
- A company-specific process that should remain outside the core.

Use released configuration packs rather than per-customer source branches. Your own group should not be an undocumented super-tenant with permissions unavailable to other customers.

Before a major engineering commitment, run a fit-gap demonstration against two relevant existing products using your actual scenarios. Buying or extending an ERP could satisfy internal needs sooner while TIQACC develops a narrower commercial product. Building the entire ERP is justified only if owning the accounting platform is central to the business and the investment is sustainable.

**5. The recommended first release is a complete, narrow finance flow with evidence and close controls.**

The initial release should support one jurisdiction and one service business profile, with multi-entity boundaries designed from the start. Prove one entity first, then a second entity and an unrelated test tenant. Multi-currency data structures should exist initially; enable and certify only the currency scenarios covered by the pilot.

| Release treatment | Capabilities |
|---|---|
| Build first | Tenant/entity access, maker-checker, controlled chart, line dimensions, periods, deterministic posting, evidence, audit, transactional numbering, import controls and migration tools. |
| Complete operational finance slice | Supplier capture and approval, AP open items, payment recording, customer invoicing, receipts and allocation, controlled bank statement import, reconciliation and corrections. |
| Deliver usable close | Trial balance, P&L, balance sheet, bank and AR/AP tie-outs, account reconciliation, close checklist and indexed evidence export. |
| Include narrowly | One validated invoice-tax/rate/register/export pack, basic known-commitment cash forecast, basic budgets, read-only assistant over supported reports. Wider corporate/deferred-tax processing and direct e-filing need separately agreed scope. |
| Add after financial integrity is proven | Supported foreign-currency settlement/revaluation, richer reporting, simple intercompany and simple consolidation, fixed assets and additional connectors. Move these earlier if the internal pilot requires them. |
| Defer explicitly in the release agreement | Manufacturing/MRP, advanced inventory costing, worldwide payroll, complex ownership/NCI, associates, leases, all languages, all industry templates and a universal no-code integration designer. |

If your internal businesses cannot operate without stock, payroll or a specialist process, keep the incumbent module connected during the first release or select a different pilot entity. Any external-payroll route needs the specification conflict identified below resolved first. Do not force a services MVP onto an unsuitable entity.

The decisive demonstration should be:

~~~text
Supplier email and original document
  -> reviewed extraction and validated supplier
  -> required evidence and maker-checker approval
  -> deterministic journal and AP open item committed together
  -> payment recorded under its own authorization
  -> statement imported and matched without duplicate posting
  -> bank, AP and GL reconciled
  -> statement line opened back to its evidence
  -> period closed and an indexed review pack produced
~~~

Prove a corresponding sales flow: issue invoice, record receipt, allocate, handle a credit/correction, reconcile, and close. Include duplicates, errors, rejections and late changes in demonstrations.

A standalone close/evidence offering is another entry hypothesis, consistent with the modular direction on pages 13-17 but not explicitly defined there as a standalone product. It needs its own scope, integration contract and acceptance criteria. It reduces operational replacement scope but introduces connector and reconciliation work, and it competes with specialist close platforms. Choose it only if customer discovery supports it; do not build both entry strategies simultaneously.

The interface should make the finance team's next action clear. Design three primary work surfaces: a work inbox, a transaction inspector and a close/review workspace. Executive views read the same governed measures.

The work inbox should distinguish missing evidence, approval, matching and accounting failures, and show an owner, due date, financial impact and specific next action. Batch actions need a preview and row-level validation; a bulk action must not bypass controls.

The transaction inspector should put source evidence beside extracted fields and the accounting preview. Keep approval history, posting rules and corrections close to the transaction. Make entity, currency, accounting period and status unmistakable. Keyboard navigation, sensible defaults and fast searchable selectors matter more than decorative animation.

The close workspace should show readiness by account/entity, responsible people, unresolved differences and the effect of late postings. Use progressive disclosure for advanced configuration. Keep inactive modules absent as the specification requires. Preserve filter/context when drilling into a number so the user can return to the exact question they were examining.

Test the visual design with large values, long translated labels, dense tables, narrow screens and accessibility requirements. A sophisticated finance product should remain calm and readable under real workload.

**6. Use a modular monolith with one transactional accounting core as the starting architecture.**

The requirements repeatedly demand that source approval and ledger posting agree continuously. A single application with strict domain boundaries and a relational transaction is a good first fit. Independent services per module would make consistency, deployment, authorization and debugging harder before there is evidence that separate deployment is needed.

~~~mermaid
flowchart TD
    U[Finance workspace and executive views] --> A[Authenticated API and authorization]
    E[Imports and external systems] --> A
    A --> M[Domain modules: AP, AR, bank, close and later modules]
    M --> K[Posting, approvals, periods and versioned configuration]
    K --> D[(PostgreSQL: source state, journals, open items, audit and outbox)]
    K --> F[Evidence metadata and retained object versions]
    D --> W[Background workers through transactional outbox]
    W --> X[Email, exports, connectors, OCR and search indexing]
    D --> R[Governed financial queries and report definitions]
    R --> U
    R --> I[Read-only AI tool gateway]
    I --> U
~~~

Core financial state is committed synchronously. Document delivery, OCR, exports, search indexing and connector calls run after commit. A queue outage must not leave an approved bill without its ledger entry.

Recommended default stack, subject to the delivery team's existing strengths:

| Layer | Recommendation and reason |
|---|---|
| Browser application | React and TypeScript with a mature accessible component and data-grid system. Prioritize fast keyboard operation, dense readable tables, localization and predictable forms. |
| API and domain | ASP.NET Core on .NET 10 LTS, with explicit domain types and module contracts. This is a default recommendation, not a requirement imposed by the PDF. |
| Financial store | Managed PostgreSQL on a supported stable release available in the selected region. Relational constraints, transactions and exact numeric arithmetic suit this workload. |
| Data access | EF Core for transactional application work; reviewed SQL for demanding financial queries. Keep posting rules in the domain layer and database integrity boundaries. |
| Background processing | Durable jobs and a transactional outbox; add a managed queue where needed. Persist job state, idempotency keys, retry counts and failures. |
| Evidence | Versioned object storage, file scanning, integrity hashes, retention policies and short-lived authorized downloads. |
| Identity | Managed OIDC/SSO provider, MFA, scoped roles and separate service identities. |
| Reporting | One governed financial query model used by reports, dashboards, exports and AI. Introduce replicas or an analytical store only when measured workload requires them. |
| Operations | Managed containers, infrastructure as code, CI/CD, OpenTelemetry and tested backups. Begin on one cloud and in the region justified by customer residency requirements. |

Microsoft currently lists [.NET 10 as LTS through 14 November 2028](https://dotnet.microsoft.com/en-us/platform/support/policy). Plan upgrades as a routine product responsibility.

Avoid adding Kubernetes, Kafka, a separate service for every module, a graph database, a vector database, or full event sourcing merely to signal modernity. An append-only journal and immutable audit records do not require every business object to be event sourced.

Preserve boundaries that permit later extraction: document processing, connectors, search, analytical reporting and notifications are more natural candidates than splitting AP posting from GL posting.

**7. Financial integrity should be expressed as enforceable invariants.**

The essential financial command is not a generic "save." It is an authorized state transition with a complete accounting effect.

When a document reaches its accounting-triggering transition, the system should perform the following steps. The trigger is defined by document type: it may be approval, issue, confirmation or release. An approved requisition or purchase order does not automatically create a financial journal.

1. Check tenant/entity access, the exact source revision, approval policy, required evidence and duplicate identity.
2. Resolve the applicable posting rule, tax facts, exchange rates, dimensions and accounting period.
3. Generate the complete journal and calculation workings.
4. Validate accounts, control-account restrictions, currency representation, periods and domain constraints, including whether the event has any accounting effect.
5. In one database transaction, finalize the source, append the journal, update the open-item or stock movement records, record approval and audit provenance, and append an outbox event.
6. After commit, process delivery, connector and search tasks using retry-safe workers.

Recheck period state and source revision within the protected commit path. A pre-validation screen alone does not prevent a period from closing or a document from changing during approval.

Core invariants include:

- Every operational journal belongs to one legal entity and one ledger/book; group adjustments belong to the consolidation layer.
- Functional-currency debits equal credits. Define how foreign and cross-currency legs are represented; never sum unlike currencies to test balance.
- A committed source event produces its accounting effect once, even after timeout, retry or file replay.
- Posted financial values are append-only. Corrections reference the original and use an approved reversal, credit, debit or reclassification route.
- Manual journals cannot bypass subledger control accounts, required dimensions, approvals or period locks.
- Source-document totals, open-item movements and journal effects agree.
- Receivable/payable allocation cannot exceed available amounts; concurrent operations must respect those limits.
- A person cannot approve their own document, including through delegated or service-account routes.
- An approval applies to a specific revision. Relevant changes invalidate it.
- A late entry invalidates any affected approved reconciliation and marks relevant consolidation results stale.

Use exact decimal arithmetic and explicit currency/quantity/rate precision. PostgreSQL recommends [numeric for monetary amounts requiring exactness](https://www.postgresql.org/docs/current/datatype-numeric.html). Define rounding at line, document, tax, allocation and reporting boundaries. Do not assume every currency has two minor digits.

For example, ignoring tax purely to illustrate the posting flow: approval of a supplier service bill for 1,000 creates expense debit 1,000 and AP credit 1,000. Recording its payment creates AP debit 1,000 and bank credit 1,000. When the matching bank statement line arrives, it confirms the existing movement; it must not create a second bank credit.

Treat queues as capable of redelivery. An outbox row is written with the accounting transaction, then workers deliver it. Consumers retain processed operation identities and reject incompatible reuse of the same key. This follows the consistency problem described in [AWS transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html). Transport delivery is not the same as exactly-once business accounting.

**8. The data model should distinguish identity, financial events, reporting basis and evidence.**

Recommended minimum concepts:

| Concept | Important retained information |
|---|---|
| Tenant and entitlement | Customer boundary, residency placement, commercial modules, plan and lifecycle. |
| Group, legal entity and location | Ownership/reporting scope versus statutory accounting scope versus operating location. |
| Shared party and entity profile | Party identity, with entity-specific tax, terms, bank instructions and accounting attributes. Sharing never crosses customer tenants implicitly. |
| Source document and revision | Original business event, lifecycle, content revision, external reference and issue identity. |
| Approval instance | Source revision/fingerprint, policy version, maker, approvers, delegation and decisions. |
| Journal and journal line | Entity, book, explicit period, source event, account, functional/transaction amounts, FX basis, dimension set and rule version. |
| Open item and allocation event | Obligation, receipt/payment link, currency, settled carrying amount and reversal history. |
| Tax fact | Taxable base, tax type, rate/version, recoverability, tax-point basis and return mapping. |
| Evidence version and link | Content hash, original source, object version, retention/residency and typed link to document, line, approval or calculation. |
| Calculation or consolidation run | Input cutoff, parameters, configuration versions, workings, approvals and resulting postings/output. |
| Reconciliation | Account/period, ledger basis, supporting balance, items, owner, reviewer and approval basis. |
| Report definition and report run | Governed definition, parameters, ledger cutoff, mapping/rate/structure versions and issued artifact. |
| Integration message and acknowledgment | Source identity, payload reference/hash, idempotency key, result, downstream acceptance and reconciliation totals. |

Keep document date, accounting date, tax-point date, bank value date, approval timestamp and system recording timestamp distinct. Adjustment and audit periods may share calendar dates, so an explicit accounting-period identifier is necessary.

Separate an invoice's lifecycle, approval, posting, settlement, dispute and hold state. "Overdue" is normally a derived condition. A single status field cannot correctly represent an invoice that is partly paid, disputed and overdue.

Do not implement dimensions as free-form labels or a fixed pair of department/project columns. Use stable dimension identities, validated line-level assignments, effective-dated descriptions/hierarchies and group mappings. Keep flexible metadata out of the authoritative monetary model.

**9. Reproducibility is a more valuable design goal than simply retaining history.**

Effective dating alone does not reproduce a number. A report for September may change after a late posting, revised mapping or corrected hierarchy, even when the requested date remains September.

Provide two explicitly labelled experiences:

- **Current view of a past period:** the latest authorized reconstruction using the chosen business date and basis.
- **Previously issued view:** the exact result approved or distributed at an earlier cutoff.

A previously issued report should retain a manifest containing its definition version, parameters, entity scope, ledger posting cutoff, account/dimension mappings, rate basis, applicable consolidation run, calculation versions, approval and output integrity hash. Keep the issued artifact itself.

Operational reports also depend on facts beyond journals: allocations, due dates, disputes, party attributes and dimension hierarchies can change. Retain their relevant history or freeze the report input dataset. Recheck current authorization when reopening an old artifact; preserving historical content must not preserve access that has since been revoked.

A cutoff must represent a committed, consistent dataset. An arbitrary timestamp or uncoordinated sequence maximum is insufficient if transactions can commit out of order.

For consolidation, freeze entity input bases, ownership/control structure, mappings, rates, eliminations and adjustments for each approved run. A later entity posting marks the run stale; it does not silently rewrite the approved result.

Distinguish a transaction's stored conversion from official group translation at closing, average or historic rates. The current specification requires both stored reporting amounts and rate-dependent consolidation, so the product must define the basis of each and agree the revised wording.

The proposed "Explain this number" panel should show:

- What the measure includes, the date/cutoff and entities.
- Which entries contribute and whether data is current, incomplete or stale.
- Source documents and calculation workings.
- Relevant approvals, policy/rule versions and exchange-rate basis.
- Subsequent corrections and changes affecting a newer view.

This uses the strongest ingredients on pages 100, 111-113 and 116-119. It should be tested with accountants on actual review work.

**10. AI should operate through governed tools and report definitions.**

Section 2.1.9 on page 20 is explicit: assistants read and propose; they do not post, approve, release or change master data, limits or rules. Deterministic auto-posting under an approved policy is a separate mechanism.

Use AI initially for document extraction suggestions, account/dimension suggestions, evidence retrieval, report-definition drafting, exception summaries and draft variance commentary. Retain the proposal and user decision where it affects workflow.

For a question such as "Why did EBITDA fall?", the safe and useful path is:

~~~text
Question
  -> identify ambiguity and confirm entity/period/basis
  -> create a typed, inspectable report definition
  -> authorize requested data and measures
  -> execute deterministic financial queries
  -> build a numerical bridge whose parts sum to the movement
  -> draft commentary linked to those results
  -> show assumptions, exclusions and source links
~~~

The model should not invent numbers or create a second accounting calculation layer. Do not give it unrestricted database access or authority to execute arbitrary SQL. Both language-driven reports and visual reports should compile to the same governed definition.

Documents and imported text are untrusted data. An invoice containing instructions must not change the assistant's permissions, tools or workflow. Apply tenant/entity/payroll filtering before retrieval and verify access again when opening an attachment.

Record model/version, relevant template/prompt version, tool inputs, data cutoff and reviewed output for auditable assistant activity, while minimizing sensitive data in operational logs. Do not train across customer data without explicit contractual authorization.

Evaluate extraction accuracy by field, suggestion acceptance, numerical consistency, unsupported statements, permission leakage and the ability to refuse or clarify an ambiguous request. A generic model confidence score is not adequate authorization for financial action.

Begin cash forecasting with known AR/AP, payroll, tax and recurring commitments plus explicit timing assumptions. Add statistical predictions when suitable history exists, and measure forecast error against actuals. Every forecast should show freshness, uncertainty and missing inputs.

**11. SaaS isolation, governance and recoverability belong in the first release.**

Model tenant, group and legal entity as separate concepts. One commercial customer may have multiple groups and entities. A branch can be an operational location rather than a separate legal entity; reflect the chosen accounting treatment explicitly.

A practical default is a shared managed database with mandatory tenant keys, entity-scoped access, composite tenant-aware foreign keys and PostgreSQL row-level security as defense in depth. Use a deployment-placement abstraction so a customer can be placed in a different database or region where required. If the first confirmed customers require dedicated tenancy or local residency, make that the initial deployment mode instead.

Do not treat RLS as sufficient by itself. PostgreSQL documents that [superusers, BYPASSRLS roles and normally table owners bypass row policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html). The application must use restricted roles; migrations and privileged operations need a separate path. Test pooled connections and tenant context for cross-request leakage.

Isolation must also cover object paths and download authorization, search indexes, cache keys, job payloads, exports, integration credentials and AI retrieval. Application permissions should distinguish individual payroll data from approved aggregate payroll measures.

Establish tenant context from authenticated, authorized server-side identity; never trust a submitted tenant identifier alone. Missing context must fail closed. For pooled database connections, make context transaction-local and test that it cannot leak into another request. Tenant/entity-aware constraints should prevent inappropriate cross-entity references while allowing explicitly modeled shared group masters.

Object storage does not participate in a PostgreSQL transaction. Upload, scan, finalize and integrity-check required evidence before the financial commit. The database transaction binds immutable evidence-version references; abandoned uploads are cleaned up under a separate policy.

Define SaaS capabilities missing or under-specified in the PDF:

- Tenant provisioning, suspension, offboarding and complete data export.
- Subscription entitlements versus user permissions versus entity module activation.
- Support access that is time-limited, authorized and audited.
- Secret rotation, session revocation and service identities.
- Upgrade and database-migration compatibility across all customers.
- Usage/cost controls for storage, document processing, AI and background exports.
- Residency of primary data, backups, logs, extracted text, email processing and AI services.
- Incident response, restore ownership and customer communications.

The numbering requirement needs a transactional counter scoped to tenant, entity, configured location/document type and reset period, not an ordinary non-transactional database sequence. Enforce uniqueness in the database. Advance the locked counter late in issuance after expensive validation; final issuance, counter advancement and retained issued-document identity must commit together, with rollback on failed commit. Cancellation preserves the issued record. Failed email delivery does not discard or renumber it. Authority-assigned identifiers require an explicit jurisdiction workflow.

The audit promise also needs an infrastructure threat model. Restrict update/delete privileges and export protected audit records to separately controlled storage; use retention controls and tamper detection. An application administrator and a database/cloud operator have different powers. Avoid claiming that a disabled edit screen makes infrastructure tampering impossible.

Page 119's availability, volume and recovery figures are placeholders. Set measurable p95/p99 latency targets and dataset/concurrency assumptions for critical commands, reports, search and imports. Define what "live" means for each projection; show freshness where background processing is involved.

Daily backup alone cannot meet a four-hour recovery point. Use a suitable point-in-time recovery strategy, protect evidence alongside the database, and test a coordinated restore. Include a single-tenant recovery procedure for a shared database. Agree availability and support targets based on customer need and budget rather than copying unconfirmed placeholders.

**12. Resolve the following requirement decisions before implementing the affected behavior.**

This is a risk-based decision register, not an assertion that every requirement is defective. The suggested resolutions require Finance/Product approval and, where applicable, jurisdiction review.

| ID | Requirement issue and reference | Recommended decision |
|---|---|---|
| D01 | Every module must be delivered; p6, section 1. | Publish a release-by-release baseline with explicit exclusions, dependencies and acceptance. Module activation must not be used to conceal undelivered scope. |
| D02 | Standalone modules can run with GL unlicensed, but the catalogue calls GL always active; pp13-14, section 2.1.7. | Separate the internal accounting kernel/output contract from the commercially visible GL module. Decide which standalone modes are actually supported at launch. |
| D03 | GL hard-close cannot coexist with an open subledger on p32; p34 acceptance allows GL closed while AR remains open; section 2.2.8. | Approve a compatibility/state-transition matrix distinguishing soft close, hard close, operational capture and financial posting. |
| D04 | Posted dimensions are immutable, then optionally editable; p29, section 2.2.6. | Preserve financial dimensions; correct them by an approved reclassification event. Treat nonfinancial annotations separately. |
| D05 | Assistants cannot act, while automated posting is widespread; p20 versus pp27, 60-65. | Define approved deterministic automation mandates, per-transaction approval and release controls. AI proposals are never authorization. |
| D06 | Customer currency is fixed after use, while a party may trade in multiple currencies; pp35, 37. | Separate default currency from enabled transaction currencies, and retain open balances by currency. |
| D07 | Bank coding can auto-post movements already recorded by AP/AR; pp60-65. | Match existing entries first. Post only previously unrecorded economic events. |
| D08 | Statement deduplication by date/amount/narrative can collapse two genuine identical transactions; p60, section 2.6.3. | Prefer bank/account transaction identity. Use controlled occurrence/sequence-aware matching where no stable identifier exists; preserve ambiguous lines for review. |
| D09 | Suspense must be nil on p60, but approved residuals may remain on p64. | Define mandatory blockers and explicitly approved residual exceptions consistently. |
| D10 | A single invoice state mixes settlement, dispute and overdue/hold conditions; pp40, 53. | Use separate state dimensions and derive ageing/overdue status. |
| D11 | Native payroll is mandatory on p90; external payroll replacement is permitted on p11. | Decide supported integrated and native modes and update first-release acceptance accordingly. |
| D12 | Reporting currency is stored on each transaction, while consolidation uses rate-specific translation; pp35, 111-113. | Define the basis of stored amounts and freeze official translation in a versioned run. |
| D13 | Live reports must also reproduce identically months later; pp104-106. | Retain the issued artifact and a consistent dataset cutoff plus definition/configuration versions. Parameters alone do not suffice. |
| D14 | Jurisdiction-dependent tax document rules coexist with blanket restrictions; pp45-48. | Approve country-specific examples and acceptance cases. Do not derive tax liability from buyer registration alone. The 18% example on p47 is explicitly illustrative. |
| D15 | Credit and debit notes share a cumulative cap at original value; p48, section 2.4.6. | Define separate sign-aware reversal and additional-charge rules by supported jurisdiction and business scenario. |
| D16 | Receipt posting creates GRNI, while period-end accruals reference open orders/receipts; pp51, 55-56, 86. | Accrue accepted goods/services once. Do not accrue an undelivered commitment or duplicate a receipt liability. |
| D17 | Intercompany counterpart posting is automatic, but approval is required in each entity; pp28, 108-109. | Define counterpart acceptance, separate entity journals and handling when one entity rejects or has a closed period. |
| D18 | Account-code class determines natural balance and account tags drive cash flow; pp23-24. | Support contra-account behavior explicitly; define cash-flow method and transaction/noncash treatment beyond account classification. |
| D19 | Auditor access to everything conflicts with payroll confidentiality; pp98, 100. | Require explicit payroll audit scope and preserve restrictions in reports, packs and attachments. |
| D20 | "Any country" tax/payroll and all supported integrations by configuration; pp11-12, 68-75, 90-98. | Define a bounded rule model, supported country/connector catalogue, maintained adapters and the process for genuinely new mechanisms. |
| D21 | Later activation needs no migration; pp13-17. | Preserve existing data but require approved initialization, opening positions and reconciliation where a newly activated module needs them. |
| D22 | All-or-nothing imports coexist with arbitrarily large batches and external systems; pp12, 27. | Define atomic batch boundaries and maximum sizes. Stage/validate before commit; external delivery uses acknowledgments and reconciliation rather than a distributed database transaction. |
| D23 | Daily backup with a four-hour RPO; p119. | Specify and test point-in-time/incremental recovery and coordinated document restoration. |
| D24 | Sizing, roles, integrations, tolerances, retention and migration depth remain bracketed; throughout, particularly pp6, 9-11, 51-52, 119-121. | Complete a signed configuration and delivery decision workbook. Do not silently convert illustrative values into product commitments. |

Also settle inventory backdating/cost-restatement, late landed-cost allocation, returns at original cost, bank payment rejection/partial acceptance, and year-end adjustments after committed close before activating those scenarios. These are important accounting policies that the current text does not fully resolve.

**13. Start with a 30-day discovery and foundation phase that produces concrete decisions and a working proof.**

| Period | Work | Reviewable outcome |
|---|---|---|
| Days 1-5 | Observe the actual AP, AR, bank and close work in one internal entity. Collect anonymized examples, volumes, current reports, exceptions, tax rules and staffing/delegations. Identify external design partners. | Process maps, first customer hypothesis, measured pain baseline, missing Annexure B inputs and a prioritized decision register. |
| Days 6-10 | Demonstrate the same scenarios in relevant existing products. Agree build-versus-buy, first jurisdiction, service profile, supported integrations and release scope. | Signed release baseline, competitive workflow evidence, architecture decisions and a costed delivery plan. |
| Days 11-15 | Prototype the exception workspace, bill review, approval, report drill-through and close. Test with finance users and an external prospect. | Clickable flows, observed task results, design changes and explicit acceptance examples. |
| Days 16-20 | Build a technical proof for tenant/entity isolation, revision-bound approval, deterministic posting, transactional numbering and retry safety. | One approved source with a balanced immutable journal; adversarial concurrency/retry tests and a second isolated tenant. |
| Days 21-30 | Connect reviewed document capture, one statement import, matching, basic reports and evidence export into a thin journey. Exercise a correction and a restore. | A small end-to-end proof in a test environment and a gated plan for production hardening. |

The day-30 proof is not a production ERP or evidence that all accounting scenarios are complete. It should establish whether the key product and technical risks are tractable.

The first implementation backlog should be organized by completed financial outcomes:

| Epic | First meaningful acceptance |
|---|---|
| Tenant/entity foundation | Two tenants with differently configured entities cannot access one another through API, search, exports, attachments or jobs. |
| Master data and approvals | A controlled supplier/account change becomes usable only after the required independent authorization; an edited submission invalidates its approval. |
| Accounting kernel | A source command produces the expected balanced entry once, rejects an invalid dimension, and leaves no partial financial effect on failure. |
| Numbering and periods | Concurrent issuance has unique retained statutory identity; a posting racing hard-close cannot slip into the closed period. |
| Evidence capture | An original incoming file is retained, reviewed extraction creates a draft, missing mandatory evidence blocks approval and replacement preserves prior versions. |
| AP-to-payment | A bill becomes an open item, payment clears only the intended amount, and a correction remains linked to the original. |
| Invoice-to-cash | The supported tax matrix selects the approved document type, receipt allocation updates balances correctly, and credits preserve traceability. |
| Bank reconciliation | Existing payments are matched rather than reposted; retry/import overlap does not double-book and two genuine identical-value lines remain distinct. |
| Reporting and close | TB, P&L, balance sheet and AR/AP/bank tie-outs agree; late posting invalidates relevant sign-off. |
| Migration and operations | Dry-run balances reconcile, restore is demonstrated, failure queues have owners and indexed audit evidence can be exported. |

Represent stories with the requirement clause, business example, expected journal, state transition, permissions and evidence of acceptance. Avoid organizing the entire project around CRUD screens.

**14. Plan subsequent delivery around exit gates, not a large module checklist.**

For planning only, a narrowly scoped internal pilot could plausibly require roughly four to six months after the initial discovery phase with five to seven experienced engineers, dedicated finance ownership, design support and strong QA. This is not a quotation: jurisdiction complexity, internal dependencies, migration depth and the unresolved requirements can materially change it. Estimate again after the first 30 days.

Use the following sequence:

1. **Foundation and test proof:** accounting kernel, isolation, evidence, approvals, rule versions and critical concurrency behavior.
2. **Internal shadow pilot:** one entity and the two complete finance flows, with the existing system still authoritative.
3. **Controlled internal live use:** only after reconciled migration, restore proof and a full parallel accounting cycle.
4. **Second entity and external pilots:** different configuration, independent users and realistic onboarding; expand intercompany/consolidation only to supported cases.
5. **Repeatable commercial release:** provisioning, billing/entitlements, contracts, support access, onboarding, observability, data exit and a maintained country pack.
6. **Broader finance and operational expansion:** prioritize assets, richer group finance, inventory or payroll according to paying demand and internal necessity.

The full specification is a multi-year product ambition unless much of it is bought or integrated. A credible full-scope estimate requires a module work breakdown, completed operational inputs, supported-country list and ongoing compliance/support budget.

The minimum cross-functional ownership should include a product owner with authority to reject scope, a qualified finance/controller owner, a technical lead, backend and frontend engineering, automated QA, product design and platform/security support. Tax/payroll packs need qualified jurisdiction specialists. A development team cannot substitute for accounting policy ownership.

Model both build cost and operating cost:

~~~text
Monthly product cost =
  fully loaded team
  + cloud/database/evidence storage and recovery
  + document extraction, AI and email usage
  + integration and bank access costs
  + compliance maintenance
  + onboarding, migration and support
~~~

Track onboarding hours and support effort per tenant from the first external pilot. A cheap subscription with expensive bespoke onboarding is not a sustainable commercial model. Consider a base platform/entity price plus clearly defined module tiers, but validate packaging with customers before fixing it. Keep evidence attachment practical, consistent with the document's objective on page 100.

**15. Build the product's financial reasoning and user workflow; buy commodity infrastructure and selective specialist capability.**

| Decision | Recommended default |
|---|---|
| Posting kernel, evidence provenance, close workflow, explainable reporting basis | Own these if they are the product's differentiating capability. |
| Identity, email delivery, object storage, file scanning, observability, payment rails | Use managed services with appropriate residency and contracts. |
| OCR/document extraction | Use a provider behind a replaceable adapter; retain originals and evaluate real documents. |
| Bank feeds, payment initiation and tax filing | Use certified/available providers where appropriate; verify actual local access and distinguish recording a payment from initiating funds movement. |
| Payroll, complex tax, specialist inventory/manufacturing | Integrate or use a mature engine until owning the capability is commercially justified. Record departures from the full native-module specification. |
| Report designer/grid components | Evaluate mature components to save effort, while keeping authorization, measures and report definitions under product control. |
| Full internal ERP replacement | Compare purchase/configuration against custom build using real fit-gap evidence and total ownership cost. |

A maintained country pack should declare supported business scenarios, tax/payroll mechanisms, document formats, effective dates, regression examples, qualified reviewers, version compatibility and update responsibility. It is not merely a rate table.

An integration framework should declare supported protocols, schemas, transformations and retry behavior. A named connector needs a version, authentication contract, source-of-record rules, sample messages, operational monitoring and reconciliation tests. "Any integration without development" must have a bounded meaning.

**16. Measure the product's advantage and require proof before promotion.**

First measure the internal baseline, then set targets jointly with finance users. The following are candidate targets, not promises inferred from the PDF:

| Outcome | Candidate measurement |
|---|---|
| Easier evidence review | Median and 90th-percentile time from a statement line to accepted supporting evidence; target within the document's four-click requirement for the specified paths. |
| Faster capture | Time to review and approve a bill, corrected-field rate and duplicate detection accuracy. |
| Better reconciliation | Manual minutes per statement, unresolved item value/age and false-match rate. |
| Faster close | Working days and staff-hours from cutoff to signed close, with overdue blockers separated. |
| Trustworthy accounting | Zero unexplained control-account differences and no duplicate accounting effects in accepted scenarios. |
| Reproducible reporting | Previously issued packs reproduce on their retained basis after permitted changes. |
| Safer configuration | Proposed changes tested before activation; changes with missing approval references measured and resolved. |
| Commercial repeatability | Time to first reconciled month, migration defects, onboarding hours, weekly active finance users and design-partner willingness to pay. |

Use the same synthetic or anonymized finance pack to compare TIQACC with the best relevant incumbent setup, including necessary add-ons. Include a duplicate import, missing evidence, partial foreign-currency settlement, reopened period, dimension restructuring, access-restricted payroll aggregate and intercompany mismatch. Measure completion and implementation effort rather than slide-deck features.

Before internal production acceptance, require:

- One full accounting cycle in parallel, reconciled with all differences explained in writing, as required by page 120, section 2.16.4.
- No open critical or high defects for the accepted scope.
- Signed migration tie-outs for opening TB and relevant subledgers.
- Successful permission, isolation, retry, approval/edit race and close/post race tests.
- Demonstrated backup/restore, evidence export and operational ownership.
- A supported-scenario catalogue that clearly states the first release's boundaries.

**17. The immediate decisions to take into kickoff are concrete.**

Confirm the first internal entity and external customer segment; the first jurisdiction and accounting framework; named banks and integrations; whether recording payments or initiating them is in scope; the first supported tax and currency scenarios; migration history depth; the release exclusions; the commercial tenancy/residency model; staffing and budget; and the Finance/Product owners who resolve D01-D24.

Then build the smallest complete journey that proves the product promise: a source transaction becomes approved accounting, reconciles, reaches a financial statement, and remains explainable from evidence after the organization changes.

The elegant solution is the one that makes this difficult work feel coherent and dependable. Its long-term advantage will come from financial correctness, usable evidence, controlled change, local operational fit and repeatable deployment, with a disciplined expansion of scope.


