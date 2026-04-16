# OpenAgent UX - Agent System Documentation

## Overview

This project uses a **hierarchical multi-agent system** where AI agents work together to build websites. The system is designed for autonomous operation with agent-to-agent task delegation.

## Agent Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                    PRINCIPAL ARCHITECT                       │
│         (Tier 1) - Strategic decisions, ownership            │
│                  Port 3000 - Always running                    │
├─────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Design Lead  │  │Frontend Lead│  │ Backend Lead│         │
│  │   (Tier 2)   │  │   (Tier 2)   │  │   (Tier 2)   │         │
│  │   Port 3001  │  │   Port 3002  │  │   Port 3003  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐                            │
│  │   QA Lead    │  │  Specialists│  ← Spawned on-demand      │
│  │   (Tier 2)   │  │   (Tier 3)  │                            │
│  │   Port 3004  │  │   Ports +   │                            │
│  └──────────────┘  └──────────────┘                            │
│                                                                 │
└─────────────────────────────────────────────────────────────┘
```

## Agent Roles

### Tier 1: Principal Architect
- **Role**: `principal-architect`
- **Port**: 3000
- **Always On**: Yes
- **Responsibilities**:
  - Analyze incoming requests
  - Create execution plans
  - Delegate to domain leads
  - Aggregate results
  - Final quality check

### Tier 2: Domain Leads
| Agent | Role | Domain | Port |
|-------|------|--------|------|
| Design Lead | `design-lead` | Design system, brand identity | 3001 |
| Frontend Lead | `frontend-lead` | UI components, pages | 3002 |
| Backend Lead | `backend-lead` | API, database, server | 3003 |
| QA Lead | `qa-lead` | Testing, review, accessibility | 3004 |

### Tier 3: Specialists
Spawned on-demand by leads for specific tasks:
- Brand specialist
- Token specialist
- Component specialist
- Page specialist
- API specialist
- Test specialist
- A11y specialist

## Pipelines

Predefined workflows that coordinate multiple agents:

### Build Pipeline

```bash
/build landing    # Build a landing page
/build fullstack  # Build fullstack application
/build component  # Build a single component
```

### Test Pipeline

```bash
/test             # Run all tests
/test unit        # Run unit tests only
/test e2e         # Run E2E tests only
```

### Review Pipeline

```bash
/review           # Code review
/audit            # Full quality audit
```

## Communication

### Message Protocol

Agents communicate via the **Workspace Server**:

```python
# Example: Principal delegates to Design Lead
messenger.send_message(
    to_agent="design-lead",
    from_agent="principal",
    action="create-brand",
    payload={"industry": "fintech", "mood": "professional"}
)
```

### Message Types
- **REQUEST**: Task delegation
- **RESPONSE**: Result of task
- **EVENT**: Broadcast (e.g., task complete)
- **ERROR**: Failure notification

## Files Structure

```
agents/
├── config/
│   ├── hierarchy.yaml    # Agent tier definitions
│   ├── roles.yaml       # Role configurations
│   └── pipelines.yaml   # Workflow definitions
│
├── roles/
│   ├── principal-architect.yaml
│   ├── design-lead.yaml
│   ├── frontend-lead.yaml
│   ├── backend-lead.yaml
│   └── qa-lead.yaml
│
├── pipelines/
│   └── (defined in config/pipelines.yaml)
│
├── scripts/
│   ├── orchestrator.py  # Agent lifecycle management
│   ├── messenger.py     # Inter-agent communication
│   ├── runner.py        # Pipeline executor
│   └── requirements.txt
│
└── docker/
    ├── agent.Dockerfile
    ├── orchestrator.Dockerfile
    └── docker-compose.yml

workspace/
├── threads/       # Agent conversation history
├── files/        # Shared project files
├── state/        # Project state JSON
└── logs/         # Execution logs
```

## Running the System

### Quick Start (Development)

```bash
# 1. Install dependencies
pip install -r agents/scripts/requirements.txt

# 2. Start the orchestrator
python agents/scripts/orchestrator.py
```

### Docker Deployment

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

### Manual Agent Startup

```bash
# Start Principal Architect (always on)
python -m opencode --role principal-architect --port 3000

# Start a Lead (on-demand)
python -m opencode --role design-lead --port 3001
```

## Available Commands

Once the system is running:

| Command | Pipeline | Description |
|---------|----------|-------------|
| `/build landing` | build-landing | Create landing page |
| `/build fullstack` | build-fullstack | Create fullstack app |
| `/build component` | build-component | Create single component |
| `/test` | run-tests | Run all tests |
| `/test unit` | run-tests | Unit tests only |
| `/review` | review-refactor | Code review |
| `/deploy` | deploy | Build and deploy |

## Design System Integration

The agent system uses the pick-and-mix design system:

### Design Personalities
- **Swiss**: High contrast, precise, functional
- **Editorial**: Sophisticated, timeless
- **Tech Noir**: Dark, technical
- **Playful**: Friendly, bouncy
- **Minimal**: Essential, reductionist
- **Contemporary**: Bold, expressive

### Usage
1. Agent receives request
2. Principal delegates to Design Lead
3. Design Lead creates brand identity
4. Frontend Lead builds with design tokens
5. QA Lead validates
6. Principal returns complete result

## Configuration

### Hierarchy (`agents/config/hierarchy.yaml`)
- Agent tiers definition
- Port assignments
- Spawning strategy
- Autonomy settings

### Roles (`agents/config/roles.yaml`)
- Responsibilities per role
- Skills available
- Trigger patterns

### Pipelines (`agents/config/pipelines.yaml`)
- Step definitions
- Dependencies
- Parallel execution
- Expected outputs

## Troubleshooting

### Agent not responding
```bash
# Check if agent is running
curl http://localhost:PORT/health

# View agent logs
docker logs openagent-{agent-name}
```

### Pipeline stuck
```bash
# View pipeline state
cat workspace/state/project.json

# Restart orchestrator
docker-compose restart orchestrator
```

### Communication issues
```bash
# Check workspace server
curl http://localhost:8000/health

# View message threads
ls workspace/threads/
```

## Extending the System

### Add a new Agent Role
1. Create `agents/roles/{role-name}.yaml`
2. Add to `agents/config/hierarchy.yaml`
3. Add triggers to `agents/config/roles.yaml`

### Add a new Pipeline
1. Add to `agents/config/pipelines.yaml`
2. Define steps with dependencies
3. Specify trigger commands

### Add a new Specialist
1. Define in lead's `specialists_can_spawn`
2. Create handler in agent code
3. Register in messenger handlers
