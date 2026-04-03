from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class PackInfo:
    id: str
    name: str
    version: str
    compatible_openclaw: str


def load_manifest(path: Path | str = "manifest.json") -> dict:
    manifest_path = Path(path)
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def load_pack_info(path: Path | str = "manifest.json") -> PackInfo:
    data = load_manifest(path)
    return PackInfo(
        id=data["id"],
        name=data["name"],
        version=data["version"],
        compatible_openclaw=data["compatible_openclaw"],
    )
