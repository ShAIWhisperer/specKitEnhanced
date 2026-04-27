# Harvest Methodology

specKitEnhanced templates are distilled from real portfolio projects. Harvest is a **read-only** process. It does not modify any project.

## What it scans

- Walk root directory (default `~/projects/`) depth 3.
- Skip `node_modules/`, `.venv/`, `dist/`, `build/`, `.next/`, `.git/`.
- Per project: match MD filenames against patterns for README, CLAUDE, AGENTS, ARCHITECTURE, DESIGN, SYSTEM, HISTORY, LESSONS, DECISIONS, ADR, PRD, SPEC, ROADMAP, CHANGELOG, TASKS, PLAN, RESEARCH, GLOSSARY, CONVENTIONS, RUNBOOK, KNOWLEDGE, MOAT, PERSONAS, RISKS, METRICS, DEPLOYMENT, SECURITY, CONTRIBUTING, QUICK_START, SKILL, MEMORY, USER_PROFILE.
- Detect signal folders: `docs/`, `specs/`, `.claude/`, `.cursor/`, `memory/`, `memory-seed/`, `templates/`, `commands/`, `agents/`, `hooks/`, `__skilss/`, `skills/`, `.github/`.

## What it emits

- `harvest/audit-matrix.csv` — project × file-type matrix (0/1).
- `harvest/pattern-library.md` — frequency table, top-15 doc-rich projects, rare-pattern exemplars.
- `harvest/exemplar-excerpts/<project>__<kind>.md` — 30-line snippets from top-15 projects.
- `harvest/voice-samples.md` — prose style samples for voice-override authoring.

## How to use it for template authoring

1. `python3 -m src.specify_x.cli harvest ~/projects`
2. Open `harvest/pattern-library.md`. Read the frequency table.
3. Any MD kind with ≥ 10% adoption is a candidate for a core template. < 5% is an extended template candidate. 0-1 project adoption is rejected.
4. Open `harvest/exemplar-excerpts/<project>__<kind>.md`. Read the 3 richest exemplars for the kind.
5. Author the template as the *smallest structure that captures the best parts of all three*.
6. Run `bash scripts/smoke.sh` to ensure the new template installs and verifies.

## When to re-harvest

- After any quarter where ≥ 5 new projects land in the portfolio.
- Before bumping the `core` preset's minor version.
- After any ADR that adds or removes a template.
