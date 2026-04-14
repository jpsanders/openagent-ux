---
name: premium-motion
description: >-
  Premium animation using Motion (Framer Motion) with spring physics, micro-interactions, and purpose-driven motion.
  Triggers on: "animate", "motion", "animation", "/animate", "transition", "spring", "make it smooth".
  Use for: React/Next.js components needing professional, polished animations.
---

# Premium Motion Patterns

## Core Philosophy

**Motion that matters, not motion for motion's sake.**

Every animation should communicate:
- State changes (what happened)
- Hierarchy (where does attention go)
- Feedback (did the system respond)

## Spring Physics Presets

### Default Premium
```typescript
const spring = {
  type: "spring",
  stiffness: 100,
  damping: 10,
}
```

### Gentle (Subtle UI)
```typescript
const gentle = {
  type: "spring",
  stiffness: 50,
  damping: 10,
}
```

### Snappy (Interactive)
```typescript
const snappy = {
  type: "spring", 
  stiffness: 300,
  damping: 30,
}
```

### Bouncy (Playful)
```typescript
const bouncy = {
  type: "spring",
  stiffness: 300,
  damping: 10,
  mass: 0.8,
}
```

### Professional (No Bounce)
```typescript
const professional = {
  type: "spring",
  stiffness: 500,
  damping: 50,
}
```

## Visual Duration (2024+)

Easier to coordinate than physics:
```typescript
transition={{
  type: "spring",
  visualDuration: 0.5,
  bounce: 0.25,
}}
```

## Micro-Interactions

### Button Press
```typescript
<motion.button
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", visualDuration: 0.15 }}
>
```

### Button Hover
```typescript
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
>
```

### Card Hover Lift
```typescript
<motion.div
  initial={{ y: 0 }}
  whileHover={{ y: -4 }}
  transition={{ type: "spring", visualDuration: 0.2 }}
>
```

### Focus Ring
```typescript
<motion.input
  whileFocus={{ 
    scale: 1.02,
    boxShadow: "0 0 0 2px var(--primary)" 
  }}
>
```

## Page Transitions

### Fade + Slide
```typescript
const pageVariants = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -8 },
}

<AnimatePresence mode="wait">
  <motion.main
    key={pathname}
    initial="initial"
    animate="animate"
    exit="exit"
    variants={pageVariants}
    transition={{ duration: 0.2 }}
  />
</AnimatePresence>
```

### Staggered List
```typescript
const containerVariants = {
  animate: {
    transition: {
      staggerChildren: 0.05,
    },
  },
}

const itemVariants = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
}

<motion.ul variants={containerVariants}>
  {items.map(item => (
    <motion.li variants={itemVariants}>
      {item}
    </motion.li>
  ))}
</motion.ul>
```

## Modal & Dialog

```typescript
const modalVariants = {
  initial: { opacity: 0, scale: 0.95 },
  animate: { opacity: 1, scale: 1 },
  exit: { opacity: 0, scale: 0.95 },
}

<AnimatePresence>
  {isOpen && (
    <motion.div
      variants={modalVariants}
      initial="initial"
      animate="animate"
      exit="exit"
      transition={{ type: "spring", visualDuration: 0.2 }}
    />
  )}
</AnimatePresence>
```

## Scroll Animations

### Fade In On Scroll
```typescript
<motion.div
  initial={{ opacity: 0, y: 20 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.4 }}
/>
```

### Parallax
```typescript
<motion.div
  style={{ y: useTransform(scrollYProgress, [0, 1], [0, -50]) }}
/>
```

## Performance Rules

### MUST use transform/opacity
```css
/* GOOD - GPU accelerated */
transform: translateY(10px);
opacity: 0;

/* BAD - triggers layout */
margin-top: 10px;
width: 100%;
```

### Respect Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Duration Caps

| Animation Type | Max Duration | Best For |
|---------------|-------------|----------|
| Micro | 100-150ms | Button press, toggle |
| Standard | 200-300ms | Card hover, modal |
| Page | 300-400ms | Route change |

## Quality Gates

- [ ] All animations < 300ms (except page)
- [ ] Uses spring physics (not ease-in-out)
- [ ] Reduced motion respected
- [ ] No layout-triggering properties
- [ ] Focus states have no motion
- [ ] Loading uses skeleton (not spinner)