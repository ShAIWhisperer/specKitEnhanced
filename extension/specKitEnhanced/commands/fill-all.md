---
id: speckit.x.fill-all
description: Agent-driven bulk autofill. Orchestrator reads project + delegates each stub spec to the right SDD specialist.
args: "[--skip <kind1,kind2>] [--only <kind1,kind2>] [--dry-run]"
template: —
produces: all stub files under specs/
---

# /speckit.x.fill-all

Populate every stub spec in this project by reading real code + existing docs + git history.
Dispatched by `sdd-orchestrator`. Runs in one Claude Code session.

## Inputs

- Project root = `pwd`.
- Spec tree = `specs/` (already scaffolded via `specify-x init`).
- Existing MD files at project root: `README.md`, `CLAUDE.md`, any `*.md` at depth ≤ 2.
- Source code: `src/`, `app/`, `backend/`, `lib/` (language-agnostic — detect from `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod`).
- Git log last 90 days (seed for `history.md`).

## Skip list (auto, unless `--only` overrides)

- `specs/history.md` — seed only from git log; does not "fill" narratively.
- `specs/lessons.md` — seed with "no lessons yet"; append happens via `/speckit.x.lessons`.
- `specs/risks.md` — scoring is human judgment; do not auto-fill.
- `specs/decisions.md` — populate index only if `specs/adr/ADR-*.md` exist.
- `specs/constitution.md` — draft principles from CLAUDE.md + README, but mark `status: draft` and flag for human review. Principles are a constitutional act.

## Execution order (respects deps)

1. **Discover** — scan project root, `src/`, docs. Emit inventory (languages, frameworks, services, entities, external APIs, existing MDs).
2. **Personas** (`sdd-scribe`) — infer from README + landing copy.
3. **Glossary** (`sdd-scribe`) — extract repeated capitalised domain terms from README + CLAUDE.md + src comments.
4. **System** (`sdd-architect`) — C4-L1 from package manifests + folder tree + existing deployment/integration MDs.
5. **Architecture/{slug}** (`sdd-architect`) — one per detected top-level subsystem (heuristic: `src/<subsystem>/`, `app/<subsystem>/`, major router modules).
6. **Data Model** (`sdd-architect`) — parse ORM models / Prisma schema / SQL migrations / SQLAlchemy classes / Drizzle schemas.
7. **API Contract** (`sdd-architect`) — parse route handlers (Express, FastAPI, Next.js App Router, tRPC).
8. **Design + UX Flow** (`sdd-architect` + `sdd-scribe`) — only if `specs/features/<slug>/spec.md` has user stories; skip empty feature folders.
9. **Security** (`sdd-risk-analyst`) — scan for auth middleware, secret usage, dependency scanner output; STRIDE table seeded from §1 assets.
10. **Observability** (`sdd-risk-analyst`) — scan for logger imports, tracing spans, `observability/` folder, dashboards referenced in existing MDs.
11. **Runbook/{svc}** (`sdd-risk-analyst`) — one per service with a deploy manifest (`Dockerfile`, `vercel.json`, `fly.toml`, `k8s/`, `docker-compose.yml`).
12. **Research** — no auto-create; only filled when a human runs `/speckit.x.research`.
13. **Decisions index** (`sdd-historian`) — list existing `specs/adr/*.md` rows (if any).
14. **History** (`sdd-historian`) — seed with one dated entry: `YYYY-MM-DD — SDD adopted via specKitEnhanced`.
15. **Constitution** (`sdd-orchestrator`, human-in-loop) — draft mission from README; draft principles from CLAUDE.md; mark `status: draft`; ask user to review before promoting to `review`.

## Rules (enforced by orchestrator)

1. **Every spec cites real files.** Every `{ref:src/...:SYMBOL}` must resolve. If you can't find a symbol, mark `[NEEDS CLARIFICATION]` and stop — do not invent.
2. **No filler prose.** If a section has no evidence, write `[NEEDS CLARIFICATION] <what's missing>` — do not hand-wave.
3. **Preserve user edits.** Before writing any file, check if it already has filled content (non-placeholder body ≥ 200 chars). If so, SKIP and log to the summary report — never clobber user work.
4. **Status stays `draft`.** All filled specs emit with `status: draft` regardless of input. User explicitly promotes to `review` after human pass.
5. **Append to history** at end of run: one entry summarising what was filled.

## Dry-run

`--dry-run` prints the execution plan (which specs would be touched, with which specialist, with which inputs) without writing. Use first.

## Output — post-run summary

```
=== /speckit.x.fill-all — summary ===
Project: <name>
Filled (N):
  ✓ specs/system.md                (sdd-architect, cited 12 files)
  ✓ specs/architecture/audio.md    (sdd-architect, cited 8 files)
  ✓ specs/data-model.md            (sdd-architect, cited 3 files)
  ...
Skipped (user content present) (M):
  · specs/constitution.md          (already filled — body 1240 chars)
Needs clarification (P):
  ! specs/security.md               (no auth middleware detected; human input needed)
  ! specs/features/_example/spec.md (no real feature scope detected; rename folder first)
Next:
  1. Review specs/constitution.md — draft status.
  2. Resolve [NEEDS CLARIFICATION] markers.
  3. Run `specify-x verify` — expect 0 errors.
```

## Delegation contract

Orchestrator reads this command file, then for each target spec:

1. Reads the target template to know required sections.
2. Invokes the specialist agent (as a sub-agent / Task tool) with:
   - Target file path
   - Template path
   - Project root
   - Inventory from step 1 (Discover)
3. Specialist returns filled body.
4. Orchestrator validates:
   - Frontmatter schema
   - `{ref:}` link resolution
   - No `{{placeholder}}` markers remain (except explicit `[NEEDS CLARIFICATION]`)
5. Orchestrator writes the file or rejects the output with a specific error.
6. Orchestrator moves to next target.

## When to abort

- Project has no detectable language / framework.
- `specs/` is missing (run `specify-x init` first).
- Constitution draft cannot be created because README is empty.

Report the abort reason; do not partially fill.
