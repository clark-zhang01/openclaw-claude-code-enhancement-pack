# OpenClaw Claude Code Enhancement Pack — Repository Scaffold

Updated: 2026-04-03 15:46 (Australia/Adelaide)

## 1. Suggested repository layout

```text
openclaw-claude-code-enhancement-pack/
├── README.md
├── LICENSE
├── manifest.json
├── pyproject.toml
├── .gitignore
├── rust/
├── src/
├── prompts/
├── tools/
├── session/
├── runtime/
├── codeflow/
├── policies/
├── examples/
├── tests/
├── scripts/
└── docs/
```

### Operating boundary

- This scaffold belongs in the workspace project folder first.
- Only repository-ready content should live here.
- Human-facing blueprint and execution log content should stay in Obsidian.

---

## 2. Directory responsibilities

### README.md
Human-readable overview, install steps, usage, and compatibility notes.

### manifest.json
Machine-readable pack contract.

### pyproject.toml
Python packaging, dependencies, entrypoints, and tooling.

### rust/
Optional Rust runtime / bridge implementation.

### src/
Python orchestration layer.

### prompts/
Prompt templates and policy-driven assembly.

### tools/
Tool routing rules, wrappers, and safety gates.

### session/
Session persistence, replay, and metadata handling.

### runtime/
Pack runtime glue and OpenClaw hook integration.

### codeflow/
Code-specific workflows like inspect, plan, patch, verify, summarize.

### policies/
Safety, compatibility, fallback, and versioning rules.

### examples/
Usage examples and minimal integration demonstrations.

### tests/
Validation for manifest, compatibility, and pack behavior.

### scripts/
Bootstrap, install, audit, and helper scripts.

---

## 3. Initial file set

A first usable scaffold should at least include:

- `README.md`
- `manifest.json`
- `pyproject.toml`
- `src/__init__.py`
- `src/pack.py`
- `src/bootstrap.py`
- `src/compat.py`
- `src/runtime.py`
- `src/prompts.py`
- `src/tools.py`
- `src/session.py`
- `src/codeflow.py`
- `tests/test_manifest.py`
- `tests/test_compat.py`

---

## 4. Design notes

- Keep core pack logic in Python for readability and orchestration speed
- Allow Rust to be introduced only where it materially improves runtime/safety
- Avoid forcing every module into Rust too early
- Make the repository easy to clone, inspect, and extend

---

## 5. Next step

Use this scaffold to draft the first implementation checklist and then build the minimal runnable pack.
