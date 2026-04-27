---
title: "History"
maintainer: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
type: history
---

# History

> Dated log of project evolution. Append-only. Human-readable. No frontmatter per entry.
> Populated automatically by `.claude/hooks/post-commit-history.sh` when `specs/` changes.
> Also append manually via `/speckit.x.history "<one-line summary>"`.

## Format

```
### YYYY-MM-DD — <headline>

<2-5 lines: what happened, who, why. Link to ADR / commit / PR if relevant.>
```

---

### {{today}} — Project scaffolded with specKitEnhanced

Initial constitution + 14 core templates installed via `specify-x init`.
