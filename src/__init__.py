from __future__ import annotations

from .runtime import PackRuntime
from .pack import load_pack_info
from .session import SessionManager
from .tools import ToolRouter
from .codeflow import CodeflowEngine

__version__ = "0.1.0"

def setup(openclaw_app) -> bool:
    """
    Entrypoint for OpenClaw core to load this enhancement pack.
    OpenClaw will call this function during startup if the pack is installed.
    """
    runtime = PackRuntime()
    if runtime.activate():
        # Inject the Claude Code codeflow and tool router into the host app
        openclaw_app.register_pack(
            name="claude-code-enhancement",
            runtime=runtime,
            router=ToolRouter(),
            session_manager=SessionManager(),
            codeflow=CodeflowEngine()
        )
        return True
    return False
