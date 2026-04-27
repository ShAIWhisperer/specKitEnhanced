---
spec_id: "api-{{api_slug}}"
title: "{{API name}} — Contract"
status: draft
type: api-contract
version: "0.1.0"
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# {{API name}} — Contract

> Contract-first. OpenAPI-compatible where possible. Breaking changes require version bump + ADR.

## 1. Overview

- Base URL: `{{https://api.example.com/v1}}`
- Transport: {{HTTP+JSON | gRPC | WebSocket | SSE}}
- Auth: {{scheme}} — see `{ref:specs/security.md#auth}`
- Versioning: {{semver in path / header / body}}

## 2. Endpoints

### `{{METHOD}} {{/path}}`

**Summary:** {{one-line purpose}}

**Request:**
```json
{
  "field": "value"
}
```

**Responses:**
| Status | Body | Meaning |
|---|---|---|
| 200 | `{{ResponseSchema}}` | success |
| 4xx | `ErrorSchema` | client error (see §4) |
| 5xx | `ErrorSchema` | server error |

**Idempotency:** {{yes/no — key header if yes}}
**Rate limit:** {{limit}}
**Auth scope:** {{required scope/role}}

<!-- Repeat per endpoint -->

## 3. Schemas

```yaml
{{SchemaName}}:
  type: object
  required: [field1]
  properties:
    field1:
      type: string
```

Refers to `{ref:specs/data-model.md}` where applicable.

## 4. Errors

| Code | HTTP | Message | Retriable |
|---|---|---|---|
| `VALIDATION` | 400 | Input failed validation | no |
| `RATE_LIMIT` | 429 | Try again later | yes (backoff) |

## 5. Versioning & Deprecation

- Policy: {{semver / date-based}}
- Deprecation window: {{N months}} — old version returns `Deprecation` header.
- Breaking change rule: bump major, open ADR.

## Changelog

- {{today}} — draft.
