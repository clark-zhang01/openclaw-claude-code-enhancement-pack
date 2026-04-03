from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PromptBlock:
    name: str
    text: str


DEFAULT_PROMPTS = (
    PromptBlock(name="identity", text="You are the OpenClaw Claude Code Enhancement Pack."),
    PromptBlock(name="profile", text="Prefer concise, direct, upgrade-safe behavior."),
    PromptBlock(name="task", text="Focus on the current coding task and its context."),
    PromptBlock(name="tool", text="Use only the tools allowed for the current task."),
    PromptBlock(name="safety", text="Gate risky operations and preserve fallback behavior."),
)


def render_prompt_blocks() -> str:
    return "\n".join(f"[{block.name}] {block.text}" for block in DEFAULT_PROMPTS)
