from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CodeflowStep:
    name: str
    description: str


DEFAULT_CODEFLOW = (
    CodeflowStep(name="inspect", description="Inspect the repository and gather context"),
    CodeflowStep(name="plan", description="Plan the change before editing"),
    CodeflowStep(name="patch", description="Apply the implementation change"),
    CodeflowStep(name="verify", description="Run validation after the change"),
    CodeflowStep(name="summarize", description="Summarize the change and follow-ups"),
)
