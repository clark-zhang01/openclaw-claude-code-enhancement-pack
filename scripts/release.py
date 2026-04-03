from __future__ import annotations

from pathlib import Path

from src.pack import load_pack_info


if __name__ == "__main__":
    info = load_pack_info(Path("manifest.json"))
    print(f"Preparing release for {info.name} {info.version}")
