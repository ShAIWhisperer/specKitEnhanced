"""PM OS bridge — installs specKitEnhanced templates into a PM OS-compatible project.

Non-destructive: symlinks templates into the PM OS seed dir and writes a small
patch manifest. Actual patches to PM OS code are left as a report the
user applies manually (to preserve auditability).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class BridgeReport:
    pmos_root: Path
    symlink: Path | None
    patch_file: Path
    env_hint: str
    files_to_edit: list[tuple[Path, str]]


def install_to_pmos(repo_root: Path, pmos_root: Path, dry_run: bool = False) -> BridgeReport:
    if not pmos_root.exists():
        raise FileNotFoundError(f"PM OS root not found: {pmos_root}")

    templates_src = repo_root / "templates"
    seed_target = pmos_root / ".specify-x" / "templates"
    seed_target.parent.mkdir(parents=True, exist_ok=True)

    symlink: Path | None = None
    if not dry_run:
        if seed_target.exists() or seed_target.is_symlink():
            seed_target.unlink()
        try:
            seed_target.symlink_to(templates_src)
            symlink = seed_target
        except OSError:
            symlink = None

    # Env hint
    env_hint = f"export SPECKIT_X_TEMPLATE_DIR={seed_target}"

    # Patch manifest (what PM OS code needs to read)
    patch_data = {
        "specs_py_patch": {
            "file": "backend/app/api/specs.py",
            "change": (
                "At top of module, add: "
                "`SPECKIT_X_TEMPLATE_DIR = os.getenv('SPECKIT_X_TEMPLATE_DIR')`. "
                "In the function that resolves SEED_SPECS_DIR, prefer that env "
                "var when set, else fall back to `settings.project_root / 'specs'`."
            ),
        },
        "skill_engine_patch": {
            "file": "backend/app/core/skill_engine.py",
            "change": (
                "Extend OUTPUT_DIR_TO_CATEGORY with `'sdd': 'SDD Framework'` "
                "and SKILL_CATEGORY_OVERRIDES similarly so new templates show up "
                "as the 'SDD Framework' category in the UI."
            ),
        },
        "agent_orchestrator_patch": {
            "file": "backend/app/core/agent_orchestrator.py",
            "change": (
                "Register the 5 SDD agents from .claude/agents/ as an additional "
                "domain alongside Strategy/Discovery/Documentation/Operations/Launch/Analytics."
            ),
        },
    }
    patch_file = pmos_root / ".specify-x" / "bridge-patches.json"
    if not dry_run:
        patch_file.write_text(json.dumps(patch_data, indent=2), encoding="utf-8")

    return BridgeReport(
        pmos_root=pmos_root,
        symlink=symlink,
        patch_file=patch_file,
        env_hint=env_hint,
        files_to_edit=[
            (pmos_root / v["file"], v["change"])
            for v in patch_data.values()
        ],
    )
