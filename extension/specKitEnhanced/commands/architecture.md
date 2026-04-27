---
id: speckit.x.architecture
description: Draft/update an architecture spec for a subsystem.
args: "<subsystem-slug> [short description]"
template: templates/core/architecture-template.md
produces: specs/architecture/{slug}.md
---

# /speckit.x.architecture

You are authoring a subsystem architecture spec for this project.

## Inputs

- `$ARGS` — subsystem slug + optional description (e.g. `auth handles login, session, RBAC`).
- Project constitution: read `specs/constitution.md` first.
- Existing architecture specs: list `specs/architecture/*.md` and avoid duplication.

## Steps

1. Derive `slug` from `$ARGS[0]`. Lowercase, hyphenate.
2. If `specs/architecture/{slug}.md` exists → update in place, bump `updated:` in frontmatter, append to inline `## Changelog`.
3. Otherwise, copy `templates/core/architecture-template.md`, fill placeholders.
4. Fill sections:
   - **Context** — cite which principle(s) the subsystem implements (`{ref:specs/constitution.md#PN}`).
   - **Components** — real files in the repo, each linked `{ref:src/...}`.
   - **Data Flow** — ASCII first pass; upgrade to mermaid if flow has ≥ 5 nodes.
   - **Invariants** — INV-1..INV-N. Must be checkable.
   - **Trade-offs** — every row points to an ADR. If none exists, draft one with `/speckit.x.adr`.
5. Set `status: draft`. Do not mark `approved` without explicit user confirmation.
6. Append entry to `specs/history.md`: `### YYYY-MM-DD — arch(<slug>) drafted`.

## Validation

Before saving, verify:
- All `{ref:...}` targets exist.
- Frontmatter matches `schemas/spec.schema.json`.
- No `[NEEDS CLARIFICATION]` markers remain OR they are explicitly listed in §8 Open Questions.
