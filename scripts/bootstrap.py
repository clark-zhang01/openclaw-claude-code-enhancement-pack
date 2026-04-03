from __future__ import annotations

from pathlib import Path

from src.bootstrap import bootstrap


if __name__ == "__main__":
    print(bootstrap(Path("manifest.json")))
