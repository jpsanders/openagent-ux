---
name: premium-brand
description: >-
  Establish unique brand identity BEFORE any website building. Forces intentional design personality choice, font pairing, color palette, and motion personality.
  Triggers on: /brand, "set brand", "define design", "brand personality", "unique design".
  AUTO-TRIGGER: Runs BEFORE /build if brand identity not configured.
  DO NOT skip - this is the FIRST step for any new website project.
---

# Premium Brand Identity

## Purpose

Establish **unique** design identity BEFORE any code is written. This prevents generic AI output by forcing intentional aesthetic choices.

## CRITICAL: Must Run First

**Before running `/build`, you MUST check for brand-identity.json:**

1. If `config/brand-identity.json` exists → Load it and use those values
2. If it does NOT exist → RUN `/brand` FIRST to create it

**Do NOT skip `/brand` - uniqueness depends on it.**

## Brand Personality Options

Ask user to choose ONE design personality:

### 1. Swiss International
- **Vibe**: Grid-focused, precision, clarity, high contrast
- **Typography**: Geist (heading) + Fraunces (body)
- **Colors**: Black/White + International Orange (#FF4D00)
- **Animation**: Reserved, precise, 150ms micro-interactions
- **Best for**: Fintech, enterprise, dashboards, professional services
- **Key traits**: Strong grid, bold typography, minimal color, functional

### 2. Warm Editorial
- **Vibe**: Sophisticated, curated, timeless, premium
- **Typography**: Playfair Display (heading) + Source Sans 3 (body)
- **Colors**: Cream (#FDFAF6) + Charcoal (#2D2A26) + Terracotta (#C4704B)
- **Animation**: Gentle, refined, 300ms ease-out
- **Best for**: Publishing, luxury,-content platforms, lifestyle
- **Key traits**: Serif headings, warm backgrounds, earthy accents

### 3. Tech Noir
- **Vibe**: Dark, technical, cutting-edge, developer-focused
- **Typography**: Geist Mono (heading/code) + Geist (body)
- **Colors**: Near-black (#0A0A0A) + Electric Cyan (#00D9FF) + Purple (#6B00FF)
- **Animation**: Snappy, functional, 100ms response
- **Best for**: Developer tools, Web3, API products, technical platforms
- **Key traits**: Dark default, monospace accents, neon accents

### 4. Playful
- **Vibe**: Friendly, approachable, energetic, memorable
- **Typography**: Outfit (heading) + Nunito (body)
- **Colors**: Coral (#FF6B6B) + Mint (#4ECDC4) + Butter Yellow (#FFE66D)
- **Animation**: Bouncy spring, 200ms, expressive
- **Best for**: Consumer apps, kids products, games, social
- **Key traits**: Rounded corners, bright colors, bouncy motion

### 5. Minimal
- **Vibe**: Essential, reductionist, gallery-quality, intentional
- **Typography**: Satoshi (heading) + General Sans (body)
- **Colors**: Off-white (#FAFAFA) + Jet black (#1A1A1A) + Warm gray (#E5E5E5)
- **Animation**: Subtle, fade-only, 200ms
- **Best for**: Agencies, portfolios, architecture, luxury brands
- **Key traits**: Maximum whitespace, one font, black on white, no decoration

### 6. Contemporary
- **Vibe**: Bold, current, expressive, design-forward
- **Typography**: Syne (heading) + DM Sans (body)
- **Colors**: Charcoal (#1A1A1A) + Hot pink (#FF3366) + Electric green (#00FF99)
- **Animation**: Dynamic, 250ms, expressive
- **Best for**: Creative agencies, design studios, bold brands
- **Key traits**: Bold color pops, expressive type, modern edge

## Questions to Ask

### Required Questions

1. **Design Personality**: Which personality matches your brand? (Show all 6 options)

2. **Industry/Mood**: What industry are you in?
   - Fintech/Enterprise → Swiss
   - Publishing/Luxury → Warm Editorial  
   - Developer/Web3 → Tech Noir
   - Consumer/Social → Playful
   - Portfolio/Agency → Minimal or Contemporary

3. **Existing Brand Assets**: Do you have brand fonts or colors already?
   - If yes → Pull those into the design

4. **Target Audience**: Who is this for?
   - Enterprise buyers → Swiss (professional)
   - Developers → Tech Noir (technical)
   - General consumers → Playful (friendly)
   - Luxury buyers → Editorial or Minimal

### Optional Questions

5. **Any color preferences?** (respect or override)
6. **Any font preferences?** (respect or override)
7. **Motion sensitivity?** (accessibility, some users prefer reduced motion)

## Output: brand-identity.json

Create `config/brand-identity.json`:

```json
{
  "brand": {
    "personality": "swiss",
    "name": "Brand Name",
    "industry": "fintech",
    "created": "2024-01-15T10:00:00Z"
  },
  "design": {
    "personality": "Swiss International",
    "typography": {
      "heading": "Geist",
      "body": "Fraunces",
      "headingVariable": "--font-heading",
      "bodyVariable": "--font-body",
      "mood": "Refined, editorial, sophisticated"
    },
    "colors": {
      "primary": "#000000",
      "secondary": "#FFFFFF", 
      "accent": "#FF4D00",
      "background": "#FFFFFF",
      "surface": "#F5F5F5",
      "foreground": "#000000",
      "mood": "High contrast, precise, professional"
    },
    "motion": {
      "personality": "reserved",
      "micro": "150ms",
      "standard": "200ms",
      "page": "300ms",
      "spring": "stiff",
      "mood": "Precise, functional, snappy"
    },
    "spacing": {
      "base": "4px",
      "scale": [0, 4, 8, 16, 24, 32, 48, 64, 96]
    }
  },
  "antiSlop": {
    "neverUse": ["blue-500", "purple-500", "Inter as primary", "gradient purple-pink"],
    "mustHave": ["micro-interactions", "distinctive empty states"]
  },
  "unique": {
    "font": "Geist + Fraunces (NOT Inter)",
    "color": "Black/White + Orange (NOT SaaS blue)",
    "personality": "Swiss International precision"
  }
}
```

## Implementation Steps

### Step 1: Determine Personality
- Ask user to choose from 6 options
- Show visual description of each
- Explain best industry fit

### Step 2: Apply Design Rules
Based on personality choice:
- Select font pairing from premium-typography
- Select color palette from premium-palettes  
- Set motion personality from motion-personality

### Step 3: Export Configuration
- Write `config/brand-identity.json`
- Use values in all subsequent builds

### Step 4: Apply to Build
All `/build` commands reference `brand-identity.json`:
- Font: from config (NOT default Inter)
- Colors: from config (NOT default blue/purple)
- Motion: from config (matches personality)
- Spacing: from config (4px base)

## Quality Gates

Before marking `/brand` complete:
- [ ] Personality explicitly chosen (not default)
- [ ] Font pairing selected (NOT Inter)
- [ ] Color palette selected (NOT generic blue/purple)
- [ ] Motion personality matched
- [ ] brand-identity.json created
- [ ] Anti-slop rules documented

## Anti-Generic Rules

**NEVER Allow:**
- Inter as primary font → MUST use distinctive pairing
- blue-500 as primary → MUST use curated palette  
- purple gradient → MUST use brand-approved colors
- Generic empty states → MUST be distinctive
- No micro-interactions → MUST add personality

**ALWAYS Require:**
- Intentional choice (not defaults)
- Brand-matched typography
- Professional polish