from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import json


@dataclass
class SessionState:
    turns: list[str] = field(default_factory=list)
    summaries: list[str] = field(default_factory=list)

    def add_turn(self, text: str) -> None:
        self.turns.append(text)

    def add_summary(self, text: str) -> None:
        self.summaries.append(text)

    def render(self) -> str:
        return "\n".join(["Session state:", *self.turns, *self.summaries])


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
