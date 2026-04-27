---
id: speckit.x.design
description: Draft/update a design spec (UX + interaction) for a feature.
args: "<feature-slug>"
template: templates/core/design-template.md
produces: specs/features/{slug}/design.md
---

# /speckit.x.design

Author a design spec for a feature. Complements the spec.md (what+why) and plan.md (how).

## Inputs

- `$ARGS` — feature slug (must match `specs/features/<slug>/` directory).
- Read `specs/features/{slug}/spec.md` for user stories + acceptance.
- Read `specs/personas.md` — every UX goal cites a persona.

## Steps

1. If `specs/features/{slug}/spec.md` missing → abort with message "run /speckit.specify first".
2. Copy `templates/core/design-template.md` into `specs/features/{slug}/design.md`.
3. Fill sections:
   - **UX Goals** — tie each to a persona ID.
   - **Flow** — number steps; ASCII arrow path first; mermaid if complex.
   - **Components** — link each to real source or note `<TBD>`.
   - **Interactions** — required loading / error / empty states.
   - **Copy** — every CTA and error message.
   - **Accessibility** — explicit keyboard + screen-reader rules.
4. Set `linked_spec` in frontmatter to the spec path.
5. Append to `specs/history.md`.
