---
spec_id: "ux-{{flow_slug}}"
title: "{{Flow name}} — UX Flow"
status: draft
type: ux-flow
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# {{Flow name}} — UX Flow

> End-to-end flow spec. Links personas → screens → success/failure paths.

## 1. Goal

{{One-sentence outcome the user is trying to achieve.}}

## 2. Personas

- `{ref:specs/personas.md#P1}` — {{why this persona uses this flow}}

## 3. Entry Points

- {{URL / screen / deep link}}
- {{push / email / share}}

## 4. Steps

### Step 1 — {{Name}}

- **Screen:** {{screen identifier}}
- **User input:** {{what they do}}
- **System response:** {{what happens}}
- **Next:** Step 2 on success, `Error A` on failure.

### Step 2 — ...

## 5. Success Path

```
Entry → Step 1 → Step 2 → ... → Confirmation
```

## 6. Edge Cases

| Case | Trigger | Handling |
|---|---|---|
| {{name}} | {{when}} | {{what we show/do}} |

## 7. Error States

- `Error A` — {{what the user sees, recovery action}}

## 8. Telemetry

- Events: `{{flow_started}}`, `{{flow_completed}}`, `{{flow_abandoned}}` at Step N
- Funnel target: {{%}} completion

## Changelog

- {{today}} — draft.
