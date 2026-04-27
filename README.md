# specKitEnhanced

> Opinionated Spec-Driven Development (SDD) framework. Extends [github/spec-kit](https://github.com/github/spec-kit) with the narrative layer teams actually reach for: History, Architecture, ADRs, Runbooks, Risks, Security, Observability — distilled from 102 real projects.

---

## Why this exists

`github/spec-kit` ships solid bones: `/speckit.specify /plan /tasks /clarify /analyze /implement`. It does not ship the surrounding docs a team opens week to week.

**specKitEnhanced adds:**

- 14 core + 7 extended markdown templates covering every major spec category
- 16 slash commands under `/speckit.x.*` that compose with, not replace, upstream spec-kit
- 5 Claude Code sub-agents for spec authoring delegation
- A Python CLI (`specify-x`) for scaffolding, linting, portfolio mining, and framework bridging
- JSON Schema validation for frontmatter + status lifecycle enforcement

Everything is **plain markdown**. No web UI. No SaaS. Works in any editor.

---

## Quick start

### Install

```bash
pip install -e .
# or
uv tool install .
```

### Scaffold a new project

```bash
# Core preset (14 templates + 10 commands + 5 agents)
specify-x init myproject --preset core

# Full preset (21 templates + 16 commands + 5 agents + framework bridge)
specify-x init myproject --preset extended

# Scaffold in current directory
specify-x init . --preset core --project-name "My App"
```

### Without installing (dev mode)

```bash
python3 -m src.specify_x.cli init . --preset core --project-name "my-project"
python3 -m src.specify_x.cli verify .
python3 -m src.specify_x.cli harvest ~/projects
```

---

## What ships

| Preset | Templates | Commands | Agents |
|--------|----------:|--------:|-------:|
| `core` | 14 | 10 | 5 |
| `extended` | 21 | 16 | 5 |

---

## Template catalog

### Core (14) — `core` and `extended` presets

| Template | Installed at | Purpose |
|----------|-------------|---------|
| **constitution** | `specs/constitution.md` | Mission, principles, decision framework — every other spec references this |
| **spec / PRD** | `specs/features/<slug>/spec.md` | User stories, acceptance criteria, scope |
| **plan** | `specs/features/<slug>/plan.md` | Technical approach, phases, milestones |
| **tasks** | `specs/features/<slug>/tasks.md` | Executable task list with status |
| **architecture** | `specs/architecture/<slug>.md` | Subsystem components, data flow, invariants |
| **design** | `specs/features/<slug>/design.md` | UX and interaction design |
| **system** | `specs/system.md` | C4-L1 system overview, external dependencies |
| **history** | `specs/history.md` | Append-only dated project log |
| **lessons** | `specs/lessons.md` | Append-only insight log |
| **decisions** | `specs/decisions.md` | ADR index |
| **personas** | `specs/personas.md` | User persona cards |
| **glossary** | `specs/glossary.md` | Shared vocabulary |
| **research** | `specs/research/<slug>.md` | Evidence and discovery log |
| **risks** | `specs/risks.md` | Active risk register |

### Extended (7) — `extended` preset only

| Template | Installed at | Purpose |
|----------|-------------|---------|
| **data-model** | `specs/data-model.md` | Entities, relations, migration notes |
| **api-contract** | `specs/contracts/<api>.md` | OpenAPI-compatible endpoint specs |
| **ux-flow** | `specs/ux/<flow>.md` | End-to-end user journey |
| **runbook** | `specs/runbooks/<svc>.md` | On-call playbook |
| **security** | `specs/security.md` | STRIDE threat model |
| **observability** | `specs/observability.md` | SLOs, alerts, dashboards |
| **ADR** | `specs/adr/ADR-NNNN-<slug>.md` | Single immutable architectural decision |

### Template dependency graph

```
constitution.md
  ├── spec.md ──── design.md ──── ux-flow
  │   ├── plan.md ──── tasks.md
  │   └── data-model ──── api-contract
  ├── architecture/*.md ──── system.md
  │   ├── security.md ──── risks.md
  │   └── observability.md ──── runbooks/*.md
  ├── decisions.md ──── adr/ADR-*.md ──── research/*.md
  └── history.md · lessons.md · personas.md · glossary.md
```

---

## Frontmatter contract

All specs use validated YAML frontmatter (`schemas/frontmatter.schema.json`).

**Required fields:** `title`, `status`, `type`

**Optional fields:** `spec_id`, `author`, `created`, `updated`, `depends_on`, `version`, `supersedes`, `superseded_by`, `implemented_by`, `linked_spec`, `linked_plan`, `owner`, `maintainer`, `adr_id`

**Status lifecycle:** `draft` → `review` → `approved` → `implemented` → `superseded`

Narrative singletons (`history`, `lessons`, `decisions`, `personas`, `glossary`, `risks`) do not require a `status` field.

**Cross-references** use `{ref:specs/<slug>.md}` syntax. The `verify` command checks all non-placeholder refs resolve to real files.

---

## Slash commands

Drop the `extension/specKitEnhanced/` folder into any spec-kit project to activate these commands in Claude Code:

| Command | Agent | Creates / Updates |
|---------|-------|------------------|
| `/speckit.x.architecture` | sdd-architect | `specs/architecture/<slug>.md` |
| `/speckit.x.system` | sdd-architect | `specs/system.md` |
| `/speckit.x.design` | sdd-architect | `specs/features/<slug>/design.md` |
| `/speckit.x.data-model` | sdd-architect | `specs/data-model.md` |
| `/speckit.x.api-contract` | sdd-architect | `specs/contracts/<api>.md` |
| `/speckit.x.history` | sdd-historian | appends to `specs/history.md` |
| `/speckit.x.lessons` | sdd-historian | appends to `specs/lessons.md` |
| `/speckit.x.adr` | sdd-historian | `specs/adr/ADR-NNNN-<slug>.md` + updates index |
| `/speckit.x.risk` | sdd-risk-analyst | `specs/risks.md` |
| `/speckit.x.security` | sdd-risk-analyst | `specs/security.md` |
| `/speckit.x.observability` | sdd-risk-analyst | `specs/observability.md` |
| `/speckit.x.runbook` | sdd-risk-analyst | `specs/runbooks/<svc>.md` |
| `/speckit.x.personas` | sdd-scribe | `specs/personas.md` |
| `/speckit.x.glossary` | sdd-scribe | `specs/glossary.md` |
| `/speckit.x.research` | sdd-scribe | `specs/research/<slug>.md` |
| `/speckit.x.ux-flow` | sdd-scribe | `specs/ux/<flow>.md` |
| `/speckit.x.fill-all` | sdd-orchestrator | bulk autofill all spec files from codebase |

### `/speckit.x.fill-all`

Most powerful command. Scans the project codebase, delegates to all 4 specialist agents in parallel, and fills every unfilled spec template. Skips files with ≥ 200 chars of non-placeholder content. All output stays in `draft` status.

```
/speckit.x.fill-all
/speckit.x.fill-all --dry-run   # preview only, no writes
```

---

## Agents

Five Claude Code sub-agents install into `.claude/agents/`:

| Agent | Handles |
|-------|---------|
| **sdd-orchestrator** | Routes commands, enforces constitution + frontmatter, validates refs |
| **sdd-architect** | Architecture, system, design, data-model, api-contract |
| **sdd-historian** | History, lessons, ADRs — append-only docs |
| **sdd-risk-analyst** | Risks, security (STRIDE), observability, runbooks |
| **sdd-scribe** | Personas, glossary, research, UX flows |

The orchestrator enforces three rules before any write:
1. `specs/constitution.md` must exist
2. Frontmatter must pass schema validation
3. Status transition must be legal

---

## CLI reference

```
specify-x init <dir> [--preset core|extended] [--project-name NAME] [--force]
specify-x verify <dir> [--path FILE]
specify-x harvest <portfolio-dir> [--dry-run]
specify-x bridge [--pmos-root PATH]
specify-x add <kind>
```

### `init`

Scaffolds `specs/`, `.claude/agents/`, `.claude/commands/`, `.specify/` in the target directory. Idempotent — never overwrites existing files unless `--force`.

### `verify`

Lints spec files for:
- Required frontmatter fields and valid status values
- Legal status lifecycle transitions
- `{ref:}` links that resolve to real files
- Schema type conformance

Placeholder refs (`{ref:<foo>}`, `{ref:specs/<slug>.md}`) are skipped — they are examples, not errors.

### `harvest`

Read-only portfolio miner. Walks a directory tree, detects spec-related markdown across projects, and emits:

- `harvest/audit-matrix.csv` — project × file-type presence matrix
- `harvest/pattern-library.md` — adoption frequency table, top-15 richest projects
- `harvest/exemplar-excerpts/<project>__<kind>.md` — 30-line snippets from best examples
- `harvest/voice-samples.md` — prose style samples

Re-harvest after every 5+ new projects to keep templates grounded in real usage.

### `bridge`

Symlinks extended templates into a target project and emits a patch manifest for integrating with AI project management backends. Requires `--pmos-root <path>`.

---

## Workflows

### New project from scratch

```bash
specify-x init myapp --preset core --project-name "My App"
cd myapp
# open in Claude Code, then:
# /speckit.x.fill-all        — autofill all specs from codebase
# /speckit.x.architecture    — deep-dive subsystem docs
specify-x verify .            # lint everything
```

### Add SDD to an existing project

```bash
specify-x init . --preset core
specify-x verify .                 # see what's missing or invalid
# /speckit.x.fill-all --dry-run   # preview what would be created
```

### Audit a single spec

```bash
specify-x verify . --path specs/features/auth/spec.md
```

### Mine your portfolio

```bash
specify-x harvest ~/projects
cat harvest/pattern-library.md
```

---

## Repo layout

```
specKitEnhanced/
├── src/specify_x/
│   ├── cli.py              # CLI entry point
│   ├── install.py          # template renderer + scaffold logic
│   ├── verify.py           # frontmatter lint + ref-link checker
│   ├── harvest.py          # read-only portfolio miner
│   ├── bridge_pmos.py      # framework integration bridge
│   └── presets.py          # loads presets/core.yml + extended.yml
├── templates/
│   ├── core/               # 14 core markdown templates
│   ├── extended/           # 7 extended markdown templates
│   └── _voice/             # caveman.md + verbose.md voice overrides
├── extension/specKitEnhanced/
│   ├── extension.yml       # spec-kit extension manifest
│   ├── commands/           # 16 slash command definitions
│   └── scripts/            # append-history.sh, new-adr.sh helpers
├── agents/                 # 5 SDD agent definitions
├── schemas/
│   ├── frontmatter.schema.json
│   ├── spec.schema.json
│   └── adr.schema.json
├── presets/
│   ├── core.yml            # core preset manifest
│   └── extended.yml        # extended preset manifest
├── docs/                   # extended documentation
├── harvest/                # output of `specify-x harvest` (generated)
├── examples/greenfield-app # gold-standard scaffold output (checked in)
├── tests/                  # pytest suite (9 tests)
└── scripts/smoke.sh        # end-to-end smoke test
```

---

## Design principles

1. **Templates are plain markdown.** No framework lock-in. Copy one file and edit.
2. **Templates come from shipped code, not imagination.** `specify-x harvest` is the source of truth.
3. **Frontmatter is the contract.** Schema-validated, status lifecycle enforced.
4. **Append-only for narrative specs.** `history.md`, `lessons.md`, `decisions.md` grow. Never rewrite.
5. **Compat over ownership.** `/speckit.*` stays upstream. This extension lives under `/speckit.x.*`.
6. **Stdlib-only CLI.** `specify-x init` runs with no pip install required. PyYAML and jsonschema are optional enhancements.

---

## Development

```bash
# End-to-end smoke test (exercises init, verify, harvest, bridge, idempotence)
bash scripts/smoke.sh

# Unit tests
pytest tests/ -v

# Rebuild gold example
rm -rf examples/greenfield-app
python3 -m src.specify_x.cli init examples/greenfield-app --preset core --force

# Re-harvest portfolio
python3 -m src.specify_x.cli harvest ~/projects
```

---

## License

MIT. Built on [github/spec-kit](https://github.com/github/spec-kit) v0.8.0 (MIT).
