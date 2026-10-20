---
id: GOV-CONVENTIONS
type: governance
title: Artifact, record and commit conventions
status: Proposed
version: 1
owner: orchestrator
links:
  decided_by: [DEC-0001]
---

# Conventions

These conventions are enforced by `tools/governance/check.py`. Change them only through a framework
change (DEC record approved by the governance owner), and update the checker and its tests in the
same change.

## Identifiers

| Prefix | Pattern | Kind | Where |
| --- | --- | --- | --- |
| SRC | `SRC-001` | Registered source | `docs/sources/source-register.yaml` |
| S1 | `S1-2.2.4-c07` | Clause of SRC-001 (section, clause number in document order) | Clause index (L1) |
| GOV | `GOV-METHOD` | Governance document | `docs/governance/` |
| BO | `BO-01` | Business objective | `docs/requirements/` |
| REQ | `REQ-GL-001` | Requirement (area code of 2 to 5 capitals) | `docs/requirements/` |
| US, AC | `US-GL-001`, `AC-US-GL-001-01` | User story; acceptance criterion inside the story | `docs/requirements/` |
| POL, ACR, INV, SCN | `POL-001`, `ACR-001`, `INV-01`, `SCN-001` | Accounting policy, rule, invariant, scenario | `docs/accounting/knowledge/` |
| DEC, ADR | `DEC-0001`, `ADR-0001` | Decision; architecture decision | `docs/governance/decisions/`, `docs/architecture/adr/` |
| TD, API, ENT | `TD-GL-001`, `API-journals`, `ENT-journal-line` | Design; API contract; data entity | `docs/design/` |
| TC | `TC-GL-001` | Test case (tag in test code) | Test code (L5) |
| Q, RISK, CR | `Q-001`, `RISK-001`, `CR-001` | Question, risk, change request | `docs/governance/` registers, `docs/changes/` |
| GATE | `GATE-0`, `GATE-A-R1`, `GATE-C-INCR-003` | Gate record | `docs/governance/gates/` |
| INCR, REL | `INCR-001`, `REL-1.0.0` | Increment; release | `docs/delivery/` |
| ULID-based | `ISS-`, `IR-`, `IA-`, `DSP-`, `BRF-`, `AREQ-`, `APR-`, `WVR-`, `EVD-`, `REV-`, `DEP-`, `WI-`, `WF-` followed by a 26-character ULID | Records that different branches may create at the same time | `ledger/`, `docs/issues/` |

ULIDs use Crockford base32 (`0-9`, `A-Z` without `I`, `L`, `O`, `U`) and sort by creation time.

## Front matter

Every governed Markdown artifact starts with YAML front matter.

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | The artifact's ID; unique in the repository |
| `type` | Yes | `governance`, `objective`, `requirement`, `story`, `policy`, `rule`, `invariant`, `scenario`, `decision`, `adr`, `design`, `question`, `issue`, `change-request`, `gate` |
| `title` | Yes | Short name |
| `status` | Yes | `Draft`, `In review`, `Proposed`, `Approved`, `Rejected`, `Deferred`, `Superseded` |
| `version` | Yes | Integer, raised on every normative change |
| `owner` | Yes | Agent name, `orchestrator`, or a role in the authority matrix |
| `tier` | For every type that has a `normative` block | `1`, `2` or `3`; approval treats a missing tier as Tier 1 |
| `normative` | For requirement, story, policy, rule, invariant, scenario, decision, adr, gate once Proposed | Mapping of the content that carries meaning: statement, acceptance criteria, rules, expected results, decision, conditions |
| `links` | No | Mapping of link type to a list of IDs (see below) |
| `effective_from`, `effective_to` | For policies, rules, requirements where time matters | `YYYY-MM-DD` |
| `supersedes`, `superseded_by` | When versions are replaced | IDs |
| `decided_in_session` | Only for decisions taken before the capture hook existed | Date, channel and the transcribing agent; such decisions stay Proposed until confirmed by a captured decision |

Text below the front matter is explanation and is **not** normative.

Link types: `derives_from`, `refines`, `governed_by`, `decided_by`, `designs`, `implements`,
`verifies`, `affects`, `resolves`, `supersedes`, `blocks`, `waives`, `related`. Every linked ID must
exist, except clause IDs (`S1-…`) before the clause index exists, which produce a warning.

## Normative hash

An approval binds to the artifact's normative hash, so editorial edits never void it.

1. Build the payload: `id`, `type`, `tier`, `normative`, `effective_from`, `effective_to`, and the
   normative links (`derives_from`, `refines`, `governed_by`, `decided_by`, `supersedes`), each list
   sorted. Missing fields are omitted.
2. Canonicalise: strings are NFC-normalised, line endings become LF, leading and trailing whitespace
   is removed and runs of whitespace become one space; mappings are serialised with sorted keys.
3. Serialise as compact JSON (UTF-8, sorted keys) and take SHA-256. Written as `sha256:<64 hex>`.

`python tools/governance/approvals.py hash <ID>` prints it.

## Records

Records under `ledger/` are created once and never edited after commit; a correction is a new record
that references the old one. The checker rejects changes to committed records.

A new file under a protected source path (`requirement-doc/`, `docs/sources/SRC-*/`) is committed
only together with its entry, with path and SHA-256, in `docs/sources/source-register.yaml`. Local
capture state (`.claude/state/`) is never committed.

| Record | File | Written by |
| --- | --- | --- |
| Approval request | `ledger/approval-requests/AREQ-<ulid>.json` | `approvals.py request` (orchestrator) |
| Approval decision | `ledger/approval-decisions/APR-<ulid>.json` | Only the capture hook (Stage 0) or the git-host mirror (Stage 1; refused until Stage 1 exists) |
| Review | `ledger/reviews/REV-<ulid>.md` | The reviewing agent or person |
| Evidence | `ledger/evidence/EVD-<ulid>.json` | `run_tests.py` (E3) or CI (E2) |
| Workflow | `ledger/workflows/WF-<ulid>.yaml` | Orchestrator |

### Approval request (AREQ)

```json
{"id": "AREQ-<ulid>", "type": "approval-request", "created_at": "<UTC ISO-8601>",
 "created_by": "orchestrator", "required_role": "governance-owner", "tier": 3,
 "subjects": [{"id": "DEC-0001", "version": 1, "hash": "sha256:…"}],
 "combined": "sha256:…", "phrase_code": "<first 12 hex of combined>",
 "provenance_commit": "<sha>", "brief": "BRF-<ulid> or null", "note": "…"}
```

`combined` is the SHA-256 of the sorted lines `<id> <hash>`, one per subject.

### Approval decision (APR)

```json
{"id": "APR-<ulid>", "type": "approval-decision", "request": "AREQ-<ulid>",
 "decision": "approve | reject | request-changes | defer | escalate | revoke",
 "subjects": [{"id": "…", "version": 1, "hash": "sha256:…"}], "combined": "sha256:…",
 "stale": false, "by": {"role": "governance-owner", "identity": "local:<os user> / git:<name>"},
 "channel": "stage0-session", "level": "E1-op",
 "attestation": {"hook": "capture-approval", "session_id": "…", "prompt_sha256": "…"},
 "recorded_at": "<UTC ISO-8601>", "comment": "<verbatim text after the phrase, if any>"}
```

The evidence level comes from the channel, not from the record: a `stage0-session` decision is
always E1-op. Before it is committed, a Stage 0 decision must match the capture hook's local log
(`.claude/state/capture-log.jsonl`) byte for byte.

### Stage 0 approval phrase

The whole prompt must be exactly one line:

```text
APPROVE AREQ-<ulid> <phrase_code>
```

Other verbs: `REJECT`, `REQUEST-CHANGES`, `DEFER`, `ESCALATE`, `REVOKE`. An optional comment may
follow ` -- `. Anything else in the prompt means no decision is captured.

A decision is **stale** if any subject's current hash differs from the request; stale decisions are
recorded but never count. A later decision by the same identity on the same request supersedes the
earlier one; both stay on file.

### Review (REV)

Markdown with front matter: `id`, `type: review`, `reviewer`, `level` (`E4` for agents, `E1` for
people), `subjects` (each an artifact ID with the hash reviewed, or `commit: <full hash>` for code),
`verdict` (`pass`, `non-blocking-findings`, `blocking-findings`), `findings` (each with `severity`,
`text` and `citation`), `created_at`.

### Workflow (WF)

YAML, written once when the workflow ends, because records are never rewritten: `id`,
`type: workflow`, `title`, `started_at`, `ended_at`, and `steps`, each with `step`, `agent`,
`objective`, `records` (IDs created), `outcome` and `validation` (what the orchestrator checked). A
follow-up workflow is a new record that names the earlier one in `follows`.

## Citations

| Form | Example |
| --- | --- |
| Artifact at a version | `REQ-GL-004@v3` |
| Code at a commit | `src/ledger/posting.py@1a2b3c4#post_entry` |
| Test run | `TC-GL-004@EVD-<ulid>` |
| Decision | `APR-<ulid>` |
| Quoted source | `"Nothing partially posts" (SRC-001 p.27, §2.2.4 Bulk journal upload, 3)` |

A citation for a factual claim carries the quoted words. Line numbers appear only beside a commit.

## Commits

- People commit under their own accounts.
- Agent work is committed by the orchestrator under the agent identity
  `TIQACC Orchestrator (Claude) <orchestrator@agents.tiqacc.invalid>`, one commit per authoring agent,
  with an `Agent: <agent name>` trailer for each agent whose work it contains.
- The commit-msg check rejects an agent commit whose changed paths fall outside the write scopes of
  the agents it names (`.claude/hooks/agent-scopes.json`).
- Commits are local. Nothing is pushed without a person's explicit instruction.
- Pass commit messages with `git commit -F <file>`. The guard reads every line of an inline message
  as a command, so a message that names a protected path or a blocked command is refused.
