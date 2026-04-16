#!/usr/bin/env python3
"""
OpenAgent UX - Pipeline Runner
Executes predefined workflows by coordinating agents.
"""

import asyncio
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

import yaml


class StepStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    WAITING = "waiting"


@dataclass
class PipelineStep:
    id: str
    name: str
    agent: str
    action: str
    depends_on: list[str] = field(default_factory=list)
    parallel: bool = False
    conditional: str = ""
    input: str = ""
    output: str = ""
    status: StepStatus = StepStatus.PENDING
    result: dict = field(default_factory=dict)
    error: str = ""


@dataclass
class Pipeline:
    name: str
    description: str
    triggers: list[str]
    steps: list[PipelineStep] = field(default_factory=list)
    status: str = "pending"
    start_time: datetime = None
    end_time: datetime = None


class PipelineRunner:
    def __init__(self, config_path: str = "agents/config/pipelines.yaml"):
        self.config_path = config_path
        self.pipelines: dict[str, Pipeline] = {}
        self.load_pipelines()
        
    def load_pipelines(self):
        """Load pipeline definitions from YAML."""
        if not os.path.exists(self.config_path):
            print(f"[Runner] Warning: Config not found: {self.config_path}")
            return
            
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        for pipe_name, pipe_data in config.get('pipelines', {}).items():
            steps = []
            for step_data in pipe_data.get('steps', []):
                step = PipelineStep(
                    id=step_data['id'],
                    name=step_data['name'],
                    agent=step_data['agent'],
                    action=step_data['action'],
                    depends_on=step_data.get('depends_on', []),
                    parallel=step_data.get('parallel', False),
                    conditional=step_data.get('conditional', ''),
                    input=step_data.get('input', ''),
                    output=step_data.get('output', '')
                )
                steps.append(step)
            
            pipeline = Pipeline(
                name=pipe_data.get('name', pipe_name),
                description=pipe_data.get('description', ''),
                triggers=pipe_data.get('triggers', []),
                steps=steps
            )
            self.pipelines[pipe_name] = pipeline
    
    def find_pipeline(self, trigger: str) -> Pipeline:
        """Find a pipeline that matches the trigger."""
        for pipe in self.pipelines.values():
            if trigger in pipe.triggers:
                return pipe
        return None
    
    def get_ready_steps(self, pipeline: Pipeline) -> list[PipelineStep]:
        """Get steps that are ready to run (dependencies met)."""
        ready = []
        for step in pipeline.steps:
            if step.status != StepStatus.PENDING:
                continue
                
            # Check dependencies
            all_complete = True
            for dep_id in step.depends_on:
                dep_step = next((s for s in pipeline.steps if s.id == dep_id), None)
                if not dep_step or dep_step.status != StepStatus.COMPLETED:
                    all_complete = False
                    break
                    
            if all_complete:
                ready.append(step)
                
        return ready
    
    def get_parallel_batches(self, steps: list[PipelineStep]) -> list[list[PipelineStep]]:
        """Group steps that can run in parallel."""
        # Steps marked parallel: true can run together if they're ready
        parallel_steps = [s for s in steps if s.parallel]
        sequential_steps = [s for s in steps if not s.parallel]
        
        batches = []
        if parallel_steps:
            batches.append(parallel_steps)
        for step in sequential_steps:
            batches.append([step])
            
        return batches
    
    async def execute_step(self, step: PipelineStep, context: dict) -> dict:
        """Execute a single pipeline step."""
        print(f"[Runner] Executing step: {step.name} ({step.agent} → {step.action})")
        
        step.status = StepStatus.RUNNING
        
        # In a real implementation, this would:
        # 1. Send message to the agent via messenger
        # 2. Wait for response
        # 3. Parse result
        # For now, we simulate:
        result = await self._simulate_agent_call(step.agent, step.action, context)
        
        step.result = result
        step.status = StepStatus.COMPLETED
        
        return result
    
    async def _simulate_agent_call(self, agent: str, action: str, context: dict) -> dict:
        """Simulate calling an agent. In real impl, this uses messenger."""
        # This would integrate with the actual agent system
        await asyncio.sleep(0.1)  # Simulate work
        
        return {
            "status": "success",
            "agent": agent,
            "action": action,
            "output": f"Result from {agent} performing {action}"
        }
    
    async def run_pipeline(self, pipeline_name: str, initial_context: dict = None) -> dict:
        """Run a pipeline by name."""
        pipeline = self.pipelines.get(pipeline_name)
        if not pipeline:
            return {"error": f"Pipeline not found: {pipeline_name}"}
        
        print(f"[Runner] Starting pipeline: {pipeline.name}")
        
        pipeline.status = "running"
        pipeline.start_time = datetime.now()
        
        context = initial_context or {}
        max_iterations = 50  # Prevent infinite loops
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            # Get ready steps
            ready_steps = self.get_ready_steps(pipeline)
            
            if not ready_steps:
                # Check if we're done
                completed = sum(1 for s in pipeline.steps if s.status == StepStatus.COMPLETED)
                total = len(pipeline.steps)
                
                if completed == total:
                    break
                elif completed > 0:
                    # Stuck - some steps waiting on failed dependencies
                    for step in pipeline.steps:
                        if step.status == StepStatus.PENDING:
                            step.status = StepStatus.FAILED
                            step.error = "Dependencies failed"
                    break
                else:
                    # Nothing ready and nothing completed
                    break
            
            # Execute in batches (parallel when possible)
            batches = self.get_parallel_batches(ready_steps)
            
            for batch in batches:
                results = []
                for step in batch:
                    result = await self.execute_step(step, context)
                    results.append(result)
                    
                    # Aggregate results into context
                    if step.output:
                        context[step.output] = result
        
        pipeline.end_time = datetime.now()
        pipeline.status = "completed"
        
        duration = (pipeline.end_time - pipeline.start_time).total_seconds()
        print(f"[Runner] Pipeline complete in {duration:.2f}s")
        
        return {
            "pipeline": pipeline.name,
            "status": pipeline.status,
            "steps_completed": len([s for s in pipeline.steps if s.status == StepStatus.COMPLETED]),
            "steps_failed": len([s for s in pipeline.steps if s.status == StepStatus.FAILED]),
            "context": context
        }
    
    async def run_from_trigger(self, trigger: str, context: dict = None) -> dict:
        """Run pipeline matching a trigger."""
        pipeline = self.find_pipeline(trigger)
        if not pipeline:
            return {"error": f"No pipeline found for trigger: {trigger}"}
        
        return await self.run_pipeline(pipeline.name, context)


def main():
    """CLI for running pipelines."""
    import argparse
    
    parser = argparse.ArgumentParser(description="OpenAgent UX Pipeline Runner")
    parser.add_argument("trigger", help="Pipeline trigger (e.g., /build landing)")
    parser.add_argument("--context", "-c", help="JSON context data")
    
    args = parser.parse_args()
    
    context = {}
    if args.context:
        context = json.loads(args.context)
    
    runner = PipelineRunner()
    
    print(f"[Runner] Processing trigger: {args.trigger}")
    result = asyncio.run(runner.run_from_trigger(args.trigger, context))
    
    print(f"\n[Runner] Result:")
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result.get("status") == "completed" else 1)


if __name__ == "__main__":
    main()
