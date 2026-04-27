# Adoption for Teams

## Principle: harvest, don't retrofit

Existing projects stay untouched. specKitEnhanced scaffolds **new** projects, learns from **old** ones. The old ones are the source material for the templates, not targets of rewrites.

## Pilot sequence (recommended)

1. **Week 1 — Harvest.** Run `specify-x harvest /path/to/portfolio`. Read `harvest/pattern-library.md`. Confirm the 14 core templates cover ≥ 80% of your adoption-weighted file kinds.
2. **Week 2 — Dogfood.** Run `specify-x init` in this very repo (`specKitEnhanced/`). Verify the constitution, history, lessons templates feel right at meta-level.
3. **Week 3 — Pilot 3 projects.** Pick 3 *new* projects. Scaffold via `specify-x init <path> --preset core`. Compare week-over-week: is the team using the new templates or ignoring them?
4. **Week 4 — Tune.** Re-harvest. Compare before/after. If a core template is untouched across all 3 pilots, move it to `extended`. If an extended template is used in every pilot, promote to `core`.
5. **Week 5+ — Broaden.** Any new project starts with `specify-x init`. Existing projects are retrofitted **only** on explicit volunteer request.

## Voice tuning

`templates/_voice/caveman.md` and `templates/_voice/verbose.md` are placeholders. The `preset.voice` field in `presets/*.yml` selects one. Every template's preamble is a `{{voice.preamble}}` placeholder (implementation forthcoming).

For now, the house voice is **caveman-full** — drop articles, fragments OK, technical terms exact.

## CI (future)

`.github/workflows/speckit-x-verify.yml` will run `specify-x verify` on every PR to a consuming project. Initially warn-only; enforced after 2 weeks of signal.

## When to open an ADR

- Adding a new core or extended template.
- Changing frontmatter required fields.
- Changing the status lifecycle.
- Breaking compatibility with spec-kit.
- Any decision that affects > 3 consumer projects.

## When to append a lesson

- Spec format feels awkward in a real session.
- Agent routing picked the wrong specialist.
- Harvest missed a real pattern.
- Framework bridge broke under version skew.
