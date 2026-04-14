# openagent-ux - AI Agent Instructions

## Overview

openagent-ux is an AI-powered frontend builder that creates UNIQUE, premium websites through a brand-first workflow. The key difference: it BLOCKS generic AI output through anti-slop guardrails while enforcing intentional design personality choices.

## CRITICAL: Brand-First Workflow

**Before any /build, you MUST establish brand identity:**

1. Check if `config/brand-identity.json` exists
2. If NOT → Run `/brand` FIRST to create it
3. Then → Use brand values in all /build commands

This ensures every website is unique, NOT generic AI output.

## Available Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/brand` | Establish unique brand identity | FIRST - before any build |
| `/build` | Build component/page/landing | After brand established |
| `/polish` | Final quality pass | Before shipping |
| `/test` | Run test suite | After build |
| `/preview` | Performance audit | Before shipping |

## Design Personalities (6 Options)

Choose one via `/brand`:

| Personality | Fonts | Colors | Animation |
|--------------|-------|--------|------------|
| Swiss | Geist + Fraunces | Black + Orange | Reserved |
| Editorial | Playfair + Source | Cream + Terracotta | Refined |
| Tech Noir | Geist + Geist Mono | Dark + Cyan | Snappy |
| Playful | Outfit + Nunito | Coral + Mint | Bouncy |
| Minimal | Satoshi + General | Off-white + Black | Subtle |
| Contemporary | Syne + DM Sans | Charcoal + Pink | Dynamic |

## Anti-Slop Rules (ALWAYS ACTIVE)

These are BLOCKED automatically:

- ❌ Inter font as primary (use distinctive pairing)
- ❌ blue-500 as primary color (use curated palette)
- ❌ purple-to-pink gradient (use solid brand colors)
- ❌ Generic empty states (must be distinctive)
- ❌ No micro-interactions (must add personality)

## Skills Structure

```
.agents/
├── skills/
│   ├── premium-brand/      # /brand command
│   ├── anti-slop/           # Blocks generic output
│   ├── premium-typography/ # 12 font pairings
│   ├── premium-palettes/   # 10 color palettes
│   ├── motion-personality/ # Animation matching
│   ├── premium-build/      # /build command
│   ├── premium-test/       # /test command
│   ├── premium-preview/     # /preview command
│   └── polish/              # /polish command
└── subagents/
    ├── design.manifest
    ├── ui-architect.manifest
    └── ...
```

## Example Workflow

```
User: Build my website

Agent: → Check config/brand-identity.json
       If NOT exists → RUN /brand
       → Ask user to choose personality
       → Create config/brand-identity.json
       
       → RUN /build landing my-site
       → Uses brand fonts/colors/motion
       
       → RUN /polish
       → RUN /test unit
       → RUN /preview
```

## Quality Gates

Before completing any build:
- [ ] Brand identity established (not default)
- [ ] Fonts: NOT Inter as primary
- [ ] Colors: NOT blue-500/purple gradient
- [ ] All interactive states (hover, focus, active)
- [ ] Micro-interactions added
- [ ] /polish passes

## Testing

```bash
# Run unit tests
npm run test

# Run E2E tests  
npm run test:e2e

# Run with coverage
npm run test:coverage
```

## Demo App

The `example-app/` folder contains a demo showcasing all 6 personalities with a personality switcher. Run with:

```bash
cd example-app
npm run dev
```

## Notes for AI Agents

1. Always run /brand FIRST for new projects
2. Never use Inter as primary font
3. Never use blue-500 as primary color
4. Always add micro-interactions
5. Match animation to brand personality
6. Run /polish before shipping
7. Run /preview to check performance