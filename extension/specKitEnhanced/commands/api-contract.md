---
id: speckit.x.api-contract
description: Draft/update an API contract spec (endpoints, schemas, errors).
args: "<api-slug>"
template: templates/extended/api-contract-template.md
produces: specs/contracts/{slug}.md
---

# /speckit.x.api-contract

Contract-first API spec. Keep OpenAPI-compatible.

## Steps

1. Copy template to `specs/contracts/{slug}.md`.
2. Auto-populate endpoints when possible (parse route handlers).
3. For each endpoint: request/response schemas + error codes + auth scope + idempotency + rate limit.
4. Cross-reference `specs/data-model.md` for entity schemas.
5. Bump `version:` in frontmatter on any breaking change → must also open an ADR.
6. Append to `specs/history.md`.
