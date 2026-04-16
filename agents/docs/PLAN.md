# Build Plan

## Overview
Step-by-step workflow for building high-performance websites with WebForge.

---

## Phase 1: Discovery

### Step 1.1: Read Context Files
1. Open PRD.md - understand project scope and exclusions
2. Open ARCHITECTURE.md - understand folder structure requirements
3. Open AI_RULES.md - understand technical constraints
4. Open agents.md - understand subagent capabilities

### Step 1.2: Clarify Requirements
- Ask clarifying questions if PRD is ambiguous
- Confirm tech stack choices
- Identify dependencies between features

---

## Phase 2: Design System

### Step 2.1: Generate Tokens
1. Invoke Design Agent with project requirements
2. Design Agent outputs: `tokens.json`, CSS variables
3. Validate semantic color names
4. Validate type scale has 7+ steps
5. Validate spacing uses 4px base

### Step 2.2: Build Component Library
1. Design Agent generates base components
2. Components include ALL states (hover, active, focus, disabled)
3. Each component exported from single entry point
4. Motion primitives applied

### Step 2.3: Design Review
- Run critique skill on design system
- Fix any visual hierarchy issues
- Confirm color contrast accessibility

---

## Phase 3: Frontend Implementation

### Step 3.1: Project Setup
1. Initialize Next.js with TypeScript
2. Configure Tailwind with design tokens
3. Set up folder structure per ARCHITECTURE.md
4. Add utility functions (cn, etc.)

### Step 3.2: Build Layout
1. Root layout with fonts, metadata
2. Header with navigation
3. Footer with links
4. Responsive behavior verified

### Step 3.3: Build Pages
For each page:
1. Create route in app/
2. Implement with design system components
3. Add loading/suspense states
4. Verify responsive at all breakpoints
5. Add metadata for SEO

### Step 3.4: Integration
- Connect to backend (if needed)
- Add form handling
- Implement data fetching patterns

---

## Phase 4: Backend (if applicable)

### Step 4.1: Schema Design
1. Define data models
2. Create migrations
3. Set up Prisma/Drizzle client

### Step 4.2: Server Actions
For each mutation:
1. Create server action
2. Add Zod validation
3. Implement revalidation
4. Handle errors gracefully

### Step 4.3: Auth (if needed)
1. Configure NextAuth/Clerk
2. Set up providers
3. Add protected routes

---

## Phase 5: Performance

### Step 5.1: Initial Audit
1. Run Lighthouse
2. Check Core Web Vitals
3. Identify issues

### Step 5.2: LCP Fixes
1. Add priority to hero images
2. Optimize fonts
3. Check for render-blocking resources

### Step 5.3: INP Fixes
1. Break long tasks
2. Remove unnecessary listeners
3. Add lazy loading

### Step 5.4: CLS Fixes
1. Add aspect ratios to images
2. Reserve space for dynamic content
3. Check font loading

---

## Phase 6: QA

### Step 6.1: Accessibility Audit
1. Run axe or Lighthouse accessibility
2. Fix all critical issues
3. Test with keyboard only

### Step 6.2: Cross-Browser
1. Test in Chrome, Firefox, Safari
2. Fix any browser-specific issues

### Step 6.3: Visual Regression
1. Review each page
2. Check design token consistency

### Step 6.4: Error Check
1. No console errors
2. All forms validate
3. Loading states exist
4. Error boundaries defined

---

## Phase 7: Deployment

### Step 7.1: Pre-Deploy
1. Environment variables configured
2. Build succeeds
3. No type errors
4. No lint errors

### Step 7.2: Deploy
1. Connect to Vercel/Netlify
2. Push to trigger deploy
3. Wait for build completion

### Step 7.3: Verify Production
1. Health check endpoint returns 200
2. Core Web Vitals still pass
3. No new console errors
4. Forms work

### Step 7.4: Monitor
1. Set up error tracking (Sentry)
2. Configure analytics
3. Document URL for client

---

## Important Notes

- **ONE STEP AT A TIME**: Complete each step before moving to the next
- **CHECK PROGRESS**: Run audits after each major phase
- **DON'T SKIP**: Complete every step in each phase
- **VERIFY**: Test locally before deploying

---

## Phase Completion Checklist

After each phase, confirm:
- [ ] All files created/updated
- [ ] No build errors
- [ ] No lint/type errors
- [ ] Manual verification done
