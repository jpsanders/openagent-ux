---
name: premium-build
description: >-
  Build premium website components/pages with design system, motion primitives, and professional polish.
  Triggers on: "/build", "build component", "build page", "build landing", "create ui", "make a page".
  Creates: Full implementation with design tokens, animations, and polish ready to ship.
---

# Premium Build Command

## Purpose

Build production-ready premium components using:
- Semantic design tokens
- Proper typography
- Spring animations
- All interactive states
- Responsive breakpoints

## Syntax

```
/build component [name]    - Single component
/build page [path]         - Full page  
/build landing [name]      - High-conversion landing
```

## Component Build

### Input Requirements

Before building, gather:
1. **Component purpose** - What does it do?
2. **States** - default, hover, active, focus, disabled, loading
3. **Variants** - primary, secondary, ghost, destructive
4. **Sizes** - sm, md, lg
5. **Motion** - entrance, hover, press animations

### Design System Application

**ALWAYS use semantic tokens:**
```typescript
// WRONG
<button className="bg-blue-500 px-4 py-2 rounded-lg">

// CORRECT  
<button className="bg-brand hover:bg-brand-600 text-white rounded-md h-10 px-4 transition-spring">
```

**Token mapping:**
- Colors: surface, brand, success, warning, error → with shades
- Spacing: 4px grid system
- Radius: sm, md, lg, full
- Typography: heading, body, small with proper line-height

## Page Build

### Page Structure

```
/app/[page]/page.tsx    - Server component
/components/           - Components
/lib/                 - Utilities
/hooks/               - Custom hooks
/styles/               - Additional styles
```

### Required Elements

1. **Layout wrapper** with max-width
2. **Navigation** (responsive)
3. **Hero/header section**
4. **Content sections** (2-4 max for focus)
5. **Footer**
6. **SEO metadata**

### Motion Integration

- Page entrance: staggered sections
- Scroll reveals: fade-up on viewport
- Hover: subtle lift on cards
- Buttons: press feedback

## Landing Page Build

### High-Conversion Sections

1. **Hero**
   - H1: Benefit statement (not features)
   - Subhead: How/why
   - CTA: Primary + secondary
   - Visual: Product/interface screenshot or abstract

2. **Social Proof**
   - Logos of companies (grayscale)
   - Testimonials (specific, not generic)
   - Numbers (revenue, users, etc.)

3. **Problem/Agitation**
   - User pain point
   - Emotional connection

4. **Solution**
   - How it works (visual)
   - Key features (3-4 max)

5. **Features Deep-Dive**
   - One feature per section
   - Visual per feature
   - Benefit-focused copy

6. **Pricing**
   - Clear tiers
   - Value per tier
   - FAQs

7. **CTA**
   - Strong close
   - Low friction

8. **Footer**
   - Links, legal, social

## Premium Quality Gates

Before returning, verify:
- [ ] Uses design tokens (not raw values)
- [ ] Has all interactive states
- [ ] Focus ring visible
- [ ] Motion uses spring (not linear)
- [ ] Responsive at 320px, 768px, 1024px
- [ ] No horizontal scroll
- [ ] Touch targets 44px minimum
- [ ] Empty/loading states exist
- [ ] Reduced motion respected

## Output Components

For each build, deliver:
```
src/
├── components/
│   └── [ComponentName]/
│       ├── index.tsx
│       ├── variants.ts
│       └── motion.ts
├── design-system/
│   └── tokens.css (updated)
└── tests/
    └── component.test.tsx
```

## Design System Requirements

### Color Semantics (Required)
```typescript
colors: {
  background: { 50-950 },
  surface: { 50-950 },
  brand: { 50-950 },
  brand-accent: { 50-950 },
  success: { 50-950 },
  warning: { 50-950 },
  error: { 50-950 },
  muted: { 50-950 },
}
```

### Type Scale (Required)
```typescript
fontSize: {
  display: ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
  h1: ['2.25rem', { lineHeight: '1.2', fontWeight: '700' }],
  h2: ['1.875rem', { lineHeight: '1.3', fontWeight: '600' }],
  h3: ['1.5rem', { lineHeight: '1.4', fontWeight: '600' }],
  body: ['1rem', { lineHeight: '1.6', fontWeight: '400' }],
  small: ['0.875rem', { lineHeight: '1.5' }],
}
```

### Spacing Scale (Required)
```typescript
space: {
  0: '0',
  1: '0.25rem',   // 4px
  2: '0.5rem',    // 8px
  3: '0.75rem',   // 12px
  4: '1rem',       // 16px
  6: '1.5rem',   // 24px
  8: '2rem',     // 32px
  12: '3rem',    // 48px
  16: '4rem',    // 64px
}
```