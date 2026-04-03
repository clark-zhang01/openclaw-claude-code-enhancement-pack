from __future__ import annotations

import logging
from typing import Iterator
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

class CodeflowEngine:
    """Manages execution of standard code-oriented workflows."""
    
    def __init__(self, steps: tuple[CodeflowStep, ...] = DEFAULT_CODEFLOW) -> None:
        self.steps = steps
        self.logger = logging.getLogger(__name__)
        self.current_step_index = 0

    def begin(self) -> None:
        self.logger.info("Starting new Codeflow execution.")
        self.current_step_index = 0

    def step(self) -> CodeflowStep | None:
        if self.current_step_index >= len(self.steps):
            return None
        step = self.steps[self.current_step_index]
        self.current_step_index += 1
        self.logger.info(f"Executing codeflow step: {step.name}")
        return step

    def execute_all(self) -> Iterator[CodeflowStep]:
        self.begin()
        while True:
            step = self.step()
            if not step:
                break
            yield step
            # Here we would integrate with the ToolRouter or LLM prompt engine
            self.logger.debug(f"Completed step {step.name}.")
        self.logger.info("Codeflow execution finished.")
