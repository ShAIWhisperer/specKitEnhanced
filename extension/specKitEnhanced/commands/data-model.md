---
id: speckit.x.data-model
description: Draft/update data model spec (entities, relations, migrations).
args: "[scope]"
template: templates/extended/data-model-template.md
produces: specs/data-model.md
---

# /speckit.x.data-model

## Steps

1. If `specs/data-model.md` exists → update.
2. Else copy template.
3. Populate Entities from code:
   - Scan ORM models / SQL migrations / type definitions (grep for `class.*Model`, `CREATE TABLE`, `interface`, `type.*=`).
   - One entity block per class/table.
4. Populate Relations.
5. Populate Migrations — link real migration files.
6. Link every entity referenced in `specs/contracts/*.md` back here.
7. Append to `specs/history.md`.
