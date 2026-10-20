---
id: REV-<ulid>
type: review
reviewer: <agent name or person>
level: E4
subjects:
  - id: <ID>
    hash: sha256:<hash reviewed>
  # For code, name the commit instead: - commit: <full 40-character hash>
verdict: pass
findings:
  - severity: non-blocking
    text: <finding>
    citation: <quoted passage or ID at version>
created_at: <UTC ISO-8601>
---

Detail of the review (optional).
