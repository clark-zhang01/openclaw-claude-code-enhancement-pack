from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import logging
from typing import Any


@dataclass(frozen=True)
class PackInfo:
    id: str
    name: str
    version: str
    compatible_openclaw: str
    capabilities: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PackInfo:
        return cls(
            id=data.get("id", "unknown"),
            name=data.get("name", "Unknown Pack"),
            version=data.get("version", "0.0.0"),
            compatible_openclaw=data.get("compatible_openclaw", "*"),
            capabilities=data.get("capabilities", []),
        )


def load_manifest(path: Path | str = "manifest.json") -> dict:
    manifest_path = Path(path)
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def load_pack_info(path: Path | str = "manifest.json") -> PackInfo:
    try:
        data = load_manifest(path)
        return PackInfo.from_dict(data)
    except Exception as e:
        logging.warning(f"Failed to load pack info from {path}: {e}")
        return PackInfo.from_dict({})
