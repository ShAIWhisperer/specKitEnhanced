---
id: speckit.x.adr
description: Open a new ADR or update existing.
args: "[--new] <title> | <ADR-NNNN> <field=value>"
template: templates/extended/adr/ADR-NNNN-slug-template.md
produces: specs/adr/ADR-{nnnn}-{slug}.md
appends_to: specs/decisions.md
---

# /speckit.x.adr

Architecture Decision Records. Immutable once `accepted` — to change, supersede with a new ADR.

## Modes

- `--new "<title>"` — allocate next `ADR-NNNN`, scaffold file, append row to `specs/decisions.md`.
- `<ADR-NNNN> status=accepted` — update existing ADR status. Allowed transitions: `proposed → accepted | rejected`, `accepted → superseded (by ADR-XXXX)`.

## Steps (new ADR)

1. Read `specs/decisions.md`. Find max `ADR-NNNN`. `next = NNNN + 1` (zero-padded 4 digits).
2. Derive `slug` from title (lowercase, hyphenate, strip stop words).
3. Create `specs/adr/ADR-{next}-{slug}.md` from template.
4. Append row to `specs/decisions.md` index:
   ```
   | ADR-{next} | {title} | proposed | {today} | — | — | specs/adr/ADR-{next}-{slug}.md |
   ```
5. Prompt user for Context / Decision / Rationale / Alternatives (interactive).
6. Set `status: proposed`.
7. Append to `specs/history.md`: `### {today} — ADR-{next} proposed: {title}`.

## Steps (supersede)

1. Verify target ADR is `accepted`.
2. Open a new ADR (mode A) referencing `supersedes: ADR-XXXX`.
3. Update old ADR frontmatter: `status: superseded`, `superseded_by: ADR-YYYY`.
4. Update both rows in `specs/decisions.md`.

## Validation

- `{ref:...}` in Rationale/Alternatives must resolve.
- Research link recommended for any `accepted` ADR — if missing, warn.
