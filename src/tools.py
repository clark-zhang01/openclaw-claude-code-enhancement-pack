from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class ToolPolicy:
    name: str
    kind: str
    requires_confirmation: bool


DEFAULT_TOOL_POLICIES = (
    ToolPolicy(name="read", kind="read-only", requires_confirmation=False),
    ToolPolicy(name="write", kind="write-capable", requires_confirmation=False),
    ToolPolicy(name="exec", kind="destructive", requires_confirmation=True),
)


def load_tool_policy(path: Path | str = "manifest.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
