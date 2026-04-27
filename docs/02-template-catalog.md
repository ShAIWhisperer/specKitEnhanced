# Template Catalog

## Core (14) — installed by `core` preset

| Template | File | Type | Purpose |
|---|---|---|---|
| Constitution | `specs/constitution.md` | constitution | Mission + principles + decision framework |
| Spec/PRD | `specs/features/<slug>/spec.md` | feature | User stories + acceptance + scope |
| Plan | `specs/features/<slug>/plan.md` | plan | Technical approach + phases |
| Tasks | `specs/features/<slug>/tasks.md` | tasks | Executable task list |
| Architecture | `specs/architecture/<slug>.md` | architecture | Subsystem: components, flow, invariants |
| Design | `specs/features/<slug>/design.md` | design | UX + interaction design |
| System | `specs/system.md` | system | C4-L1 overview, external deps |
| History | `specs/history.md` | history | Append-only dated log |
| Lessons | `specs/lessons.md` | lessons | Append-only insight log |
| Decisions | `specs/decisions.md` | decisions | ADR index |
| Personas | `specs/personas.md` | personas | Persona cards |
| Glossary | `specs/glossary.md` | glossary | Shared vocabulary |
| Research | `specs/research/<slug>.md` | research | Evidence log |
| Risks | `specs/risks.md` | risks | Active risk register |

## Extended (7) — installed by `pm-os` preset

| Template | File | Type | Purpose |
|---|---|---|---|
| Data Model | `specs/data-model.md` | data-model | Entities, relations, migrations |
| API Contract | `specs/contracts/<api>.md` | api-contract | OpenAPI-compat endpoints |
| UX Flow | `specs/ux/<flow>.md` | ux-flow | End-to-end user journey |
| Runbook | `specs/runbooks/<svc>.md` | runbook | Oncall playbook |
| Security | `specs/security.md` | security | STRIDE threat model |
| Observability | `specs/observability.md` | observability | SLOs + alerts |
| ADR (per-decision) | `specs/adr/ADR-NNNN-<slug>.md` | adr | Single immutable decision |

## Dependency graph

```
constitution.md
  ├── spec.md ──── design.md ──── ux-flow
  │   ├── plan.md ──── tasks.md
  │   └── data-model ──── api-contract
  ├── architecture/*.md ──── system.md
  │   ├── security.md ──── risks.md
  │   └── observability.md ──── runbooks/*.md
  ├── decisions.md ──── adr/ADR-*.md ──── research/*.md
  └── history.md · lessons.md · personas.md · glossary.md
```

All specs reference the constitution. The rest forms a partial order.

## Frontmatter contract

See `schemas/frontmatter.schema.json`. Required: `title`, `status`, `type`. Optional: `spec_id`, `author`, `created`, `updated`, `depends_on`, `version`, `supersedes`, `superseded_by`, `implemented_by`, `linked_spec`, `linked_plan`, `owner`, `maintainer`, `adr_id`.

`status` is *not* required for narrative singletons: `history`, `lessons`, `decisions`, `personas`, `glossary`, `risks`.
