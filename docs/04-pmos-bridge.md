# PM OS Bridge

specKitEnhanced installs into any PM OS-compatible project as a template source. The PM OS skill engine can then emit specKitEnhanced-shaped outputs.

## What `specify-x bridge` does

1. Creates `<pmos-root>/.specify-x/templates/` as a symlink to this repo's `templates/` directory.
2. Writes `.specify-x/bridge-patches.json` — a manifest describing three PM OS source-code patches that must be applied manually (we do not edit PM OS code automatically, for auditability).

## Usage

```bash
specify-x bridge --pmos-root /path/to/your-pm-os
specify-x bridge --pmos-root /path/to/your-pm-os --dry-run
```

## Required PM OS code patches

### 1. `backend/app/api/specs.py`

At the top of the module:
```python
import os

SPECKIT_X_TEMPLATE_DIR = os.getenv("SPECKIT_X_TEMPLATE_DIR")
```

In whatever function resolves `SEED_SPECS_DIR`, prefer the env var when set:
```python
if SPECKIT_X_TEMPLATE_DIR:
    SEED_SPECS_DIR = Path(SPECKIT_X_TEMPLATE_DIR) / "core"
else:
    SEED_SPECS_DIR = settings.project_root / "specs"
```

### 2. `backend/app/core/skill_engine.py`

Extend `OUTPUT_DIR_TO_CATEGORY`:
```python
OUTPUT_DIR_TO_CATEGORY = {
    ...existing entries...,
    "sdd": "SDD Framework",
}
```

Same for `SKILL_CATEGORY_OVERRIDES` so any skill with `category: sdd` surfaces under the new "SDD Framework" UI category.

### 3. `backend/app/core/agent_orchestrator.py`

Register the 5 SDD agents (`sdd-orchestrator`, `sdd-architect`, `sdd-historian`, `sdd-risk-analyst`, `sdd-scribe`) as an additional domain alongside the existing domains. The agents' prompt files live at `.claude/agents/` — load them via the usual agent loader pattern.

## Env var hint

After `specify-x bridge`, the CLI prints:
```
export SPECKIT_X_TEMPLATE_DIR=/path/to/your-pm-os/.specify-x/templates
```

Add that to your shell profile or PM OS's `.env` before starting the backend.

## Flow

1. User in PM OS chat says "draft an architecture spec for the agent orchestrator".
2. PM OS `AgentOrchestrator` routes to `sdd-architect` (new SDD domain).
3. `sdd-architect` reads `SPECKIT_X_TEMPLATE_DIR/core/architecture-template.md`.
4. Output saved as a PM OS artifact with specKitEnhanced frontmatter (`spec_id`, `title`, `status`, `type`, `author`, `created`, `updated`, `depends_on`).
5. Same output is valid as a free-standing `specs/architecture/<slug>.md` outside PM OS.

## Compatibility guarantee

PM OS specs and specKitEnhanced specs are the same shape. You can move a spec between environments without edits. `{ref:}` syntax works identically in both.
