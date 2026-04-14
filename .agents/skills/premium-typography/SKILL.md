---
name: premium-typography
description: >-
  12 distinctive premium font pairings that avoid generic Inter/Roboto defaults. Each with @next/font configuration and aesthetic mapping.
  Referenced by /brand command. DO NOT use Inter as primary font - it has become the generic of AI websites.
---

# Premium Typography

## Purpose

**Avoid the generic.** Inter has become the "default" font of AI-generated websites. This skill provides 12 distinctive alternatives.

## CRITICAL: Never Use Inter

**Primary font NEITHER:**
- Inter as primary heading
- Inter as primary body
- Inter anywhere in visible text

**This is non-negotiable for premium uniqueness.**

## 12 Premium Font Pairings

### 1. Geist + Fraunces (Swiss/Refined)
```
Mood: Sophisticated, premium, editorial
Use: Premium SaaS, fintech, enterprise dashboards

Heading: Geist (variable)
Body: Fraunces (variable serif)

Display: swap, subsets: latin
```

### 2. Satoshi + DM Sans (Modern Minimal)
```
Mood: Clean, tech-forward, premium
Use: AI tools, modern startups, developer platforms

@next/font: DM Sans + @fontshare: Satoshi
Note: Satoshi via Fontshare CDN
```

### 3. Outfit + Plus Jakarta Sans (B2B SaaS)
```
Mood: Professional, trustworthy, modern
Use: SaaS platforms, AI products, B2B tools

@next/font: Outfit + Plus Jakarta Sans
Note: Popular for AI tools - add personality via weights
```

### 4. Syne + DM Sans (Brutalist Bold)
```
Mood: Bold, edgy, creative, expressive
Use: Creative agencies, design studios, portfolios

@next/font: Syne (heading) + DM Sans (body)
Note: Aggressive width in heavier weights
```

### 5. Bricolage Grotesque + Space Mono (Indie Hacker)
```
Mood: Raw, authentic, technical
Use: Indie projects, developer tools, Web3

@next/font: Bricolage Grotesque + Space Mono
Note: Variable width, slightly unpolished feel
```

### 6. Sora + Manrope (Futuristic)
```
Mood: Technical, futuristic, DAO/ Web3
Use: Crypto apps, DeFi, Web3 products

@next/font: Sora + Manrope
Note: Sharp angles, technical character
```

### 7. Instrument Serif + Instrument Sans (Cohesive Premium)
```
Mood: Elegant, premium, brand-focused
Use: Luxury brands, high-end services

@next/font: Instrument Serif + Instrument Sans
Note: Same family - excellent harmony
```

### 8. Fraunces + Chivo (Fintech Premium)
```
Mood: Trustworthy, established, premium
Use: Financial services, banking, enterprise

@next/font: Fraunces (soft serif) + Chivo (geometric sans)
Note: Optical sizing on Fraunces
```

### 9. Playfair Display + Source Sans 3 (Editorial)
```
Mood: Editorial, content-focused, timeless
Use: CMS platforms, newsletters, publishing, blogs

@next/font: Playfair Display + Source Sans 3
Note: Classic high-contrast serif
```

### 10. Geist + Geist Mono (Developer Premium)
```
Mood: Technical, functional, Vercel-aligned
Use: Dev tools, API products, documentation

@next/font: Geist + Geist_Mono
Note: Cohesive mono pairing
```

### 11. Clash Display + Satoshi (Bold Modern)
```
Mood: Bold, premium, distinctive
Use: Premium agencies, creative portfolios

@fontshare: Clash Display + Satoshi
Note: Fontshare CDN required
```

### 12. Recollet + General Sans (Editorial Elegant)
```
Mood: Editorial, elegant, distinctive
Use: Fashion, luxury, design-forward

@fontshare: Recollet + General Sans
Note: Unique narrow serif - memorable
```

## Font Setup Methods

### Method 1: @next/font/google (Recommended)
```typescript
// app/layout.tsx
import { Geist, Fraunces } from 'next/font/google'

const geist = Geist({ 
  subsets: ['latin'], 
  variable: '--font-heading',
  display: 'swap',
})

const fraunces = Fraunces({ 
  subsets: ['latin'], 
  variable: '--font-body',
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${geist.variable} ${fraunces.variable}`}>
      {children}
    </html>
  )
}
```

### Method 2: Fontshare CDN
```css
/* globals.css */
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap');
@import url('https://api.fontshare.com/v2/css?f[]=clash-display@400,500,700&display=swap');
```

### Method 3: @fontsource (NPM)
```bash
npm install @fontsource/outfit @fontsource/plus-jakarta-sans
```

## Font Pairing Selection Guide

### By Industry

| Industry | Primary Choice | Mood |
|----------|-------------|------|
| Fintech/Enterprise | Geist + Fraunces | Professional |
| Developer/Web3 | Geist Mono + Geist | Technical |
| AI/Tech Startup | Satoshi + DM Sans | Modern |
| Creative/Agency | Syne + DM Sans | Bold |
| Publishing/Editorial | Playfair + Source | Classic |
| Luxury/Premium | Instrument Serif + Sans | Elegant |
| B2B SaaS | Outfit + Plus Jakarta | Trustworthy |
| Web3/Crypto | Sora + Manrope | Futuristic |

### By Brand Personality

| Personality | Font Pairing |
|-------------|------------|
| Swiss | Geist + Fraunces |
| Warm Editorial | Playfair + Source Sans 3 |
| Tech Noir | Geist Mono + Geist |
| Playful | Outfit + Nunito |
| Minimal | Satoshi + General Sans |
| Contemporary | Syne + DM Sans |

## Never Use List

**NEVER use these as primary:**
- Inter (becoming generic)
- Roboto (dated)
- Open Sans (generic)
- Lato (generic)
- Montserrat (overused)

## Typography Rules

### Body Text
- Minimum: 16px
- Line height: 1.6 (relative)
- Line length: 45-75 characters (optimal)

### Headings
- H1: 2.25-3rem, 700 weight
- H2: 1.875rem, 600 weight  
- H3: 1.5rem, 600 weight
- Line height: 1.2-1.3

### Code
- Monospace: Geist Mono, JetBrains Mono, or Source Code Pro
- Size: 14px (readable)

## Quality Gates

Before marking build complete:
- [ ] Font: NOT Inter
- [ ] Font: Using 2-font pairing
- [ ] Font: Proper @next/font setup
- [ ] Typography: 16px minimum body
- [ ] Typography: Proper line heights
- [ ] Typography: Line length controlled