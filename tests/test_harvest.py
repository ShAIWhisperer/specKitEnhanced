"""Smoke tests for harvest.py — zero external deps."""

from __future__ import annotations

import tempfile
from pathlib import Path

from src.specify_x import harvest


def test_harvest_scans_project(tmp_path: Path) -> None:
    proj = tmp_path / "demo-project"
    proj.mkdir()
    (proj / "README.md").write_text("# demo\n")
    (proj / "CLAUDE.md").write_text("claude context\n")
    (proj / "docs").mkdir()
    (proj / "docs" / "ARCHITECTURE.md").write_text("# arch\n")

    audit = harvest.scan_project(proj)
    assert audit.has("README")
    assert audit.has("CLAUDE")
    assert audit.has("ARCHITECTURE")
    assert "docs" in audit.folder_hits


def test_harvest_run_writes_outputs(tmp_path: Path) -> None:
    root = tmp_path / "portfolio"
    root.mkdir()
    (root / "a").mkdir()
    (root / "a" / "README.md").write_text("# a\n")
    (root / "b").mkdir()
    (root / "b" / "CLAUDE.md").write_text("# b\n")

    out = tmp_path / "out"
    audits = harvest.run(root, out)

    assert len(audits) == 2
    assert (out / "audit-matrix.csv").exists()
    assert (out / "pattern-library.md").exists()
    assert (out / "exemplar-excerpts").is_dir()
