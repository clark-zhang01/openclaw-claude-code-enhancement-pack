from __future__ import annotations

from pathlib import Path

from .pack import load_pack_info


def bootstrap(manifest_path: Path | str = "manifest.json") -> str:
    info = load_pack_info(manifest_path)
    return (
        f"Bootstrapping {info.name} ({info.version}) for OpenClaw "
        f"[{info.compatible_openclaw}]"
    )
