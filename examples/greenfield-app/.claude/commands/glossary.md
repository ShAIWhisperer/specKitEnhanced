---
id: speckit.x.glossary
description: Add a term to the glossary.
args: "<term> [definition]"
template: templates/core/glossary-template.md
produces: specs/glossary.md
mode: append
---

# /speckit.x.glossary

## Steps

1. If `specs/glossary.md` missing → copy template.
2. Check for duplicate term (case-insensitive). If exists → suggest edit, don't duplicate.
3. Insert row alphabetically.
4. If term appears in ≥ 2 existing specs, add `Cite` column references.
5. Bump `updated:`.
