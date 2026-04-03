# Claude Code Enhancement Pack (OpenClaw Skill)

## Trigger
Activate when the user says "启用 claude-code 外挂", "activate claude code", "enter coding mode", or explicitly asks to use the Claude Code codeflow.
Deactivate when the user says "停用 claude-code 外挂", "deactivate claude code", or "exit coding mode".

## State Management
When activated, you MUST:
1. Announce: "🔌 Claude Code Enhancement Pack 已激活。进入 Codeflow 模式。"
2. Route all complex coding tasks (like refactoring, bug fixing, or feature implementation) through the 4-step Codeflow:
   - **INSPECT**: Read relevant files and gather context first.
   - **PLAN**: Propose a concrete implementation plan.
   - **PATCH**: Apply the changes using precise tool calls.
   - **VERIFY**: Run tests or checks to validate the patch.
3. For any destructive tool calls (like `exec` for system modifications or running unknown scripts), you MUST explicitly warn the user and ensure they approve the action (the ToolRouter policy).
4. Maintain a persistent focus on the current coding session. 

When deactivated, you MUST:
1. Announce: "🔌 Claude Code Enhancement Pack 已停用。恢复标准模式。"
2. Return to normal conversational and standard tool execution without the strict 4-step codeflow.

## Integration Note
This SKILL.md acts as the OpenClaw native bridge to the Python-based `openclaw-claude-code-enhancement-pack`. It maps the pack's runtime policies (Codeflow, ToolRouter, Session tracking) into direct Agent behavior constraints.
