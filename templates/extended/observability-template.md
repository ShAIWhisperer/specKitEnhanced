---
spec_id: "observability"
title: "Observability"
status: draft
type: observability
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# Observability

> Metrics, logs, traces, SLOs, alerts. Single source of truth for "how we see the system."

## 1. SLOs

| Service | SLI | Target | Window |
|---|---|---|---|
| {{name}} | availability | 99.9% | 30d |
| {{name}} | p95 latency | < 200ms | 30d |

## 2. Golden Signals

| Signal | Metric | Threshold | Alert |
|---|---|---|---|
| Latency | p95_request_ms | > 500 for 5m | `{{alert_name}}` |
| Traffic | rps | — | dashboard only |
| Errors | error_rate | > 1% for 5m | `{{alert_name}}` |
| Saturation | cpu_pct | > 85% for 10m | `{{alert_name}}` |

## 3. Logs

- Structured (JSON). Required fields: `ts`, `level`, `service`, `trace_id`, `user_id` (hashed).
- Retention: {{N}} days hot, {{N}} days cold.
- PII redaction: {{rules}}

## 4. Traces

- Propagation: W3C TraceContext.
- Sampling: {{rate / rules}}
- Critical spans: {{list}}

## 5. Dashboards

| Name | Audience | Link |
|---|---|---|
| Service overview | oncall | {{url}} |
| Business KPIs | PM | {{url}} |

## 6. Alerts

| Alert | Trigger | Route | Runbook |
|---|---|---|---|
| `{{name}}` | {{condition}} | {{pager/slack}} | `{ref:specs/runbooks/<svc>.md#alert}` |

## 7. Synthetic Probes

- {{URL / endpoint}} — every {{interval}}, from {{regions}}.

## Changelog

- {{today}} — draft.
