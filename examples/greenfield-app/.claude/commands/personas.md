---
id: speckit.x.personas
description: Add/update persona cards.
args: "[persona-name]"
template: templates/core/personas-template.md
produces: specs/personas.md
---

# /speckit.x.personas

## Steps

1. If `specs/personas.md` missing → copy template.
2. Add new card at end: `## P-NNN — <name>` with JTBD, Goals, Pains, Context, Signals, Tools.
3. Interactive prompts if fields missing.
4. Validate: every user story in `specs/features/*/spec.md` cites a persona by ID.
5. Append to `specs/history.md`.
