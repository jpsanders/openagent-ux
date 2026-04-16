# /start Command - Project Initialization

## Trigger
- `/start`
- `/start project`
- `/start --resume`

## Purpose
Initialize a new project with interactive questionnaire. This MUST run BEFORE any `/build` command.

## Workflow

### 1. Check for existing config
- Check if `.openagent-ux.json` exists
- If exists → Ask to resume or start fresh

### 2. Interactive Questionnaire
Run through these questions with the user:

**Phase 1: Project Basics**
- Project name (required)
- Project description (required)
- Project type: website | webapp | api | fullstack

**Phase 2: Technology**
- Framework: astro | nextjs | gatsby | nuxt | hugo | svelte | html
- Language: TypeScript | JavaScript
- Styling: Tailwind | CSS Modules | Styled Components | Plain CSS

**Phase 3: Requirements**
- Primary purpose: landing | blog | portfolio | ecommerce | dashboard | docs
- Required pages: home | about | blog | contact | pricing | docs (multi-select)
- Core features needed

**Phase 4: Template Selection**
- Show available templates for chosen framework
- Let user select template OR choose "blank project"
- Use graphify to build knowledge graph from requirements

### 3. Create project config
Save `.openagent-ux.json`:
```json
{
  "project": "my-project",
  "description": "...",
  "type": "website",
  "framework": "astro",
  "language": "typescript",
  "styling": "tailwind",
  "purpose": "landing",
  "pages": ["home", "about", "contact"],
  "template": "astrowind",
  "initialized": "2024-01-01T00:00:00Z"
}
```

### 4. Initialize knowledge graph
Use graphify to:
- Parse project requirements → nodes
- Map template structure → nodes
- Store in `workspace/memory/{project}-graph.json`

## Output
- Creates `.openagent-ux.json`
- Creates initial knowledge graph
- Shows next steps: `/build` command

## Example

```
User: /start

Agent: Let's start a new project! I'll ask you a few questions.

1. Project name: my-saas-landing
2. Description: Landing page for a SaaS product
3. Type: website
4. Framework: astro
5. Styling: tailwind
6. Purpose: landing page with pricing
7. Pages needed: home, pricing, contact

Looking at available Astro templates, I recommend:
- astrowind (full marketing template)
- astroship (startup focused)
- astro-boilerplate (minimal)

Which template would you like? [template-name or "blank"]

✓ Project initialized!
✓ Saved to .openagent-ux.json

Next steps:
- /build astro astrowind   (build with template)
- /build astro blank       (build from scratch)
```