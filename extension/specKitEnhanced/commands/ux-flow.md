---
id: speckit.x.ux-flow
description: Draft/update a UX flow spec.
args: "<flow-slug>"
template: templates/extended/ux-flow-template.md
produces: specs/ux/{slug}.md
---

# /speckit.x.ux-flow

## Steps

1. Copy template to `specs/ux/{slug}.md`.
2. Cite personas from `specs/personas.md`.
3. Enumerate entry points.
4. Number each step with screen + input + system response.
5. Cover edge cases: no-network, slow-network, permission-denied, partial-input.
6. List telemetry events the flow must emit — sync with `specs/observability.md`.
7. Append to `specs/history.md`.
