"""Preset loader — reads presets/*.yml with stdlib-only parser fallback."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


def _try_yaml_load(text: str) -> dict:
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text) or {}
    except ImportError:
        return _minimal_yaml(text)


def _minimal_yaml(text: str) -> dict:
    """Very small YAML parser covering only the shape used in presets/*.yml.

    Handles: scalar keys, nested maps (2-space indent), list items `- value`.
    Stops at anything more exotic.
    """
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = raw.rstrip()
        indent = len(stripped) - len(stripped.lstrip(" "))
        body = stripped.strip()

        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack else root

        if body.startswith("- "):
            val = body[2:].strip().strip('"\'')
            if isinstance(parent, list):
                parent.append(val)
            else:
                # parent should be a list-owning key. Fallback: skip.
                continue
            continue

        if ":" in body:
            key, _, rest = body.partition(":")
            key = key.strip()
            rest = rest.strip().strip('"\'')
            if rest == "" or rest == ">":
                # folded-scalar or nested
                # peek next line to decide
                nxt_i = i
                while nxt_i < len(lines) and not lines[nxt_i].strip():
                    nxt_i += 1
                if nxt_i < len(lines):
                    nxt = lines[nxt_i]
                    nxt_indent = len(nxt) - len(nxt.lstrip(" "))
                    if nxt.lstrip().startswith("- ") and nxt_indent > indent:
                        new: Any = []
                    else:
                        new = {}
                else:
                    new = {}
                if isinstance(parent, dict):
                    parent[key] = new
                stack.append((indent, new))
            else:
                if isinstance(parent, dict):
                    parent[key] = rest
    return root


@dataclass
class Preset:
    name: str
    description: str
    templates: list[str] = field(default_factory=list)
    commands: list[str] = field(default_factory=list)
    agents: list[str] = field(default_factory=list)
    schemas: list[str] = field(default_factory=list)
    voice: str = "caveman"
    extends: str | None = None
    bridge: dict[str, Any] = field(default_factory=dict)


def load_preset(preset_path: Path) -> Preset:
    data = _try_yaml_load(preset_path.read_text(encoding="utf-8"))
    return Preset(
        name=data.get("name", preset_path.stem),
        description=(data.get("description") or "").strip(),
        templates=data.get("templates") or [],
        commands=data.get("commands") or [],
        agents=data.get("agents") or [],
        schemas=data.get("schemas") or [],
        voice=data.get("voice") or "caveman",
        extends=data.get("extends"),
        bridge=data.get("bridge") or {},
    )


def resolve(preset_name: str, presets_dir: Path) -> Preset:
    """Load preset and recursively merge any `extends:` parent."""
    path = presets_dir / f"{preset_name}.yml"
    if not path.exists():
        raise FileNotFoundError(f"No preset: {path}")
    p = load_preset(path)
    if p.extends:
        parent = resolve(p.extends, presets_dir)
        p.templates = parent.templates + p.templates
        p.commands = parent.commands + p.commands
        p.agents = parent.agents + p.agents
        p.schemas = parent.schemas + p.schemas
        if not p.bridge:
            p.bridge = parent.bridge
    return p
