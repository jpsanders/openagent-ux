# /agent Command - Delegate to Agent

## Trigger
- `/agent [role]`
- `/agent list`
- `/agent status`

## Purpose
Delegate tasks to specific agents in the OpenAgents network. Uses the hierarchical agent system.

## Agent Roles

| Role | Description | Tier |
|------|-------------|------|
| principal | Principal Architect - project owner | 1 |
| design | Design Lead - design system, brand | 2 |
| frontend | Frontend Lead - UI components, pages | 2 |
| backend | Backend Lead - API, database | 2 |
| qa | QA Lead - testing, accessibility | 2 |

## Workflow

### 1. Parse role
```
/agent design          # delegate to Design Lead
/agent frontend       # delegate to Frontend Lead
/agent qa             # delegate to QA Lead
/agent list           # show all available agents
/agent status         # show agent status
```

### 2. Check OpenAgents network
- Verify agn daemon is running
- Check workspace connection
- List available agents

### 3. Delegate task
- Send task to specified agent via OpenAgents messaging
- Include project context from:
  - `.openagent-ux.json`
  - `workspace/memory/{project}-graph.json`
- Wait for response

### 4. Aggregate results
- Collect agent output
- Update knowledge graph if needed
- Report back to user

## Agent Details

### Principal Architect (always-on)
- Role: `principal`
- Port: 3000
- Spawns: design, frontend, backend, qa
- Owns: project strategy, final decisions

### Design Lead
- Role: `design-lead`
- Domain: design
- Spawns: brand specialist, token specialist
- Tasks: brand identity, design system, UI patterns

### Frontend Lead
- Role: `frontend-lead`
- Domain: frontend
- Spawns: component specialist, page specialist
- Tasks: UI components, responsive layouts, pages

### Backend Lead
- Role: `backend-lead`
- Domain: backend
- Spawns: api specialist, db specialist
- Tasks: API endpoints, database, server logic

### QA Lead
- Role: `qa-lead`
- Domain: qa
- Spawns: test specialist, a11y specialist
- Tasks: testing, accessibility, code quality

## Example

```
User: /agent design

Agent: Delegating to Design Lead...

Design Lead: I'd like to understand your brand preferences:

1. Industry: What type of business? (SaaS, E-commerce, Portfolio, etc.)
2. Mood: How do you want to appear? (Professional, Creative, Minimal, etc.)
3. Colors: Any brand colors? (or generate from preferences)
4. Audience: Who is your target user?

[User answers questions]

Design Lead: Based on your inputs:
- Industry: SaaS
- Mood: Professional, modern
- Generated palette: Deep Blue (#1E3A5F), Accent Orange (#F97316)
- Font: Inter (default) → changed to Geist

✓ Brand identity saved to .openagent-ux.json
✓ Design system tokens generated
```

## Error Handling

| Error | Solution |
|-------|----------|
| "Agent not found" | Check if agent is running with `agn status` |
| "Network error" | Start agn daemon with `agn up` |
| "Role not recognized" | Use `/agent list` for valid roles |
| "Task failed" | Check agent logs, retry with more context |