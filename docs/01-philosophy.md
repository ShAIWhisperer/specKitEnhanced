# Philosophy

## Why another SDD thing?

spec-kit is strong, compact, and ships good bones (`/specify /plan /tasks /clarify /analyze /implement`). It does **not** ship the surrounding narrative layer — History, Lessons, ADRs, Runbooks, Risks — that a team actually opens week-to-week.

PM OS-compatible projects have a working spec engine but are PM-domain-locked.

specKitEnhanced distils 102 real portfolio projects into a minimal, markdown-only extension that stays compatible with both.

## Core beliefs

1. **Markdown is the artifact.** Not YAML. Not a DSL. Not a web UI.
2. **Templates come from shipped code, not imagination.** `specify-x harvest` is the source of truth.
3. **Frontmatter is the contract.** Schema-validated. Status lifecycle enforced.
4. **Append-only for narrative.** History never lies; it only grows.
5. **Compat > ownership.** `/speckit.*` stays upstream. Extension lives under `/speckit.x.*`.

## What this is not

- A replacement for `github/spec-kit`.
- A CI gate (not yet).
- A retrofit tool for existing projects.
- A monorepo framework.

## What this is

- 14 core + 7 extended MD templates, real and simple.
- A 5-agent Claude Code drop-in for spec authoring.
- A Python CLI for init, verify, harvest, bridge.
- A read-only portfolio miner that keeps the template library honest.
