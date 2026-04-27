---
spec_id: "{{feature_slug}}-plan"
title: "{{Feature title}} — Plan"
status: draft
type: plan
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
linked_spec: "{ref:specs/features/{{feature_slug}}/spec.md}"
---

# {{Feature title}} — Technical Plan

> Inherits spec-kit plan-template. Gates: constitution check must pass before Phase 0.

## 1. Summary

{{2-3 sentences: spec restate + technical approach headline.}}

## 2. Technical Context

| Field | Value |
|---|---|
| Language / version | {{e.g. Python 3.14}} |
| Framework | {{e.g. FastAPI 0.110}} |
| Storage | {{e.g. SQLite / Postgres / ChromaDB}} |
| Testing | {{e.g. pytest 8.x}} |
| Target platform | {{e.g. macOS local / Linux container}} |
| Project type | {{single | web | mobile+api}} |
| Performance goal | {{e.g. p95 < 200ms}} |
| Scale/scope | {{e.g. 10 concurrent users}} |

## 3. Constitution Check

- [ ] Principle P1: {{pass/fail — reasoning}}
- [ ] Principle P2: {{pass/fail — reasoning}}
- [ ] Principle P3: {{pass/fail — reasoning}}

Any failure → add to **Complexity Tracking** below.

## 4. Approach

{{Phased breakdown. Phase 0 research → Phase 1 skeleton → Phase 2 story impl → Phase 3 polish.}}

### Phase 0 — Research
- [ ] {{open question from spec → research task}}

### Phase 1 — Foundation
- [ ] {{scaffolding work that blocks all story impls}}

### Phase 2 — User stories
Ordered by priority. Each story is independently shippable.
- [ ] US-1 — {{1-line plan}}
- [ ] US-2 — {{1-line plan}}

### Phase 3 — Polish
- [ ] Observability per `{ref:specs/observability.md}`
- [ ] Runbook per `{ref:specs/runbooks/<svc>.md}`

## 5. Project Structure (target layout)

```
{{proposed folder tree for this feature}}
```

## 6. Risks

- **R1** ({{high|med|low}}) — {{risk}} → mitigation: {{how}}

## 7. Complexity Tracking

Required only if constitution violations exist.

| Violation | Why justified | Compensation |
|---|---|---|

## 8. Open Questions

- [ ] [NEEDS CLARIFICATION] {{question}}

## Changelog

- {{today}} — draft.
