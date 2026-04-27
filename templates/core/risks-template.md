---
title: "Risk Register"
maintainer: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
type: risks
---

# Risk Register

> Active risks only. Closed risks graduate to `history.md`.
> Add via `/speckit.x.risk "<description>"`.

## Scoring

- **Likelihood:** 1 (rare) – 5 (almost certain)
- **Impact:** 1 (minor) – 5 (catastrophic)
- **Score:** likelihood × impact (1–25). Treat ≥ 12 as priority.

## Active risks

| ID | Description | L | I | Score | Owner | Mitigation | Status | Source |
|---|---|---:|---:|---:|---|---|---|---|
| R-001 | {{risk}} | 3 | 4 | 12 | {{@who}} | {{action / link}} | open | `{ref:...}` |

## Closed risks

| ID | Description | Outcome | Closed on |
|---|---|---|---|

## Changelog

- {{today}} — draft.
