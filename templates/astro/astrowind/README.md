# AstroWind - Production-ready Astro + Tailwind Template

## Overview
AstroWind is one of the most popular free Astro templates, perfect for SaaS, startup, and marketing websites.

## Source
- GitHub: https://github.com/onwidget/astrowind
- Stars: 5500+

## Quick Start
```bash
npm create astro@latest -- --template onwidget/astrowind
```

## Template Structure

```
astrowind/
├── public/
│   ├── favicon.svg
│   ├── images/
│   └── robots.txt
├── src/
│   ├── components/
│   │   ├── blog/
│   │   │   ├── FeaturedPosts.astro
│   │   │   └── Pagination.astro
│   │   ├── common/
│   │   │   ├── Analytics.astro
│   │   │   ├── Client.router.ts
│   │   │   ├── Footer.astro
│   │   │   └── Metadata.astro
│   │   ├── CustomStyles.astro
│   │   ├── FAQ.astro
│   │   ├── Features.astro
│   │   ├── Footer.astro
│   │   ├── Grid.astro
│   │   ├── HeadSEO.astro
│   │   ├── Header.astro
│   │   ├── Hero.astro
│   │   ├── Image.astro
│   │   ├── Logo.astro
│   │   ├── Navigation.astro
│   │   ├── Pagination.astro
│   │   ├── Pricing.astro
│   │   ├── Testimonials.astro
│   │   └── stats/
│   │       ├── About.astro
│   │       ├── Contact.astro
│   │       ├── Cta.astro
│   │       ├── Hero.astro
│   │       ├── Logos.astro
│   │       ├── Stats.astro
│   │       └── Team.astro
│   ├── content/
│   │   ├── blog/
│   │   │   ├── astro-is-dead-statements.md
│   │   │   ├── how-to-update-astro-5.md
│   │   │   └──...
│   │   ├── config.ts
│   │   └── pages.md
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   ├── blog/
│   │   │   ├── BlogArchiveList.astro
│   │   │   └── BlogPostComments.giscus
│   │   └── Layouts.ts
│   ├── pages/
│   │   ├── 404.astro
│   │   ├── blog/
│   │   │   ├── [...page].astro
│   │   │   ├── category/
│   │   │   │   └── [...slug].astro
│   │   │   └── index.astro
│   │   ├── index.astro
│   │   ├── landing/
│   │   │   └── multi-tenant.astro
│   │   └── [...all].astro
│   ├── styles/
│   │   └── global.css
│   └── utils/
│       ├── common.ts
│       └── utils.ts
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
└── tsconfig.json
```

## Key Sections

### Landing Page (src/pages/index.astro)
Sections included:
- **Header** - Navigation with logo, nav links, mobile menu
- **Hero** - Large headline, subtext, CTA buttons, illustration
- **Logos** - Company/tech logos (SVG)
- **Features** - 3-6 feature cards with icons
- **Stats** - Metrics/numbers
- **Testimonials** - Customer quotes
- **Pricing** - Pricing tiers
- **FAQ** - Accordion questions
- **CTA** - Call to action
- **Footer** - Links, copyright

### Blog Page (src/pages/blog/)
- Blog post listing
- Category pages
- Tag pages
- Pagination
- RSS feed

## Tailwind Integration
Using Tailwind CSS v3 with custom:
- **Typography** - Prose plugin
- **Forms** - Forms plugin  
- **Aspect ratio** - For images
- **Container queries** - CSS

## Brand Customization

### Colors (tailwind.config.mjs)
```javascript
const colors = {
  // Primary brand color
  primary: {
    50: '#eff6ff',
    100: '#dbeafe',
    200: '#bfdbfe',
    300: '#93c5fd',
    400: '#60a5fa',
    500: '#3b82f6',
    600: '#2563eb',
    700: '#1d4ed8',
    800: '#1e40af',
    900: '#1e3a8a',
    950: '#172554',
  },
};
```

### Fonts
- **Headings**: Outfit (Google Fonts)
- **Body**: Public Sans (Google Fonts)
- **Code**: Fira Code (Google Fonts)

## Responsive Breakpoints
- **sm** - Mobile landscape
- **md** - Tablet portrait
- **lg** - Tablet landscape
- **xl** - Desktop
- **2xl** - Large desktop

## Image Placeholders
Using picsum.photos:
- Hero: `https://picsum.photos/seed/hero/1200x600`
- Blog: `https://picsum.photos/seed/blog/800x400`
- Portfolio: `https://picsum.photos/seed/portfolio/600x400`

## Logo Placeholders
Using logoipsum.com:
- Light: `https://logoipsum.com/assets/logo/logoipsum-light.svg`
- Dark: `https://logoipsum.com/assets/logo/logoipsum.svg`

## Design System Application

### Applying a Design Personality

**To apply Swiss personality to this template:**
```css
/* Add to global.css */
:root {
  --font-heading: 'Syne', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --color-primary: #000000;
  --color-accent: #FF4D00;
  --color-background: #FFFFFF;
}
```

**To apply Tech Noir personality:**
```css
[data-personality="tech-noir"] {
  --font-heading: 'Syne', sans-serif;
  --color-primary: #00D9FF;
  --color-accent: #6B00FF;
  --color-background: #0A0A0A;
}
```

## License
MIT

## Demo
https://astrowind.vercel.app