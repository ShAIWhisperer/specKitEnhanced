---
id: speckit.x.observability
description: Draft/update the observability spec (SLOs, signals, alerts).
args: "[scope]"
template: templates/extended/observability-template.md
produces: specs/observability.md
---

# /speckit.x.observability

## Steps

1. If `specs/observability.md` exists → update.
2. Else copy template.
3. Fill SLOs per service in `specs/architecture/*`.
4. Golden Signals rows: Latency, Traffic, Errors, Saturation — each with metric name + threshold + alert id.
5. Every alert listed here must have matching diagnostic in `specs/runbooks/*`.
6. Log retention + PII redaction rules explicit.
7. Append to `specs/history.md`.
