---
spec_id: "system"
title: "{{project_name}} — System Overview"
status: draft
type: system
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
depends_on:
  - "{ref:specs/constitution.md}"
---

# {{project_name}} — System Overview

> System-level spec. One file per project. Index into `specs/architecture/*` for subsystem detail.

## 1. System Context (C4-L1)

```
{{Mermaid or ASCII: product box + external systems + users}}
```

## 2. External Dependencies

| External | Purpose | Coupling | Failure impact |
|---|---|---|---|
| {{Service}} | {{why}} | {{sync/async/cache}} | {{what breaks if down}} |

## 3. Subsystems

| Subsystem | Spec | Owner |
|---|---|---|
| {{name}} | `{ref:specs/architecture/<slug>.md}` | {{who}} |

## 4. Deployment Topology

{{How the system runs. Single binary? Monorepo services? Containers? Cron? Describe the shipping shape.}}

## 5. Boundaries

- **Trust boundary**: {{where untrusted input enters}}
- **Data boundary**: {{what crosses host/network/disk}}
- **Product boundary**: {{multi-tenant isolation model, if any}}

## 6. Cross-cutting Concerns

- Auth: see `{ref:specs/security.md#auth}`
- Telemetry: see `{ref:specs/observability.md}`
- Config: see `{ref:specs/architecture/config.md}` (if split)

## 7. Lifecycle

- Startup: {{what happens}}
- Shutdown: {{graceful drain steps}}
- Upgrade: {{migration pattern}} — see `{ref:specs/runbooks/upgrade.md}`

## Changelog

- {{today}} — draft.
