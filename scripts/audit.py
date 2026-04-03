from __future__ import annotations

from pathlib import Path

from src.compat import compatibility_summary


if __name__ == "__main__":
    print(compatibility_summary(Path("manifest.json")))
