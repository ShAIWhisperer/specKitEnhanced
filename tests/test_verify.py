"""Verify detects malformed specs."""

from __future__ import annotations

from pathlib import Path

from src.specify_x import verify as verify_mod


def test_placeholders_skipped(tmp_path: Path) -> None:
    root = tmp_path / "proj"
    (root / "specs").mkdir(parents=True)
    (root / "specs" / "constitution.md").write_text(
        "---\ntitle: t\nstatus: draft\ntype: constitution\n---\n\n"
        "See `{ref:path#section}` as example.\n"
        "See `{ref:specs/<slug>.md}` placeholder.\n"
    )
    r = verify_mod.verify(root)
    # angle-brackets and explicit `path#section` are placeholders → no errors
    assert r.ok, [i.message for i in r.issues]


def test_missing_constitution_detected(tmp_path: Path) -> None:
    root = tmp_path / "proj"
    (root / "specs").mkdir(parents=True)
    (root / "specs" / "other.md").write_text(
        "---\ntitle: x\nstatus: draft\ntype: architecture\n---\n"
    )
    r = verify_mod.verify(root)
    assert any(i.kind == "layout" for i in r.issues)


def test_unresolved_ref_flagged(tmp_path: Path) -> None:
    root = tmp_path / "proj"
    (root / "specs").mkdir(parents=True)
    (root / "specs" / "constitution.md").write_text(
        "---\ntitle: c\nstatus: draft\ntype: constitution\n---\n"
    )
    (root / "specs" / "architecture").mkdir()
    (root / "specs" / "architecture" / "a.md").write_text(
        "---\ntitle: a\nstatus: draft\ntype: architecture\n---\n\n"
        "Cites {ref:specs/does/not/exist.md}\n"
    )
    r = verify_mod.verify(root)
    assert any(i.kind == "ref-link" for i in r.issues)


def test_missing_required_field(tmp_path: Path) -> None:
    root = tmp_path / "proj"
    (root / "specs").mkdir(parents=True)
    (root / "specs" / "constitution.md").write_text(
        "---\ntitle: c\nstatus: draft\ntype: constitution\n---\n"
    )
    (root / "specs" / "architecture").mkdir()
    # missing `type`
    (root / "specs" / "architecture" / "bad.md").write_text(
        "---\ntitle: x\nstatus: draft\n---\n"
    )
    r = verify_mod.verify(root)
    assert any(
        "missing required field: type" in i.message for i in r.issues
    ), [i.message for i in r.issues]
