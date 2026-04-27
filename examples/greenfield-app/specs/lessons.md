---
title: "Lessons Learned"
maintainer: "@author"
created: "2026-04-24"
updated: "2026-04-24"
type: lessons
---

# Lessons Learned

> Append-only log of non-obvious insights. One entry per lesson.
> Trigger: append via `/speckit.x.lessons "<insight>"` after incident, ship, or surprise.
> Feedback loop: every 2 weeks, review for patterns → candidate ADR or constitution amendment.

## Entry format

```
### <ID> — <Title> (YYYY-MM-DD)

**Context:** <what we were doing>
**Lesson:** <what we learned — the insight itself>
**Action:** <rule/change adopted as a result>
**References:** {ref:...}
```

---

### L-001 — Example lesson (2026-04-24)

**Context:** Setting up specKitEnhanced for the first time.
**Lesson:** Harvesting real portfolio MD patterns beats inventing templates from scratch — actual adoption data catches the gap between "what we say we use" and "what we actually reach for."
**Action:** Run `specify-x harvest` before any template rewrite. Pattern-library.md is the source of truth, not intuition.
**References:** `{ref:specs/constitution.md#P2}`
