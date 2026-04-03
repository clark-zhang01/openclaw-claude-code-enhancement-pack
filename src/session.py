from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import json
import logging
import uuid
import time
from typing import Any


@dataclass
class SessionState:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)
    turns: list[str] = field(default_factory=list)
    summaries: list[str] = field(default_factory=list)
    active: bool = True

    def add_turn(self, text: str) -> None:
        self.turns.append(f"[{time.time():.2f}] {text}")

    def add_summary(self, text: str) -> None:
        self.summaries.append(text)
        
    def end_session(self) -> None:
        self.active = False

    def render(self) -> str:
        state_str = "Active" if self.active else "Closed"
        lines = [f"Session {self.id} ({state_str})", "---", "Turns:"]
        lines.extend(self.turns)
        lines.append("---")
        lines.append("Summaries:")
        lines.extend(self.summaries)
        return "\n".join(lines)

class SessionManager:
    """Handles persistence, recovery, and indexing of Claude Code-style sessions."""
    def __init__(self, data_dir: Path | str = "sessions") -> None:
        self.data_dir = Path(data_dir)
        self.logger = logging.getLogger(__name__)
        
    def save(self, state: SessionState) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        file_path = self.data_dir / f"{state.id}.json"
        data = {
            "id": state.id,
            "created_at": state.created_at,
            "turns": state.turns,
            "summaries": state.summaries,
            "active": state.active
        }
        file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        self.logger.debug(f"Saved session {state.id} to {file_path}")

    def load(self, session_id: str) -> SessionState | None:
        file_path = self.data_dir / f"{session_id}.json"
        if not file_path.exists():
            self.logger.warning(f"Session file not found: {file_path}")
            return None
            
        data = json.loads(file_path.read_text(encoding="utf-8"))
        state = SessionState(
            id=data.get("id", session_id),
            created_at=data.get("created_at", time.time()),
            active=data.get("active", False)
        )
        state.turns = data.get("turns", [])
        state.summaries = data.get("summaries", [])
        return state


def load_session_state(path: Path | str = "session.json") -> SessionState:
    session_path = Path(path)
    if not session_path.exists():
        return SessionState()
    data = json.loads(session_path.read_text(encoding="utf-8"))
    state = SessionState()
    for turn in data.get("turns", []):
        state.add_turn(str(turn))
    for summary in data.get("summaries", []):
        state.add_summary(str(summary))
    return state
