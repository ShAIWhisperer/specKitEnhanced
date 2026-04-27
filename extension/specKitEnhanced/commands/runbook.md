---
id: speckit.x.runbook
description: Draft/update operational runbook for a service.
args: "<service-slug>"
template: templates/extended/runbook-template.md
produces: specs/runbooks/{svc}.md
---

# /speckit.x.runbook

Oncall-facing runbook. Every alert in `specs/observability.md` should link here.

## Steps

1. Derive slug from `$ARGS`.
2. Copy template to `specs/runbooks/{slug}.md`.
3. Fill:
   - Service Summary (owner, SLO, dashboards, logs).
   - Alerts — mirror rows from `specs/observability.md`.
   - Diagnostics (symptom → cause → verify → fix).
   - Recovery (restart / rollback commands, tested).
   - Escalation.
4. Cross-link to `specs/architecture/<service>.md` and `specs/observability.md`.
5. Append to `specs/history.md`.
