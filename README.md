# openagent-ux

> AI-powered frontend builder that creates UNIQUE, premium websites - NOT generic AI slop.

[![Stars](https://img.shields.io/github/stars/jpsanders/openagent-ux?style=flat&label=Stars)](https://github.com/jpsanders/openagent-ux/stargazers)
[![Forks](https://img.shields.io/github/forks/jpsanders/openagent-ux?style=flat&label=Forks)](https://github.com/jpsanders/openagent-ux/network)
[![License](https://img.shields.io/github/license/jpsanders/openagent-ux?style=flat)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/jpsanders/openagent-ux/main?style=flat)](https://github.com/jpsanders/openagent-ux/commits/main)

Built with: **Next.js 14** | **React 19** | **Framer Motion** | **Claude Code**

---

## The Problem

Every AI-generated website looks the same:

- Inter font everywhere
- Blue buttons, purple gradients
- Generic components
- Like "AI made this" 😓

## The Solution - Brand First

openagent-ux forces intentional brand identity BEFORE any code:

```
/brand     → Choose your personality (Swiss, Editorial, Tech Noir, Playful, Minimal, Contemporary)
/build     → Build with your unique fonts, colors, motion
/polish    → Fine-tune every detail
/test      → Verify with unit, E2E, accessibility tests
/preview   → Ship with performance confidence
```

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/jpsanders/openagent-ux.git
cd openagent-ux

# Install dependencies
npm install

# Copy skills to Claude Code (for local use)
mkdir -p ~/.claude/agents
cp -r .agents/* ~/.claude/agents/

# Start the demo
cd example-app
npm run dev
```

**Then in your AI agent:**

```
/brand     → First! Choose one of 6 personalities
/build landing my-site
/polish
/test all
/preview
```

---

## 6 Design Personalities

Choose your brand's personality - this determines fonts, colors, AND animations:

| Personality | Font Pairing | Colors | Animation Feel | Best For |
|--------------|--------------|--------|----------------|----------|
| **Swiss** | Geist + Fraunces | Black + Orange | Reserved, precise | Fintech, enterprise |
| **Editorial** | Playfair + Source | Cream + Terracotta | Refined, gentle | Publishing, luxury |
| **Tech Noir** | Geist + Geist Mono | Dark + Cyan | Snappy, functional | Dev tools, Web3 |
| **Playful** | Outfit + Nunito | Coral + Mint | Bouncy, expressive | Consumer apps, games |
| **Minimal** | Satoshi + General | Off-white + Black | Subtle, essential | Agencies, portfolios |
| **Contemporary** | Syne + DM Sans | Charcoal + Pink | Dynamic, bold | Creative agencies |

---

## Anti-Slop System (Always Active)

These guardrails BLOCK generic AI output automatically:

```
❌ Inter font as primary          → BLOCKED - Must use distinctive pairing
❌ blue-500 as primary color    → BLOCKED - Must use curated palette
❌ purple-to-pink gradient     → BLOCKED - Must use brand colors
❌ Generic empty states        → BLOCKED - Must create distinctive
❌ No micro-interactions       → BLOCKED - Must add personality
```

**Result**: Every website built through this system feels UNIQUE - NOT generic AI output.

---

## Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/brand` | Establish unique brand identity (FIRST!) | `/brand` then choose personality |
| `/build` | Build component/page/landing | `/build landing my-site` |
| `/polish` | Final quality pass | `/polish` |
| `/test` | Run tests (unit/e2e/visual/a11y) | `/test all` |
| `/preview` | Dev server with audit | `/preview` |

---

## Demo Features

The included demo showcases ALL 6 personalities:

- **Landing page** with live personality switcher
- **6 complete design systems** (fonts + colors + animations)
- **Premium components**: Button, Card, Navigation with all states
- **Smooth Framer Motion animations** matched to personality
- **Responsive** on all devices
- **Dark/light mode** support

Run the demo:
```bash
cd example-app
npm run dev
```

---

## Installation

### Option 1: Git clone + copy to Claude Code
```bash
git clone https://github.com/jpsanders/openagent-ux.git
cp -r .agents/* ~/.claude/agents/
```

### Option 2: Claude Code plugin (coming soon)
```bash
/plugin marketplace add https://github.com/jpsanders/openagent-ux
/plugin install openagent-ux@latest
```

---

## Tech Stack

- Next.js 14 (App Router)
- React 19
- Tailwind CSS (semantic design tokens)
- Framer Motion (spring physics)
- Vitest (unit testing)
- Playwright (E2E testing)
- Claude Code (agent orchestration)

---

## What's Inside

```
openagent-ux/
├── .agents/              # Skills & subagents (copy to ~/.claude/)
│   ├── skills/
│   │   ├── premium-brand/     # /brand command - FIRST STEP
│   │   ├── anti-slop/         # Blocks generic output
│   │   ├── premium-typography/# 12 distinctive fonts
│   │   ├── premium-palettes/  # 10 curated color palettes
│   │   ├── motion-personality/# Animation → brand matching
│   │   ├── premium-build/    # /build command
│   │   ├── premium-test/     # /test command
│   │   ├── premium-preview/  # /preview command
│   │   └── polish/           # /polish command
│   └── subagents/            # Specialized agents
│       ├── design.manifest
│       ├── ui-architect.manifest
│       └── ...
├── example-app/          # Demo landing with switcher
│   ├── app/
│   ├── components/
│   └── lib/
└── config/               # Generated brand identity
    └── brand-identity.json
```

---

## Star This Repo If...

- ✅ You want **unique** websites, NOT generic AI output
- ✅ You want **premium** design, NOT Bootstrap defaults  
- ✅ You want **brand-first** workflow, NOT build-first
- ✅ You're tired of Inter + blue-500
- ✅ You want production-ready testing (Vitest + Playwright)

---

## Roadmap

- [ ] Claude Code plugin marketplace submission
- [ ] VS Code extension
- [ ] More component templates
- [ ] AI-powered content generation
- [ ] Figma import

---

## Contributing

Contributions welcome! Feel free to open issues and PRs.

---

## License

MIT License - Use it for anything.

---

<a href="https://github.com/jpsanders/openagent-ux">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="24" height="24" alt="GitHub">
</a>