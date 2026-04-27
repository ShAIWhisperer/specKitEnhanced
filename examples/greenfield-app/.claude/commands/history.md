---
id: speckit.x.history
description: Append a dated entry to history.md.
args: "<headline> [body]"
template: templates/core/history-template.md
produces: specs/history.md
mode: append
---

# /speckit.x.history

Append dated entry. Called manually or by `.claude/hooks/post-commit-history.sh`.

## Steps

1. If `specs/history.md` missing → copy template.
2. Append:
   ```
   ### YYYY-MM-DD — <headline>

   <body — 2-5 lines. Commit/PR link if known.>
   ```
3. Bump `updated:` in frontmatter.

## Guardrail

- Do not batch multiple events into one entry. One event = one entry.
- Entries are immutable. To correct, append a new "correction" entry referencing the wrong one.
