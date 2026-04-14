---
name: anti-slop
description: >-
  Anti-generic guardrails that block common "AI slop" outputs. Blocks defaults like Inter font, blue-500 colors, generic gradients.
  AUTO-ACTIVE: Runs automatically with EVERY build command. DO NOT skip.
  Triggers on: Any /build, /build component, /build page, /build landing.
---

# Anti-Slop Guardrails

## Purpose

**Automatically block** generic outputs that make AI-generated websites feel cheap and identical. These guardrails are ALWAYS active.

## CRITICAL: Always Active

**This skill runs automatically with EVERY build. Do NOT disable.**

## Blocked Patterns

### Font Blocking (NEVER Allow)

```
STOP if:
- "Inter" used as primary font → MUST use distinctive pairing
- "Roboto" as primary font
- System fonts (Arial, Helvetica default)
- Same font for heading + body (always use pairing)

REPLACE WITH:
- Geist + Fraunces (Swiss/Editorial)
- Geist Mono + Geist (Tech)
- Outfit + Nunito (Playful)
- Satoshi + General Sans (Minimal)
- Syne + DM Sans (Contemporary)
```

### Color Blocking (NEVER Allow)

```
STOP if:
- blue-500, blue-600 as primary → MUST use curated palette
- purple-to-pink gradient
- "brand blue" / "primary blue" without specific hue
- Generic "SaaS purple"
- Any color without purpose

REPLACE WITH: Brand personality palette from /brand choice
- Swiss: Black + White + International Orange
- Editorial: Cream + Terracotta
- Tech Noir: Dark + Cyan + Purple
- Playful: Coral + Mint + Yellow
- Minimal: Off-white + Black
- Contemporary: Charcoal + Pink + Green
```

### Gradient Blocking (NEVER Allow)

```
STOP if:
- "purple-to-pink gradient"
- "blue-to-purple gradient"  
- Any default gradient without brand purpose
- "brand gradient" (too vague)
- Linear gradient used without intention

REPLACE WITH: Solid brand colors OR intentional gradients
- Subtle brand accent as background
- Noise texture instead of gradient
- Minimal color blocks (not fades)
```

### Component Blocking (NEVER Allow)

```
STOP if:
- Uniform border-radius everywhere (add variation)
- Generic card with white background + shadow
- Default skeleton (gray rectangle)
- Standard button (no personality)

REPLACE WITH:
- Personality-matched border-radius
- Card with brand treatment
- Skeleton with pulse/location hint
- Button with micro-interaction
```

### Empty State Blocking (NEVER Allow)

```
STOP if:
- "No items yet" text only
- Generic empty illustration
- No empty state at all (blank space)

REPLACE WITH:
- Brand-tied empty illustration
- Action-oriented messaging
- Helpful next steps
- Distinctive per personality
```

### Typography Blocking (NEVER Allow)

```
STOP if:
- Line height < 1.5 for body text
- Line height > 1.7 for headings
- Line length > 80 characters
- Line length < 45 characters
- Text < 16px for body

REPLACE WITH:
- Body: 16px minimum, line-height 1.6
- Headings: proper hierarchy
- Line length: 45-75 characters
- Proper spacing
```

## Quality Gates (Anti-Slop)

Before marking build complete, verify:
- [ ] Font: NOT Inter as primary
- [ ] Font: Using distinctive pairing (2 fonts min)
- [ ] Colors: NO generic blue-500
- [ ] Colors: NO purple-pink gradient
- [ ] Components: Border-radius has variation
- [ ] Empty states: Designed (not blank)
- [ ] Typography: 16px minimum body
- [ ] Typography: Line length 45-75 chars

## Always Include

### Micro-Interactions
Every interactive element needs:
- Hover feedback (not just color)
- Press feedback (scale/shadow)
- Focus visible ring
- Loading state for async

### Loading States
No bare skeletons:
- Pulsing brand-colored skeleton
- Location hint (shimmer direction)
- Loading text/message

### Error States
Not generic:
- Clear explanation
- Recovery action
- Brand treatment

### Empty States
Not generic "No items":
- Brand illustration
- Action prompt
- Helpful messaging

## Common Slop → Premium Fixes

| Slop | Premium Fix |
|------|-----------|
| Inter font | Geist + Fraunces |
| blue-500 | Brand palette from /brand |
| Purple gradient | Solid accent or noise |
| White card | Brand-tied surface |
| "No items yet" | Brand empty state |
| Gray skeleton | Brand-colored pulse |
| Generic button | Micro-interaction |

## Auto-Check List

Run this check BEFORE completing any build:

```
[ ] Font pairing used (NOT Inter)
[ ] Primary color from brand (NOT blue-500)  
[ ] No purple-pink gradients
[ ] Border-radius has variation (not all 8px)
[ ] Empty states designed
[ ] Skeleton with brand color
[ ] Micro-interactions on buttons
[ ] Focus states visible
```

## Violation Handling

If anti-slop violation found:
1. STOP the build
2. Identify the violation
3. Apply fix from replacement column
4. Resume build

**Do NOT ship with anti-slop violations.**