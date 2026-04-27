---
id: speckit.x.lessons
description: Append a new lesson-learned entry.
args: "<one-line insight>"
template: templates/core/lessons-template.md
produces: specs/lessons.md
mode: append
---

# /speckit.x.lessons

Capture a non-obvious insight. Append-only. Never delete — supersede via new entry.

## Steps

1. If `specs/lessons.md` missing → copy from template.
2. Parse `$ARGS` into `<title>`. Prompt user (if interactive) for:
   - **Context:** what were we doing?
   - **Lesson:** the insight
   - **Action:** rule/change adopted
3. Allocate next `L-NNN` id.
4. Append block:
   ```
   ### L-NNN — <title> (YYYY-MM-DD)

   **Context:** ...
   **Lesson:** ...
   **Action:** ...
   **References:** {ref:...}
   ```
5. Bump `updated:` in frontmatter.
6. Append to `specs/history.md`: `### YYYY-MM-DD — lesson L-NNN logged`.

## Pattern detection

If ≥ 3 lessons in last 30 days share a theme (keyword overlap ≥ 2), suggest an ADR.
