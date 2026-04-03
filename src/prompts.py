from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class PromptBlock:
    name: str
    text: str

DEFAULT_PROMPTS = (
    PromptBlock(name="identity", text="You are an advanced Agentic Runtime inspired by Claude Code. You handle complex logic, coding, research, and analysis."),
    PromptBlock(name="context_facts", text="Inject environment facts, paths, and current date here to ground the agent."),
    PromptBlock(name="context_preferences", text="Inject the user's communication style and constraints here."),
    PromptBlock(name="context_workstate", text="Track the current task, recent progress, and pending steps to maintain session continuity."),
    PromptBlock(name="safety", text="Gate risky operations via ToolRouter and preserve fallback behavior.")
)

def render_prompt_blocks() -> str:
    return "\n".join(f"[{block.name}] {block.text}" for block in DEFAULT_PROMPTS)
