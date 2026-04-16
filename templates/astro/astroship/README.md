# Astroship - Astro SaaS/Startup Template

## Overview
Popular Astro template for startups and marketing websites.

## Source
- GitHub: https://github.com/surjithctly/astroship
- Stars: 1900+
- License: GPL-3.0

## Quick Start
```bash
npm create astro@latest -- --template surjithctly/astroship
```

## Template Structure

```
astroship/
├── src/
│   ├── components/
│   │   ├── Brand.astro
│   │   ├── Cta.astro
│   │   ├── Feature.astro
│   │   ├── Footer.astro
│   │   ├── Header.astro
│   │   ├── Hero.astro
│   │   ├── Logo.astro
│   │   ├── Navbar.astro
│   │   ├── Pricing.astro
│   │   ├── Section.astro
│   │   ├── Seo.astro
│   │   └── Testimonial.astro
│   ├── layouts/
│   │   ├── Layout.astro
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── pricing.astro
│   │   ├── features.astro
│   │   ├── about.astro
│   │   └── contact.astro
│   └── styles/
│       └── global.css
├── public/
├── astro.config.mjs
├── tailwind.config.cjs
└── package.json
```

## Key Sections
- **Hero** - Headline, subtext, dual CTAs
- **Features** - 3-column feature grid
- **Pricing** - 3-tier pricing table
- **Testimonials** - Customer quotes
- **CTA** - Final call to action

## Design Integration
Apply design system via Tailwind config or global.css

## Image Placeholders
- Hero: `https://picsum.photos/seed/hero-astro/1200x700`
- Features: `https://picsum.photos/seed/feature/600x400`
- Testimonials: `https://picsum.photos/seed/avatar/100x100`

## Demo
https://astroship.netlify.app