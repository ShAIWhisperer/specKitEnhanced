---
spec_id: "research-{{slug}}"
title: "{{Research question}}"
status: draft
type: research
author: "@author"
created: "2026-04-24"
updated: "2026-04-24"
---

# {{Research question}}

> Evidence spec. Preserves the work behind a decision so the next person can audit or overturn it.
> If this research drives a decision, link it from the matching ADR.

## 1. Question

{{The exact question we are answering. One sentence.}}

## 2. Why now

{{Trigger — what prompted the research. Bug, spec ambiguity, architectural fork, vendor pitch.}}

## 3. Sources

| Source | Type | Reliability | Accessed |
|---|---|---|---|
| {{URL or title}} | docs / paper / interview / benchmark | {{high/med/low}} | {{YYYY-MM-DD}} |

## 4. Findings

### Finding F-1

{{Concrete observation. Quote or number.}}

**Evidence:** {{link or excerpt}}

### Finding F-2

{{...}}

## 5. Synthesis

{{2-4 paragraphs. What do the findings mean together? Where do they conflict? What's the confidence level?}}

## 6. Decision

{{Resulting choice. If ADR-worthy, open one and link it.}}

- Linked ADR: `{ref:specs/adr/ADR-NNNN-<slug>.md}`

## 7. Open Questions

- [ ] {{question the research did not close}}

## Changelog

- 2026-04-24 — draft.
