# /start Command - Project Initialization

## Trigger
- `/start`
- `/start project`
- `/init project`
- `/new project`

## Description
Interactive questionnaire that guides users through project setup. Stores configuration and triggers the Principal Architect to orchestrate the build.

## Flow

### Step 1: Architecture
```
Agent: "What type of project are you building?"
Options: SaaS application, Marketing website, Blog/Content site, Portfolio, E-commerce store, Documentation site, Dashboard/Admin, Other"

Agent: "What is your project name?"

Agent: "Briefly describe your project:"
```
Record: projectType, projectName, description

### Step 2: Tech Stack
```
Agent: "Which framework do you want to use?"
Options: Astro, Next.js, Gatsby, Nuxt, Hugo, HTML (vanilla), React (Vite)"

Agent: "Preferred language?"
Options: TypeScript, JavaScript"

Agent: "Which styling approach?"
Options: Tailwind CSS, CSS Modules, Styled Components, Plain CSS, Sass/SCSS"
```
Record: framework, language, styling

### Step 3: Design
```
Agent: "Choose a design personality (this determines typography, colors, and animations):"
Options:
- Swiss - High contrast, precise, functional (Fintech, enterprise)
- Editorial - Sophisticated, timeless (Publishing, luxury)
- Tech Noir - Dark, technical, futuristic (Dev tools, Web3)
- Playful - Friendly, bouncy, creative (Consumer apps)
- Minimal - Essential, reductionist (Agencies, portfolios)
- Contemporary - Bold, expressive (Creative agencies)

Agent: "Do you have brand colors? (enter hex codes or color names, or 'no')"

Agent: "Any typography preferences? (font names or categories, or 'no')"

Agent: "Motion preference?"
Options: Subtle (minimal animations), Standard (typical web animations), Playful (bouncy, engaging), None (static)
```
Record: personality, colors, typography, motion

### Step 4: Frontend - Pages
```
Agent: "Which pages do you need? (select all that apply)"
Multi-select options: Home, About, Contact, Blog, Pricing, Portfolio, Shop/Products, Dashboard, Login/Register, Documentation
```
Record: requiredPages (array)

### Step 5: Frontend - Components
```
Agent: "Hero section style?"
Options: Full-width image/video, Split (text + image), Centered text, Minimal/Text-only, Interactive/Animated

Agent: "Navigation type?"
Options: Standard navbar, Mega menu, Sidebar navigation, Floating/Sticky, None (single page)

Agent: "Footer style?"
Options: Multi-column (rich), Simple (links only), Minimal, None
```
Record: heroStyle, navigation, footer

### Step 6: Backend
```
Agent: "Authentication needs?"
Options: None needed, User login/signup, Social login (OAuth), Admin dashboard with auth

Agent: "Database requirements?"
Options: None (static site), SQL database (PostgreSQL/MySQL), NoSQL (MongoDB), Edge database (D1/Supabase), CMS as backend

Agent: "Custom API needs?"
Options: None, REST API, GraphQL, Real-time (WebSockets)

Agent: "Preferred hosting?"
Options: Vercel, Netlify, Cloudflare Pages, Node.js server, Static hosting
```
Record: auth, database, api, hosting

### Step 7: Pick n' Mix (Unique Feature)
```
Agent: "Now for the unique part - you can mix and match components from our 50+ pre-built templates. Your choices create a truly unique site."

Agent: "Pick a hero component style:"
Options:
- From astrowind - SaaS marketing hero
- From astroship - Startup hero
- From nextjs-dashboard - Clean admin hero
- Create custom

Agent: "Pick a button style:"
Options: From shadcn-ui, From daisyui, From mantine, From custom design system

Agent: "Pick a card style:"
Options: From gatsby-portfolio-cara, From nextjs-commerce, From astro-paper, Create custom

Agent: "Pick a navbar style:"
Options: From astrowind, From starlight-docs, From gatsby-starter-blog, Create custom

Agent: "Pick a footer style:"
Options: From astrowind (multi-column), From hugo-universal, From nextjs-commerce, Create custom
```
Record: heroComponents, buttonComponents, cardComponents, navbarComponents, footerComponents

## Storage

Save configuration to `.openagent-ux.json`:

```json
{
  "version": "1.0",
  "created": "2024-01-01T00:00:00Z",
  "architecture": {
    "projectType": "SaaS application",
    "projectName": "my-saas",
    "description": "A project management tool"
  },
  "techstack": {
    "framework": "Next.js",
    "language": "TypeScript",
    "styling": "Tailwind CSS"
  },
  "design": {
    "personality": "Tech Noir",
    "colors": "#000000, #00ffff",
    "typography": " Geist",
    "motion": "Standard"
  },
  "frontend": {
    "pages": ["Home", "About", "Pricing", "Dashboard"],
    "heroStyle": "Split (text + image)",
    "navigation": "Standard navbar",
    "footer": "Multi-column (rich)"
  },
  "backend": {
    "auth": "User login/signup",
    "database": "PostgreSQL",
    "api": "REST API",
    "hosting": "Vercel"
  },
  "pickAndMix": {
    "heroComponents": "From astrowind - SaaS marketing hero",
    "buttonComponents": "From shadcn-ui",
    "cardComponents": "From nextjs-commerce",
    "navbarComponents": "From astrowind",
    "footerComponents": "From astrowind (multi-column)"
  }
}
```

## Completion

After questionnaire completes:

1. Display summary to user
2. Signal Principal Architect with config
3. Begin orchestration

### Summary Display
```
╔══════════════════════════════════════════════════════════════════╗
║                    CONFIGURATION COMPLETE                         ║
╠══════════════════════════════════════════════════════════════════╣
║  Project: my-saas (SaaS application)                              ║
║  Framework: Next.js + TypeScript + Tailwind CSS                 ║
║  Design: Tech Noir (dark, technical, futuristic)                 ║
║  Pages: Home, About, Pricing, Dashboard                          ║
║  Hero: astrowind SaaS hero                                       ║
║  Buttons: shadcn-ui                                              ║
║  Cards: nextjs-commerce                                          ║
║  Navbar: astrowind                                               ║
║  Footer: astrowind multi-column                                   ║
╚══════════════════════════════════════════════════════════════════╝

Starting Principal Architect to orchestrate the build...
```

## Agent Handoff

After saving config, delegate to Principal Architect:

```
The user has completed the project questionnaire. Configuration is saved to .openagent-ux.json

Please proceed with:
1. Read the configuration from .openagent-ux.json
2. Analyze requirements and create execution plan
3. Delegate to domain leads (Design, Frontend, Backend, QA)
4. Assemble site using pick n' mix components from templates/

Available templates: templates/ (Astro, Gatsby, Next.js, Nuxt, Hugo)
Community components: components/community/ (shadcn-ui, radix-ui, etc.)
Design systems: design-systems/ (6 personality token sets)
Component registry: components-registry.json

IMPORTANT: Use pre-built components from templates as much as possible to avoid generic AI output.
```

## Error Handling

- If user cancels mid-questionnaire: Save partial config, offer to resume
- If invalid input: Re-prompt with valid options
- If framework/template not available: Offer alternatives

## Examples

### Example 1: Complete SaaS Project
```
User: /start
Agent: What type of project are you building?
User: SaaS application
Agent: What is your project name?
User: taskflow
Agent: Briefly describe your project...
User: A project management tool for remote teams
Agent: Which framework do you want to use?
User: Next.js
... (continues through all questions)
Agent: Configuration complete. Starting build...
```

### Example 2: Resume Partial Config
```
User: /start
Agent: I see you have a partial configuration from a previous session. Would you like to:
1. Resume where you left off
2. Start fresh
3. View current configuration

User: Resume
Agent: Continuing from "Tech Stack" section...
```