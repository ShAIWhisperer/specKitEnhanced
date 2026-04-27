"""Installer — renders templates into a target project's specs/ directory."""

from __future__ import annotations

import datetime
import re
import shutil
from pathlib import Path

from .presets import Preset, resolve

PLACEHOLDER_RE = re.compile(r"\{\{([A-Za-z0-9_.]+)\}\}")


def _render(text: str, ctx: dict[str, str]) -> str:
    """Tiny {{key}} substitution. Missing keys stay literal so user can see TODOs."""

    def sub(m: re.Match) -> str:
        key = m.group(1)
        return ctx.get(key, m.group(0))

    return PLACEHOLDER_RE.sub(sub, text)


def _dest_for_template(template_path: Path, target_specs: Path) -> Path:
    """Map `templates/core/X-template.md` → `specs/X.md`."""
    name = template_path.name
    if name.endswith("-template.md"):
        base = name[: -len("-template.md")]
    else:
        base = template_path.stem
    # Special layouts:
    if base == "adr/ADR-NNNN-slug":
        return target_specs / "adr" / "ADR-NNNN-slug-template.md"
    if base == "constitution":
        return target_specs / "constitution.md"
    if base in {
        "system", "history", "lessons", "decisions", "personas",
        "glossary", "risks", "security", "observability", "data-model",
    }:
        return target_specs / f"{base}.md"
    # "spec" / "plan" / "tasks" are feature-level, live under features/<slug>/
    if base in {"spec", "plan", "tasks", "design"}:
        return target_specs / "features" / "_example" / f"{base}.md"
    if base == "architecture":
        return target_specs / "architecture" / "_example.md"
    if base == "research":
        return target_specs / "research" / "_example.md"
    if base == "runbook":
        return target_specs / "runbooks" / "_example.md"
    if base == "api-contract":
        return target_specs / "contracts" / "_example.md"
    if base == "ux-flow":
        return target_specs / "ux" / "_example.md"
    # ADR per-decision template
    return target_specs / "adr" / name


def install(
    repo_root: Path,
    target: Path,
    preset_name: str = "core",
    author: str = "@author",
    project_name: str | None = None,
    force: bool = False,
) -> dict:
    """Install a preset into `target`. Returns a manifest dict."""
    presets_dir = repo_root / "presets"
    preset: Preset = resolve(preset_name, presets_dir)
    today = datetime.date.today().isoformat()
    ctx = {
        "author": author,
        "today": today,
        "project_name": project_name or target.name,
    }

    target_specs = target / "specs"
    target_specs.mkdir(parents=True, exist_ok=True)

    written: list[str] = []
    skipped: list[str] = []

    for tmpl in preset.templates:
        src = repo_root / tmpl
        if not src.exists():
            continue
        dest = _dest_for_template(src, target_specs)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and not force:
            skipped.append(str(dest.relative_to(target)))
            continue
        rendered = _render(src.read_text(encoding="utf-8"), ctx)
        dest.write_text(rendered, encoding="utf-8")
        written.append(str(dest.relative_to(target)))

    # Claude command drop-ins: copy extension commands under .claude/commands/
    claude_dir = target / ".claude" / "commands"
    claude_dir.mkdir(parents=True, exist_ok=True)
    for cmd in preset.commands:
        src = repo_root / cmd
        if not src.exists():
            continue
        dest = claude_dir / src.name
        if dest.exists() and not force:
            skipped.append(str(dest.relative_to(target)))
            continue
        shutil.copy2(src, dest)
        written.append(str(dest.relative_to(target)))

    # Claude agent drop-ins
    agents_dir = target / ".claude" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    for agent in preset.agents:
        src = repo_root / agent
        if not src.exists():
            continue
        dest = agents_dir / src.name
        if dest.exists() and not force:
            skipped.append(str(dest.relative_to(target)))
            continue
        shutil.copy2(src, dest)
        written.append(str(dest.relative_to(target)))

    # Schemas drop
    schemas_dest = target / ".specify" / "schemas"
    schemas_dest.mkdir(parents=True, exist_ok=True)
    for s in preset.schemas:
        src = repo_root / s
        if not src.exists():
            continue
        dest = schemas_dest / src.name
        if dest.exists() and not force:
            skipped.append(str(dest.relative_to(target)))
            continue
        shutil.copy2(src, dest)
        written.append(str(dest.relative_to(target)))

    # Profile file — records which preset + voice was installed
    profile = target / ".specify" / "profile.yml"
    profile.parent.mkdir(parents=True, exist_ok=True)
    profile.write_text(
        f"preset: {preset.name}\n"
        f"voice: {preset.voice}\n"
        f"installed_on: {today}\n"
        f"installed_by: {author}\n",
        encoding="utf-8",
    )
    written.append(str(profile.relative_to(target)))

    return {"preset": preset.name, "written": written, "skipped": skipped}
