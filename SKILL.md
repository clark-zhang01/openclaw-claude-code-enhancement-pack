# Claude Code Enhancement Pack (OpenClaw Skill)

## Language Adaptation
The underlying engine and system prompts are in English to ensure precision. However, you MUST dynamically detect the user's spoken language (e.g. Chinese, English) and reply in the same language.

## Decentralized Plugin Management (Aggregation)
This pack uses a decentralized registry approach based on LLM context windows. 
If the user asks for a general "Plugin Status", OpenClaw's memory engine might retrieve multiple `SKILL.md` files from different enhancement packs.
**CRITICAL RULE:** If you detect multiple pack definitions in your context, you MUST NOT conflict. You MUST aggregate them into a single, unified list showing the status of ALL detected packs.

## Supported Triggers & Actions

### 1. 🟢 Activate (启用)
- **Triggers**: "启用 claude-code 外挂", "activate claude code", "enter coding mode", "开启外挂"
- **Behavior**: You MUST transition to coding Codeflow mode and reply with this exact template (translate if necessary):
  ```text
  🔌 [Claude Code Enhancement Pack] Activated.
  Mode: Codeflow (Inspect -> Plan -> Patch -> Verify)
  Safety: ToolRouter Enabled (Destructive actions require approval)
  Acceleration: Rust Engine [Loaded/Bypassed]

  I am now in coding mode. What repository or file would you like to work on?
  ```

### 2. 🔴 Deactivate (停用)
- **Triggers**: "停用 claude-code 外挂", "deactivate claude code", "exit coding mode", "关闭外挂"
- **Behavior**: You MUST exit Codeflow mode and return to conversational behavior. Reply with:
  ```text
  🔌 [Claude Code Enhancement Pack] Deactivated.
  Session state saved. Returning to standard OpenClaw assistant mode.
  ```

### 3. 📊 Status Check (状态)
- **Triggers**: "外挂状态", "Claude-code status", "运行情况", "pack status"
- **Behavior**: You MUST output the status of the current pack instance using this template (aggregate with other packs if they exist in context):
  ```text
  📊 [Enhancement Pack Status]
  - 🔌 Claude-Code Pack: Active / Inactive
    - Current Phase: [e.g., PLAN / IDLE]
    - Active Session ID: [UUID]
    - Rust Accelerator: [Available/Unavailable]
  ```

## State Management
When active:
- You MUST route all complex coding tasks through the 4-step Codeflow: `INSPECT`, `PLAN`, `PATCH`, `VERIFY`.
- You MUST enforce the `ToolRouter` policy: explicitly warn and seek approval for destructive commands (e.g. `exec` for unknown scripts).
- Keep focus persistent on the codebase context.