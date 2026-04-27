---
spec_id: "constitution"
title: "{{project_name}} Constitution"
version: "0.1.0"
status: draft
type: constitution
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# {{project_name}} Constitution

> This is the root anchor spec. Every other spec links back here via `{ref:specs/constitution.md#PX}`.
> Amend via ADR + bump `version:` + append `history.md`.

## 1. Mission

{{ONE-PARAGRAPH mission. What this product exists for, who it serves, what success looks like.}}

## 2. Architectural Principles

### P1: {{Principle name, e.g. "Privacy by Default"}}

{{One paragraph. State the invariant and its enforcement point in code/config.}}

### P2: {{Principle name}}

{{One paragraph.}}

### P3: {{Principle name}}

{{One paragraph.}}

<!-- Add P4, P5, ... as needed. Each principle must be citable as `{ref:specs/constitution.md#PN}`. -->

## 3. Decision Framework

Every design decision passes these filters in order:

1. **{{Filter 1}}** — {{question it asks}}
2. **{{Filter 2}}** — {{question it asks}}
3. **{{Filter 3}}** — {{question it asks}}

If any filter fails, log an ADR at `specs/adr/ADR-NNNN-*.md` and reference it in `decisions.md`.

## 4. Glossary

| Term | Definition |
|---|---|
| **{{Term}}** | {{Definition, concrete and scoped to this product}} |

See also: `specs/glossary.md` for the full term inventory.

## 5. Spec Conventions

### Reference syntax

Use `{ref:path#section}` to link specs and code:
- `{ref:specs/constitution.md#P1}` — principle
- `{ref:src/core/module.py:SYMBOL}` — code symbol
- `{ref:specs/features/login/spec.md}` — another spec

### Status lifecycle

`draft → review → approved → implemented → deprecated`

Backward transitions allowed — log the reason in the spec's inline `## Changelog` section.

### Task ID format

`{{PROJECT-PREFIX}}-{number}` (e.g. `ACME-142`).

### Acceptance criteria

GIVEN/WHEN/THEN. Testable. Each maps to at least one task in `tasks.md`.

## 6. Template Minima

A project is **SDD-compliant** when:
- `specs/constitution.md` (this file) exists with filled mission + ≥ 3 principles
- `specs/history.md` exists
- `specs/decisions.md` exists (may be empty)
- At least one `specs/features/<slug>/{spec,plan,tasks}.md` triple exists
- `specs/architecture/` contains ≥ 1 architecture spec

Run `specify-x verify` to check.

## 7. Enforcement

- `.claude/hooks/pre-commit-sdd-lint.sh` — validates frontmatter schema before commit.
- `.claude/hooks/post-commit-history.sh` — appends to `history.md` when `specs/` changes.
- CI: `.github/workflows/speckit-x-verify.yml` — warn-only status check.

## 8. Amendment Process

1. Open ADR: `/speckit.x.adr --new "Amend constitution — <summary>"`.
2. Bump `version:` in this file's frontmatter.
3. Append dated entry to `specs/history.md`.
4. Update `specs/decisions.md` index.

## Changelog

<!-- Inline changelog. Append entries; don't overwrite. -->
- {{today}} — Constitution created from specKitEnhanced template.
