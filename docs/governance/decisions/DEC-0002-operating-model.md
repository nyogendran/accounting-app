---
id: DEC-0002
type: decision
title: Ten agents; product review through decision briefs
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Use ten agents and no AI Product Owner agent. The product lens comes from the Requirements
    Steward's value rationale for each story, Requirements Assurance's check of that rationale, and
    the orchestrator's one-page decision brief. The human Product Owner is the only approver of
    requirements.
  conditions:
    - Agents are created in stages. F0 creates requirements-engineer, requirements-assurance, accounting-domain-expert and code-security-reviewer. Solution-architect and technical-designer follow at Gate A; the remaining four at Gate B.
    - An advisory Product Reviewer agent may be added later if the Product Owner finds the briefs miss value or scope problems.
links:
  related: [SRC-005]
decided_in_session:
  date: 2026-10-20
  channel: Claude Code session, structured question (G1)
  question: How should product review work (G1)?
  answer: 10 agents, brief-based (Recommended)
  transcribed_by: orchestrator
---

# DEC-0002: Ten agents; product review through decision briefs

Option (a) of decision G1 in SRC-005. An AI co-approver was rejected because it adds an approval
nobody is accountable for. Staged creation follows the F0 scope in SRC-005, section F.
