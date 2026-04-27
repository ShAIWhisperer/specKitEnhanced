# CLAUDE.md — specKitEnhanced repo context

## What this repo is

Opinionated Spec-Driven Development (SDD) framework. Fork-and-wrap of github/spec-kit v0.8.0 (MIT). Ships 14 core + 7 extended MD templates + 16 slash commands + 5 agents + Python CLI (`specify-x`).

## How to work here

- **Always run** `bash scripts/smoke.sh` before declaring done. It exercises init (core + extended), verify, harvest dry-run, bridge dry-run, idempotence.
- **Tests:** `pytest tests/ -v` — 9 tests, must stay green.
- **Harvest output** (`harvest/pattern-library.md`, `harvest/audit-matrix.csv`, `harvest/exemplar-excerpts/`) is generated, not hand-edited.
- **Templates** under `templates/` are the product. Changes here ripple into every project scaffolded via `specify-x init`. Review diffs carefully.
- **Do NOT** edit files under `examples/greenfield-app/` by hand — regenerate via `specify-x init ... --force`.

## File map

| Path | Purpose |
|---|---|
| `src/specify_x/cli.py` | argparse entry; subcommands: init, add, harvest, verify, bridge |
| `src/specify_x/harvest.py` | read-only portfolio miner; emits audit-matrix.csv + pattern-library.md |
| `src/specify_x/install.py` | template renderer; creates `specs/`, `.claude/agents/`, `.claude/commands/`, `.specify/` |
| `src/specify_x/verify.py` | frontmatter schema + ref-link + status-lifecycle lint |
| `src/specify_x/bridge_pmos.py` | symlinks templates into a target framework project, writes patch manifest |
| `src/specify_x/presets.py` | loads presets/core.yml + extended.yml with stdlib YAML fallback |
| `templates/core/*.md` | 14 core templates, installed by default |
| `templates/extended/*.md` | 7 extended templates, opt-in via `extended` preset |
| `extension/specKitEnhanced/extension.yml` | spec-kit extension manifest |
| `extension/specKitEnhanced/commands/*.md` | 16 slash command definitions |
| `agents/*.md` | 5 SDD agents (orchestrator + 4 specialists) |
| `schemas/*.json` | JSON Schema: frontmatter, spec, ADR |
| `presets/core.yml`, `presets/extended.yml` | what each preset installs |

## Key constraints

- **Stdlib-only** for the CLI. No pip install required to run `specify-x init`. PyYAML + jsonschema are optional.
- **Idempotent installs.** Re-running `init` never clobbers existing files unless `--force`.
- **Placeholder refs are skipped** in verify — `{ref:...}`, `{ref:<foo>}`, `{ref:specs/<slug>.md}` are examples, not errors.
- **Append-only narrative specs.** `history.md`, `lessons.md`, `decisions.md` grow; never rewrite.

## Known-good commands

```bash
# full suite
bash scripts/smoke.sh

# rebuild gold example
rm -rf examples/greenfield-app && \
  python3 -m src.specify_x.cli init examples/greenfield-app --preset core --force

# re-run harvest
python3 -m src.specify_x.cli harvest ~/projects
```

## Top-of-mind follow-ups

- Implement `specify-x add <kind>` properly (today it prints a copy hint).
- Wire `.claude/hooks/pre-commit-sdd-lint.sh` + `post-commit-history.sh` templates.
- Hook harvest output into template authoring loop — "re-harvest after portfolio grows, re-distill templates."
- Framework bridge: actually apply the 3 patches (specs.py, skill_engine.py, agent_orchestrator.py) rather than emitting them as a manifest. Requires `--pmos-root <path>`.
