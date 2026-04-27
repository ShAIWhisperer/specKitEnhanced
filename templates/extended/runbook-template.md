---
spec_id: "runbook-{{svc_slug}}"
title: "{{Service name}} — Runbook"
status: draft
type: runbook
owner: "{{@oncall}}"
author: "{{author}}"
created: "{{today}}"
updated: "{{today}}"
---

# {{Service name}} — Runbook

> Operational playbook. Read when paged. Every alert should link here.

## 1. Service Summary

- Purpose: {{one sentence}}
- Owning team: {{team}}
- SLO: {{uptime / latency target}}
- Dashboards: {{link}}
- Logs: {{link}}
- Source: `{ref:specs/architecture/<slug>.md}`

## 2. Alerts

| Alert | Severity | What it means | First action |
|---|---|---|---|
| {{name}} | SEV{{1-4}} | {{meaning}} | see §3.{{X}} |

## 3. Diagnostics

### 3.1 {{Symptom}}

**Symptoms:** {{what you see}}
**Likely cause:** {{why}}
**Verify:**
```
{{command / query}}
```
**Fix:**
```
{{command / query}}
```

### 3.2 {{Symptom}}

{{...}}

## 4. Recovery

### Restart
```
{{command}}
```

### Rollback
```
{{command — e.g. `vercel rollback` or `git revert`}}
```

## 5. Escalation

1. Page on-call: {{how}}
2. If unresolved in {{N}} min: escalate to {{who}}.
3. If customer-impacting: post to {{channel}}.

## 6. Post-incident

- Open lesson: `/speckit.x.lessons "<incident summary>"`.
- If root cause implies spec change: open ADR.

## Changelog

- {{today}} — draft.
