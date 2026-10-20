I've finished Steps 1–6. This is the bootstrap plan for your review. Nothing in the repository has been created or changed. My only writes were a text extraction of the specification in my scratchpad and two notes in my cross-session memory.

## 1. What I found

| Item | What it is | How the framework treats it |
|---|---|---|
| [TIQACC-Cloud-Accounting-Requirement - V1.pdf](requirement-doc/TIQACC-Cloud-Accounting-Requirement%20-%20V1.pdf) | 121-page buyer's specification: 14 modules, acceptance tests per module, about 180 bracketed values still to be confirmed | **SRC-001**, the authoritative input. It is **not a signed baseline**: the §3 sign-off block (Finance Manager, Internal Audit, Managing Director) is unfilled, and Annexures A and B (vendor response matrix, current chart of accounts, volumes, invoice formats) are missing |
| [01-strategic-architecture-discovery.md](docs/architecture/01-strategic-architecture-discovery.md) | 1,258-line AI-generated strategic analysis dated today, marked "Draft for stakeholder review" | **SRC-002**, an input with status Proposed. Nothing in it is approved, and it stays byte-for-byte unchanged |
| `output/analysis/` | Empty folder | Left alone |

There is related material outside the repo in `c:\yogi\tiqacc-documents\`:
- **Kickoff analysis:** a second AI analysis. It records TIQACC as both an internal group platform and a commercial SaaS product, "as confirmed by the requirements owner".
- **Prompt sequence:** strategic discovery, then detailed blueprint, then architecture challenge.

**Environment:** Windows 11 with VS Code.
- This session runs Claude Code **2.1.301**, bundled with the extension. The `claude` command in the terminal is **2.1.227** and hasn't updated since August.
- Installed tools: Git, Node 25, Python 3.14 (pdfplumber and PyYAML already installed), Docker.
- No CLAUDE.md, `.claude/`, agents, skills or hooks exist yet.
- Your organization's policy only disables Remote Control and quick web setup.

**What I checked, and what I couldn't:**
- **Checked:** file inventory, tool versions, `claude doctor` (no issues), the PDF's fingerprint and page count, and an extraction of its text.
- **Read:** the parts of both analyses that matter for governance, plus the spec's front matter, acceptance protocol (§2.16.4) and sign-off page. SRC-002 §8–12 (detailed architecture) I only skimmed; they matter in Phase 3.
- **Docs:** an agent checked the official Claude Code docs. I confirmed one key point myself: file permission rules only work as `Edit(...)`/`Read(...)`; `Write(...)` rules are silently ignored.
- **Not verified yet:** how hooks behave on this version. That's tested in step B4.

**Findings that shape the framework:**
1. **Phase 1 is mostly baselining an existing, unsigned spec,** not starting from a blank page. The spec says every module is to be built, and any change after signature needs a change request. So releasing in phases is a scope decision someone has to approve, not an interpretation.
2. **The two prior analyses disagree,** one proposing a broad first release and one a narrow one. **Their numbering also collides** (`D-01…` vs `D01…`). Both are model output, so the framework treats them as hypotheses to re-check.
3. **Spec clause numbers restart under each sub-heading.** §2.2.4 has two separate "1–5" lists, so a reference like "2.2.4.1" (used in SRC-002) is ambiguous. Clause-level tracing needs a generated clause index.
4. **Agents can't read the PDF here,** because the Read tool needs a PDF renderer that isn't installed. A version-controlled text extraction, tied to the PDF by its fingerprint, is a prerequisite. The PDF stays authoritative.

## 2. Methodology

- **Spec-driven workflow alone (e.g. GitHub Spec Kit):** the per-increment shape is good. It has no decision registers, accountable approvals, independent review or clause-level tracing, so it isn't enough on its own.
- **Heavy formal process (full SRS, V-model documents up front):** out of proportion. Agents can produce far more text than people can review.
- **Recommended: a thin governance layer around a spec-driven increment workflow.**
  - Each increment goes spec → design → tasks.
  - Requirements are written as "When…, the system shall…"; acceptance criteria as Given/When/Then; code is built test-first.
  - The whole spec is triaged coarsely first (release 1 / later / excluded / needs decision). Detail is written just in time for each increment.
  - Domain-driven design is used where it pays: the accounting kernel and module boundaries.
  - Verification scales with risk:
    - **Tier 1** — posting, numbering, periods, audit, authorisation, money/rounding. Needs accounting review, security review, invariant tests, and human approval of any policy effect.
    - **Tier 2** — module logic, APIs, integrations. Needs independent review and test evaluation.
    - **Tier 3** — screens, docs, tooling. Needs a light review.
- **Limitations:**
  - Agents don't reliably follow instructions, so critical controls are enforced mechanically.
  - Ten agents cost more time and tokens per change than one.
  - No process replaces a qualified accountant signing off accounting policy.

## 3. Governance model

| Phase | TIQACC focus | Gate | Proposed approver |
|---|---|---|---|
| 0 Framework | This bootstrap | **Gate 0** | You |
| 1 Discovery | Clause index; business objectives; actors; workbook for the ~180 bracketed values; missing annexure data; release-1 scope | — | — |
| 2 Requirements assurance | Independent challenge; re-check both prior analyses | **Gate A** (release-1 requirements) | Product owner + finance owner |
| 3 Architecture & design | Re-evaluate SRC-002 against the approved requirements; architecture decisions including the tech stack. Your blueprint and challenge prompts become the agents' briefs | **Gate B** | Tech lead (+ security) |
| 4 UX & test specs | Prototypes and executable acceptance specs | **Gate C**, per increment | Product owner + tech lead |
| 5 Test-first build | Small, reviewed work items | — | — |
| 6 Release | Evidence against spec §2.16.4: no open critical or high defects, plus a full parallel accounting cycle | **Gate D** | Release authority |
| 7 Improvement | Retrospectives, process change log | — | — |

- **Approvals:** each gate record lists who approved, the exact documents and commit approved, and any conditions or accepted risks.
- **No self-approval:** agents never mark anything Approved. The checker rejects any Approved item without a matching approval record.
- **Status labels:**
  - For decision items: Proposed, Assumption, Pending Clarification, Approved, Rejected, Superseded.
  - For documents: Draft → In Review → Approved → Implemented → Verified.
- **Disagreements:** both sides' evidence is recorded. Factual disputes are settled by evidence or tests. Policy disputes go to the named owner, never to whichever proposal came first.
- **Change control:** after Gate A, any change to an approved item goes through a change request with an impact check, matching the spec's own rule.

## 4. Agents and orchestration

This main session is Agent 0, the orchestrator. Ten subagents:

| # | Agent | Writes only to | Independently checks |
|---|---|---|---|
| 1 | requirements-engineer | `docs/requirements/` (except assurance files) | — |
| 2 | requirements-assurance | Assurance reports, gap/conflict register | Agent 1; claims in both prior analyses |
| 3 | accounting-domain (+ cited web research) | `docs/accounting/` | Accounting behaviour in agents 1, 5, 7, 8 |
| 4 | solution-architect (+ cited web research) | `docs/architecture/` | Design and code conformance |
| 5 | technical-designer | `docs/design/` | — |
| 6 | ux-designer | `docs/ux/`, prototypes | — |
| 7 | quality-engineer (+ Bash) | `docs/quality/`, acceptance tests | Test adequacy for agent 8 |
| 8 | implementation-engineer (+ Bash) | Source code, migrations | — |
| 9 | code-security-reviewer (+ Bash) | Review records only | Agents 7, 8, 10 |
| 10 | devops-release (+ Bash) | CI/CD, `docs/operations/` | — |

- Every agent gets an explicit tool list that excludes spawning other agents, so all delegation runs through me.
- All use `model: inherit` (whatever model you run).
- Per-agent memory is off. Lessons go through Phase 7 change control instead.
- Agents 5–10 are **provisional**. Their stack-specific commands get filled in after the tech-stack decision at Gate B.

**How a task runs:**
1. I hand the agent a brief (`/delegate`): objective, inputs, what it may write, and acceptance criteria.
2. It returns a fixed handoff report: what's done, files changed, labelled assumptions, open questions, and the checks it actually ran. Subagents can't ask you questions directly, so escalation always comes through me.
3. I check the report against the brief, run the checker, and send important work to its paired reviewer before anything reaches a gate.
4. Agents only run in parallel when they write to different places. Each document has one owner.
5. If a task fails, I retry once with a clearer brief, then escalate to you.

## 5. Tooling configuration

| Mechanism | Content |
|---|---|
| `CLAUDE.md` (under 200 lines; subagents load it too) | The project rules, lifecycle, agent roster and escalation path. It pulls in a short current-status file |
| `.claude/settings.json` (committed) | **Blocked:** editing source documents, their extractions and the prior analysis; reading secrets; force-push, hard reset and recursive delete (in both Bash and PowerShell). **Asks you first:** `git push`, installing dependencies, editing `CLAUDE.md`, governance tooling or gate records. **Allowed:** read-only git and the checker |
| Hooks (Python, set to block if the hook itself fails) | **Write guard:** protects source paths for everyone, and keeps each subagent inside its write area by agent name. If that turns out not to work on this version, the fallback is a hook in each agent's own file. **Validator:** checks headers, IDs, statuses and approval links on every document edit. It also checks agent and skill files, because Claude Code silently ignores a mistyped `tools:` field and the agent would then get every tool |
| Skills | `/delegate`, `/governance-check`, `/gate-review`, `/record-decision`, `/change-impact`, `/status-report`. Test-first and code-review skills come after Gate B |
| Path rule | Document conventions load only when files under `docs/` are touched |
| `tools/governance/check.py` | Checker with unit tests written first: unique IDs, valid references, legal statuses, approvals backed by a record, source fingerprints, trace coverage per gate. Reusable in CI later |
| Not used | Agent teams (experimental). Saved multi-agent workflow scripts (expensive; proposed later only with your opt-in) |

## 6. Repository layout and IDs

```text
CLAUDE.md · README.md · .gitignore · .gitattributes
.claude/        settings.json · agents/ (10) · skills/ (6) · hooks/ · rules/
requirement-doc/                      unchanged (SRC-001)
docs/governance/    methodology · conventions · agent operating model · project status
                    decisions/ · risks.yaml · questions.yaml · change-requests/ · gates/ · templates/
docs/sources/       source register with fingerprints · spec text extraction · imports (decision 2)
docs/requirements/  objectives · actors · glossary · clause index · requirements · issues.yaml · assurance/
docs/accounting/    rules · invariants · policies · posting specs · scenarios
docs/architecture/  existing analysis (unchanged, SRC-002) · adr/
docs/design · ux · quality · delivery · operations   (created when first needed)
tools/governance/ · tools/sources/
```

- **ID prefixes:** SRC, BO, REQ-‹AREA›, US, AC, INV, ACR, POL, DEC, ADR, Q, GAP/CNF/AMB, RISK, CR, TC, INC, WI, DEF, REV, GATE.
- **Old IDs:** the IDs in the two prior analyses get a mapping table, not reuse.
- **Spec clauses:** IDs like `S1-2.2.4-c07`, recording the page and sub-heading.
- **File formats:** documents are Markdown with a YAML header; large registers are YAML files.
- **No empty placeholders:** templates are created only for what's needed up to Gate A, plus the architecture decision record.

## 7. Implementation plan (after your approval)

| Step | Produces | Verification I'll report |
|---|---|---|
| **B1** | Git repository, ignore files, README, first folders | Repository state and folder check |
| **B2** | `CLAUDE.md`, methodology, conventions, operating model, templates; DEC-0001 "adopt framework" (Proposed); framework risks | A fresh agent reviews these documents for contradictions |
| **B3** | Governance checker, tests written first | Tests actually run and pass; checker run on the repo |
| **B4** | Settings, hooks, 10 agents, 6 skills | Settings checked against the published schema; `claude doctor`. Hook tests that block and allow cases, Windows paths, and a deliberate crash that must block. Live checks that agents receive their name, load `CLAUDE.md`, and stay in their write area. Anything I can't test in this session is reported as unverified |
| **B5** | Source register with fingerprints; spec text extraction; old-ID mapping table | Fingerprints match; 121/121 pages; spot checks of quoted clauses |
| **B6** | Validation report, plus a Gate 0 record waiting for your approval | Full checker run; independent review of the hook and checker code |

B6 ends with the first Phase 1 discovery questions, so you can approve Gate 0 and answer them in one reply.

## 8. Risks of the framework itself

| Risk | Mitigation |
|---|---|
| Overhead outweighs value | Risk tiers, detail written just in time, Phase 7 pruning |
| Agent output outpaces your review | Small batches; you approve decisions, not every line |
| Agents ignore instructions | Blocks and hooks apply in every permission mode, including auto |
| Prior AI analyses treated as fact | Registered as Proposed and re-checked in Phase 2 |
| A hook silently doesn't run | Hooks set to block on failure; smoke tests; minimum version 2.1.295 documented |
| No qualified accounting approver | Accounting policies can't reach Approved; this shows up as a blocker |
| Confidential spec content leaves the machine | Web research only for agents 3 and 4, with no spec text in queries; no push without your approval |

## 9. Decisions I need from you

1. **Version control.** I recommend creating a local git repository now. I'd commit locally at each verified step and never push without your explicit instruction. Should the spec PDF be committed too? I'd say yes, unless the repo will go somewhere client material shouldn't.
2. **Outside material.** I recommend copying, not moving, the kickoff analysis and your four prompts into `docs/sources/` as registered sources, so their influence can be traced.
3. **Who approves what.** I recommend you approve Gate 0 and the engineering gates (B, C). A named finance owner would approve Gate A and accounting policies; the spec names Finance Manager, Internal Audit and Managing Director as its signatories. Until someone is named, accounting policies stay "Proposed — pending qualified review". Who approves releases (Gate D)?
4. **Agents and model.** I recommend creating all ten now, with 5–10 provisional, all using your model. That gives the best quality but the highest token cost. Alternatives: create 5–10 at Gate B, or put cheaper models on low-risk roles later.
5. **Enforcement.** I recommend the Python hooks and checker as described; nothing new needs installing. I also recommend running `claude update` so the terminal `claude` matches the VS Code version and enforces the same controls.

Reply "approve with defaults" or tell me what to change. If you want to share this plan with finance or audit stakeholders, I can publish it as a page.
