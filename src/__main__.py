import sys
import logging
from pathlib import Path

from src.runtime import PackRuntime
from src.session import SessionManager, SessionState
from src.tools import ToolRouter
from src.codeflow import CodeflowEngine
from src.prompts import render_prompt_blocks

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main() -> None:
    print("=== OpenClaw Claude Code Enhancement Pack ===")
    
    # 1. Activate Runtime
    runtime = PackRuntime()
    if not runtime.activate():
        print("Failed to activate runtime.")
        sys.exit(1)
        
    print("\n[Runtime Status]")
    print(runtime.prepare().as_text())
    
    # 2. Setup Session
    session_mgr = SessionManager()
    state = SessionState()
    state.add_turn("User: Initialize enhancement pack environment.")
    
    # 3. Setup Tools & Codeflow
    router = ToolRouter()
    codeflow = CodeflowEngine()
    
    print("\n[System Prompts]")
    print(render_prompt_blocks())
    
    print("\n[Executing Codeflow Demo]")
    # Run a simulated workflow
    codeflow.begin()
    for i in range(3):  # Just run the first 3 steps: inspect, plan, patch
        step = codeflow.step()
        if not step:
            break
        print(f"-> Step: {step.name.upper()} ({step.description})")
        
        # Simulate tool calls based on the step
        if step.name == "inspect":
            res = router.route_tool_call("read", {"path": "README.md"})
            print(f"   Tool result: {res}")
        elif step.name == "patch":
            res = router.route_tool_call("exec", {"command": "echo 'patch applied'"})
            print(f"   Tool result: {res} (Notice pending_approval for exec)")
            
        state.add_turn(f"System: Completed {step.name}")

    # 4. Save Session and Deactivate
    session_mgr.save(state)
    print(f"\n[Session Persistence]")
    print(f"Saved session state to: {session_mgr.data_dir}/{state.id}.json")
    
    runtime.deactivate()

if __name__ == "__main__":
    main()
