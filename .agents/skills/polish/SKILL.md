---
name: polish
description: >-
  Final quality pass catching alignment, spacing, interaction details, and micro-polish that separates professional work from amateur.
  Triggers on: "finish", "polish", "quality pass", "make it professional", "/polish", "shipping", "ship it".
  Skip if: early in development, prototype phase, MVP only.
---

# Polish - Premium Quality Pass

## When to Use

This skill is for **near-final or production** work — it assumes functional completeness.

**DO NOT USE when:**
- Building prototypes
- Early iteration (save polish for when feature is stable)
- MVP only / throwaway code

**USE WHEN:**
- Feature is functionally complete
- Ready to ship to production
- Want that "designed by a professional" feel

## The Polish Sequence

Run these in order:

### 1. Alignment Audit
Check every breakpoint:
- [ ] Header alignment: logo, nav, actions aligned
- [ ] Card padding: consistent across all cards
- [ ] Grid gaps: uniform spacing
- [ ] Mobile text: no horizontal scroll

### 2. Spacing Tokens
- [ ] Consistent padding scale (8px base)
- [ ] Consistent margin scale
- [ ] No orphan margins (stick to grid)
- [ ] Content max-width: 65-75 chars

### 3. Interactive States
Every interactive element must have:
- [ ] Hover state (visible, not just color)
- [ ] Active/pressed state
- [ ] Focus ring (visible, high contrast)
- [ ] Disabled state (if applicable)
- [ ] Loading state (for async)

### 4. Motion Check
- [ ] Animations: 300ms max
- [ ] Micro-interactions: 150ms max
- [ ] No layout shifts during load
- [ ] Skeleton for async content
- [ ] Reduced motion respected

### 5. Touch & Mobile
- [ ] Touch targets: 44×44px minimum
- [ ] Spacing between targets: 8px+
- [ ] No hover-only functionality
- [ ] Tested at 320px, 375px, 768px

### 6. Typography
- [ ] Line height: 1.5-1.6 for body
- [ ] Line length: 45-75 characters
- [ ] Paragraph spacing: consistent
- [ ] No orphans in headings

### 7. Empty States
- [ ] Empty states designed (no blank space with error)
- [ ] Loading states designed
- [ ] Error states designed
- [ ] 404/500 pages have design

### 8. Accessibility Check
- [ ] Focus order logical
- [ ] No keyboard traps
- [ ] ARIA labels where needed
- [ ] Color not only indicator
- [ ] Contrast ratio pass

## Premium Details That Matter

### Micro-interactions
- Button press: subtle scale (0.98)
- Hover: lift + shadow increase
- Focus: ring outside element
- Active: slight darkening

### Loading States
- Skeleton matching content layout
- Subtle pulse animation
- No layout shift when loaded

### Transitions
- Page: fade + slight slide (200ms)
- Modal: scale + fade
- Dropdown: fade + slide down
- Toast: slide in from corner

### Responsive Behavior
- Mobile nav: hamburger → drawer
- Desktop: no horizontal scroll
- Images: proper aspect ratios

## Output Format

For each issue found, output:
```
FILE: component.tsx
ISSUE: inconsistent padding
LINE: 14
FIX: change padding="md" to padding="lg" for hero cards
```

## Quality Gates

Before marking complete:
- [ ] Alignment checked at all breakpoints
- [ ] Interactive states on all elements
- [ ] Motion respects reduced-motion
- [ ] Touch targets 44px minimum
- [ ] Empty/loading/error states exist
- [ ] No console errors