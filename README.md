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

## Install / bootstrap

This repo is being prepared as a public, installable pack. The first implementation will add:

- a machine-readable manifest
- a Python orchestration layer
- optional Rust runtime support
- compatibility audit helpers
- a minimal bootstrap flow

## Compatibility

The pack declares its compatible OpenClaw version range in `manifest.json` and supports fallback / disable behavior when compatibility changes.

## Status

This repository is in active preparation and initial implementation.
