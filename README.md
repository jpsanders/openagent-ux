# openagent-ux

> AI-powered frontend builder that creates UNIQUE, premium websites - NOT generic AI slop.

The **pick n' mix** website builder powered by 50+ pre-built templates, 19 community component libraries, and a multi-agent system.

[![Stars](https://img.shields.io/github/stars/jpsanders/openagent-ux?style=flat&label=Stars)](https://github.com/jpsanders/openagent-ux/stargazers)
[![License](https://img.shields.io/github/license/jpsanders/openagent-ux?style=flat)](LICENSE)

---

## The Problem

Every AI-generated website looks the same:
- Inter font everywhere
- Blue buttons, purple gradients
- Generic components
- Like "AI made this" 😓

## The Solution - Pick n' Mix from Real Code

openagent-ux uses **50+ pre-built templates** and **19 component libraries** as the foundation. Instead of generating generic AI code, the AI assembles unique sites from real, quality components you can see and choose from.

```
git clone → npm install → /start → AI builds your site
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/jpsanders/openagent-ux.git
cd openagent-ux

# 2. Install dependencies
npm install

# 3. Run /start in your AI agent
# Agent runs interactive questionnaire, then builds your site

# Optional: Fetch templates first for offline use
npm run fetch:all
```

**What happens during `/start`:**

1. Agent asks interactive questions about: Architecture, Tech Stack, Design, Frontend, Backend
2. **Pick n' Mix** section - choose components from real templates
3. Configuration saved to `.openagent-ux.json`
4. **Principal Architect** orchestrates the build using your choices

---

## The Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PROJECT WORKFLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   git clone           npm install          /start (in agent)            │
│       │                    │                    │                       │
│       ▼                    ▼                    ▼                       │
│   [Clone Repo]    →   [Install Deps]   →   [Interactive Questionnaire] │
│                                                │                        │
│                                                ▼                        │
│                                    1. Architecture (project type)      │
│                                    2. Tech Stack (framework, etc)       │
│                                    3. Design (personality, colors)     │
│                                    4. Frontend (pages, components)     │
│                                    5. Backend (auth, DB, API)          │
│                                    6. Pick n' Mix (choose components)  │
│                                                │                        │
│                                                ▼                        │
│                                    Config saved to .openagent-ux.json  │
│                                                │                        │
│                                                ▼                        │
│                                    Principal Architect Orchestrates     │
│                                    ├─ Design Lead                      │
│                                    ├─ Frontend Lead                     │
│                                    ├─ Backend Lead                     │
│                                    └─ QA Lead                           │
│                                                │                        │
│                                                ▼                        │
│                                    Site Assembled from Pick n' Mix      │
│                                    Using Real Template Components      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Available Templates (33 Downloaded)

### Astro (9)
- astrowind - SaaS/marketing
- astroship - Startup
- astro-paper - Blog
- astrofy - Portfolio
- blogsmith-free - Blog
- astro-cactus - Blog/Docs
- flowbite-admin - Dashboard
- starlight-docs - Documentation
- astro-boilerplate - Boilerplate

### Gatsby (8)
- gatsby-starter-blog - Blog
- gatsby-portfolio-cara - Portfolio
- gatsby-minimal-blog - Blog
- gatsby-advanced-starter - Boilerplate
- gatsby-decap-cms - Blog/CMS
- gatsby-starter-shopify - E-commerce
- gatsby-gitbook-starter - Docs
- gatsby-starter-ghost - Blog

### Next.js (7)
- nextjs-blog-starter - Blog
- nextjs-commerce - E-commerce
- nextjs-dashboard - Dashboard
- nextjs-saas-starter - SaaS
- nextjs-docs - Documentation
- nextjs-portfolio - Portfolio
- nextjs-medusa - E-commerce

### Nuxt (6)
- nuxt-starter - Boilerplate
- nuxt-content-template - Blog/Docs
- nuxt-docus - Documentation
- nuxt-commerce - E-commerce
- nuxt-layered-architecture - Boilerplate
- nuxt-module-starter - Development

### Hugo (3)
- hugo-ananke - Blog/Marketing
- hugo-papermod - Blog
- hugo-universal - Business

---

## Community Components (16 Downloaded)

### UI Component Libraries
- **shadcn-ui** - Beautiful React components
- **radix-ui** - Unstyled accessible primitives
- **headless-ui** - Accessible UI components
- **ark-ui** - Headless UI for React
- **daisyui** - Tailwind CSS component library

### Design Systems
- **chakra-ui** - Component library
- **mantine** - React components
- **primereact** - UI Component Library
- **ant-design** - Enterprise UI

### Animation Libraries
- **framer-motion** - Animation library
- **react-spring** - Spring-based animation
- **motion-one** - Lightweight animation

### Icons
- **heroicons** - SVG icons
- **lucide-react** - Beautiful icons
- **phosphor-icons** - Phosphor Icons
- **remix-icon** - Open source icons

---

## Component Registry

After running `npm run extract:components`, a registry is generated at `components-registry.json`:

- **14,000+** components extracted
- **200+** pages
- **4,400+** page sections
- Organized by type: button, navbar, hero, card, form, modal, etc.

```json
{
  "components": {
    "button": [{"name": "Button", "template": "astrowind", "path": "..."}],
    "navbar": [{"name": "Navbar", "template": "starlight", "path": "..."}],
    ...
  },
  "pages": {
    "home": [{"name": "index", "template": "nextjs-dashboard", "path": "..."}],
    ...
  }
}
```

---

## 6 Design Personalities

Choose your brand's personality - determines fonts, colors, AND animations:

| Personality | Font Pairing | Colors | Animation Feel | Best For |
|-------------|---------------|--------|----------------|----------|
| **Swiss** | Geist + Fraunces | Black + Orange | Reserved, precise | Fintech, enterprise |
| **Editorial** | Playfair + Source | Cream + Terracotta | Refined, gentle | Publishing, luxury |
| **Tech Noir** | Geist + Geist Mono | Dark + Cyan | Snappy, functional | Dev tools, Web3 |
| **Playful** | Outfit + Nunito | Coral + Mint | Bouncy, expressive | Consumer apps |
| **Minimal** | Satoshi + General | Off-white + Black | Subtle, essential | Agencies, portfolios |
| **Contemporary** | Syne + DM Sans | Charcoal + Pink | Dynamic, bold | Creative agencies |

---

## NPM Scripts

| Script | Description |
|--------|-------------|
| `npm run fetch:templates` | Download all templates |
| `npm run fetch:components` | Download community components |
| `npm run fetch:all` | Download everything |
| `npm run extract:components` | Generate component registry |
| `npm run dev` | Start Next.js dev server |
| `npm run test` | Run tests |

---

## Agent Commands

| Command | Description |
|---------|-------------|
| `/start` | **FIRST** - Initialize project with interactive questionnaire |
| `/brand` | Set design personality (after /start) |
| `/build` | Build component/page/landing |
| `/polish` | Final quality pass |
| `/test` | Run tests (unit/e2e/visual/a11y) |

---

## Multi-Agent System

openagent-ux uses a hierarchical multi-agent system:

```
┌─────────────────────────────────────────────────────────────┐
│                    PRINCIPAL ARCHITECT                       │
│         (Tier 1) - Strategic decisions, ownership            │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Design Lead  │  │Frontend Lead│  │ Backend Lead│      │
│  │   (Tier 2)   │  │   (Tier 2)   │  │   (Tier 2)   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │   QA Lead    │  │  Specialists│                          │
│  │   (Tier 2)   │  │   (Tier 3)  │                          │
│  └──────────────┘  └──────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

The Principal Architect receives the questionnaire config and orchestrates all agents.

---

## Directory Structure

```
openagent-ux/
├── .agents/                    # AI agent skills
│   ├── skills/
│   │   ├── brand/             # Design personality selection
│   │   ├── build/             # Build commands
│   │   ├── anti-slop/         # Block generic AI output
│   │   └── ...
│   └── subagents/             # Specialized subagents
│
├── templates/                  # 33 downloaded templates
│   ├── astro/                 # Astro templates
│   ├── gatsby/               # Gatsby templates
│   ├── nextjs/               # Next.js templates
│   ├── nuxt/                 # Nuxt templates
│   ├── hugo/                 # Hugo templates
│   └── registry/             # Template catalog
│
├── components/                # 16 community component libs
│   └── community/            # shadcn-ui, radix-ui, etc.
│
├── design-systems/            # 6 personality CSS token sets
│   ├── swiss/
│   ├── editorial/
│   ├── tech-noir/
│   ├── playful/
│   ├── minimal/
│   └── contemporary/
│
├── layouts/                   # Page layout templates
│   ├── landing/
│   ├── dashboard/
│   └── blog/
│
├── scripts/
│   ├── fetch_all_templates.py # Download templates
│   └── extract_components.py # Generate component registry
│
├── agents/                   # Multi-agent system config
│   ├── config/               # hierarchy, roles, pipelines
│   ├── roles/                # Agent role definitions
│   └── scripts/              # Python orchestration scripts
│
└── .agents/skills/init/      # /start command skill
└── components-registry.json  # Generated component database
```

---

## Environment Variables

Create a `.env` file:

```env
# AI Agent configuration
OPENCODE_AGENT=opencode        # Default agent (can override to 'claude')
OPENCODE_MODE=interactive      # or 'autonomous'

# Database (if using)
DATABASE_URL=postgresql://...

# Auth (if using)
AUTH_SECRET=your-secret-key
```

---

## Tech Stack

- **Next.js 14** (App Router)
- **React 18**
- **Tailwind CSS**
- **Framer Motion**
- **Python 3** (for template fetching/extraction)
- **Vitest** (unit testing)
- **Playwright** (E2E testing)

---

## Star This Repo If...

- ✅ You want **unique** websites, NOT generic AI output
- ✅ You want **premium** design, NOT Bootstrap defaults
- ✅ You want **pick n' mix** workflow from real templates
- ✅ You're tired of Inter + blue-500
- ✅ You want production-ready testing

---

## Roadmap

- [x] 33+ templates downloaded
- [x] 16 community components imported
- [x] Component extraction + registry
- [x] Init questionnaire + AI agent workflow
- [ ] Remaining templates (fetch on demand)
- [ ] More design personalities
- [ ] Figma import
- [ ] Visual editor

---

## License

MIT License - Use it for anything.