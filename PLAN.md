# specKitEnhanced — Spec-Driven Development Framework

## Context

Teams running many projects under `~/projects/`. You like `github/spec-kit` but find it thin on the MD templates you actually reach for (History, LessonsLearned, Design, Architecture, System, etc.). `PM OS` already ships a working spec engine (constitution.md, 7 architecture specs, 12 feature folders × 3 files, 3 cross-cutting, `{ref:}` refs, status lifecycle) but is PM-domain-locked.

**Decision:** build `specKitEnhanced` as a **fork-and-wrap of spec-kit v0.8.0 (MIT)**, adding the missing 14-template catalog, tight two-way bridge to PM OS, and — crucially — **harvesting** the 110 existing projects for proven MD patterns to fold into the framework. **No retrofits**. Existing projects stay untouched. specKitEnhanced ships for new projects + volunteer pilots.

**Outcome:** one house-branded SDD framework, 14-file core template pack distilled from your real portfolio, PM OS-wired, team-adoptable via `.claude/` commands. New projects scaffold in <2 min. PM OS's 97 skills emit specKitEnhanced-shaped artifacts.

---

## 1. Strategic Recommendation — Fork + Wrap spec-kit

Install `spec-kit` as pinned dependency. Ship a thin `specify-x` CLI + a spec-kit extension pack. Keep `/speckit.*` commands, add `/speckit.x.*` for the 14 missing templates.

Why not the alternatives:
- Upstream PRs — merge timelines at GitHub's pace, not yours. Caveman tonal preferences won't survive upstream review.
- Ground-up — throws away `specify init --here --force --ai <agent>` refresh loop + 30+ agent integrations (Claude, Cursor, Copilot, Gemini, Qwen, etc.).
- Extend PM OS only — locks SDD to PM domain; no portable CLI for the other 109 projects.

License: spec-kit MIT. Forking/embedding permitted.

---

## 2. Repo Layout — `/path/to/specKitEnhanced/`

```
specKitEnhanced/
├── README.md
├── CLAUDE.md                              # LLM context for this repo
├── PLAN.md                                # this file
├── constitution.md                        # dogfood — SDD for SDD
├── pyproject.toml                         # `specify-x` CLI
│
├── src/specify_x/
│   ├── cli.py                             # `specify-x init|add|harvest|verify|bridge`
│   ├── install.py                         # pins spec-kit, applies extension
│   ├── presets.py                         # core | pm-os
│   ├── verify.py                          # frontmatter + link lint
│   ├── harvest.py                         # portfolio miner (phase 1)
│   └── bridge_pmos.py                     # PM OS skill_engine integration
│
├── extension/specKitEnhanced/
│   ├── extension.yml                      # declares commands, templates
│   ├── commands/                          # slash commands (16 files)
│   │   ├── architecture.md · design.md · system.md
│   │   ├── adr.md · lessons.md · history.md
│   │   ├── runbook.md · risk.md · security.md
│   │   ├── data-model.md · api-contract.md · ux-flow.md
│   │   ├── personas.md · glossary.md · observability.md
│   │   └── research.md
│   └── scripts/
│       ├── new-adr.sh                     # allocates ADR-NNNN
│       └── append-history.sh
│
├── templates/
│   ├── core/                              # 14 files, installed by default
│   │   ├── constitution-template.md
│   │   ├── spec-template.md               # inherits spec-kit
│   │   ├── plan-template.md               # inherits spec-kit
│   │   ├── tasks-template.md              # inherits spec-kit
│   │   ├── architecture-template.md
│   │   ├── design-template.md
│   │   ├── system-template.md
│   │   ├── history-template.md
│   │   ├── lessons-template.md
│   │   ├── decisions-template.md          # ADR log
│   │   ├── personas-template.md
│   │   ├── glossary-template.md
│   │   ├── research-template.md
│   │   └── risks-template.md
│   └── extended/                          # opt-in via `specify-x add <kind>`
│       ├── data-model-template.md
│       ├── api-contract-template.md
│       ├── ux-flow-template.md
│       ├── runbook-template.md
│       ├── security-template.md
│       ├── observability-template.md
│       └── adr/ADR-NNNN-slug-template.md
│
├── agents/                                # .claude/agents/ drop-ins
│   ├── sdd-orchestrator.md
│   ├── sdd-architect.md
│   ├── sdd-historian.md
│   ├── sdd-risk-analyst.md
│   └── sdd-scribe.md
│
├── schemas/
│   ├── frontmatter.schema.json
│   ├── spec.schema.json
│   └── adr.schema.json
│
├── presets/
│   ├── core.yml                           # 14 files, 12 commands
│   └── pm-os.yml                          # core + PM OS bridge wiring
│
├── harvest/                               # PHASE 1 OUTPUT — portfolio mining
│   ├── audit-matrix.csv                   # per-project: which MD files exist
│   ├── pattern-library.md                 # extracted reusable patterns
│   ├── exemplar-excerpts/                 # snippets pulled from top 10 projects
│   │   ├── Vibe-3-Studio_claude-md.md
│   │   ├── UIUXExpert_docs-hierarchy.md
│   │   ├── __Claude_Skills_skill-md.md
│   │   ├── PM OS_constitution.md
│   │   └── ...
│   └── voice-samples.md                   # tone/voice patterns found
│
├── examples/
│   ├── greenfield-app/                    # gold standard scaffold, all core filled
│   └── pm-os-wired/                       # proof of PM OS bridge
│
└── docs/
    ├── 01-philosophy.md
    ├── 02-template-catalog.md
    ├── 03-harvest-methodology.md
    ├── 04-pmos-bridge.md
    └── 05-adoption-for-teams.md
```

---

## 3. Template Catalog — 14 Core + 7 Extended

All templates share frontmatter (PM OS–compatible):

```yaml
---
spec_id: <auto|feature-slug|ADR-NNNN>
title: <short>
status: draft | review | approved | implemented | deprecated
type: feature | architecture | cross-cutting | adr | runbook | ...
author: "@author"
created: 2026-04-24
updated: 2026-04-24
depends_on: []          # list of {ref:path} pointers
---
```

| # | Template | Tier | Filename | Required sections | Links to | Command |
|---|---|---|---|---|---|---|
| 1 | Constitution | core | `specs/constitution.md` | Mission, Principles (P1..Pn), Decision Framework, Enforcement | all | `/speckit.constitution` |
| 2 | Spec/PRD | core | `specs/features/<slug>/spec.md` | Problem, User Stories, Scope, Acceptance, Out-of-Scope | plan, design | `/speckit.specify` |
| 3 | Plan | core | `specs/features/<slug>/plan.md` | Approach, Milestones, Risks, Open Qs | spec, tasks | `/speckit.plan` |
| 4 | Tasks | core | `specs/features/<slug>/tasks.md` | Task list (ID, title, owner, DoD) | plan | `/speckit.tasks` |
| 5 | Architecture | core | `specs/architecture/<slug>.md` | Context, Components, Data Flow, Trade-offs | system, decisions | `/speckit.x.architecture` |
| 6 | Design | core | `specs/features/<slug>/design.md` | UX, Components, Interactions, States | spec, ux-flow | `/speckit.x.design` |
| 7 | System | core | `specs/system.md` | System Context, External Deps, Boundaries | arch | `/speckit.x.system` |
| 8 | History | core | `specs/history.md` | Dated entries (YYYY-MM-DD) | all | `/speckit.x.history` |
| 9 | Lessons-Learned | core | `specs/lessons.md` | Entries: Context, Lesson, Action | history, decisions | `/speckit.x.lessons` |
| 10 | Decisions Log (ADR index) | core | `specs/decisions.md` | ADR table: id, title, status, date | arch | `/speckit.x.adr` |
| 11 | Personas | core | `specs/personas.md` | Persona cards (Name, JTBD, Goals, Pains) | ux, spec | `/speckit.x.personas` |
| 12 | Glossary | core | `specs/glossary.md` | term → definition | all | `/speckit.x.glossary` |
| 13 | Research | core | `specs/research/<slug>.md` | Question, Sources, Findings, Decision | spec, adr | `/speckit.x.research` |
| 14 | Risk Register | core | `specs/risks.md` | id, desc, likelihood, impact, owner, mitigation | decisions | `/speckit.x.risk` |
| 15 | Data Model | extended | `specs/data-model.md` | Entities, Fields, Relations, Migrations | arch, api | `/speckit.x.data-model` |
| 16 | API Contract | extended | `specs/contracts/<api>.md` | Endpoints, Schemas, Errors, Auth | data-model | `/speckit.x.api-contract` |
| 17 | UX Flow | extended | `specs/ux/<flow>.md` | Personas, Steps, Screens, Edge cases | personas, design | `/speckit.x.ux-flow` |
| 18 | Runbook | extended | `specs/runbooks/<svc>.md` | Alerts, Diagnostics, Recovery, Rollback | observability | `/speckit.x.runbook` |
| 19 | Security/Threat | extended | `specs/security.md` | Assets, Threats (STRIDE), Mitigations | arch, risk | `/speckit.x.security` |
| 20 | Observability | extended | `specs/observability.md` | Metrics, Logs, Traces, SLOs, Alerts | runbook, arch | `/speckit.x.observability` |
| 21 | Per-decision ADR | extended | `specs/adr/ADR-NNNN-<slug>.md` | Context, Decision, Consequences, Alternatives | decisions.md | `/speckit.x.adr --new` |

**Reference syntax** (inherited from PM OS): `{ref:specs/features/x/spec.md#section}` · `{ref:backend/app/core/file.py:SYMBOL}` · `{ref:__skilss/<name>/SKILL.md}`.

**Status lifecycle** (inherited from PM OS): `draft → review → approved → implemented → deprecated`. Backward transitions allowed; must log in inline `## Changelog` section.

---

## 4. Slash Commands

Keep spec-kit originals verbatim (`/speckit.constitution|specify|clarify|plan|tasks|analyze|implement`). Add under `speckit.x.*` namespace so upstream updates never collide.

All `/speckit.x.*` commands enforce: constitution present, valid frontmatter, legal status transition, `depends_on` resolves.

---

## 5. Agent Set

One orchestrator + four specialists. Drop-ins for `.claude/agents/`. Map to PM OS where overlap exists — don't duplicate.

- `sdd-orchestrator` — routes `/speckit.x.*`, enforces constitution, checks frontmatter.
- `sdd-architect` — Architecture, System, Design. (Reuses PM OS `Documentation` agent via bridge.)
- `sdd-historian` — History, Lessons, ADRs. (NEW — no PM OS equivalent.)
- `sdd-risk-analyst` — Risks, Security. (Reuses PM OS `risk-register-builder` skill.)
- `sdd-scribe` — Glossary, Personas, Research. (Reuses PM OS `Discovery` agent.)

Mapping documented in `docs/04-pmos-bridge.md`.

---

## 6. PM OS Bridge — tight two-way

Concrete integration points:

- `/path/to/your-pm-os/backend/app/core/skill_engine.py` — extend `OUTPUT_DIR_TO_CATEGORY` + `SKILL_CATEGORY_OVERRIDES` with `"sdd"` → `"SDD Framework"`. Register specKitEnhanced templates as skill output destinations.
- `/path/to/your-pm-os/backend/app/api/specs.py` — add env var `SPECKIT_X_TEMPLATE_DIR` read before `settings.project_root / "specs"`. Extend `SPEC_FILE_LABELS` dict with the 14 core filenames.
- `/path/to/your-pm-os/backend/app/core/agent_orchestrator.py` — register 5 new SDD agents as an added domain.
- `specKitEnhanced/src/specify_x/bridge_pmos.py` — exposes `install_to_pmos(pmos_root)`: symlinks `templates/core/` into PM OS seed dir, patches `settings.json` with new categories.

Flow:
1. PM OS `SkillEngine.load_all()` discovers specKitEnhanced templates via `SPECKIT_X_TEMPLATE_DIR`.
2. Any PM OS skill with `category: sdd` emits output in specKitEnhanced frontmatter shape.
3. PM OS `specs.py` API serves extended template set by default.

---

## 7. Constitution & Governance

`templates/core/constitution-template.md` (Caveman-tuned, ≤80 lines):
1. Mission
2. Principles (P1..Pn, one paragraph each)
3. Decision Framework — when to ADR vs commit; when to log Lessons
4. Template Minima — files MUST exist to claim SDD-compliant
5. Enforcement Hooks:
   - `.claude/hooks/pre-commit-sdd-lint.sh` — validate frontmatter schema
   - `.claude/hooks/post-commit-history.sh` — append to `history.md` when `specs/` touched
   - CI: `specify-x verify` as GitHub Action (warn-only, never block)
6. Amendment process — bump `version:` in frontmatter, log ADR, append history.

---

## 8. Adoption Path — Harvest, not Retrofit

Existing projects stay untouched. Strategy is **mine them for gold, fold the gold into specKitEnhanced's templates**.

### Phase 1 — Harvest (week 1)

`src/specify_x/harvest.py` runs a read-only audit:

1. Walk `~/projects/*/` (depth 2). Skip `node_modules`, `.venv`, `dist`.
2. For each project, detect MD files matching: `README`, `CLAUDE`, `AGENTS`, `ARCHITECTURE`, `DESIGN`, `SYSTEM`, `HISTORY`, `LESSONS*`, `DECISIONS`, `ADR*`, `PRD`, `SPEC`, `ROADMAP`, `CHANGELOG`, `TASKS`, `PLAN`, `RESEARCH`, `GLOSSARY`, `CONVENTIONS`, `RUNBOOK`, `KNOWLEDGE`, `MOAT`, `PERSONAS`, `RISKS`, `METRICS`, `DEPLOYMENT*`.
3. Detect folders: `docs/`, `specs/`, `.claude/`, `.cursor/`, `memory/`, `templates/`, `commands/`, `agents/`.
4. Emit `harvest/audit-matrix.csv` — project × file-type matrix.
5. Emit `harvest/pattern-library.md` — distilled patterns, ranked by uniqueness + portability.
6. Copy excerpts (3–20 lines max) into `harvest/exemplar-excerpts/<project>_<filetype>.md` — raw samples for later template authoring.

Already-identified exemplars worth mining (from exploration):
- **PM OS** — `specs/constitution.md`, 3-file feature split, `{ref:}` syntax, status lifecycle, SKILL.md = spec+prompt+metadata.
- **Vibe-3-Studio** — `.claude/{agents,commands,hooks}` triad, DEPLOYMENT_PLAN, PERFORMANCE_OPTIMIZATION_REPORT, AUDIO_TESTING_GUIDE (runbook pattern).
- **UIUXExpert** — numbered `docs/00-*.md…16-*.md` curriculum hierarchy, `agent-system-prompt.md`.
- **__Claude_Skills** — `SKILL.md` per-module + `SKILLS_CATALOG.md` indexing (21 instances).
- **Apex — Personal AI Chief of Staff** — `memory-seed/`, `user_profile.md`, `feedback_response_style.md`.
- **ProjectsDashboard** — `feature-folder-tree-view-plan.md` + 160 MD files ≈ feature-planning pattern.
- **HowToGuide** — `KNOWLEDGE.md` + `PROJECT_SUMMARY.md` + `RESEARCH_ANALYSIS.md` separation.
- **Linear_Upgrades** — `MOAT.md` competitive moat doc (candidate for specKitEnhanced optional template).
- **ManyMany.dev** — `COMPREHENSIVE_README.md`, `DISTRIBUTION.md`.
- **__DNB / CallGuardAI** — `ARCHITECTURE.md` clean example.

### Phase 2 — Distill (week 2)

Turn harvest into templates.

1. `harvest/pattern-library.md` → cross-check against 14 core templates. For each: does your portfolio already have a better example than spec-kit's baseline? If yes, rewrite the template section headings + preamble from the portfolio exemplar.
2. Extract voice samples from top 3 projects → `templates/_voice/caveman.md` (your tone), `templates/_voice/verbose.md` (team-readable). Templates read `{{voice.preamble}}`.
3. Lift PM OS's `constitution.md` wholesale as the seed for `templates/core/constitution-template.md` (with field placeholders).
4. Lift PM OS's 3-file feature split as `spec.md` / `plan.md` / `tasks.md` baseline structure.
5. Lift `__Claude_Skills`' SKILLS_CATALOG.md → `specs/README.md` template section on spec indexing.
6. Candidate additions to `templates/extended/` based on harvest hits: `moat-template.md` (Linear_Upgrades), `knowledge-template.md` (13 projects use it — real signal), `comprehensive-readme-template.md` (ManyMany.dev).

### Phase 3 — Ship (week 3)

1. `specify-x init --preset core` scaffolds a new project in <2 min.
2. `specify-x init --preset pm-os` scaffolds + wires PM OS bridge.
3. Publish repo as internal package. Team installs via `uv tool install git+...`.
4. Add specKitEnhanced to the PM OS repo itself via `bridge_pmos.install_to_pmos()` — PM OS becomes first dogfood consumer.

### Phase 4 — Voluntary Pilots (week 4+)

No forced retrofit. When a new project starts OR a team member volunteers an existing one, they run `specify-x init --here`. Collect lessons into `specs/lessons.md` on specKitEnhanced itself.

---

## 9. Extensibility

- **Plugins**: `extension/<name>/extension.yml` with composition strategies (prepend/append/wrap) — spec-kit v0.8.0 native. specKitEnhanced is itself one such extension, proving the pattern.
- **Per-project opt-in**: `.specify/profile.yml` declares enabled templates. Command for missing template emits "add `specify-x add <kind>` first" and exits.
- **Voice overrides**: `templates/_voice/<name>.md` + `profile.yml` selects one. Every template's preamble reads `{{voice.preamble}}`.
- **Presets**: `presets/*.yml` bundles templates + commands + agents.

---

## 10. Verification

End-to-end smoke test (scripted in `scripts/smoke.sh`):

1. `mkdir /tmp/sdd-smoke && cd /tmp/sdd-smoke`
2. `specify-x init --preset core --ai claude --here` → assert 14 core files exist.
3. `/speckit.specify "user login"` → `specs/features/user-login/spec.md`.
4. `/speckit.plan` → `plan.md`.
5. `/speckit.tasks` → `tasks.md`.
6. `/speckit.x.architecture "auth"` → `specs/architecture/auth.md`.
7. `/speckit.x.adr --new "use JWT"` → `specs/adr/ADR-0001-use-jwt.md` + row in `decisions.md`.
8. `/speckit.x.lessons "hooks caveat"` → append to `lessons.md`.
9. `specify-x verify` runs:
   - JSON Schema validation on frontmatter (every spec file).
   - `{ref:}` link integrity — all targets exist.
   - Status lifecycle legality — no `draft → implemented` skip.
   - `depends_on` all resolve.
10. Diff against `examples/greenfield-app/` — byte-equivalent modulo dates.
11. `specify-x harvest --dry-run ~/projects` → emits audit-matrix.csv without mutations.
12. PM OS bridge: `cd /path/to/your-pm-os && python -c "from app.api.specs import SEED_SPECS_DIR; assert SPECKIT_X_TEMPLATE_DIR resolves"`.

CI: `.github/workflows/speckit-x-verify.yml` runs steps 9–10 on every PR to specKitEnhanced.

---

## Critical Files to Create

- `/path/to/specKitEnhanced/src/specify_x/cli.py` — `specify-x init|add|harvest|verify|bridge` entry points
- `/path/to/specKitEnhanced/src/specify_x/harvest.py` — portfolio miner (Phase 1)
- `/path/to/specKitEnhanced/src/specify_x/bridge_pmos.py` — PM OS integration
- `/path/to/specKitEnhanced/src/specify_x/verify.py` — schema + link lint
- `/path/to/specKitEnhanced/extension/specKitEnhanced/extension.yml` — spec-kit extension manifest
- `/path/to/specKitEnhanced/templates/core/constitution-template.md` — seeded from PM OS `specs/constitution.md`
- `/path/to/specKitEnhanced/templates/core/{architecture,design,system,history,lessons,decisions,personas,glossary,research,risks}-template.md` — 10 new files
- `/path/to/specKitEnhanced/templates/extended/{data-model,api-contract,ux-flow,runbook,security,observability}-template.md` — 6 new files
- `/path/to/specKitEnhanced/templates/extended/adr/ADR-NNNN-slug-template.md`
- `/path/to/specKitEnhanced/agents/{sdd-orchestrator,sdd-architect,sdd-historian,sdd-risk-analyst,sdd-scribe}.md`
- `/path/to/specKitEnhanced/schemas/{frontmatter,spec,adr}.schema.json`
- `/path/to/specKitEnhanced/presets/{core,pm-os}.yml`

## Critical Files to Modify (PM OS bridge)

- `/path/to/your-pm-os/backend/app/api/specs.py` — add `SPECKIT_X_TEMPLATE_DIR` env lookup, extend `SPEC_FILE_LABELS`
- `/path/to/your-pm-os/backend/app/core/skill_engine.py` — extend `OUTPUT_DIR_TO_CATEGORY` with `"sdd"` mapping
- `/path/to/your-pm-os/backend/app/core/agent_orchestrator.py` — register 5 SDD agents

## Critical Existing Code to Reuse

- PM OS `SkillEngine._parse_skill()` — frontmatter parsing (proven, reuse shape)
- PM OS `specs.py::_build_tree()` — spec tree navigation (port or call)
- PM OS `constitution.md` — seed for specKitEnhanced constitution template
- spec-kit `specify init --here --force --ai <agent>` — refresh loop (don't reimplement)
- spec-kit `extensions/X/extension.yml` composition strategies (prepend/append/wrap) — native extensibility

---

## Out of Scope (explicit)

- Retrofitting the 110 existing projects. Existing projects stay as-is.
- Rewriting `/speckit.constitution|specify|plan|tasks|clarify|analyze|implement`. Inherit verbatim.
- Building own parser/scaffolder. Use spec-kit's.
- Upstream PRs to `github/spec-kit`. Keep as private fork-and-wrap.
- CI enforcement / blocking gates. Warn-only until adoption proves itself.

---

## Execution Hints for Auto Mode

Start sequence on resume:
1. `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git` (pin to v0.8.0)
2. Scaffold directory tree from section 2.
3. Write `src/specify_x/harvest.py` first → run it read-only against `~/projects/` → generate `harvest/audit-matrix.csv` and `harvest/exemplar-excerpts/`.
4. Use harvest output to draft each of the 14 core templates.
5. Copy `/path/to/your-pm-os/specs/constitution.md` as seed for `templates/core/constitution-template.md` and replace specifics with placeholders.
6. Write `extension/specKitEnhanced/extension.yml` per spec-kit's extension spec.
7. Implement `specify-x init` (Python) that: runs `specify init --here --ai claude`, then copies `templates/core/*` into `specs/`, then writes `.specify/profile.yml`.
8. Implement `specify-x verify` with JSON Schema + link lint.
9. Implement `bridge_pmos.install_to_pmos()`.
10. Smoke test per section 10 in `/tmp/sdd-smoke`.

Key references:
- spec-kit repo: https://github.com/github/spec-kit (MIT, v0.8.0, active)
- PM OS: `/path/to/your-pm-os/` — tight bridge target
- Harvest source dir: `~/projects/*/` — read-only

Caveman mode on — keep templates compact, avoid filler prose.
