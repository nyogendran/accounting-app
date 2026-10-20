# TIQACC Engineering System — Architecture and Operating-Model Review

Oct 20, 2026 · @Yogi

**Recommendation: approve the extended framework in a leaner form.** One human approval per decision, recorded on the git host under an identity no agent holds, and mirrored into the repository. Persistent accounting knowledge lives in a governed knowledge base, not in agent memory. Traceability and evidence run as deterministic tools, and lifecycle states are computed from evidence, never asserted.

Re-inspected on 20 October 2026: the repository is now under git, with one commit and no remote, and still has no Claude Code configuration. Nothing has been changed. An independent adversarial review of the first draft found 25 problems, including approvals an agent could write and a misquoted acceptance clause; this version fixes them. This review is Proposed, not approved.

## Terms used here

| Term | Meaning |
| --- | --- |
| L0 to L7 | Product lifecycle phases from the bootstrap plan: L0 framework, L1 discovery, L2 requirements assurance, L3 architecture and design, L4 UX and test specification, L5 build, L6 release readiness, L7 improvement |
| Gates | Gate 0 ends L0. Gate A (requirements baseline) ends L2. Gate B (architecture and stack) ends L3. Gate C (implementation readiness) runs per increment. Gate D (internal release) ends L6 |
| F0 to F6 | Phases for building this framework (section F) |
| Stage 0 to 3 | Strength of the approval channel (section E) |
| Tier 1 to 3 | Risk tiers. Tier 1: posting, numbering, periods, audit, authorisation, isolation, money and rounding, financial data migration. Tier 2: module logic, APIs, integrations. Tier 3: presentation, documentation, tooling |
| E1, E1-op, E2, E3, E4 | Evidence levels (A5) |
| Integration | A service someone else runs that needs our credentials: git host, CI service, issue tracker, chat |
| Infrastructure | Something we must set up and run ourselves: self-hosted runners, an evidence archive, a bot endpoint |
| Bootstrap plan | The framework plan proposed on 19 October 2026, not yet approved |
| Stack ADR | The architecture decision record that chooses the technology stack, at Gate B |
| Void, at risk, stale, disputed, pending | Void: an approval whose hash no longer matches. At risk: an approval whose upstream dependency changed, awaiting impact analysis. Stale: evidence from a commit other than the one asked about. Disputed: an agent's claim contradicted by tool evidence. Pending: awaiting a named person's decision |

## A. Critical assessment

Proposals 1 to 4 keep their goals but need a different mechanism; proposals 5 to 8 are adopted with additions. None needs a database server or an always-on service at this stage.

| # | Proposal | Verdict | What changes |
| --- | --- | --- | --- |
| 1 | Persistent Accounting Domain Expert | Keep the goal, change the mechanism | Persistence moves into a governed, versioned knowledge base. The agent stays stateless and merges with the accounting agent already planned |
| 2 | Dual Product Owner approval | Reject the mechanism, keep the goal | One approval, the human's. The product lens becomes a decision brief, not a second approver; a separate AI reviewer stays optional (G1) |
| 3 | Closed-loop defect management | Keep the goal, change the mechanism | An independent agent classifies and a person confirms severity. The requirements agent authors changes but does not judge its own requirements |
| 4 | Requirements agent as central coordinator | Reject the mechanism, keep the goal | A requirements steward backed by a deterministic trace tool; workflow coordination stays with the orchestrator |
| 5 | Evidence-based engineering | Adopt, strengthened | States are computed at a named commit, and each names the evidence level it rests on |
| 6 | Queryable knowledge system | Adopt, minimal | Git, one-file-per-record ledgers and a generated index; adopt an existing requirements-as-code tool where one fits |
| 7 | Governance and failure handling | Adopt, extended | A control matrix that says when each control starts working; agents get their own identity so they cannot approve |
| 8 | Operating model | Adopt, revised | 10 agents (two reshaped), 3 tools plus evidence collectors, and an authority matrix of named people |

**Benefits, limits, prerequisites and decisions per proposal.** The sections below give the assessment and recommended approach in detail.

| # | Main benefit | Main limitation or risk | Depends on | Your decision |
| --- | --- | --- | --- | --- |
| 1 | Knowledge survives sessions, staff and model changes; answers cite approved sources | Only as current as its last reviewed update; the agent is not a qualified accountant | F0 tools; a named accountant; approved policies to learn from | G2, G5 |
| 2 | One accountable decision per version, with a brief that saves the PO's time | The PO's throughput becomes the bottleneck; non-technical approvers need readable briefs, not diffs | Approval requests and hashing (F0); a git host and a separate agent identity (F2) | G1, G2, G4 |
| 3 | Requirements stay true after release; every confirmed defect leaves a regression test | Production and customer intake need external systems; classification depends on trace quality | An issue tracker; CI (F4); trace links | G3 |
| 4 | One accountable owner for intent questions; reproducible answers | Answers are only as complete as the trace links | The `trace` tool (F0); code annotations from L5 | G1 |
| 5 | No state claims more than its evidence level supports | Until CI exists, evidence is local (E3) and not release-grade | CI and the stack decision (F4, Gate B) | G3, G4 |
| 6 | No servers to run; history comes from git | Queries need tooling, built or adopted; evidence bodies need an archive | A git host with branch protection; an archive later | G3, G5 |
| 7 | Interruptions and integration failures cannot lose or duplicate decisions | Until the git host separates identities, agents and people share one OS account | Protected branch, CI checks, a bot identity for agents | G2, G4 |
| 8 | Clear authority; no more agents than the bootstrap plan, with overlap removed | 10 agents still cost tokens and time per change | All of the above | G1, G2 |

### A1. Persistent Accounting Domain Expert

Keep the goal, but put the persistence in a governed, version-controlled knowledge base, not in an agent. A Claude Code subagent starts every invocation knowing only what it reads from files, so anything it "learned" before survives only if it was written down and approved.

| Option | Verdict | Why |
| --- | --- | --- |
| Specialized subagent alone | Necessary, not sufficient | Stateless between invocations; knowledge is lost unless re-read from files |
| Persistent knowledge service (always on) | Not justified | Hosting, authentication, uptime and a second source of truth, with no capability the repository lacks |
| Version-controlled accounting knowledge base | Core | Reviewable diffs and point-in-time history through git; survives model upgrades and staff changes |
| Retrieval-augmented generation over a vector index | Not now | Adds an embedding model (a second data processor, or a local model to run), index sync, and non-authoritative fragments. Exact search over IDs covers this corpus. Revisit only if the C6 benchmark shows misses exact search cannot fix |
| Combination | **Recommended** | Stateless agent + governed knowledge base + deterministic trace index + exact search |

**Recommended design**

- **One agent**, `accounting-domain-expert`, replacing the accounting agent in the bootstrap plan: analysis on request, and stewardship of the knowledge base. A second accounting agent would duplicate judgment and split ownership.
- **Knowledge base** under `docs/accounting/knowledge/`. Normative kinds need the qualified accountant's approval: policies (POL), rules (ACR), invariants (INV) and the expected results of scenarios (SCN). Supporting kinds: concepts, glossary, jurisdiction notes, open questions.
- **Two separate labels per entry.** A stored decision status (Proposed, Approved, Rejected, Superseded), and a derived verification state (scenario tests pass at a commit, contradicted, or unverified). Knowledge entries never reuse requirement states such as Specified.
- **The expert reasons only from approved entries and specification clauses.** Its own Proposed interpretations can raise questions, never support a finding.
- **Executable scenarios.** Approved scenarios run as tests, checking the code against the approved knowledge on every CI run from F4. They test the code, not the policy.
- **Learning is a promotion workflow** (C8): an event with evidence, a drafted change, citations the checker can resolve, review, and a person's approval to merge.
- **Agent memory stays off.** Claude Code's per-agent memory lets an agent write notes that load into its next run. Project-scope memory sits in the repository, so git shows its changes, but nothing requires a review before the notes load. The orchestrator's auto memory works the same way and should be off for this project too (G6).

| Category | What it covers |
| --- | --- |
| Feasible now in Claude Code | The agent, knowledge-base structure, citation and status checks, promotion workflow, exact search |
| Needs external integration | Production reconciliation and incident evidence from monitoring and finance operations |
| Needs additional infrastructure | None now. Optional later: a vector index (index store and sync job) |
| Needs human oversight | A qualified accountant approves normative entries; a person approves every merge; people settle inconsistencies |

**Risks.** Knowledge debt: the knowledge base lags the code; mitigate by making its update part of "done" for any change touching accounting. False authority: fluent answers read as approved; mitigate with mandatory status labels and quoted citations, and "no evidence found" as a valid answer. The agent is not a qualified accountant and cannot become one.

**Decisions for you:** who the qualified accounting reviewer is (G2); whether a second data processor for embeddings is ever acceptable (G5).

### A2. Dual Product Owner approval

Reject the second approval and keep the goal. An AI "Product Owner" carries no accountability, and labelling its output an approval invites people to defer to it. Keep one approval, the human's, and give that person a better brief.

**Why not two approvals**

- **Automation bias.** Reviewers anchor on an earlier "approved" verdict, which weakens the human review it was meant to support.
- **Overlap.** Completeness, consistency and acceptance criteria are already Requirements Assurance's job; value and priority are the human PO's.
- **No data.** An AI reviewer has no usage, revenue or customer data, so its value judgments mostly restate the stated objectives.
- **Approval fatigue.** Individual approvals for every low-risk story train people to click through.

**Recommended design**

- **The product lens goes into the work, not into a new agent.** The Requirements Steward states each story's value and links it to a business objective; Assurance checks that rationale for consistency; the orchestrator's decision-brief skill presents value, scope, usability questions and risks to the PO. G1 offers a separate advisory Product Reviewer agent if you want an AI challenger.
- **The decision brief** is one page, readable without git: what is being decided, the options, the recommendation, open risks, and the version and hash being approved.
- **Human decisions:** Approve, Reject, Request changes, Defer, or Escalate to the authority named in A8. Each is recorded against an approval request that pins every artifact's ID, version and content hash.
- **Limits of PO authority.** The PO decides scope and priority, not accounting policy or security controls. A PO decision that conflicts with an approved policy goes to that policy's owner.
- **AI–human disagreement** is recorded beside the decision. The human decision stands; the AI's note stays on file.

**When an approval stays valid**

- The content hash decides validity; the commit is recorded only as provenance.
- The hash covers normative fields: the statement, acceptance criteria, business rules, and trace links such as `governed_by` and `derives_from`. It is computed on a canonical form (parsed fields, normalised whitespace and line endings), so reformatting does not void an approval.
- Priority sits outside the hash. It is approved in the backlog or release package, so reordering the backlog never voids a story.

| Change after approval | Effect |
| --- | --- |
| Normative content or trace links | The approval is void automatically |
| Editorial content outside normative fields | No reapproval; the change is logged |
| An upstream dependency changes: policy, ADR, parent requirement | The approval is at risk; the PO decides, using the impact analysis (C5), whether to reapprove |
| The approver changes their mind | A revocation or newer decision is recorded; the approver's latest decision counts, and both stay on file |

| Category | What it covers |
| --- | --- |
| Feasible now | Approval requests, hash binding, readiness checks; your decisions captured by a hook in the VS Code session (E1-op, A5) |
| Needs external integration | Authenticated approvals on a git host; Teams or Slack notifications and actions (E) |
| Needs additional infrastructure | None for git-host approvals; a bot service only if chat buttons must record decisions themselves |
| Needs human oversight | Every decision; naming the PO and a delegate |

**Decisions for you:** a brief or a separate agent for product review (G1); who the PO and delegate are (G2). Approval granularity: batches for Tier-3 stories, individual approval for Tiers 1 and 2 (recommended).

### A3. Closed-loop requirements and defect management

Keep the closed loop, but don't let the requirements agent judge its own requirements, and don't let any agent set the severity a release gate depends on. Deciding whether a fault lies in the code or in the requirement is a conflict of interest for the requirement's author, in either direction.

| Step | Owner | Why this owner |
| --- | --- | --- |
| Intake and deduplication | Orchestrator, in a scheduled intake sweep | One register (`ISS`); once a tracker exists it owns intake, status and assignee |
| Reproduce: observed versus expected, with evidence | Quality engineer | Independent of author and implementer |
| Classify against the approved baseline at a stated version | Requirements Assurance | The independent challenger |
| Confirm severity Critical or High, any downgrade, and any "not a defect" | A named person (A8) | The release gate depends on it |
| Find affected requirements; author any change request | Requirements Steward | Owns requirement text and its trace |
| Assess financial impact | Accounting Domain Expert | Mandatory for Tier-1 areas and financial data |
| Assess technical impact | Architect or technical designer | Design and data consequences |
| Approve a requirement change | Human PO, plus the accountant for policy | Authority |
| Write the failing regression test | Quality engineer | Test first, independent of the fix |
| Fix | Implementation engineer | Implements against the failing test |
| Verify and close | Quality engineer and a human reviewer | Evidence, not assertion |

**Classification and routing**, one class per issue:

- Implementation defect: fixed through C3.
- Specification defect or requirement gap: a change request (C4).
- New capability: the backlog, for the PO to prioritise.
- Change request: C4.
- Architectural concern: the architect, with an ADR if needed.
- Operational issue: DevOps.
- Not a defect: a person confirms, and the reporter is told why.

**Severity** (proposed scale, to be approved at Gate A). Critical: a financial misstatement, data loss or exposure, or a blocked core process with no workaround. High: wrong behaviour in a core process with a workaround, or a weakened control. Medium and Low otherwise. Agents propose; a person confirms Critical, High and every downgrade.

**Rules enforced by tooling, not by instruction**

- Behaviour that violates an approved requirement is an implementation defect unless an approved change request says otherwise. The classification record must cite the requirement version and the observed evidence.
- An Approved requirement's normative text cannot change without a linked, approved change request. The checker enforces this from F0, and branch protection from F2.
- Root cause has three states: Suspected, Confirmed, Not determined. Confirmed needs a test that fails before the fix and passes after, plus a reviewed causal explanation.

**Automated impact discovery** is described in C5: trace traversal gives a Linked set, search gives a Suggested set, and every impact dimension has an owner.

**Intake when no session is running.** Incident response is a human, on-call process; its record enters the register afterwards. The orchestrator runs an intake sweep on a fixed schedule (proposed: daily during L5).

| Category | What it covers |
| --- | --- |
| Feasible now | Issue records, classification protocol, trace traversal, regression-test rule, checker enforcement |
| Needs external integration | An issue tracker and a CI service; production incident, support and monitoring feeds |
| Needs additional infrastructure | None beyond what those services bring |
| Needs human oversight | Severity confirmation, change approval, policy decisions, risk acceptance, closing Tier-1 issues |

**Decision for you:** which issue tracker becomes the intake system (G3).

### A4. Requirements Engineering Agent as knowledge coordinator

Reject the coordinating role and keep the goal. Make the requirements agent the steward of requirements knowledge, not a second workflow coordinator; the central piece should be a deterministic trace index that any agent or person can query.

**Why not a central coordinating agent**

- Two coordinators, the orchestrator and the requirements agent, blur who started, paused or advanced a workflow.
- In the proposed configuration, subagents cannot start other subagents. This is deliberate: one place of control and one audit trail. "Asking another agent" therefore means asking the orchestrator to dispatch it, or reading that agent's published artifacts.
- An agent's recall is not evidence. A trace query over versioned artifacts is reproducible; an agent's summary of it is not.

**Recommended design**

- **Requirements Steward** (file still `requirements-engineer`): owns requirement artifacts, requirement-side trace links and change requests, and answers questions about intended behaviour.
- **It runs `trace` and `check` itself**, through allow-listed read-only commands. The central hook blocks any other shell command from this agent. Interpretation, such as "does this code implement the rule's meaning?", goes back through the orchestrator to the right specialist.
- **Fixed evidence chain** for "how is X implemented?" (C6). Each link is marked verified, present but unverified, stale, or missing. A chain with a missing link is reported as incomplete, never as complete.
- **Lifecycle states are computed** by the tool from evidence (A5), never asserted by the agent.

| Category | What it covers |
| --- | --- |
| Feasible now | The trace tool; evidence-chain answers up to "Tested, local" |
| Needs external integration | "Deployed" and "Operationally verified" need CI/CD and monitoring evidence |
| Needs additional infrastructure | None |
| Needs human oversight | None to answer a question; answers are advisory and cite their evidence |

### A5. Evidence-based engineering

Adopt, and make it machine-checkable. Three risks matter most: agents writing or overstating evidence, citations that resolve but do not support the claim, and evidence from one commit being read as true for another.

**Evidence levels**

| Level | Source | Can establish |
| --- | --- | --- |
| E1 | A person's decision on an authenticated account that no agent holds (git host, single sign-on) | Approvals, risk acceptances, human review |
| E1-op | Operator-attested: an approval phrase you type in the Claude Code session, captured by a hook rather than written by an agent | Approvals in Stage 0, never for Tier 1, and re-confirmed when Stage 1 starts |
| E2 | Generated by CI: run ID, commit, stored artifacts | Built, tested, scanned, deployed |
| E3 | Captured locally by the evidence wrapper or a hook: command, exit code, tree hash, and whether the tree was clean | Supporting evidence; never release-grade |
| E4 | An agent's statement, including an agent's review | Nothing on its own |

**Stored status versus derived states.** An artifact stores one authoring status: Draft, In review, Proposed, Approved, Rejected, Deferred or Superseded. The checker accepts Approved only with an unrevoked decision record on the current normative hash; otherwise it reports the approval void. Everything in the next table is derived by `trace` and never stored:

| Derived state | Established by | Level |
| --- | --- | --- |
| Specified | The behaviour is described in an approved requirement, story or accounting rule at its current hash | E1 or E1-op |
| Implementation claimed | A code annotation for the ID exists at commit C | Checker on an E4 claim |
| Implemented | A linked test that executes the annotated code passed at C | E2 (E3 gives "Implemented, local") |
| Tested | Every acceptance criterion of the item has at least one linked test, and all passed at C. No linked tests means Not tested | E2 (E3 gives "Tested, local") |
| Agent-reviewed | An agent's review record covers the change set at C | E4 |
| Reviewed | A person approved the pull request containing C | E1 |
| Deployed | C is an ancestor of the build running in environment X, and no rollback has removed it | E2 |
| Operationally verified | A post-deployment check or reconciliation for that build passed in X | E2 |

The states are independent, and each is evaluated at a named commit (and environment, where it applies). Evidence from another commit is stale and does not carry over. Approvals are the exception, because they bind to content hashes. Contradictions are flagged as anomalies, for example Implemented while the approval is void.

**Citations must resolve and support.** A citation is one of: artifact ID and version; file path, commit and symbol; test ID and run ID; approval ID; build or release ID. The checker reports any citation it cannot resolve. A citation for a factual claim also carries the quoted words, so a reviewer can check that the source actually supports it.

**What the system never infers:** a green build is not correctness; a passing test is not a valid policy; an approval is not a deployment.

**Evidence minimums by risk tier**

| Tier | Before merge | Before release |
| --- | --- | --- |
| Tier 1 | E2 tests for every acceptance criterion and scenario; agent review; human review (E1); the accountant's sign-off where policy is touched | Operational verification in a test environment |
| Tier 2 | E2 tests for every acceptance criterion; agent review; human review | E2 regression run |
| Tier 3 | E2 or E3 tests; agent review; human approval may cover a batch | E2 regression run |

| Category | What it covers |
| --- | --- |
| Feasible now | Citation resolver, hook capture (E1-op, E3), derived states up to "Tested, local" |
| Needs external integration | E1 identity on a git host; E2 from a CI service; deployment and monitoring evidence |
| Needs additional infrastructure | An evidence archive with retention, once evidence must outlive the CI service's retention |
| Needs human oversight | Approvals, human reviews, and exceptions where evidence is missing or contradictory |

### A6. Knowledge system

Use git as the single source of truth for artifacts and decisions, and generate the index from it. The assumed scale, low thousands of artifacts plus a growing evidence stream, doesn't justify a database server; re-check that assumption after release 1.

| Option | Benefit | Cost and burden | Verdict |
| --- | --- | --- | --- |
| Git: Markdown and YAML artifacts, one file per ledger record | Authoritative, reviewable, history for free; branches never conflict on records | Needs a query tool; unsuitable for large evidence bodies | **Core** |
| Existing requirements-as-code tools: Doorstop, StrictDoc, Sphinx-Needs, OpenFastTrace | Proven linking, coverage reports and change detection | Their own formats and limits; fit untested | **Evaluate in F0 before building `trace`** |
| Generated index: in-memory graph, optional SQLite file | Typed queries and traversal; rebuildable at any commit | Code to maintain, if no tool fits | Core, adopted or built |
| Graph database | Rich traversal and visual exploration | Server operations, sync from git, a second source of truth, duplicated access control | Not now. Revisit if several products share one graph or many people need a live query interface |
| Relational database server | Concurrency and reporting | Same burden as a graph database | Not now; SQLite covers local queries |
| Vector index | Fuzzy discovery, such as "where do we round FX?" | A second data processor for embeddings (or a local model to run), sync, non-authoritative results | Optional later; every hit resolved to its source artifact |
| Document platform (Confluence, SharePoint) | Easy reading for business users | Drift if anyone edits there | Publish-only view, if wanted |
| Evidence archive (object storage) | Long retention for evidence bodies | Cloud account, retention policy | With CI (F4) |

Build only what nothing else covers. That is most likely the approval binding (requests, normative hashing, decision capture) and the glue between tools.

**Historical questions.** "What was approved on date T, and on what evidence?" comes from decision records ordered by ledger sequence and the git host's merge time, the artifact content at each approval's hash, and the evidence each request pinned. Git holds decisions and metadata; evidence bodies stay in CI or the archive, referenced by digest, so their retention matters.

**Decided versus in force.** Policies, rules and requirements carry `effective_from` and `effective_to`. "What was decided as of T" and "what was in force for accounting period P" are separate questions: a tax rate approved in October may apply from 1 January.

**Authority rule.** Generated summaries, index output and search hits are never cited when the original artifact exists. Each summary records the commit it was generated from, and the checker flags it once its sources change.

**Access and audit.** Git host permissions and branch protection control who can change what; git history and the host's audit log show who did. Production financial data never enters the repository: evidence stores references and digests instead (A7).

| Category | What it covers |
| --- | --- |
| Feasible now | Git storage, one-file ledger records, index generation, the tool evaluation |
| Needs external integration | A git host, for protected history and trustworthy merge times |
| Needs additional infrastructure | Nothing now; an evidence archive from F4 |
| Needs human oversight | Choosing a tool to adopt; approving changes to record formats |

### A7. Governance, security and failure handling

Every listed failure gets a prevention, a detection and a recovery, and the matrix says when each control starts working. Until the git host exists (F2), agents and people share one OS account, so controls before then are best effort.

| Failure | Prevent | Detect | Recover | Active from |
| --- | --- | --- | --- | --- |
| Conflicting agent conclusions | Distinct scope per agent | A dispute record opens when findings conflict | Evidence settles facts; policy goes to the named owner; never a majority vote | F0 |
| Incorrect or hallucinated information | Quoted, resolvable citations | Checker resolves citations; reviewers check the quotes support the claim | Claim marked disputed; issue opened | F0 |
| Stale documentation | Derived documents record their source versions | Checker flags changed sources | Regenerate, or re-review if normative | F0 |
| Unapproved specification change | Write-guard hook; branch protection and code owners | Checker: a normative change to an Approved artifact without a change request | Revert, or raise a change request | F0 hook; F2 host |
| An agent writes or fakes an approval | Agents cannot reach approval records; agents commit as a bot that cannot approve; your token never enters agent sessions | Checker rejects decision records without a hook or git-host attestation; a FileChanged hook flags any write to them | Remove the record; incident record | F0 best effort; F2 enforced |
| An agent writes outside its scope through the shell | The central hook limits each agent's shell commands by agent name | A commit-time check maps changed paths to the agent named in the commit trailer | Revert | F0 pre-commit; F2 CI |
| Missing approval record | Approved status requires a decision record | Checker and gate review | Item stays Proposed | F0 |
| Partial or failed integration | Requests written to an outbox before sending | Reconciliation compares outbox, platform and ledger | Idempotent retry; fall back to the git host or Stage 0 | F5 |
| Duplicate or delayed approval event | De-duplication on the source event ID | A second copy of the same event is ignored | A late decision on an outdated hash is recorded as stale, and the approver is told | F2 |
| Concurrent modification | One owner per artifact; branches and pull requests; one file per record | Merge conflict; checker on merge | Owner resolves; orchestrator serialises overlapping scopes | F0 |
| Wrong requirement-to-code link | Typed, validated links; Implemented needs a test that executes the code | Checker; Assurance samples links each increment | Fix the link; open an issue if behaviour is affected | L5 |
| Agent failure or interrupted workflow | Workflow record; idempotent steps | Orchestrator compares records with the tree on resume | Resume from the last completed step; never re-run an approval | F0 |
| Sensitive financial or production data | Classification rules; synthetic test data; secrets in a vault; web tools only for research roles | Secret and personal-data scanning, pre-commit then CI | Purge from history under an incident record; rotate secrets | F0 pre-commit; F4 CI |
| Unauthorised change to audit records | Records never edited after merge; protected branch; signed gate tags | Checker, then CI, fails if a merged record changes | Restore from history; incident record | F0 checker; F2 CI |
| Human override or emergency fix | Break-glass: a named approver and an emergency change request | Records flag break-glass use | Retrospective review, tests and approvals within a fixed period (proposed: 5 working days) | F0 |

**Always needs a human, even when every automated check passes**

- Changes to posting, numbering, period-close, rounding or reversal logic.
- New or changed accounting policies, and tax or statutory rules.
- Migrations or corrections that touch financial records.
- Changes to authorisation, segregation of duties, audit logging or tenant isolation.
- Production deployments and rollbacks.
- Changes to the framework itself: agents, hooks, permissions, checker, record formats.
- Accepting a risk, or waiving a gate criterion.

**AI output stays distinguishable.** Agents commit under a bot identity with an `Agent:` trailer naming the role; people commit under their own accounts. The checker rejects decision records that lack a hook or git-host attestation.

| Category | What it covers |
| --- | --- |
| Feasible now | Hooks, checker, pre-commit checks, workflow records, break-glass procedure |
| Needs external integration | Git host (protected branch, code owners, bot identity); CI service |
| Needs additional infrastructure | A secrets vault if CI secrets are not enough; nothing else now |
| Needs human oversight | Every break-glass use; risk acceptances; the high-risk actions above |

### A8. Operating model

Reshape two agents and add none by default. Put traceability, evidence and approvals into deterministic tools, and put authority in a matrix of named people rather than in agent roles.

| Element | Change from the bootstrap plan |
| --- | --- |
| Orchestrator (main session) | Still the only workflow coordinator. Adds workflow records, a resume protocol and a scheduled intake sweep. Never approves and never writes decision records |
| Requirements Steward (was requirements engineer) | Adds intent questions, a value rationale for each story, requirement-side trace stewardship and change requests. Loses defect classification. Shell limited to `trace` and `check` |
| Requirements Assurance | Adds defect classification and sampling audits of trace links |
| Accounting Domain Expert (was accounting domain) | Merges analysis with knowledge stewardship. Reasons only from approved entries; proposes, never approves |
| Product Reviewer | Optional (G1); not created by default |
| Quality engineer | Adds defect reproduction, regression tests for confirmed defects, and CI evidence |
| Code and Security Reviewer | Adds citation and evidence checks; files security findings as issues. Its reviews are E4; human review is separate |
| Architect, designer, UX, implementation, DevOps | Add evidence duties: code annotations, design links, deployment records |

**Created when needed.** In F0: the Steward, Assurance, the Accounting Domain Expert, and the Code and Security Reviewer, which reviews the framework's own code. At Gate A: the architect and technical designer. At Gate B, once the stack is known: UX, quality, implementation and DevOps.

**Deterministic tools, not agents.** `check` covers validation, status rules, citations and readiness. `trace` covers the index, explain, impact, coverage and point-in-time queries, adopted or built (A6). `approvals` covers requests, hashing, decision capture, and stale and void detection. Evidence collectors are a local test wrapper and session hooks now, CI reporters later.

**Authority matrix** (names to be filled in under G2)

| Decision | Role, with a named delegate | Escalates to | Must not also be |
| --- | --- | --- | --- |
| Requirement scope and priority; acceptance of business outcomes | Human PO | The specification's approver (§3: Managing Director) | The change's author |
| Accounting policy, normative knowledge, accounting-risk acceptance | Qualified accountant | Finance Manager, with Internal Audit informed | The PO, for Tier-1 policies |
| Tax and statutory rules per jurisdiction | Tax or compliance specialist | Qualified accountant | None |
| Architecture and stack | Tech lead | The PO, where cost or scope is affected | None |
| Security exceptions | Security owner | Managing Director | The change's author |
| Internal release (Gate D) | Release authority | PO and tech lead jointly | Author of Tier-1 changes in that release |
| Customer module acceptance (spec §2.16.4) | The customer's §3 signatories: Finance Manager, Internal Audit, Managing Director | The contract | Anyone on the delivery team |
| Correction of a tenant's posted data | The tenant's authorised finance approver, plus the accountant for closed periods or filed returns | Tenant management | Whoever caused the error |
| Changes to this framework | Tech lead, with you as governance owner | None | The agent that proposed the change |

**Small-team fallback.** If one person must hold several roles, the matrix records it. Tier-1 policy approvals and Tier-1 releases still need a second named person, external if necessary.

**Rejected:** a separate traceability agent, because a tool does this more reliably; two accounting agents; agent-to-agent calls; a graph or vector database at this stage.

| Category | What it covers |
| --- | --- |
| Feasible now | Agent definitions, tools, the authority matrix as a version-controlled file |
| Needs external integration | Git host accounts for each named person and a bot identity for agents |
| Needs additional infrastructure | None |
| Needs human oversight | Naming the people; approving changes to the matrix, which needs two approvers |

## B. Target architecture

Authority sits with named people, truth sits in the git repository, judgment sits with stateless agents, and checking sits with deterministic tools. External systems add identity, CI evidence, intake and notifications, but never a second source of truth.

| Layer | What it is | Holds authority? | How it persists |
| --- | --- | --- | --- |
| People | The roles in the authority matrix (A8) | Yes, for their own decisions | Decision records captured by a hook or the git host |
| Orchestrator | The main Claude Code session in VS Code | No | Through workflow records only |
| Agents (10) | Role definitions in `.claude/agents/`, stateless per invocation | No | Only through artifacts they write inside their scope, committed under the agent bot identity |
| Deterministic tools | `check`, `trace`, `approvals`, evidence collectors | No; they enforce rules | Output is reproducible from the repository |
| Authoritative store | Git: specifications, knowledge base, ADRs, designs, tests, code, records | Records decisions | Yes, with full history |
| Generated views | Index, reports, summaries | No; never cited when the source exists | Rebuilt on demand |
| External systems | Git host, CI service, issue tracker, Teams or Slack, monitoring, evidence archive | Supply identity (git host, single sign-on) | Their events are mirrored into records |

**Agent roster** (target state; when each is created is in A8)

| Agent | Writes | Reviews | Never | Shell | From, then to |
| --- | --- | --- | --- | --- | --- |
| Requirements Steward | `docs/requirements/`, except assurance | Nothing | Classifies defects; approves | `trace`, `check` only | Orchestrator, then Assurance and the accounting expert |
| Requirements Assurance | Assurance reports, issue classifications | The Steward's work, claims in prior analyses, defect classification | Edits requirements | `trace`, `check` only | Orchestrator, then the Steward |
| Accounting Domain Expert | `docs/accounting/` | Accounting effect of requirements, designs, tests, code | Approves policy; relies on its own Proposed entries | `trace`, `check` only | Orchestrator, then the Steward |
| Solution Architect | `docs/architecture/` | Design and code conformance | Changes an approved ADR without a change request | `trace`, `check` only | Orchestrator, then the designer |
| Technical Designer | `docs/design/` | Nothing | Decides architecture | `trace`, `check` only | Architect, then quality and implementation |
| UX Designer | `docs/ux/`, prototypes | Flows against rules, with the accounting expert | Defines business rules | Prototype tooling | Steward, then quality |
| Quality Engineer | `docs/quality/`, acceptance and regression tests | Test adequacy | Weakens a test to make it pass | Yes | Steward and designer, then implementation |
| Implementation Engineer | Source code, migrations, unit tests | Nothing | Edits acceptance tests; invents rules | Yes | Quality engineer, then the reviewer |
| Code and Security Reviewer | Review records | Code, tests, CI, framework tools | Edits what it reviews | Yes, read-only use | Implementation, then the orchestrator |
| DevOps and Release | CI/CD, `docs/operations/` | Nothing | Deploys without an approval | Yes | Orchestrator, then the reviewer |

**What each kind of thing is for**

- **Agents** apply judgment: drafting, analysing, reviewing. They propose and never decide.
- **Authoritative artifacts** are what the organisation has decided, at a version.
- **Persistent knowledge** is the knowledge base, the records and git history, not any agent's memory. Claude Code's auto memory is turned off for this project (G6).
- **Automation** checks, computes and records, the same way every time.
- **External integrations** bring identity, CI evidence, intake and reach, and are mirrored back into the repository.

**Interaction rules**

1. Only the orchestrator dispatches agents. Agents return reports and write only inside their scope: a hook guards file edits and shell commands by agent name, and a commit-time check backs it up.
2. Only tools write derived state. Decision records come only from people: a hook-captured phrase in Stage 0, then the git host from Stage 1. Agents may draft approval requests, never decisions.
3. External events (approvals, CI runs, deployments) are mirrored into the repository as records with their source IDs. The repository can then answer historical questions about decisions and metadata; evidence bodies stay in CI or the archive, referenced by digest.
4. When a tool and an agent disagree, the tool's evidence wins and the agent's claim is recorded as disputed.

&#91;embedded content: target architecture · who acts on what\]

Only people create approval decisions. Agents write only inside their own scope, and every external event is mirrored into the ledgers, so the repository alone can answer historical questions.

## C. End-to-end workflows

Each workflow runs from a record the orchestrator opens (WF), so it survives interruption. No workflow advances on an agent's claim alone.

### C1. Create and approve a user story

A story becomes eligible for implementation only when the Human PO has approved the exact version that every mandatory review examined.

1. The orchestrator opens a workflow record and briefs the Requirements Steward with the source clauses, objectives and policies.
2. The Steward drafts the story, its value rationale linked to an objective, Given/When/Then acceptance criteria and trace links: status Proposed, version 1.
3. `check` validates IDs, links and required fields.
4. Two mandatory reviews run in parallel against version 1's hash. Assurance covers quality, contradictions, testability and the consistency of the value rationale. The Accounting Domain Expert covers financial effect and open policy questions. Each writes a review record.
5. The Steward revises. Any normative change re-runs every mandatory review on the diff, so all reviews end bound to the same final hash.
6. The orchestrator's decision-brief skill assembles the approval request: pinned versions and hashes, review dispositions, and a one-page brief on value, scope, usability questions and risks.
7. The Human PO, or the named delegate, decides: Approve, Reject, Request changes, Defer or Escalate.
8. The decision is captured, by a hook in Stage 0 or by the git host from Stage 1, and `trace` recomputes readiness.

**Ready for implementation** means all of these hold:

- The approval's hash matches the current normative content.
- Every mandatory review is bound to that hash, with no open blocking finding.
- No blocking question or issue is open.
- Every governing policy and rule is Approved.
- Every acceptance criterion has a planned test.
- The risk tier is set.

Implementation also needs Gate C for its increment.

| Aspect | Detail |
| --- | --- |
| Inputs | A release-scope item or approved change request; source clauses; objectives; approved policies |
| Responsible | Steward (author); Assurance and the Accounting Domain Expert (reviewers); orchestrator (flow and brief) |
| Outputs | Story at version N, review records, approval request with brief, captured decision |
| Approval | Human PO or delegate; also the qualified accountant if a policy decision is embedded |
| Evidence | Review records bound to the final hash; the approval request; a decision record with identity and channel |
| Failure handling | A reviewer fails: one retry, then escalate. Reviewers conflict: a dispute record. PO unavailable: the delegate decides; with neither, the story stays Proposed, never approved by timeout. Content changes after approval: the approval is void |
| Complete when | The readiness conditions above hold |

### C2. Resolve an accounting policy question

Only a qualified accountant's recorded decision closes a policy question; until then, dependent Tier-1 work cannot start.

1. The question is registered (Q-nnn) with the work it blocks.
2. The Accounting Domain Expert analyses the options: relevant spec clauses, standards and jurisdiction references (cited, and flagged as needing professional validation), worked journals for each option, and a recommendation.
3. Assurance checks consistency with other policies and requirements.
4. The decision brief states the business impact where the options differ for users.
5. A decision brief goes to the accountant, plus the PO for business trade-offs and a tax or compliance specialist for statutory rules.
6. The decision is recorded, and policy POL-nnn becomes Approved at version N.
7. The knowledge base is updated (C8). Affected requirements change through change requests, and scenario tests are added.

| Aspect | Detail |
| --- | --- |
| Inputs | The question, the items it blocks, spec clauses, the current knowledge base |
| Responsible | Accounting Domain Expert (analysis); Assurance (consistency); orchestrator (flow) |
| Outputs | Policy analysis, policy at version N, knowledge-base change, change requests where needed |
| Approval | Qualified accountant, always; the PO and specialists as above |
| Evidence | Analysis with cited sources and access dates; worked examples; a ledger decision |
| Failure handling | No accountant available: the question stays Pending and Tier-1 work stays blocked. Tier-2 and Tier-3 work may proceed on a labelled assumption, with the accountant's risk acceptance and a design that can be reversed |
| Complete when | The policy is approved, the knowledge base is merged, dependents are updated or flagged, and scenario tests exist |

### C3. Report and fix a defect

Evidence closes a defect: a regression test that failed before the fix and passes in CI, plus verification where the defect was found.

**Issue states:** Reported, Triaged, Classified, In progress, Fixed (merged, with a passing E2 regression run), Verified (checked where it was found), Closed. Rejected and Duplicate end early, and both need a person's confirmation.

1. Intake: the issue (ISS) is recorded with its source, environment, version and evidence; duplicates are linked.
2. The quality engineer reproduces it, recording observed versus expected behaviour and the authoritative source of the expected behaviour.
3. Assurance classifies it against the approved baseline at that version and routes it as A3 describes.
4. Agents propose severity: the Accounting Domain Expert for Tier-1 areas or financial data, the Code and Security Reviewer for security. A named person confirms Critical, High, any downgrade and any "not a defect".
5. The quality engineer writes the failing regression test; the implementation engineer fixes it. Root cause is recorded as Suspected, Confirmed or Not determined.
6. Review by the Code and Security Reviewer, then by a person (E1). For Tier 1, the Accounting Domain Expert reviews as well.
7. The issue is Fixed when merged with a passing E2 regression run. A development defect is Verified at that point. A production defect is Verified only after the fix is deployed (C7) and checked in production.
8. If posted data was affected, it is corrected with new reversing or adjusting entries. The tenant's authorised finance approver signs, plus the accountant for closed periods or filed returns. Posted data is never edited.

| Aspect | Detail |
| --- | --- |
| Inputs | A report from any source, with evidence, environment and version |
| Responsible | Quality engineer (reproduce, test, verify); Assurance (classify); implementation engineer (fix); reviewers; a named person (severity) |
| Outputs | Issue record, regression test, fix commit, reviews, root-cause record, release link where relevant |
| Approval | Severity Critical or High, downgrades and "not a defect": a named person. Tier-1 fixes: the tech lead and accountant confirm the expected behaviour before merge. Data corrections: as in step 8 |
| Evidence | A failing run before the fix (E2 or E3), a passing E2 run after, a human review, and for production defects a deployment record and production check |
| Failure handling | Not reproducible: recorded with what was tried, and the PO decides whether to keep it open. A fix breaks other tests: tests are never weakened, and the issue reopens. Root cause unclear: closed as Not determined, with a person's sign-off |
| Complete when | Verified as in step 7; the issue links to test, fix, reviews and, for production defects, the release; the knowledge base is updated if knowledge changed |

### C4. Introduce a conflicting requirement

An explicit decision on a change request resolves a conflict. The system never silently picks one requirement, and never edits an approved one in place.

1. Assurance or `trace` detects the conflict with an approved requirement or policy. A change request (CR-nnn) opens, with a dispute record if agents disagree.
2. Assurance documents the competing interpretations and their consequences.
3. Impact analysis runs (C5).
4. Options are laid out with consequences: keep the current rule; adopt the new one; vary by configuration, jurisdiction or effective date; or defer.
5. The decision brief covers business effects, the Accounting Domain Expert policy effects, and the architect technical effects.
6. People decide: the PO, plus the accountant for policy and the tech lead for architecture.
7. The Steward writes the new requirement version. The old version becomes Superseded, with a link. Dependent approvals are flagged, and tests and designs are updated through tasks.

| Aspect | Detail |
| --- | --- |
| Inputs | The new request; the conflicting approved artifacts |
| Responsible | Assurance (detect, document); Steward (author); orchestrator (flow) |
| Outputs | Change request, impact assessment, decision, new versions, superseded versions |
| Approval | The PO, plus the accountant or tech lead as the conflict requires |
| Evidence | Impact assessment, decision brief, ledger decision |
| Failure handling | Decision deferred: both stay, the new one Proposed, and the conflict is a tracked blocker. Authorities disagree: escalate as the authority matrix (A8) names |
| Complete when | The change request is decided; every affected artifact is updated or explicitly waived; the trace is consistent; reapprovals are recorded |

### C5. Cross-artifact impact analysis

Impact analysis combines a deterministic trace traversal with search-based suggestions and labels every result by how it was found. It cannot be completed by marking dimensions "not assessed".

1. `trace impact <ID>` walks the typed links upstream and downstream. This is the Linked set.
2. Code discovery: symbols annotated with the affected IDs, references outward from them (a language server where available, text search otherwise), and files that historically change together (empty early in the project). This is the Suggested set.
3. Data: linked entities and migrations, and the effect on historical data. Posted records are immutable, so corrections are always new entries.
4. Each dimension has an owner and is marked assessed, not applicable (with a reason), or not assessed. "Not assessed" needs a named person's waiver and is never allowed for Tier 1.
5. The risk tier and the required approvals are derived from the affected artifacts.
6. A person reviews the assessment if the change is Tier 1, touches data, or has more Suggested items than Linked ones.

| Dimension | Owner |
| --- | --- |
| Business processes and users | Human PO |
| Accounting rules and financial controls | Accounting Domain Expert |
| Functional and non-functional requirements | Requirements Steward |
| Architecture and technical design | Architect |
| Data integrity, migration, APIs and integrations | Technical designer |
| Security and authorisation | Code and Security Reviewer |
| Automated and manual tests | Quality engineer |
| Existing customers and historical data | Accounting Domain Expert, with the PO |
| Deployment, rollback and operational support | DevOps |
| Documentation and approval dependencies | Orchestrator |

| Aspect | Detail |
| --- | --- |
| Inputs | The proposed change: change request, fix, ADR change, migration or dependency upgrade |
| Responsible | The orchestrator runs `trace`; the dimension owners above assess |
| Outputs | An impact assessment (IA) with Linked, Suggested and not-assessed sections |
| Approval | Waivers for any "not assessed" dimension; otherwise the assessment determines which approvals the change needs |
| Evidence | Tool output pinned to a commit; owners' sign-offs |
| Failure handling | Missing trace links: listed as gaps, with an issue to repair the trace. Tool failure: manual analysis, labelled manual |
| Complete when | Every dimension is assessed, not applicable, or waived by a named person outside Tier 1, and the required approvals are identified |

### C6. Answer "how is requirement X implemented?"

The answer is an evidence chain with every link marked. A missing link is reported as missing, never filled from general knowledge.

1. The Steward runs `trace explain <ID>` at HEAD, or at a stated commit, date or environment.
2. The Steward opens the key artifacts and code to confirm the links still say what the index says.
3. Where interpretation is needed (does the code implement the rule's meaning?), the orchestrator asks the Accounting Domain Expert or implementation engineer for a read-only review.
4. The answer follows a fixed chain: rule and its approval; requirement and its approval; story and acceptance criteria; design; code (symbol at commit); tests (latest run and result); reviews; issues and changes; deployment; operational verification; gaps and open questions.

| Aspect | Detail |
| --- | --- |
| Inputs | The question; optionally a commit, date or environment |
| Responsible | Requirements Steward |
| Outputs | An answer with its evidence chain; an issue if the answer exposes a defect or a broken trace |
| Approval | None |
| Evidence | Each link cites an ID at a version, a commit, a run or a record |
| Failure handling | Contradictory evidence: both are shown. Stale evidence: labelled stale, with its date. Nothing found: the answer says "no evidence" |
| Complete when | Every link in the chain is either evidenced or explicitly marked missing |

The same questions double as a benchmark. A person writes about 20 questions and their reference answers, pinned to a commit. They are re-run after framework or model changes to check that answers stay correct and fully cited.

### C7. Review and approve a release

An internal release (Gate D) and the customer's module acceptance (spec §2.16.4) are separate approvals with separate evidence. Neither carries over from one release candidate to the next.

**Internal release, Gate D**

1. DevOps builds the candidate from a commit. CI runs the tests, the accounting scenario suite, static analysis, security scans, a migration rehearsal including rollback, and a backup-and-restore check.
2. `trace` produces the release manifest: approved scope with derived states at that commit, open issues by confirmed severity, waivers, and evidence digests.
3. Reviews by the Code and Security Reviewer (readiness), the Accounting Domain Expert (invariants, reconciliation evidence) and Assurance (scope against the approved baseline), then by people.
4. Approval by the release authority and the PO; the accountant for Tier-1 financial scope; the security owner for a security exception. Any other exception needs the owner of that decision type (A8), recorded as a waiver.
5. Deployment runs through the pipeline's authenticated environment approval, and the deployment record and post-deployment checks are captured.

**Customer module acceptance, spec §2.16.4.** The specification gives no exception route:

- Each module is accepted separately against the acceptance tests in its section of the specification.
- Test scripts are written from the specification, executed by the customer's users, and results recorded with evidence.
- No module is accepted with an open critical or high defect. A waiver would be a contract change signed by the specification's §3 signatories.
- Final acceptance follows one full accounting cycle run in parallel, with both sets of figures reconciled and the differences explained in writing.
- Each migration load is reconciled and signed by Finance before the next load proceeds (§2.16.2).

| Aspect | Detail |
| --- | --- |
| Inputs | Release-candidate commit, approved scope, evidence. For acceptance: user test results, parallel-run reconciliation, migration sign-offs |
| Responsible | DevOps (build, deploy); reviewers; orchestrator (manifest, Gate D record); the customer's users (acceptance testing) |
| Outputs | Manifest, review records, Gate D record, deployment record, verification evidence; an acceptance record per module |
| Approval | Gate D: release authority and PO, plus the approvers in step 4. Acceptance: the customer's signatories |
| Evidence | E2 runs at the candidate commit; E1 approvals bound to it; deployment record; post-deployment checks; user test evidence; reconciliation reports; signed migration loads |
| Failure handling | Open Critical or High defect: Gate D blocked unless waived as in step 4; module acceptance blocked with no exception. Missing evidence: blocked. Failed deployment: rollback procedure and an incident issue |
| Complete when | Gate D: a deployment record and post-deployment verification exist, and the Gate D record names the deployed commit. Acceptance: all four §2.16.4 conditions are evidenced and signed |

### C8. Update domain knowledge from verified evidence

Knowledge changes only through a reviewed change that carries evidence. An agent's statement on its own can add an open question or a proposed interpretation, nothing more.

1. A trigger fires: a policy or change request is approved; a root cause is confirmed; test or reconciliation evidence contradicts the knowledge base; an incident review completes; or a verified regulatory notice arrives.
2. The orchestrator dispatches the Accounting Domain Expert with the event and its evidence.
3. The expert drafts the change: new or changed entries, each with a status and citations, and superseded entries marked.
4. `check` resolves citations and enforces status rules. Approved needs a decision record; a verification state needs E2 or E3 evidence.
5. Review: Assurance checks consistency with requirements; the qualified accountant approves normative entries (policies, rules, invariants, scenario results); a named person approves the merge of any other entry.
6. The change merges and the knowledge-base version advances. `trace` flags dependent requirements, tests and scenarios for review.

| Aspect | Detail |
| --- | --- |
| Inputs | The triggering event, with evidence references |
| Responsible | Accounting Domain Expert (author); Assurance (review); orchestrator (flow) |
| Outputs | Knowledge-base change; flags on dependent artifacts |
| Approval | Qualified accountant for normative entries; a named person for other entries, after Assurance review |
| Evidence | Resolvable citations; review records; a decision record for normative changes |
| Failure handling | Evidence conflicts: an issue opens and the knowledge base does not change. Update not done: the triggering change request or issue cannot close |
| Complete when | The change is merged with resolvable evidence and correct statuses, and dependents are flagged |

## D. Traceability and evidence model

One ID scheme, typed links and one-file-per-record ledgers connect business intent to production behaviour. Normative artifacts are versioned by content hash; evidence is bound to commits, runs and environments.

**Entities**

| Entity | ID pattern | Stored as | Decided by |
| --- | --- | --- | --- |
| Source document | SRC-nnn | File plus SHA-256 in the source register | Not applicable |
| Specification clause | S1-2.2.4-c07 | Generated clause index | Not applicable |
| Business objective | BO-nn | Markdown | Human PO |
| Requirement | REQ-AREA-nnn | Markdown with YAML front matter | Human PO |
| User story with acceptance criteria | US-AREA-nnn, AC-US-AREA-nnn-nn | Markdown | Human PO |
| Accounting policy, rule, invariant | POL-nnn, ACR-nnn, INV-nn | Knowledge base | Qualified accountant (invariants with the tech lead) |
| Scenario with expected journals | SCN-nnn | Knowledge base, executable as tests | Qualified accountant |
| Decision, architecture decision | DEC-nnnn, ADR-nnnn | Markdown | Owner in the authority matrix |
| Design, API contract, data entity | TD-AREA-nnn, API-name, ENT-name | Markdown, contract and schema files | Tech lead |
| Code unit | symbol at commit | Annotation in the code | Evidence, not a decision |
| Test | TC-AREA-nnn | ID tags in test code | Quality engineer |
| Issue, incident | ISS-ulid, IR-ulid | Record files; later a tracker, mirrored | Classified by Assurance; severity confirmed by a person |
| Change request, impact assessment | CR-nnn, IA-ulid | Markdown, record file | By change type |
| Question, risk, dispute | Q-nnn, RISK-nnn, DSP-ulid | Record files | Decision owner; risk owner; evidence or owner |
| Decision brief, approval request, approval decision | BRF-ulid, AREQ-ulid, APR-ulid | Record files | A person decides; agents only draft |
| Waiver or risk acceptance | WVR-ulid | Record file | Owner in the authority matrix |
| Evidence record | EVD-ulid | Pointer record; body in CI or the archive | A tool or CI |
| Review | REV-ulid | Record file | An agent (E4) or a person (E1) |
| Gate record | GATE-0, GATE-A-R1, GATE-C-INCR-003 | Markdown | Named approvers |
| Release, deployment | REL-x.y.z, DEP-ulid | Record files | Release authority |
| Increment, work item, workflow | INCR-nnn, WI-ulid, WF-ulid | Markdown, YAML | Tech lead; orchestrator |

Records that different branches may create at the same time use ULIDs (unique, time-ordered IDs), so they never collide; short forms are fine in prose. `ISS` replaces the separate GAP, CNF, AMB and DEF registers of the bootstrap plan, and `INCR` replaces `INC` to avoid confusion with incidents.

**Links**

| Link | From and to | Maintained by | Verified by |
| --- | --- | --- | --- |
| derives\_from | Requirement to clause or objective | Steward | Checker: target exists |
| refines | Story to requirement; criterion to story | Steward | Checker |
| governed\_by | Requirement or story to policy or rule | Steward, Accounting Domain Expert | Checker; Assurance sampling |
| decided\_by | Any artifact to DEC or ADR | Owner | Checker |
| designs | Design to requirement or story | Designer | Checker; architect review |
| implements | Code symbol to requirement, story or rule | Implementation engineer, as code annotations | Checker at each commit; Implemented also needs a test that executes the code |
| verifies | Test to criterion, rule or invariant | Quality engineer, as test tags | Checker; E2 run maps results to IDs |
| reviewed\_by | Change set or artifact to review | Reviewer | Checker; Reviewed needs a human review |
| evidenced\_by | Derived state to evidence record | Tools, CI | Digest check |
| approves | Decision to request to artifact at version and hash | A person, through an approval channel | Hash match and attestation |
| affects, resolves | Issue or change to any artifact; commit to issue | Steward, Assurance, implementation engineer | Checker |
| waives | Waiver to gate criterion or rule | Owner in the authority matrix | Checker, including expiry |
| supersedes | Newer version to older; policy to policy | Owner | Checker |
| blocks | Question or issue to any artifact | Orchestrator | Readiness check |
| deployed\_in | Release to environment and commit | CI/CD | E2 record |

**Versioning and validity**

- Normative artifacts carry an integer version and a normative hash over canonicalised normative fields, trace links included. Editorial edits change neither, and priority sits outside the hash.
- An approval is valid for the hash it names; the commit is provenance only. A revocation, or a later decision by the same approver, supersedes the earlier one, and both stay on file.
- Evidence binds to commit, run ID and environment, and never carries over to another commit.
- Policies, rules and requirements carry `effective_from` and `effective_to`.

**Time.** History is ordered by record sequence and the git host's merge time, not by commit dates, which whoever commits can set. Stage 0 records carry the local clock and are labelled so. Two questions stay separate: what was decided as of time T, and what was in force for accounting period P.

**Ledger storage.** One file per record, for example `ledger/approvals/APR-<ulid>.json`, so branches never conflict. Records are never edited after merge, and the checker (later CI) fails if one changes. Signed gate tags anchor the history at each gate. Evidence bodies stay in CI or the archive; the repository holds pointer records with digests.

```json
{"id":"APR-01JB7Q4ZP3…","request":"AREQ-01JB7P…","subjects":[{"id":"US-GL-012","v":2,"hash":"sha256:…"}],"decision":"approve","by":{"role":"Human PO","identity":"<git-host user id>"},"channel":"pr-review","source_event":"<host review id>","recorded_at":"2026-11-02T09:41:00Z","provenance_commit":"<sha>","comment":"<verbatim>","level":"E1"}
```

**Record templates** carry the grounding fields you asked for:

- **ADR or technical recommendation:** the motivating requirement or constraint, alternatives considered, trade-offs, evidence and assumptions, decision owner and approval status, verification method.
- **Defect:** observed failure, expected behaviour and its authoritative source, root-cause state, corrective change, tests and regression protection, actual verification results.
- **Deployment:** approved release version, target environment, approval and pipeline evidence, observed result, post-deployment checks, unresolved operational concerns.
- **Any material assertion:** source provenance and confidence limitations.

**Special cases**

- **Superseded artifacts** are never deleted. They carry `superseded_by`, and history queries return whichever version was in force at T.
- **Historical approvals** stay valid for the hash they name and nothing else; a later version needs its own.
- **Unresolved questions** with `blocks` links fail readiness. Non-blocking questions appear in every answer that touches the item.
- **Incomplete traceability** is reported as gaps per item and coverage per area. Proposed gate minimums: at Gate A, every release-1 requirement traces to a clause or a decision. At Gate C, every acceptance criterion has a test ID. At Gate D, every in-scope requirement is Tested at the release commit on E2 evidence.

&#91;embedded content: trace chain · intent to production\]

Upward arrows show what each piece of evidence realises. States are evaluated at a named commit, so evidence from an older commit does not carry over; approvals bind to content hashes instead, and a normative change voids them. Issues and change requests can attach to any box.

## E. Teams/Slack approval design

Record approvals on the git host and mirror them into the repository's ledger; use Teams or Slack only to notify and link. GitHub's Slack and Teams apps cannot approve a pull request, and GitLab's Slack app has no approve command. An in-chat Approve button therefore means building, and securing, a second decision path.

**Mechanisms compared** (checked against vendor documentation on 20 October 2026)

| Mechanism | Approver identity | Bound to a version? | Extra infrastructure | Use for |
| --- | --- | --- | --- | --- |
| [Pull-request review](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) with code owners and stale-approval dismissal | Authenticated host account; the [review record](https://docs.github.com/en/rest/pulls/reviews) holds user, commit and time | Yes: approvals are dismissed when new commits change the diff | A plan that enforces these rules on private repositories: GitHub Pro or Team, GitLab or Bitbucket Premium, or Azure DevOps | **Requirements, policies, ADRs (primary)** |
| [GitLab Premium approval with re-authentication](https://docs.gitlab.com/user/project/merge_requests/approvals/settings/) | Host account plus password or SAML re-entry, which GitLab documents as an electronic signature | Yes: the [approval API](https://docs.gitlab.com/api/merge_request_approvals/) can require the current head commit | GitLab Premium | Strongest option if auditors expect e-signatures |
| Deployment approval from chat: [GitHub app for Slack or Teams](https://docs.github.com/en/integrations/how-tos/slack/customize-notifications), [Azure Pipelines app for Slack](https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/slack) | Linked host account | Yes: tied to the pipeline run's commit | On GitHub, [required reviewers on private repositories need Enterprise](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) | Release approvals (Gate D), not requirements |
| [Power Automate Approvals](https://learn.microsoft.com/en-us/connectors/approvals/) in Teams | Entra ID (id, user principal name, email); request and response times | Only if the request carries the hash and the write-back re-checks it | Standard connector, Dataverse, and a write-back job holding a git token; flow runs end after [30 days](https://learn.microsoft.com/en-us/power-automate/limits-and-config) | Fallback if the PO must approve inside Teams |
| Custom [Teams bot](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/universal-actions-for-adaptive-cards/overview) or Slack app with buttons | Teams user ID; Slack user and team IDs in a [signed request](https://docs.slack.dev/authentication/verifying-requests-from-slack) | Must be built | A hosted HTTPS endpoint (Slack can use Socket Mode instead), bot registration, your own store | Not justified now |
| [Teams Workflows webhook](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) or [Slack incoming webhook](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) | None: Teams posts appear from the Workflows bot | No | A workflow owned by one person, or a Slack app | Notifications only |
| Decision typed in the Claude Code session | A phrase you type, captured by a hook; agents share your OS account | Yes: the decision record binds the hash | None | Stage 0 only (E1-op) |

Teams' older incoming webhooks are gone: Microsoft [retired Office 365 Connectors](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) in a rollout from 18 to 22 May 2026.

**Recommended staging**

1. **Stage 0, available now.** The orchestrator creates the approval request and shows its ID and hash. You approve by typing one exact phrase as the whole prompt, such as "APPROVE AREQ-01JB7P sha256:3f9a…". A UserPromptSubmit hook captures it from the [prompt text](https://code.claude.com/docs/en/hooks) and writes the record; no agent writes it. That hook also fires on scheduled tasks, subagent reports and messages from other sessions, so it accepts only an exact whole-prompt phrase; the remaining risk is one reason Stage 0 is best effort. This level is operator-attested (E1-op). Agents run under your OS account, so it never counts for Tier 1, and Stage 0 approvals are re-confirmed on the git host when Stage 1 starts. Session transcripts are not evidence: Claude Code keeps them for [30 days by default](https://code.claude.com/docs/en/settings), unencrypted.
2. **Stage 1, with a git host.** Agents commit and push under a bot identity whose token cannot approve, and your token never enters agent sessions. GitHub, for one, [does not let authors approve their own pull requests](https://docs.github.com/en/enterprise-server@3.17/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews), so agents must not push under your account. Normative changes reach main only through pull requests, with code owners on `docs/requirements/`, `docs/accounting/` and ADRs. Stale approvals are dismissed, a code owner other than the author must approve, and signed commits are required. A CI job mirrors each approving review into the repository after checking the normative hash at the reviewed commit.
3. **Stage 2, chat notifications.** The host's official Teams or Slack app, or a Workflows or incoming webhook, posts the request card with a link to the pull request. Nothing is decided in chat.
4. **Stage 3, only if needed.** Chat-initiated approval through Power Automate Approvals (Teams) or a Slack app, with a write-back that re-checks identity and hash. Release approvals from chat where the host supports them.

**Security model**

- Only accounts mapped to named roles in the version-controlled authority matrix (A8) can approve; changing the matrix needs two approvers.
- Agents never hold an approving identity or a person's token. Permission rules and the central hook also block approval commands such as `gh pr review` and `gh pr merge`, as defence in depth; the git host enforces it.
- The author of a change cannot approve it.
- Chat apps get notification scopes only until Stage 3. Tokens live in CI secrets or a vault, never in the repository.
- Messages carry IDs, titles, summaries and links, never financial data or specification excerpts (G5).
- People who don't read diffs approve from the rendered decision brief, which shows the version and hash it binds to.
- Do not let Claude Tag change this repository. Its documentation says [hooks in the repository's settings don't run](https://claude.com/docs/claude-tag/concepts/for-claude-code-users.md) and sessions run in auto mode, so the framework's guardrails would not apply. In channels it also opens pull requests as the Claude GitHub App, not as the requester.

**Request card** (Stages 2 and 3)

| Field | Content |
| --- | --- |
| Header | "Approval requested: US-GL-012 v2", the hash prefix and the approver role |
| Context | Business context and rationale, in two lines |
| Story | The story and its first acceptance criteria, with a count of the rest |
| Value | Priority and business value, from the decision brief |
| Implications | Accounting and technical implications, one line each |
| Open items | Questions, risks and dependencies: counts plus the most important |
| Links | Pull request, rendered specification, prototype, decision brief |
| Actions | Stage 2: "Review on the git host". Stage 3: Approve, Request changes, Reject, Defer, Escalate |
| Footer | "Bound to version 2. Any normative change voids this request." |

**Decision capture and version validation**

1. The approval request records artifact IDs, versions, normative hashes, the provenance commit and the required role.
2. Notifications leave through an outbox that records each as sent or failed.
3. On a decision, the receiver verifies its source (the Stage 0 hook, a host webhook signature, a Slack signing secret or an Entra token), maps the identity to a role, and checks that the approver is not the author.
4. It recomputes the normative hash at the commit the person reviewed, or of the current content in Stage 0. If that differs from the request's hash, the decision is recorded as stale and the approver is asked to review the new version.
5. Events are de-duplicated on their source event ID. A later decision by the same approver on the same request supersedes the earlier one, and both stay on file.
6. The decision is written as its own record file, and readiness is recomputed.

**Failure handling**

| Failure | Handling |
| --- | --- |
| Chat unavailable | Approvals continue on the git host; notifications retry from the outbox |
| Git host unavailable | Wait. An urgent decision can be captured in session (E1-op), flagged for re-confirmation |
| Mirror job fails | A daily reconciliation compares host reviews with the ledger and adds missing entries idempotently |
| Duplicate event | Ignored by its source event ID |
| Approval arrives after the content changed | Recorded as stale; not counted |
| Unmapped person approves | Rejected and logged |
| Power Automate request expires after 30 days | Recorded as no decision, then reissued |
| Host audit log expires (GitHub organisations: [180 days](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)) | The ledger mirror is the long-term record |

**Now versus later**

| Capability | Available now? | Needs |
| --- | --- | --- |
| Approval requests, hashing, record files, hook-captured decisions | Yes | Nothing |
| Signed commits for Stage 0 | Yes | Your SSH or GPG signing key |
| Pull-request approvals with code owners and stale dismissal | No | A git host plan that enforces them on private repositories |
| CI mirror into the ledger | No | CI and a bot account token |
| Chat notifications | No | Teams Workflows or a Slack app, with tenant admin consent |
| Chat-initiated approvals | No | Power Automate with Dataverse and a write-back job, or a Slack app with an endpoint. Release approvals from chat on private GitHub repositories also need Enterprise |

&#91;embedded content: approval flow · 1 check, 2 outcomes\]

Stale and duplicate decisions are logged but never counted. A re-issued request names the new version, so an earlier approval can never authorise changed content.

## F. Implementation roadmap

Seven phases. F0 delivers only what discovery needs and ends at Gate 0; every later phase is gated by acceptance tests of the framework itself, not by the existence of files.

| Phase | Deliverables | Depends on | Accepted when | Main risk | Validation |
| --- | --- | --- | --- | --- | --- |
| F0 Governance core | Repository hygiene; CLAUDE.md; 4 agents (Steward, Assurance, Accounting Domain Expert, Code and Security Reviewer); `check`; `trace` explain and coverage, adopted or built after a timeboxed tool evaluation; `approvals` with hook capture (Stage 0); edit, shell and validator hooks; pre-commit checks; source registration; issue and change-request records | Your decisions (G); ends at Gate 0 | Tool tests pass. Hook tests cover allow, block, Windows paths, shell writes and fail-closed. An agent's attempt to write a decision record is blocked. A synthetic requirement goes through drafting, two reviews and a hook-captured approval, and a normative edit then voids it | Building more than discovery needs | Dry run on synthetic data; human review of the tools |
| F1 Knowledge base | Knowledge-base structure, promotion workflow (C8), consistency sweep, first entries from approved artifacts | F0; a named accountant for normative entries | A person-written benchmark of about 20 questions, pinned to a commit, is answered with resolvable, quoted citations and correct statuses; one promotion completes with approval | Filling the base with unapproved interpretations | Benchmark; Assurance review |
| F2 Authenticated PO approval | Decision-brief skill; readiness checks; git host with protected branches, code owners and stale-approval dismissal (Stage 1); a bot identity for agents; governance CI that runs the checker and mirrors approvals | F0; the git host chosen (G3) | A pull-request approval is mirrored with identity and hash; a stale approval is rejected; a duplicate event is ignored; the host refuses an agent's attempt to approve | Approvers find the git host unfamiliar | Rehearsal with the PO and the accountant |
| F3 Defect and change-impact workflows | Issue states and classification, severity confirmation, `trace impact`, regression-test rule, change-request flow | F0 | Drill: three planted defects are classified correctly, and the impact report finds every known affected artifact in a prepared case | Missing links hide impact | Seeded-defect drills |
| F4 Automated evidence | CI producing E2 evidence mapped to IDs; tests that execute annotated code; evidence archive; record-immutability checks in CI | Gate B (stack); the governance CI from F2 | Every CI run yields evidence records; derived states match a hand-checked sample; a changed record fails CI | CI retention shorter than audit needs | Tamper and retention tests |
| F5 Chat integration | Notifications (Stage 2), then chat-initiated approvals only if needed (Stage 3); tracker sync | F2; admin consent and credentials | A chat-initiated approval lands with identity and hash; an outage falls back cleanly; a late approval on an outdated hash is rejected | A second system of record appears | Failure drills |
| F6 Continuous verification | Deployment and operational evidence, reconciliation feeds, scheduled consistency sweeps; vector search only if the benchmark shows misses | F4; deployed environments | Operational verification for a release in a test environment; trace coverage reported per gate | Alert fatigue | Release rehearsal |

**Fit with the product lifecycle.** F0 lands before any discovery record, at Gate 0. F1 runs alongside L1 and L2. F2 lands before Gate A, unless you accept Stage 0 for Gate A (G4). F3 lands before L5 starts. F4 starts after Gate B and runs through L5. F6 must be in place before Gate D. F5 is optional, at any point after F2.

**Overhead budget.** Each increment reports what the framework costs: elapsed time from story draft to decision, tokens per story, the share of review findings acted on, and the time people spend reviewing. Controls that cost more than they catch become candidates for pruning in L7.

&#91;embedded content: framework roadmap · 7 phases against 4 gates\]

Only F0 must finish before discovery work is recorded. F4 cannot start until Gate B fixes the stack, and F5 is optional.

## G. Decisions needed from you

Six decisions shape the architecture. Everything else I can recommend, and you review it in the framework's first increment.

| # | Decision | Options | Recommendation |
| --- | --- | --- | --- |
| G1 | Operating model and product review | (a) 10 agents. The product lens is the Steward's value rationale, Assurance's check of it, and the orchestrator's decision brief. (b) (a) plus an advisory Product Reviewer agent. (c) Your original model, with an AI Product Owner as co-approver | **(a)**. Add (b) only if, after the first increment, the PO finds the briefs miss value or scope problems. (c) adds an approval nobody is accountable for |
| G2 | Human authorities | Fill in the authority matrix (A8): names, delegates, escalation, and roles that must not be combined | **Fill it before Gate A**, mapping the specification's §3 signatories (Finance Manager, Internal Audit, Managing Director) to their roles. Until an accountant is named, accounting policies stay Proposed |
| G3 | Platforms and identities | Git host: GitHub Team, GitLab Premium, Azure DevOps or Bitbucket Premium. Tracker: the host's own, or Jira. Chat: Teams, Slack, or none yet. Plus a bot identity for agents on the chosen host | **Use what the organisation already licenses.** For a new choice, GitHub Team is the easiest to adopt; choose GitLab Premium if auditors expect re-authenticated, e-signature-style approvals. Agents get a bot identity either way. Chat starts as notifications only |
| G4 | Approval strength before the git host exists | (a) Stage 0 hook-captured approvals (E1-op) for discovery and Gate A, re-confirmed at Stage 1; Stage 1 required before any Tier-1 approval. (b) No approvals until Stage 1 | **(a)**. Also commit under your organisation account, since the repository's only commit uses a personal email address, and set up commit signing, which is not configured yet |
| G5 | What may leave the organisation, beyond what every Claude call already sends | (a) Chat messages carry IDs, titles, summaries and links; no embedding provider; web research queries never include specification text. (b) Requirement text allowed in chat. (c) An approved embedding provider as a second data processor | **(a)**, revisited only if a vector index is ever justified (A6) |
| G6 | Carry-over from the bootstrap plan, revised | Import the kickoff analysis and your prompts as registered sources; create agents in stages (A8) rather than all at once; run all agents on your session model; update the terminal CLI; turn off Claude Code's auto memory for this project | **Yes to all five.** Fail-closed hooks need Claude Code 2.1.295 or later; VS Code runs 2.1.301, but the terminal CLI is 2.1.227. Auto memory already holds two notes I wrote outside the repository, on where your earlier analyses live and on that version gap. They contain no requirements or decisions |

Already settled since the bootstrap plan: the repository is under git, with one commit on `master` holding the specification PDF and the strategic analysis, and no remote.

## Sources

Pages opened on 19 and 20 October 2026. A research agent read them all. I checked the load-bearing facts directly: the Teams connector retirement, GitHub's lack of pull-request approval from chat, GitHub environment plans, Claude Tag hooks, Claude Code's path-rule handling, the prompt hook's input, and GitHub's block on authors approving their own pull requests. An independent agent then reviewed the first draft adversarially, and its findings are incorporated.

**Claude and Claude Code:** [Subagents](https://code.claude.com/docs/en/sub-agents) · [Hooks](https://code.claude.com/docs/en/hooks) · [Permissions](https://code.claude.com/docs/en/permissions) · [Settings](https://code.claude.com/docs/en/settings) · [Memory and rules](https://code.claude.com/docs/en/memory) · [Skills](https://code.claude.com/docs/en/skills) · [Workflows](https://code.claude.com/docs/en/workflows) · [Agent teams](https://code.claude.com/docs/en/agent-teams) · [Claude Code in Slack](https://code.claude.com/docs/en/slack) · [GitHub Actions](https://code.claude.com/docs/en/github-actions) · [Claude Tag for Claude Code users](https://claude.com/docs/claude-tag/concepts/for-claude-code-users.md)

**Microsoft:** [Retirement of Office 365 Connectors](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) · [Workflows webhooks for Teams](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) · [Approvals connector](https://learn.microsoft.com/en-us/connectors/approvals/) · [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config) · [Universal Actions for Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/universal-actions-for-adaptive-cards/overview) · [Azure DevOps branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies) · [Azure Pipelines app for Slack](https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/slack)

**GitHub:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) · [Pull-request reviews API](https://docs.github.com/en/rest/pulls/reviews) · [Approving with required reviews](https://docs.github.com/en/enterprise-server@3.17/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews) · [Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) · [GitHub in Slack notifications](https://docs.github.com/en/integrations/how-tos/slack/customize-notifications) · [Organisation audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)

**GitLab, Bitbucket, Slack:** [GitLab approval settings](https://docs.gitlab.com/user/project/merge_requests/approvals/settings/) · [GitLab approvals API](https://docs.gitlab.com/api/merge_request_approvals/) · [Bitbucket merge checks](https://support.atlassian.com/bitbucket-cloud/docs/suggest-or-require-checks-before-a-merge/) · [Verifying Slack requests](https://docs.slack.dev/authentication/verifying-requests-from-slack) · [Slack incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) · [Slack Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode)

**Not verified:** whether the Azure Pipelines app for Teams is still supported; how long Dataverse keeps approval records; whether Teams Workflows can post to private channels (Microsoft's pages disagree); whether the code-intelligence (language server) tool works in VS Code sessions; whether the prompt hook's input marks automated turns; and the features of the requirements-as-code tools named in A6, which are candidates for evaluation, not findings.
