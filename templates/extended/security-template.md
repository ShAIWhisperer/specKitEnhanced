---
spec_id: "security"
title: "Security & Threat Model"
status: draft
type: security
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
depends_on:
  - "{ref:specs/constitution.md}"
  - "{ref:specs/system.md}"
---

# Security & Threat Model

> STRIDE-based. One project-wide file. Expand sections per subsystem as needed.

## 1. Assets

| Asset | Classification | Store | Encryption |
|---|---|---|---|
| {{what}} | {{PII / secret / public}} | {{where}} | {{at rest / in transit}} |

## 2. Threat Model (STRIDE)

| Threat | Category | Asset | Likelihood | Impact | Mitigation |
|---|---|---|---:|---:|---|
| {{Spoofed identity}} | Spoofing | Auth token | M | H | {{MFA + short-lived tokens}} |
| {{...}} | Tampering | | | | |
| {{...}} | Repudiation | | | | |
| {{...}} | Information Disclosure | | | | |
| {{...}} | Denial of Service | | | | |
| {{...}} | Elevation of Privilege | | | | |

## 3. Auth

- Scheme: {{OAuth2 / JWT / API key}}
- Session: {{duration, rotation}}
- RBAC model: {{roles → permissions}} — see `{ref:specs/data-model.md#Role}`

## 4. Secrets

- Store: {{env / vault / KMS}}
- Rotation: {{cadence}}
- Never-commit list: {{patterns}}

## 5. Dependencies

- Scanner: {{e.g. `npm audit`, `pip-audit`}}
- Cadence: {{weekly / on PR}}
- CVE triage: severity ≥ {{high}} → patch within {{N}} days.

## 6. Compliance

- {{SOC2 / GDPR / HIPAA}} — applicable: {{yes/no}}, controls mapped in `{ref:...}`

## 7. Incident Response

See `{ref:specs/runbooks/security-incident.md}`.

## Changelog

- {{today}} — draft.
