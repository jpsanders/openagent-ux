# AI Rules - Non-Negotiables

## Technical Standards

### Stack Requirements
- **Framework**: Next.js 14+ (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS + CSS Modules for complex components
- **State**: Server Actions, React Context, no Redux
- **Database**: PostgreSQL with Prisma or Drizzle

### Security Requirements
- **Secrets**: NEVER commit .env, use environment variables
- **Auth**: Use NextAuth.js or Clerk, never roll your own
- **Validation**: All inputs validated with Zod
- **CSRF**: Handled by Next.js Server Actions
- **Rate Limiting**: On all mutation endpoints

### Code Quality
- **No `any`**: Use proper TypeScript types
- **No `// @ts-ignore`**: Fix issues properly
- **No console.log in production**: Use proper logging
- **No raw hex in components**: Use design tokens
- **No magic numbers**: Use named constants

---

## Design Rules

### Design System Compliance
- **Colors**: Use semantic tokens (background, surface, brand, success, error) - NEVER raw hex in components
- **Typography**: Use type scale tokens (display, heading-1, body, small)
- **Spacing**: Use spacing scale (1 = 4px, 2 = 8px, 4 = 16px)
- **Components**: Must have all states (hover, active, focus, disabled)

### Accessibility (WCAG 2.1 AA)
- **Contrast**: 4.5:1 for text, 3:1 for UI elements
- **Focus**: Visible focus indicators on ALL interactive elements
- **Semantics**: Proper landmarks (header, main, nav, footer)
- **Forms**: Labels associated, error messages accessible
- **Keyboard**: Full keyboard navigation

---

## Performance Rules

### Core Web Vitals
- **LCP**: Must be < 2.5s
- **INP**: Must be < 200ms
- **CLS**: Must be < 0.1

### Optimization Requirements
- **Images**: Use Next.js Image with explicit sizes
- **Fonts**: Use next/font with display: swap
- **Bundles**: No more than 200kb initial JS (gzipped)
- **Lazy Loading**: Dynamic imports for heavy components

---

## Architecture Rules

### File Organization
```
src/
├── app/           # Next.js App Router
├── components/    # Reusable UI components
│   ├── ui/        # Design system components
│   └── [feature]/ # Feature-specific components
├── lib/           # Utilities and configs
├── hooks/         # Custom React hooks
└── types/         # TypeScript definitions
```

### Component Patterns
- Use compound components for complex patterns
- Accept className for styling overrides
- Support forwardRef when needed
- Export components from single entry point

---

## Git & Deployment Rules

### Commit Rules
- Conventional commits (feat:, fix:, refactor:)
- No committing secrets or .env files
- Run lint/typecheck before committing

### Deployment Rules
- Deploy via Vercel (recommended)
- Preview deployments for PRs
- Production only after QA phase complete
- Environment variables set in dashboard

---

## Testing Rules

### Coverage Requirements
- Unit tests for utilities and hooks
- Integration tests for server actions
- E2E tests for critical flows

### Test Patterns
- Use Vitest or Jest
- Use Playwright or Cypress for E2E
- Mock external services

---

## Breaking These Rules

These rules are **non-negotiable**. If a client requests something that violates these rules:
1. Explain the risk/impact
2. Offer a compliant alternative
3. If they insist, note it in writing before proceeding

---

## Exceptions

If you must deviate from these rules:
1. Document the reason
2. Note it in the PR description
3. Get explicit approval in writing
