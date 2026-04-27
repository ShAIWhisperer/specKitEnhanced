---
spec_id: "constitution"
title: "specKitEnhanced Constitution"
version: "0.1.0"
status: draft
type: constitution
author: "ShAIWhisperer"
created: 2026-04-24
updated: 2026-04-24
---

# specKitEnhanced Constitution

> Dogfood. specKitEnhanced uses its own constitution template.

## 1. Mission

Ship one house-branded SDD framework that works across 102+ projects. Distil proven MD patterns from the portfolio, expose them as templates/slash commands/agents, stay compatible with `github/spec-kit` and other SDD tooling.

## 2. Architectural Principles

### P1: Distil, don't invent

Templates come from real, shipping projects. Before authoring a template, run `specify-x harvest` and read `harvest/pattern-library.md`. Templates that have zero real-world precedent do not ship.

### P2: Markdown is the artifact

Templates are plain `.md`. No framework lock-in, no DSL. A user who deletes specKitEnhanced keeps working specs.

### P3: Frontmatter is the contract

Every spec carries YAML frontmatter matching `schemas/frontmatter.schema.json`. Status lifecycle is enforced: `draft → review → approved → implemented → deprecated` (and ADR flavor: `proposed → accepted → superseded`).

### P4: Append-only for narrative

`history.md`, `lessons.md`, `decisions.md` are append-only. To correct, append a new entry referencing the wrong one. To change an ADR, supersede with a new one.

### P5: Compatible, not monopolistic

`/speckit.*` commands and templates inherited from spec-kit stay verbatim. Extensions live under `/speckit.x.*`. Standard `{ref:}` cross-reference syntax and frontmatter shape are adopted from community conventions, not reinvented.

### P6: Stdlib-first CLI

The `specify-x` CLI runs on Python 3.11+ stdlib alone. PyYAML and jsonschema are optional upgrades. A user without `pip install` should still scaffold a project.

## 3. Decision Framework

Every design decision passes these filters in order:

1. **Harvest filter** — Does this pattern exist in ≥ 1 real portfolio project? If no, don't ship it.
2. **Idempotence filter** — Does re-running the command preserve user edits? If no, fix before shipping.
3. **Caveman filter** — Is the output under 80 lines of compact MD? If no, trim or split.
4. **Compat filter** — Does this break existing `/speckit.*` users? If yes, open an ADR.

If any filter fails, log an ADR at `specs/adr/ADR-NNNN-*.md`.

## 4. Glossary

| Term | Definition |
|---|---|
| **Preset** | A YAML bundle that declares templates + commands + agents + schemas to install. `core.yml`, `extended.yml`. |
| **Harvest** | Read-only audit of a portfolio directory that emits an adoption matrix + exemplar excerpts. |
| **Bridge** | Framework integration that symlinks templates into a target project and emits a patch manifest. |
| **SDD-compliant** | Project satisfies the minima in `templates/core/constitution-template.md §6`. |

## 5. Spec Conventions

Adopted conventions:

- `{ref:path#section}` — link to spec section
- `{ref:src/file.py:SYMBOL}` — link to code symbol
- Status lifecycle — `draft → review → approved → implemented → deprecated`
- Task ID format — `SKE-{NNN}` for specKitEnhanced internal tasks

## 6. Template Minima

This repo is SDD-compliant when:

- `README.md`, `CLAUDE.md`, `PLAN.md`, `constitution.md` present at root.
- `templates/core/*.md` — 14 files.
- `schemas/*.json` — 3 files.
- `presets/*.yml` — ≥ 2 files.
- `tests/` — ≥ 9 tests, all passing.
- `scripts/smoke.sh` — passes end-to-end.

Run `bash scripts/smoke.sh && pytest tests/` to verify.

## 7. Enforcement

- `scripts/smoke.sh` — must pass before commit.
- `pytest tests/` — must pass before commit.
- GitHub Action CI (future) — `.github/workflows/speckit-x-verify.yml`.

## 8. Amendment Process

1. Open ADR — `python3 -m src.specify_x.cli` (or manual write).
2. Bump `version:` in this file's frontmatter.
3. Add entry to a repo `specs/history.md` (to be created once repo dogfoods itself).

## Changelog

- 2026-04-24 — Constitution v0.1.0 drafted.
