---
spec_id: "arch-{{slug}}"
title: "{{Subsystem name}} — Architecture"
status: draft
type: architecture
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
depends_on:
  - "{ref:specs/constitution.md}"
---

# {{Subsystem name}} — Architecture

## 1. Context

{{Why this subsystem exists. Which principle(s) from constitution it implements. 2-4 sentences.}}

## 2. Components

| Component | File/Module | Responsibility |
|---|---|---|
| {{Name}} | `{ref:src/...}` | {{one-line}} |

## 3. Data Flow

```
{{ASCII or mermaid. Show who calls whom, which direction data moves.}}
```

Example:
```
[Client] --WS--> [Orchestrator] --dispatch--> [Worker pool]
                         |                          |
                         v                          v
                    [Event log]               [Result store]
```

## 4. Interfaces

### Inbound
- {{endpoint/API/event — consumer, schema, version}}

### Outbound
- {{call/write/publish — target, schema, version}}

## 5. Invariants

- INV-1: {{invariant — must always hold}}
- INV-2: {{invariant}}

## 6. Trade-offs

| Decision | Chose | Over | Because |
|---|---|---|---|
| {{area}} | {{X}} | {{Y}} | {{reason}} — see `{ref:specs/adr/ADR-NNNN-*.md}` |

## 7. Non-functional

- Scale: {{target}}
- Latency: {{target}}
- Failure modes: {{which, how handled}}
- Observability: see `{ref:specs/observability.md}`

## 8. Related

- `{ref:specs/system.md}`
- `{ref:specs/architecture/<other>.md}`
- `{ref:specs/decisions.md}`

## Changelog

- {{today}} — draft.
