---
id: speckit.x.risk
description: Add/update entry in risk register.
args: "<description> [L=1-5] [I=1-5] [owner=@who]"
template: templates/core/risks-template.md
produces: specs/risks.md
mode: append
---

# /speckit.x.risk

## Steps

1. If `specs/risks.md` missing → copy template.
2. Parse `$ARGS`. Default L=3, I=3 if not supplied.
3. Allocate `R-NNN`. Compute score = L × I.
4. Append row. Status `open`.
5. If score ≥ 12 → warn user and suggest opening mitigation task in current sprint.
6. Append to `specs/history.md`: `### YYYY-MM-DD — risk R-NNN added (score=X)`.

## Close a risk

`/speckit.x.risk --close R-NNN "<outcome>"` → moves row to "Closed risks" table.
