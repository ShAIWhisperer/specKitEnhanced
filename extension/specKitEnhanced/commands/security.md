---
id: speckit.x.security
description: Draft/update the project-wide Security & Threat Model spec.
args: "[scope]"
template: templates/extended/security-template.md
produces: specs/security.md
---

# /speckit.x.security

STRIDE-based threat model + auth + secrets + dependency hygiene.

## Steps

1. Read `specs/system.md` → identify trust/data boundaries.
2. Read `specs/data-model.md` → classify assets.
3. If `specs/security.md` exists → update in place.
4. Else copy template.
5. Fill STRIDE rows — at least 1 per category (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation).
6. For any row with score ≥ 12 → open a risk via `/speckit.x.risk`.
7. Append to `specs/history.md`.

## Validation

- Every asset in §1 appears in ≥ 1 STRIDE row.
- Every high-severity threat links to a mitigation spec or runbook.
