---
id: DEC-0005
type: decision
title: Carry-over items from the bootstrap plan
status: Approved
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Import the kickoff analysis and the prompt history as registered sources (SRC-003, SRC-004).
    Update the terminal Claude Code CLI. Keep Claude Code's auto memory enabled for this project;
    its notes are convenience only, never evidence or decisions, and repository artifacts always win.
  conditions:
    - The auto-memory risk (RISK-009) is accepted by this decision.
    - All agents use the session model (model inherit).
links:
  related: [SRC-003, SRC-004, SRC-005]
decided_in_session:
  date: 2026-10-20
  channel: Claude Code session, structured question (G5 and G6)
  question: Which of these setup defaults do you accept?
  answer: Update terminal CLI; Import prior inputs. Turning off auto memory was not selected.
  transcribed_by: orchestrator
---

# DEC-0005: Carry-over items from the bootstrap plan

Done so far: SRC-003 and SRC-004 imported byte-exact on 2026-10-20; the terminal CLI updated from
2.1.227 to 2.1.304 on 2026-10-20, which supports fail-closed hooks (2.1.295 or later).
