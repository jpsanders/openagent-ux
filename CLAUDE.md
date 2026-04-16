# openagent-ux - AI Agent Instructions

## Overview

openagent-ux is an AI-powered website builder that uses pre-built templates and OpenAgents multi-agent collaboration.

## CRITICAL: Start with /start

**Before any build, ALWAYS initialize project:**

1. Check `.openagent-ux.json` exists
2. If NOT → Run `/start` FIRST
3. Then → Build with configuration

## Available Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/start` | Initialize project | FIRST - before any build |
| `/build [framework] [template]` | Build with template | After /start |
| `/deploy` | Deploy project | After build |
| `/agent [role]` | Delegate to agent | Anytime |

## Templates Library

Located in `templates/`:

```
templates/
├── astro/           # 8 templates
├── nextjs/          # 7 templates
├── gatsby/          # 8 templates
├── nuxt/            # 6 templates
├── hugo/            # 3 templates
├── svelte/          # 4 templates
└── html/            # (static)
```

## Agent System

Uses OpenAgents local network:

```
Principal Architect (always-on)
├── Design Lead
├── Frontend Lead
├── Backend Lead
└── QA Lead
```

Run with: `agn up`

## Knowledge Graph

Use graphify skill for agent memory:
- Build knowledge graph from requirements
- Store in `workspace/memory/{project}-graph.json`
- Query for relevant context on agent handoff

## Example Workflow

```
User: /start
Agent: Questionnaire → Creates .openagent-ux.json

User: /build astro astrowind
Agent: Copies template, installs deps

User: /agent design
Agent: Delegates to Design Lead

User: /deploy
Agent: Deploys to Vercel/Netlify
```