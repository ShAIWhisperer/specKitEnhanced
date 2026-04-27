---
id: speckit.x.research
description: Create a research spec capturing evidence for a decision.
args: "<research-slug> <question>"
template: templates/core/research-template.md
produces: specs/research/{slug}.md
---

# /speckit.x.research

Evidence log for a design/architecture decision. Link from ADR.

## Steps

1. Derive `slug` + `question` from `$ARGS`.
2. Copy template to `specs/research/{slug}.md`.
3. Fill:
   - Question (exact phrasing).
   - Why now (trigger).
   - Sources table — at minimum 2 sources; mark reliability.
   - Findings F-1..F-N, each with evidence quote/link.
   - Synthesis — confidence + remaining uncertainty.
   - Decision section — link ADR if one exists yet.
4. On save, add row to `specs/decisions.md` (or suggest opening ADR).
5. Append to `specs/history.md`.
