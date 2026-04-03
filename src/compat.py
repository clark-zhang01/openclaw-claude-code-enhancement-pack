from __future__ import annotations

from pathlib import Path

from .pack import load_pack_info


def compatibility_summary(manifest_path: Path | str = "manifest.json") -> str:
    info = load_pack_info(manifest_path)
    return f"{info.name} is compatible with OpenClaw {info.compatible_openclaw}"
