---
spec_id: "data-model{{#if feature_slug}}-{{feature_slug}}{{/if}}"
title: "Data Model{{#if feature_title}} — {{feature_title}}{{/if}}"
status: draft
type: data-model
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# Data Model

> Entities, fields, relations, migrations. One file project-wide OR one per feature.

## 1. Entities

### `{{EntityName}}`

| Field | Type | Constraints | Notes |
|---|---|---|---|
| `id` | UUID | PK, not null | |
| `{{field}}` | {{type}} | {{nullable, unique, default}} | |

**Indexes:** {{list}}
**Lifecycle:** {{create/update/delete rules}}

## 2. Relations

```
{{EntityA}} 1 ──< {{EntityB}}
{{EntityA}}.id = {{EntityB}}.{{fk}}
```

## 3. Invariants

- INV-1: {{rule that must always hold across rows}}

## 4. Migrations

| # | Description | File | Status |
|---|---|---|---|
| 001 | Initial schema | `{ref:migrations/001_init.sql}` | applied |

## 5. Access Patterns

- **Read:** {{query shape}} — p95 target {{ms}}
- **Write:** {{rate}} — consistency model {{sync/async/eventual}}

## 6. Retention

{{How long data lives, when purged, by what process.}}

## Changelog

- {{today}} — draft.
