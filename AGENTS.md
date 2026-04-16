# openagent-ux - Multi-Agent Website Builder

## Overview

openagent-ux uses **OpenAgents** (openagents.org) as the multi-agent framework to build websites from pre-built templates.

## Architecture

```
OpenAgents Workspace (workspace.openagents.org)
    │
    ├── Principal Architect (always-on daemon)
    │   └── Delegates to domain leads via agn
    │
    ├── Design Lead
    ├── Frontend Lead
    ├── Backend Lead
    └── QA Lead
```

## Getting Started

### 1. Install OpenAgents

```bash
curl -fsSL https://openagents.org/install.sh | bash
```

### 2. Start the daemon

```bash
agn up
```

### 3. Initialize a project

```bash
# In the agent, type:
/start
```

### 4. Build with a template

```bash
# After initialization:
/build astro astrowind
```

### 5. Deploy

```bash
/deploy
```

## Agent System

The system uses OpenAgents local network:

- **Principal Architect** - Always-on, manages project strategy
- **Design Lead** - Brand identity, design system
- **Frontend Lead** - UI components, pages
- **Backend Lead** - API, database
- **QA Lead** - Testing, accessibility

Communication via OpenAgents messaging mod.

## Templates

50+ templates available in `templates/`:

| Framework | Count | Templates |
|-----------|-------|-----------|
| astro | 8 | astrowind, astroship, etc. |
| nextjs | 7 | nextjs-dashboard, etc. |
| gatsby | 8 | gatsby-starter-blog, etc. |
| nuxt | 6 | nuxt-starter, etc. |
| hugo | 3 | hugo-ananke, etc. |
| svelte | 4 | sveltekit-blog, etc. |

## Knowledge Graph

Use **graphify** skill for agent memory:
- Build knowledge graph from requirements
- Store in `workspace/memory/{project}-graph.json`
- Query for context on agent handoff

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Initialize new project |
| `/build [framework] [template]` | Build with template |
| `/deploy` | Deploy project |
| `/agent [role]` | Delegate to agent |

## Project Structure

```
openagent-ux/
├── .agents/              # OpenAgents config & skills
│   ├── main.manifest
│   ├── skills/
│   │   ├── start/       # /start command
│   │   ├── build/       # /build command
│   │   ├── deploy/      # /deploy command
│   │   └── agent/       # /agent command
│   └── subagents/       # Agent manifests
├── templates/           # Template library (downloaded)
├── scripts/             # Utility scripts
└── tests/               # Test files
```