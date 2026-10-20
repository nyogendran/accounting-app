---
id: DEC-0004
type: decision
title: Data boundary for external services (deferred)
status: Deferred
version: 1
owner: orchestrator
tier: 3
normative:
  question: >-
    What may leave the organisation, beyond what every Claude call already sends: requirement text
    in chat messages, specification text sent to an embedding provider, specification text in web
    research queries?
  options:
    - (a) IDs, titles, summaries and links in chat; no embedding provider; no specification text in web queries.
    - (b) Requirement text allowed in chat messages.
    - (c) An approved embedding provider as a second data processor.
  interim: >-
    No chat integration or embedding provider is built before this is decided (none is in scope
    before F5). Web research queries by agents avoid verbatim specification text; this is an
    assumption pending the decision, not an approved policy.
links:
  related: [SRC-005]
decided_in_session:
  date: 2026-10-20
  channel: Claude Code session, structured question (G5 and G6)
  question: Which of these setup defaults do you accept?
  answer: The default for G5 (option a) was not selected; the decision is deferred.
  transcribed_by: orchestrator
---

# DEC-0004: Data boundary for external services (deferred)

The governance owner did not accept the recommended default on 2026-10-20. The decision stays open
(RISK-008) and is needed before F5 (chat integration) or any embedding-based search.
