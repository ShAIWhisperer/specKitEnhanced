"""Verify — frontmatter schema + ref-link integrity + status lifecycle legality."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REF_RE = re.compile(r"\{ref:([^}]+)\}")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

LEGAL_TRANSITIONS = {
    "draft": {"review", "draft"},
    "review": {"approved", "draft", "review"},
    "approved": {"implemented", "review", "approved"},
    "implemented": {"deprecated", "implemented"},
    "deprecated": {"deprecated"},
    # ADR flavor
    "proposed": {"accepted", "rejected", "proposed"},
    "accepted": {"superseded", "deprecated", "accepted"},
    "rejected": {"rejected"},
    "superseded": {"superseded"},
}

LEGAL_STATUS = set().union(*LEGAL_TRANSITIONS.values()) | set(LEGAL_TRANSITIONS.keys())


@dataclass
class Issue:
    path: Path
    kind: str
    message: str


@dataclass
class Report:
    issues: list[Issue] = field(default_factory=list)
    checked: int = 0

    @property
    def ok(self) -> bool:
        return not self.issues


def _parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    data: dict = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith("  "):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            data[k.strip()] = v.strip().strip('"\'')
    return data


def _load_schema(schema_path: Path) -> dict:
    return json.loads(schema_path.read_text(encoding="utf-8"))


NO_STATUS_REQUIRED_TYPES = {
    "history", "lessons", "decisions", "personas", "glossary", "risks",
}


def _validate_frontmatter(fm: dict, schema: dict, path: Path, issues: list[Issue]) -> None:
    fm_type = fm.get("type")
    required = schema.get("required", [])
    for field_name in required:
        # Singleton maintained docs (history/lessons/etc) don't carry a status.
        if field_name == "status" and fm_type in NO_STATUS_REQUIRED_TYPES:
            continue
        if field_name not in fm or not fm.get(field_name):
            issues.append(Issue(path, "frontmatter", f"missing required field: {field_name}"))

    props = schema.get("properties", {})
    status = fm.get("status")
    if status and status not in LEGAL_STATUS:
        issues.append(Issue(path, "frontmatter", f"illegal status: {status}"))

    type_prop = props.get("type", {})
    if "enum" in type_prop and fm_type and fm_type not in type_prop["enum"]:
        issues.append(Issue(path, "frontmatter", f"illegal type: {fm_type}"))


PLACEHOLDER_MARKERS = ("<", ">", "...", "{{", "}}", "NNNN", "XXXX")


def _is_placeholder(ref: str) -> bool:
    return any(mark in ref for mark in PLACEHOLDER_MARKERS) or ref.strip() == ""


def _check_refs(text: str, project_root: Path, path: Path, issues: list[Issue]) -> None:
    # Strip fenced code blocks — refs in backticks or fences are examples, not links.
    text_no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text_no_code = re.sub(r"`[^`\n]*`", "", text_no_code)
    for m in REF_RE.finditer(text_no_code):
        ref = m.group(1).strip()
        if _is_placeholder(ref):
            continue
        # strip #anchor and :symbol for filesystem check
        target = ref.split("#", 1)[0].split(":", 1)[0]
        if not target:
            continue
        p = project_root / target
        if not p.exists():
            issues.append(Issue(path, "ref-link", f"unresolved reference: {{ref:{ref}}}"))


def verify(project_root: Path, schema_path: Path | None = None) -> Report:
    report = Report()
    specs_dir = project_root / "specs"
    if not specs_dir.exists():
        report.issues.append(Issue(project_root, "layout", "specs/ directory missing"))
        return report

    if schema_path is None:
        # prefer .specify/schemas/ then repo schemas/
        cand1 = project_root / ".specify" / "schemas" / "frontmatter.schema.json"
        cand2 = project_root / "schemas" / "frontmatter.schema.json"
        schema_path = cand1 if cand1.exists() else cand2 if cand2.exists() else None

    schema = _load_schema(schema_path) if schema_path and schema_path.exists() else {
        "required": ["title", "status", "type"],
        "properties": {},
    }

    for md in specs_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(text)
        if not fm:
            report.issues.append(Issue(md, "frontmatter", "missing YAML frontmatter"))
            continue
        report.checked += 1
        _validate_frontmatter(fm, schema, md, report.issues)
        _check_refs(text, project_root, md, report.issues)

    # constitution presence
    if not (specs_dir / "constitution.md").exists():
        report.issues.append(Issue(project_root, "layout", "specs/constitution.md missing"))

    return report


def format_report(r: Report) -> str:
    lines = [f"Verified {r.checked} spec files.", ""]
    if not r.issues:
        lines.append("OK — no issues.")
        return "\n".join(lines)
    by_kind: dict[str, list[Issue]] = {}
    for i in r.issues:
        by_kind.setdefault(i.kind, []).append(i)
    for kind, issues in sorted(by_kind.items()):
        lines.append(f"## {kind} ({len(issues)})")
        for i in issues:
            try:
                rel = i.path.relative_to(Path.cwd())
            except ValueError:
                rel = i.path
            lines.append(f"  {rel}: {i.message}")
        lines.append("")
    lines.append(f"FAIL — {len(r.issues)} issue(s).")
    return "\n".join(lines)
