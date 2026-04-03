from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

from .bootstrap import bootstrap
from .compat import compatibility_summary
from .pack import load_pack_info


@dataclass(frozen=True)
class RuntimeReport:
    pack_name: str
    bootstrap_message: str
    compatibility_message: str

    def as_text(self) -> str:
        return "\n".join([
            f"Pack: {self.pack_name}",
            self.bootstrap_message,
            self.compatibility_message,
        ])


class PackRuntime:
    def __init__(self, manifest_path: Path | str = "manifest.json") -> None:
        self.manifest_path = Path(manifest_path)
        self.pack_info = load_pack_info(self.manifest_path)

    def prepare(self) -> RuntimeReport:
        return RuntimeReport(
            pack_name=self.pack_info.name,
            bootstrap_message=bootstrap(self.manifest_path),
            compatibility_message=compatibility_summary(self.manifest_path),
        )

    def render_manifest(self) -> str:
        return json.dumps(load_manifest(self.manifest_path), indent=2, ensure_ascii=False)


def load_manifest(path: Path | str = "manifest.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
