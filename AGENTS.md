# AGENTS.md - Subagent Documentation

## Overview

openagent-ux uses specialized subagents to handle different aspects of website building. Each subagent has a focused role and works together through the main orchestration.

## Subagent Routing

| Task Type | Subagent | Purpose |
|-----------|----------|----------|
| Visual Design | Design Agent | Semantic tokens, type scale, design system |
| Interface Design | UI Architect | Module depth, component composition |
| Animation | Animation Engineer | Spring physics, micro-interactions |
| Accessibility | Accessibility Audit | WCAG 2.1 AA compliance |
| Responsive | Responsive Specialist | Mobile-first layouts |
| Implementation | Frontend Agent | React/Next.js with design tokens |
| APIs | Backend Agent | Server actions, data layer |
| Performance | Performance Agent | Core Web Vitals, bundle optimization |
| Testing | QA Agent | Unit, E2E, accessibility verification |
| Deployment | Deploy Agent | Vercel/Netlify, CI/CD |

## Subagent Details

### Design Agent

**Purpose**: Creates semantic design systems

**Responsibilities**:
- Define semantic color tokens (not shade-based)
- Create type scale
- Establish spacing grid
- Build component library with all states

**Skills Used**:
- `premium-brand` - for brand matching
- `ui-typography` - for professional typography

### UI Architect

**Purpose**: Ensures interface design decisions

**Responsibilities**:
- Module depth (small interface, big capability)
- Component composition patterns
- Multiple design exploration

**Skills Used**:
- `design-an-interface` - for multi-option exploration

### Animation Engineer

**Purpose**: Creates purposeful motion

**Responsibilities**:
- Spring physics configuration
- Micro-interactions
- Page transitions
- Reduced motion support

**Skills Used**:
- `premium-motion` - spring physics
- `motion-personality` - brand-matched animation

### Accessibility Audit

**Purpose**: WCAG 2.1 AA compliance

**Responsibilities**:
- Contrast ratio verification
- Keyboard navigation
- Screen reader compatibility
- Focus management

### Responsive Specialist

**Purpose**: Mobile-first responsive design

**Responsibilities**:
- Breakpoint strategy
- Fluid typography
- Touch target sizing
- Cross-device testing

### Frontend Agent

**Purpose**: React/Next.js implementation

**Responsibilities**:
- Component development
- Page routing
- State management
- Integration with design tokens

### Backend Agent

**Purpose**: Server-side functionality

**Responsibilities**:
- API routes
- Database integration
- Authentication
- Server actions

### Performance Agent

**Purpose**: Core Web Vitals optimization

**Responsibilities**:
- LCP optimization
- INP improvement  
- CLS minimization
- Bundle analysis

### QA Agent

**Purpose**: Testing and verification

**Responsibilities**:
- Unit test coordination
- E2E test execution
- Accessibility auditing
- Visual regression

### Deploy Agent

**Purpose**: Deployment and CI/CD

**Responsibilities**:
- Platform deployment (Vercel/Netlify)
- Environment configuration
- CI/CD pipeline

## Workflow

```
/brand (chooses personality)
    ↓
Main manifest (orchestrates)
    ↓
Design Agent → UI Architect → Animation Engineer (design phase)
    ↓
Frontend Agent → Backend Agent (build phase)
    ↓
Performance Agent → QA Agent → Deploy Agent (ship phase)
```

## Quality Gates

Each subagent must verify:
- Uses brand values from `config/brand-identity.json`
- Anti-slop rules passed
- All interactive states implemented
- Micro-interactions added
- Reduced motion respected