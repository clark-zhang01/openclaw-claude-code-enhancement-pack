# OpenClaw Claude Code Enhancement Pack

Updated: 2026-04-03 16:05 (Australia/Adelaide)

This repository hosts the first public OpenClaw enhancement pack for Claude Code-style capabilities.

## What this pack is

- an OpenClaw enhancement pack
- a Claude Code-inspired capability layer
- a Python-first orchestration layer with optional Rust runtime support
- a modular extension that can be installed, removed, and upgraded safely

## What this pack provides

- prompt engineering improvements
- command / tool routing logic
- session recovery and replay support
- coding-oriented workflows
- codebase-aware context handling
- compatibility auditing
- safe fallback / disable behavior

## What this pack is not

- not a fork of Claude Code
- not a rewrite of OpenClaw core
- not a direct copy of Claude Code source code

## Repository layout

```text
openclaw-claude-code-enhancement-pack/
├── README.md
├── LICENSE
├── manifest.json
├── pyproject.toml
├── .gitignore
├── docs/
├── src/
├── prompts/
├── tools/
├── session/
├── runtime/
├── codeflow/
├── policies/
├── examples/
├── tests/
└── scripts/
```

## Language Support

The core system, prompts, and runtime engine of this enhancement pack are built in **English** to ensure maximum compatibility and predictability with LLMs. However, the OpenClaw agent acting as the bridge will **auto-adapt** its conversational language to match the user's input language (e.g., if you speak Chinese, it will respond and summarize in Chinese while executing the English codeflow underneath).

## Usage & Commands

This enhancement pack operates as a skill bridge. You do NOT need to use slash commands (like `/config`). You can simply talk to your OpenClaw agent using natural language to control the pack. 

### Supported Commands (Natural Language Triggers)

| Intent | Example Utterance | Behavior |
|--------|-------------------|----------|
| **Turn On** | "Enable claude-code", "启用 claude-code 外挂" | Activates the Codeflow engine, ToolRouter, and Codebase session tracking. |
| **Turn Off** | "Disable claude-code", "关闭 claude-code 外挂" | Safely detaches the Codeflow engine and returns OpenClaw to standard assistant mode. |
| **Status Check** | "Claude-code status", "查看外挂状态" | The agent will report whether the pack is active, which capabilities are enabled, and if the Rust accelerator is loaded. |

### Standard Response Templates

To ensure a predictable and professional experience, the agent will use consistent response templates when you issue the above commands.

#### 1. On Activation
```text
🔌 [Claude Code Enhancement Pack] Activated.
Mode: Codeflow (Inspect -> Plan -> Patch -> Verify)
Safety: ToolRouter Enabled (Destructive actions require approval)
Acceleration: Rust Engine [Loaded/Bypassed]

I am now in coding mode. What repository or file would you like to work on?
```

#### 2. On Deactivation
```text
🔌 [Claude Code Enhancement Pack] Deactivated.
Session state saved. Returning to standard OpenClaw assistant mode.
```

#### 3. On Status Check
```text
📊 [Claude Code Enhancement Pack Status]
- State: Active / Inactive
- Current Phase: [e.g., PLAN]
- Active Session ID: [UUID]
- Rust Accelerator: [Available/Unavailable]
```

## Install / bootstrap

To install and deploy this pack to any OpenClaw instance:

1. Clone this repository into your workspace.
2. Link the `SKILL.md` to your OpenClaw skills directory:
   ```bash
   mkdir -p ~/.openclaw/workspace/skills/claude-code-enhancement
   ln -s /path/to/openclaw-claude-code-enhancement-pack/SKILL.md ~/.openclaw/workspace/skills/claude-code-enhancement/SKILL.md
   ```
3. (Optional) Compile the Rust accelerator for high-performance codebase inspection:
   ```bash
   cd rust_bridge && cargo build --release && cp target/release/libclaude_code_runtime.so ../claude_code_runtime.so
   ```
4. Tell your OpenClaw agent: "Enable claude-code".

## Compatibility

The pack declares its compatible OpenClaw version range in `manifest.json` and supports fallback / disable behavior when compatibility changes.

## Status

This repository is in active preparation and initial implementation.
