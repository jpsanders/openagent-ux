# Subagent Onboarding Guide

## Welcome to WebForge

This document introduces the subagents that power WebForge's website building system.

---

## Agent Architecture

```
WebForge (Main Agent)
├── Design Agent       → Visual design & design system
├── Frontend Agent    → React/Next.js implementation
├── Backend Agent     → Server actions & data
├── Performance Agent → Optimization & Core Web Vitals
├── QA Agent          → Testing & accessibility
└── Deploy Agent      → CI/CD & deployment
```

---

## Design Agent

**Purpose**: Creates semantic design systems, UI components, motion primitives

**Specialties**:
- Semantic color tokens (purpose-based, not shade-based)
- Type scale (intentional hierarchy)
- Spacing grid (4px base)
- Component states (all 5 states)
- Motion primitives (enter/exit/interaction)

**How to invoke**:
```
Task the Design Agent to:
- Generate design tokens for [brand colors]
- Build button component with all states
- Create card component variants
- Set up motion animations
```

**Output location**: `src/design-system/`

---

## Frontend Agent

**Purpose**: Translates design systems into production React code

**Specialties**:
- Next.js App Router patterns
- Tailwind + CSS Modules
- Responsive implementation
- Accessibility (WCAG 2.1 AA)
- Component composition

**How to invoke**:
```
Task the Frontend Agent to:
- Build landing page from design tokens
- Create contact form with validation
- Implement responsive navigation
- Add SEO metadata to pages
```

**Output location**: `src/app/`, `src/components/`

---

## Backend Agent

**Purpose**: Builds server-side logic, APIs, data layer

**Specialties**:
- Server Actions
- Prisma/Drizzle ORM
- NextAuth/Clerk auth
- Zod validation
- Edge functions

**How to invoke**:
```
Task the Backend Agent to:
- Create user schema and migrations
- Build server action for form submission
- Set up authentication flow
- Add API route for [feature]
```

**Output location**: `src/app/actions/`, `prisma/`

---

## Performance Agent

**Purpose**: Optimizes for Core Web Vitals and runtime performance

**Specialties**:
- LCP optimization
- INP optimization
- CLS prevention
- Bundle analysis
- Image/font optimization

**How to invoke**:
```
Task the Performance Agent to:
- Audit current performance scores
- Fix LCP issues on hero section
- Optimize bundle size
- Add lazy loading to components
```

**Output location**: Recommendations + code fixes

---

## QA Agent

**Purpose**: Ensures quality through testing and accessibility

**Specialties**:
- Accessibility auditing (axe, Lighthouse)
- Cross-browser testing
- Visual regression
- Error detection
- Testing setup

**How to invoke**:
```
Task the QA Agent to:
- Run accessibility audit
- Check for console errors
- Review component states
- Verify responsive breakpoints
```

**Output location**: Audit reports + fix recommendations

---

## Deploy Agent

**Purpose**: Ships sites to production with CI/CD

**Specialties**:
- Vercel/Netlify deployment
- Environment configuration
- CI/CD pipeline setup
- Health checks
- Monitoring setup

**How to invoke**:
```
Task the Deploy Agent to:
- Deploy to Vercel
- Set up environment variables
- Configure CI/CD pipeline
- Verify production health
```

**Output location**: Deployed site + monitoring

---

## Working with Subagents

### Routing Guidelines

| Task | Route To |
|------|----------|
| Visual design, tokens, components | Design Agent |
| Page implementation, forms, responsive | Frontend Agent |
| Database, auth, server actions | Backend Agent |
| Speed optimization, Core Web Vitals | Performance Agent |
| Testing, accessibility, QA | QA Agent |
| Deployment, CI/CD | Deploy Agent |

### Chaining Agents
For complex tasks, chain multiple agents:

1. **Design → Frontend**: Design Agent creates tokens → Frontend Agent implements
2. **Frontend → Backend**: Frontend builds form → Backend adds server action
3. **Implementation → Performance**: Build complete → Performance Agent optimizes
4. **Build → QA → Deploy**: Implement → QA audit → Deploy Agent ships

### Quality Gates
Each agent has quality gates to meet before advancing:
- Design Agent: All tokens semantic, components have all states
- Frontend Agent: Uses tokens, no raw hex, responsive
- Backend Agent: Zod validation, no secrets exposed
- Performance Agent: Core Web Vitals targets met
- QA Agent: No critical issues, accessibility score 90+
- Deploy Agent: Build succeeds, health check passes

---

## Skills Available to All Agents

- **design-system.skills**: Token generation, component patterns
- **responsive.skills**: Breakpoint patterns, mobile-first
- **performance.skills**: Optimization techniques
- **audit.skills**: Quality auditing
- **refactor.skills**: Accessibility fixes

---

## Communication

When invoking agents:
1. Be specific about the deliverable
2. Reference existing files when relevant
3. Set clear acceptance criteria
4. Ask for confirmation before proceeding to next phase

---

*This guide is loaded by the Main Agent before delegating work to subagents.*
