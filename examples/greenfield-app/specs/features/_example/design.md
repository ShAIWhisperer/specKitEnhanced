---
spec_id: "{{feature_slug}}-design"
title: "{{Feature title}} — Design"
status: draft
type: design
author: "@author"
created: "2026-04-24"
updated: "2026-04-24"
linked_spec: "{ref:specs/features/{{feature_slug}}/spec.md}"
---

# {{Feature title}} — Design

> UX + interaction design. Implementation mechanics live in `plan.md`.

## 1. UX Goals

{{What must the user feel/achieve. Tied to personas in `{ref:specs/personas.md}`.}}

## 2. Flow

{{Step-by-step user journey. Mermaid or numbered list.}}

1. User {{action}} → system shows {{state}}
2. User {{action}} → system shows {{state}}

Reference: `{ref:specs/ux/<flow>.md}` for full flow spec.

## 3. Components (UI)

| Component | Purpose | Source |
|---|---|---|
| {{Name}} | {{purpose}} | `{ref:src/components/...}` |

## 4. Interactions

- **{{Event}}** → {{system response}} → {{next state}}
- Loading states: {{placeholder/skeleton/spinner}}
- Error states: {{copy + recovery action}}
- Empty states: {{copy + CTA}}

## 5. Copy

| Key | Copy |
|---|---|
| `cta.primary` | {{text}} |
| `error.network` | {{text}} |

## 6. Accessibility

- Keyboard navigation: {{pattern}}
- Screen reader: {{aria-* rules}}
- Color contrast: WCAG {{AA|AAA}}

## 7. Open Questions

- [ ] [NEEDS CLARIFICATION] {{question}}

## Changelog

- 2026-04-24 — draft.
