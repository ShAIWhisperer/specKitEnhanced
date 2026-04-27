---
id: speckit.x.system
description: Draft/update the project-wide System Overview spec.
args: "[brief]"
template: templates/core/system-template.md
produces: specs/system.md
---

# /speckit.x.system

Author or update the C4-L1 system overview spec. One file per project.

## Inputs

- Read `specs/constitution.md`.
- Scan `specs/architecture/*.md` — every subsystem listed there must appear in §3.
- External services used (grep for HTTP clients / SDKs).

## Steps

1. If `specs/system.md` exists → update in place; bump `updated:`; append changelog.
2. Else copy template, fill placeholders.
3. Fill sections:
   - **System Context (C4-L1)** — product box + users + external systems. ASCII or mermaid.
   - **External Dependencies** — table with failure impact filled.
   - **Subsystems** — link every `specs/architecture/*.md` present.
   - **Deployment Topology** — where this runs in production.
   - **Boundaries** — trust, data, product (multi-tenant).
   - **Lifecycle** — startup, shutdown, upgrade.
4. Cross-link to `specs/security.md` and `specs/observability.md` if they exist.
5. Append to `specs/history.md`.
