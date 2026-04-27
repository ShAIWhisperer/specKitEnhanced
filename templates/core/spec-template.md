---
spec_id: "{{feature_slug}}"
title: "{{Feature title}}"
status: draft
type: feature
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
depends_on:
  - "{ref:specs/constitution.md}"
---

# {{Feature title}} — Spec

> Inherits spec-kit spec-template structure. Compact by default.

## 1. Problem

{{Who hurts, what breaks, why now. 2-4 sentences. No hypothetical users.}}

## 2. User Stories

### US-1 ({{priority: P1|P2|P3}})

**As a** {{persona from `specs/personas.md`}}
**I want** {{capability}}
**So that** {{outcome}}

**Acceptance (GIVEN/WHEN/THEN):**
```
GIVEN {{precondition}}
WHEN {{action}}
THEN {{observable result}}
```

<!-- Repeat US-N blocks. Each must be independently testable. -->

## 3. Scope

### In scope
- {{bullet}}

### Out of scope
- {{bullet}} — reason: {{why excluded}}

## 4. Success Criteria

| ID | Metric | Target | Source |
|---|---|---|---|
| SC-1 | {{metric}} | {{target}} | {{how measured}} |

## 5. Dependencies

- `{ref:specs/features/<other>/spec.md}` — {{why linked}}
- `{ref:specs/architecture/<subsystem>.md}` — {{why linked}}

## 6. Open Questions

- [ ] [NEEDS CLARIFICATION] {{question}}

## 7. Non-functional

- Performance: {{target}}
- Security: see `{ref:specs/security.md}`
- Observability: see `{ref:specs/observability.md}`

## Changelog

- {{today}} — draft created.
