"""specify-x CLI — init | add | harvest | verify | bridge.

Stdlib-only argparse to avoid install-time deps. Uses rich prints when available.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import harvest as harvest_mod
from . import install as install_mod
from . import verify as verify_mod
from . import bridge_pmos as bridge_mod

REPO_ROOT = Path(__file__).resolve().parents[2]


def _info(msg: str) -> None:
    print(msg)


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    manifest = install_mod.install(
        repo_root=REPO_ROOT,
        target=target,
        preset_name=args.preset,
        author=args.author,
        project_name=args.project_name,
        force=args.force,
    )
    _info(f"Installed preset '{manifest['preset']}' → {target}")
    _info(f"  wrote {len(manifest['written'])} files; skipped {len(manifest['skipped'])}")
    for p in manifest["written"][:20]:
        _info(f"    + {p}")
    if len(manifest["written"]) > 20:
        _info(f"    + ... ({len(manifest['written']) - 20} more)")
    if manifest["skipped"]:
        _info(f"  existing files left in place (use --force to overwrite):")
        for p in manifest["skipped"][:10]:
            _info(f"    · {p}")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    # Same logic as init but with a preset that only contains the requested kind.
    # For MVP: reuse install with --preset extended, then the user picks what to keep.
    _info("add subcommand: forthcoming. For now, copy the extended template you want:")
    _info(f"  cp {REPO_ROOT}/templates/extended/{args.kind}-template.md {target}/specs/{args.kind}.md")
    return 0


def cmd_harvest(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    out_dir = REPO_ROOT / "harvest"
    harvest_mod.run(root, out_dir, dry_run=args.dry_run)
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    report = verify_mod.verify(target)
    print(verify_mod.format_report(report))
    return 0 if report.ok else 1


def cmd_bridge(args: argparse.Namespace) -> int:
    pmos = Path(args.pmos_root).resolve()
    rpt = bridge_mod.install_to_pmos(REPO_ROOT, pmos, dry_run=args.dry_run)
    _info(f"Framework bridge:")
    _info(f"  symlink: {rpt.symlink}")
    _info(f"  env hint: {rpt.env_hint}")
    _info(f"  patch manifest: {rpt.patch_file}")
    _info("  files to edit:")
    for p, change in rpt.files_to_edit:
        _info(f"    - {p}")
        _info(f"      → {change}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="specify-x", description="specKitEnhanced CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init", help="Scaffold a new SDD-compliant project")
    pi.add_argument("target", nargs="?", default=".", help="target directory (default: cwd)")
    pi.add_argument("--preset", default="core", help="preset name: core | extended")
    pi.add_argument("--author", default="@author", help='author handle, e.g. "@alice"')
    pi.add_argument("--project-name", default=None, help="project name (default: basename of target)")
    pi.add_argument("--force", action="store_true", help="overwrite existing spec files")
    pi.set_defaults(func=cmd_init)

    pa = sub.add_parser("add", help="Add an extended template to an existing project")
    pa.add_argument("kind", help="template kind: runbook | security | ...")
    pa.add_argument("--target", default=".")
    pa.set_defaults(func=cmd_add)

    ph = sub.add_parser("harvest", help="Mine a portfolio directory for MD patterns")
    ph.add_argument("root", help="portfolio root directory to scan")
    ph.add_argument("--dry-run", action="store_true")
    ph.set_defaults(func=cmd_harvest)

    pv = sub.add_parser("verify", help="Lint a project's specs/ for schema + ref-link integrity")
    pv.add_argument("target", nargs="?", default=".")
    pv.set_defaults(func=cmd_verify)

    pb = sub.add_parser("bridge", help="Install specKitEnhanced into an AI project management backend")
    pb.add_argument("--pmos-root", required=True, help="path to target AI project management backend root")
    pb.add_argument("--dry-run", action="store_true")
    pb.set_defaults(func=cmd_bridge)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


app = main  # alias for pyproject `specify-x = "specify_x.cli:app"`


if __name__ == "__main__":
    raise SystemExit(main())
