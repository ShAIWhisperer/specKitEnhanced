"""End-to-end install + verify test."""

from __future__ import annotations

from pathlib import Path

from src.specify_x import install as install_mod
from src.specify_x import verify as verify_mod

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_core_preset_install(tmp_path: Path) -> None:
    target = tmp_path / "project"
    manifest = install_mod.install(
        repo_root=REPO_ROOT,
        target=target,
        preset_name="core",
        author="@test",
        project_name="pkg-under-test",
        force=False,
    )
    assert manifest["preset"] == "core"
    specs = target / "specs"
    for name in [
        "constitution.md",
        "system.md",
        "history.md",
        "lessons.md",
        "decisions.md",
        "personas.md",
        "glossary.md",
        "risks.md",
    ]:
        assert (specs / name).exists(), f"missing {name}"
    # feature triple + architecture + research
    assert (specs / "features" / "_example" / "spec.md").exists()
    assert (specs / "features" / "_example" / "plan.md").exists()
    assert (specs / "features" / "_example" / "tasks.md").exists()
    assert (specs / "features" / "_example" / "design.md").exists()
    assert (specs / "architecture" / "_example.md").exists()
    assert (specs / "research" / "_example.md").exists()

    # verify passes
    report = verify_mod.verify(target)
    assert report.ok, f"verify failed: {report.issues}"


def test_pm_os_preset_install(tmp_path: Path) -> None:
    target = tmp_path / "project"
    manifest = install_mod.install(
        repo_root=REPO_ROOT,
        target=target,
        preset_name="pm-os",
        author="@test",
        project_name="pkg-under-test",
        force=False,
    )
    assert manifest["preset"] == "pm-os"
    specs = target / "specs"
    for name in [
        "data-model.md",
        "security.md",
        "observability.md",
        "contracts/_example.md",
        "runbooks/_example.md",
        "ux/_example.md",
    ]:
        assert (specs / name).exists(), f"missing {name}"

    report = verify_mod.verify(target)
    assert report.ok, f"verify failed: {report.issues}"


def test_idempotent(tmp_path: Path) -> None:
    target = tmp_path / "project"
    install_mod.install(REPO_ROOT, target, "core")
    # modify a file
    arch_file = target / "specs" / "architecture" / "_example.md"
    arch_file.write_text("# user edits\n")
    # re-run must not overwrite
    install_mod.install(REPO_ROOT, target, "core")
    assert arch_file.read_text() == "# user edits\n"
