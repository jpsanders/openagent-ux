---
name: motion-personality
description: >-
  Animation personality matched to brand identity. Not all animations should feel the same - motion should match brand personality.
  Referenced by /brand command. Defines micro-interactions, transitions, and page animations per personality.
---

# Motion Personality

## Purpose

**Motion should match brand personality.** A fintech app and a social game should animate differently. This skill maps animation feel to brand identity.

## CRITICAL: Match to Brand

**Animation personality MUST match brand personality from /brand:**
- Swiss → Reserved
- Warm Editorial → Refined
- Tech Noir → Snappy
- Playful → Expressive
- Minimal → Subtle
- Contemporary → Dynamic

## 6 Motion Personalities

### 1. Swiss - Reserved
```
Vibe: Precise, functional, minimal

Spring Config:
- stiffness: 500
- damping: 50
- mass: 1

Durations:
- micro: 100ms (buttons)
- standard: 150ms (hover)
- page: 200ms

Easing: ease-out-expo
Feel: Instant, professional, no bounce
Use: Buttons, toggles, inputs

Micro-interactions:
- Scale: none (too playful)
- Focus: ring appear
- Press: subtle darken
- No bounce
```

### 2. Warm Editorial - Refined
```
Vibe: Sophisticated, gentle, premium

Spring Config:
- stiffness: 50
- damping: 15
- mass: 1

Durations:
- micro: 150ms
- standard: 300ms
- page: 400ms

Easing: ease-out
Feel: Smooth, luxurious, deliberate
Use: Page transitions, modals

Micro-interactions:
- Fade + slight slide up
- Long ease (feels premium)
- No snap or bounce
- Subtle scale on hover
```

### 3. Tech Noir - Snappy
```
Vibe: Technical, functional, instant

Spring Config:
- stiffness: 300
- damping: 30
- mass: 1

Durations:
- micro: 80ms
- standard: 100ms  
- page: 200ms

Easing: ease-out
Feel: Instant response, technical
Use: Code snippets, toggles, interactions

Micro-interactions:
- Near-instant feedback
- No decorative animation
- Functional only
- Focus on clarity
```

### 4. Playful - Expressive
```
Vibe: Friendly, bouncy, memorable

Spring Config:
- stiffness: 300
- damping: 10
- mass: 0.8

Durations:
- micro: 150ms
- standard: 250ms
- page: 350ms

Easing: spring with bounce
Feel: Bouncy, delightful
Use: Buttons, cards, avatars

Micro-interactions:
- Scale bounce on press
- Wobble on hover
- Celebratory on success
- Expressive throughout
```

### 5. Minimal - Subtle
```
Vibe: Essential, gallery, intentional

Spring Config:
- stiffness: 100
- damping: 20
- mass: 1

Durations:
- micro: 100ms
- standard: 200ms
- page: 300ms

Easing: ease-in-out
Feel: Fade-based, minimal
Use: Page transitions, reveals

Micro-interactions:
- Opacity fade only
- No scale or transform
- Subtle position shift
- Maximum restraint
```

### 6. Contemporary - Dynamic
```
Vibe: Bold, current, expressive

Spring Config:
- stiffness: 200
- damping: 15
- mass: 0.9

Durations:
- micro: 120ms
- standard: 250ms
- page: 350ms

Easing: ease-out-expo
Feel: Dynamic, modern
Use: Hero reveals, CTAs

Micro-interactions:
- Scale + fade combo
- Expressive but controlled
- Dynamic entrance
- Bold but not playful
```

## Spring Presets

### Precise (Swiss)
```typescript
const spring = {
  type: "spring",
  stiffness: 500,
  damping: 50,
}
```

### Refined (Editorial)
```typescript
const spring = {
  type: "spring", 
  stiffness: 50,
  damping: 15,
}
```

### Snappy (Tech)
```typescript
const spring = {
  type: "spring",
  stiffness: 300,
  damping: 30,
}
```

### Bouncy (Playful)
```typescript
const spring = {
  type: "spring",
  stiffness: 300,
  damping: 10,
  mass: 0.8,
}
```

### Subtle (Minimal)
```typescript
const spring = {
  type: "spring",
  stiffness: 100,
  damping: 20,
}
```

### Dynamic (Contemporary)
```typescript
const spring = {
  type: "spring",
  stiffness: 200,
  damping: 15,
}
```

## Visual Duration (2024+)

Easier to coordinate:
```typescript
transition={{
  type: "spring",
  visualDuration: 0.2,  // 200ms
  bounce: 0.1,
}}
```

## Micro-Interaction Patterns

### Button Press
```typescript
// Reserved (Swiss)
whileTap={{ scale: 0.98 }}

// Refined (Editorial)  
whileTap={{ scale: 0.99, opacity: 0.9 }}

// Snappy (Tech)
whileTap={{ scale: 0.99 }}

// Expressive (Playful)
whileTap={{ scale: 0.95, rotate: -2 }}

// Subtle (Minimal)
whileTap={{ opacity: 0.9 }}

// Dynamic (Contemporary)
whileTap={{ scale: 0.97, y: 2 }}
```

### Card Hover
```typescript
// Reserved: Subtle lift
whileHover={{ y: -2 }}

// Refined: Gentle + shadow
whileHover={{ y: -4, boxShadow: "0 8px 24px rgba(0,0,0,0.12)" }}

// Snappy: Quick lift
whileHover={{ y: -2 }}

// Expressive: Scale + bounce
whileHover={{ scale: 1.02 }}

// Subtle: Slight lift only
whileHover={{ y: -1 }}

// Dynamic: Bold scale
whileHover={{ scale: 1.03, y: -4 }}
```

### Focus Ring
```typescript
// All personalities: visible ring REQUIRED
whileFocus={{
  outline: "2px solid var(--accent)",
  outlineOffset: "2px",
}}
```

## Page Transitions

### Reserved - Quick Fade
```typescript
const pageVariants = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0 },
}
```

### Refined - Slide + Fade
```typescript
const pageVariants = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -8 },
}
```

### Snappy - Instant
```typescript
const pageVariants = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0 },
}
// Keep fast
```

### Expressive - Stagger
```typescript
const containerVariants = {
  animate: {
    transition: { staggerChildren: 0.1 },
  },
}
```

## Reduced Motion

**ALWAYS respect:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Quality Gates

Before marking build complete:
- [ ] Motion: Matches brand personality
- [ ] Motion: NOT generic ease-in-out
- [ ] Micro: Under 150ms
- [ ] Page: Under 400ms
- [ ] Focus: Has animation (no motion)
- [ ] Reduced motion: Respected
- [ ] Performance: transform/opacity only