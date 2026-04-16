#!/usr/bin/env python3
"""
OpenAgent UX - Agent Orchestrator
Manages the agent lifecycle: spawning, monitoring, and terminating agents.
"""

import asyncio
import json
import os
import signal
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

import yaml


class AgentState(Enum):
    STARTING = "starting"
    RUNNING = "running"
    IDLE = "idle"
    BUSY = "busy"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


@dataclass
class Agent:
    name: str
    role: str
    tier: int
    port: int
    process: subprocess.Popen = None
    state: AgentState = AgentState.STOPPED
    last_active: datetime = field(default_factory=datetime.now)
    spawn_time: datetime = None
    memory: dict = field(default_factory=dict)


class Orchestrator:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)
        self.agents: dict[str, Agent] = {}
        self.workspace_path = Path("workspace")
        self.state_file = self.workspace_path / "state" / "project.json"
        
    def load_config(self, path: str) -> dict:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_agent_config(self, agent_name: str) -> dict:
        for tier in self.config.get('hierarchy', {}).get('tiers', []):
            if tier['name'] == agent_name:
                return tier
        return None
    
    def spawn_agent(self, agent_name: str, command: list = None) -> Agent:
        """Spawn a new agent process."""
        config = self.get_agent_config(agent_name)
        if not config:
            raise ValueError(f"Unknown agent: {agent_name}")
        
        # Build command - starts the agent with appropriate config
        if command is None:
            command = [
                sys.executable, "-m", "opencode",
                "--role", config['role'],
                "--port", str(config['port']),
                "--project", "."
            ]
        
        print(f"[Orchestrator] Spawning {agent_name} (port {config['port']})...")
        
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, "OPENCODE_ROLE": config['role']}
        )
        
        agent = Agent(
            name=agent_name,
            role=config['role'],
            tier=config['tier'],
            port=config['port'],
            process=process,
            state=AgentState.STARTING,
            spawn_time=datetime.now()
        )
        
        self.agents[agent_name] = agent
        return agent
    
    def spawn_principal(self) -> Agent:
        """Spawn the Principal Architect (always-on)."""
        return self.spawn_agent("principal")
    
    def spawn_on_demand(self, agent_name: str) -> Agent:
        """Spawn an agent when needed."""
        return self.spawn_agent(agent_name)
    
    def terminate_agent(self, agent_name: str) -> bool:
        """Terminate an agent process."""
        if agent_name not in self.agents:
            return False
            
        agent = self.agents[agent_name]
        if agent.process:
            agent.process.terminate()
            try:
                agent.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                agent.process.kill()
        
        agent.state = AgentState.STOPPED
        print(f"[Orchestrator] Terminated {agent_name}")
        return True
    
    def check_agent_health(self, agent_name: str) -> AgentState:
        """Check if an agent is still running and healthy."""
        if agent_name not in self.agents:
            return AgentState.STOPPED
            
        agent = self.agents[agent_name]
        
        if agent.process is None:
            return AgentState.STOPPED
            
        # Check if process is still running
        if agent.process.poll() is not None:
            agent.state = AgentState.FAILED
            return AgentState.FAILED
        
        # Check idle timeout
        config = self.get_agent_config(agent_name)
        idle_timeout = config.get('sleep_timeout_minutes', 30) * 60 if config else 1800
        
        time_since_active = (datetime.now() - agent.last_active).total_seconds()
        
        if agent.state == AgentState.BUSY:
            return AgentState.BUSY
        elif time_since_active > idle_timeout:
            return AgentState.IDLE
            
        return AgentState.RUNNING
    
    def cleanup_idle_agents(self):
        """Terminate idle agents beyond timeout."""
        for name, agent in self.agents.items():
            config = self.get_agent_config(name)
            if not config:
                continue
                
            idle_timeout = config.get('idle_terminate_minutes', 15) * 60
            time_since_active = (datetime.now() - agent.last_active).total_seconds()
            
            # Don't terminate principal or leads with always_on
            if config.get('always_on', False):
                continue
                
            if time_since_active > idle_timeout and agent.state != AgentState.BUSY:
                print(f"[Orchestrator] Terminating idle agent: {name}")
                self.terminate_agent(name)
    
    def get_agent(self, agent_name: str) -> Agent:
        """Get an agent, spawning if needed."""
        if agent_name not in self.agents:
            return self.spawn_on_demand(agent_name)
        
        health = self.check_agent_health(agent_name)
        if health == AgentState.STOPPED or health == AgentState.FAILED:
            return self.spawn_on_demand(agent_name)
            
        return self.agents[agent_name]
    
    def update_state(self, key: str, value: Any):
        """Update project state."""
        state = self.load_state()
        state[key] = value
        state['last_updated'] = datetime.now().isoformat()
        self.save_state(state)
    
    def load_state(self) -> dict:
        """Load project state."""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {"agents": {}, "tasks": {}}
    
    def save_state(self, state: dict):
        """Save project state."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def run(self):
        """Run the orchestrator loop."""
        print("[Orchestrator] Starting...")
        
        # Spawn principal architect (always on)
        self.spawn_principal()
        
        print("[Orchestrator] Principal Architect running on port 3000")
        print("[Orchestrator] Agent system ready!")
        print("\nAvailable commands:")
        print("  /build landing    - Build a landing page")
        print("  /build fullstack  - Build a fullstack app")
        print("  /test             - Run tests")
        print("  /review            - Review code")
        print("\nPress Ctrl+C to stop all agents")
        
        try:
            while True:
                time.sleep(10)
                self.cleanup_idle_agents()
        except KeyboardInterrupt:
            print("\n[Orchestrator] Shutting down...")
            for name in list(self.agents.keys()):
                self.terminate_agent(name)


def main():
    config_path = "agents/config/hierarchy.yaml"
    if not os.path.exists(config_path):
        print(f"Error: Config file not found: {config_path}")
        sys.exit(1)
    
    orchestrator = Orchestrator(config_path)
    orchestrator.run()


if __name__ == "__main__":
    main()
