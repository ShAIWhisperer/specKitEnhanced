"""Portfolio miner — read-only audit of ~/ai-projects/ for MD patterns.

Emits:
  harvest/audit-matrix.csv       — project × file-type matrix (1/0)
  harvest/pattern-library.md     — distilled patterns, ranked
  harvest/exemplar-excerpts/*.md — raw samples from top projects
  harvest/voice-samples.md       — tone/voice snippets

Stdlib-only. Safe to run without installing the package.
"""

from __future__ import annotations

import csv
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

SKIP_DIRS = {
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    ".next",
    ".git",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "myenv",
    "target",
}

MD_PATTERNS: dict[str, re.Pattern] = {
    "README": re.compile(r"^README(\.md)?$", re.I),
    "CLAUDE": re.compile(r"^CLAUDE(\.md)?$", re.I),
    "AGENTS": re.compile(r"^AGENTS(\.md)?$", re.I),
    "ARCHITECTURE": re.compile(r"^ARCHITECTURE(\.md)?$", re.I),
    "DESIGN": re.compile(r"^DESIGN(\.md)?$", re.I),
    "SYSTEM": re.compile(r"^SYSTEM(\.md)?$", re.I),
    "HISTORY": re.compile(r"^HISTORY(\.md)?$", re.I),
    "LESSONS": re.compile(r"^LESSONS.*(\.md)?$", re.I),
    "DECISIONS": re.compile(r"^DECISIONS(\.md)?$", re.I),
    "ADR": re.compile(r"^ADR.*\.md$", re.I),
    "PRD": re.compile(r"^PRD(\.md)?$", re.I),
    "SPEC": re.compile(r"^SPEC(\.md)?$", re.I),
    "ROADMAP": re.compile(r"^ROADMAP(\.md)?$", re.I),
    "CHANGELOG": re.compile(r"^CHANGELOG(\.md)?$", re.I),
    "TASKS": re.compile(r"^TASKS(\.md)?$", re.I),
    "PLAN": re.compile(r"^PLAN(\.md)?$", re.I),
    "RESEARCH": re.compile(r"^RESEARCH.*(\.md)?$", re.I),
    "GLOSSARY": re.compile(r"^GLOSSARY(\.md)?$", re.I),
    "CONVENTIONS": re.compile(r"^CONVENTIONS(\.md)?$", re.I),
    "RUNBOOK": re.compile(r"^RUNBOOK(\.md)?$", re.I),
    "KNOWLEDGE": re.compile(r"^KNOWLEDGE(\.md)?$", re.I),
    "MOAT": re.compile(r"^MOAT(\.md)?$", re.I),
    "PERSONAS": re.compile(r"^PERSONAS(\.md)?$", re.I),
    "RISKS": re.compile(r"^RISKS(\.md)?$", re.I),
    "METRICS": re.compile(r"^METRICS(\.md)?$", re.I),
    "DEPLOYMENT": re.compile(r"^DEPLOYMENT.*(\.md)?$", re.I),
    "SECURITY": re.compile(r"^SECURITY(\.md)?$", re.I),
    "CONTRIBUTING": re.compile(r"^CONTRIBUTING(\.md)?$", re.I),
    "QUICK_START": re.compile(r"^QUICK[_-]?START(\.md)?$", re.I),
    "SKILL": re.compile(r"^SKILL(\.md)?$", re.I),
    "MEMORY": re.compile(r"^MEMORY(\.md)?$", re.I),
    "USER_PROFILE": re.compile(r"^USER[_-]?PROFILE(\.md)?$", re.I),
}

SIGNAL_FOLDERS = {
    "docs",
    "specs",
    ".claude",
    ".cursor",
    "memory",
    "memory-seed",
    "templates",
    "commands",
    "agents",
    "hooks",
    "__skilss",  # PM OS typo kept intentionally
    "skills",
    ".github",
}


@dataclass
class ProjectAudit:
    name: str
    path: Path
    md_hits: dict[str, list[Path]] = field(default_factory=lambda: defaultdict(list))
    folder_hits: set[str] = field(default_factory=set)
    total_md_files: int = 0

    def has(self, kind: str) -> bool:
        return bool(self.md_hits.get(kind))


def scan_project(project_dir: Path, max_depth: int = 3) -> ProjectAudit:
    audit = ProjectAudit(name=project_dir.name, path=project_dir)
    root_depth = len(project_dir.parts)

    for dirpath, dirnames, filenames in os.walk(project_dir):
        depth = len(Path(dirpath).parts) - root_depth
        if depth > max_depth:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for d in list(dirnames):
            if d in SIGNAL_FOLDERS:
                audit.folder_hits.add(d)
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            audit.total_md_files += 1
            for kind, pat in MD_PATTERNS.items():
                if pat.match(fn):
                    audit.md_hits[kind].append(Path(dirpath) / fn)
                    break
        if depth == 0:
            for hidden in (".claude", ".cursor", ".github"):
                if hidden in os.listdir(project_dir) if project_dir.exists() else False:
                    audit.folder_hits.add(hidden)
    return audit


def excerpt(path: Path, max_lines: int = 20) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    lines = text.splitlines()[:max_lines]
    return "\n".join(lines)


def write_matrix(audits: list[ProjectAudit], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    kinds = sorted(MD_PATTERNS.keys())
    folders = sorted(SIGNAL_FOLDERS)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["project", "total_md", *kinds, *[f"folder:{f}" for f in folders]])
        for a in audits:
            w.writerow(
                [
                    a.name,
                    a.total_md_files,
                    *(1 if a.has(k) else 0 for k in kinds),
                    *(1 if f in a.folder_hits else 0 for f in folders),
                ]
            )


def rank_patterns(audits: list[ProjectAudit]) -> tuple[Counter, Counter]:
    md_counter: Counter = Counter()
    folder_counter: Counter = Counter()
    for a in audits:
        for k, hits in a.md_hits.items():
            if hits:
                md_counter[k] += 1
        for f in a.folder_hits:
            folder_counter[f] += 1
    return md_counter, folder_counter


def write_pattern_library(audits: list[ProjectAudit], out: Path) -> None:
    md_counter, folder_counter = rank_patterns(audits)
    n = len(audits)
    lines = [
        "# Pattern Library — harvested from portfolio",
        "",
        f"Audited **{n} projects**.",
        "",
        "## MD file adoption (frequency)",
        "",
        "| File kind | Projects | % |",
        "|---|---:|---:|",
    ]
    for k, c in md_counter.most_common():
        lines.append(f"| {k} | {c} | {c / n:.0%} |")
    lines += [
        "",
        "## Signal folders (frequency)",
        "",
        "| Folder | Projects | % |",
        "|---|---:|---:|",
    ]
    for f, c in folder_counter.most_common():
        lines.append(f"| `{f}/` | {c} | {c / n:.0%} |")

    lines += ["", "## Top 15 projects by total MD files (likely doc-rich)", ""]
    top = sorted(audits, key=lambda a: a.total_md_files, reverse=True)[:15]
    for a in top:
        lines.append(f"- **{a.name}** — {a.total_md_files} MD files, kinds: {sorted(k for k in a.md_hits)}")

    lines += [
        "",
        "## Exemplar candidates (projects with rare/unique files)",
        "",
    ]
    rare = {k for k, c in md_counter.items() if 0 < c <= max(1, n // 20)}
    for a in audits:
        rare_hits = [k for k in a.md_hits if k in rare]
        if rare_hits:
            lines.append(f"- **{a.name}** — rare: {rare_hits}")

    out.write_text("\n".join(lines) + "\n")


def write_excerpts(audits: list[ProjectAudit], out_dir: Path, top_n: int = 15) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    top = sorted(audits, key=lambda a: a.total_md_files, reverse=True)[:top_n]
    for a in top:
        for kind, paths in a.md_hits.items():
            if not paths:
                continue
            safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", a.name)
            out_path = out_dir / f"{safe_name}__{kind}.md"
            p = paths[0]
            snippet = excerpt(p, max_lines=30)
            out_path.write_text(
                f"# {a.name} — {kind}\n\n"
                f"Source: `{p.relative_to(a.path.parent) if a.path.parent in p.parents else p}`\n\n"
                f"```md\n{snippet}\n```\n"
            )


def write_voice_samples(audits: list[ProjectAudit], out: Path) -> None:
    lines = ["# Voice samples — tone/prose style across portfolio", ""]
    candidates = ["README", "CLAUDE", "KNOWLEDGE", "PRD", "ARCHITECTURE"]
    for a in sorted(audits, key=lambda a: a.total_md_files, reverse=True)[:10]:
        for k in candidates:
            if a.md_hits.get(k):
                p = a.md_hits[k][0]
                snippet = excerpt(p, max_lines=12)
                lines += [f"## {a.name} — {k}", "```", snippet, "```", ""]
                break
    out.write_text("\n".join(lines) + "\n")


def run(root: Path, out_dir: Path, dry_run: bool = False) -> list[ProjectAudit]:
    audits: list[ProjectAudit] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith(".") or child.name in SKIP_DIRS:
            continue
        if child.name == "specKitEnhanced":
            continue
        audits.append(scan_project(child))
    if dry_run:
        print(f"Would audit {len(audits)} projects under {root}")
        return audits
    write_matrix(audits, out_dir / "audit-matrix.csv")
    write_pattern_library(audits, out_dir / "pattern-library.md")
    write_excerpts(audits, out_dir / "exemplar-excerpts")
    write_voice_samples(audits, out_dir / "voice-samples.md")
    print(
        f"Harvested {len(audits)} projects → {out_dir}/"
        f"\n  audit-matrix.csv"
        f"\n  pattern-library.md"
        f"\n  exemplar-excerpts/ ({len(list((out_dir / 'exemplar-excerpts').iterdir()))} files)"
        f"\n  voice-samples.md"
    )
    return audits


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0].startswith("-"):
        print("Usage: python -m specify_x.harvest <portfolio-root> [--dry-run]", file=sys.stderr)
        return 1
    root = Path(argv[0])
    out_dir = Path(__file__).resolve().parents[2] / "harvest"
    dry = "--dry-run" in argv
    run(root, out_dir, dry_run=dry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
