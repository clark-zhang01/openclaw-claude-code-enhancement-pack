from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import logging
from typing import Any


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

class ToolRouter:
    """Manages tool routing and intercepts tool calls for policy enforcement."""
    def __init__(self, policies: tuple[ToolPolicy, ...] = DEFAULT_TOOL_POLICIES) -> None:
        self.policies = {p.name: p for p in policies}
        self.logger = logging.getLogger(__name__)

    def route_tool_call(self, tool_name: str, args: dict[str, Any]) -> dict[str, Any]:
        """Intercepts and routes a tool call, applying policy rules."""
        if tool_name not in self.policies:
            self.logger.warning(f"Unknown tool called: {tool_name}")
            return {"status": "error", "message": f"Tool {tool_name} is not supported by policy."}
        
        policy = self.policies[tool_name]
        if policy.requires_confirmation:
            # Here we would normally trigger an interactive prompt or return a 'requires_approval' payload
            self.logger.info(f"Tool {tool_name} requires confirmation. Invoking interceptor.")
            return {"status": "pending_approval", "tool": tool_name, "args": args}

        self.logger.debug(f"Executing allowed tool: {tool_name}")
        return {"status": "routed", "tool": tool_name, "args": args}


DEFAULT_TOOL_POLICIES = (
    ToolPolicy(name="read", kind="read-only", requires_confirmation=False),
    ToolPolicy(name="write", kind="write-capable", requires_confirmation=False),
    ToolPolicy(name="exec", kind="destructive", requires_confirmation=True),
)


def load_tool_policy(path: Path | str = "manifest.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
