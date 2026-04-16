# OpenAgent UX Design System

A modular, pick-and-mix design system for building premium websites.

## Structure

```
/
├── design-systems/          # Swappable design tokens
│   ├── swiss/              # Swiss International
│   ├── editorial/         # Warm Editorial
│   ├── tech-noir/          # Tech Noir
│   ├── playful/            # Playful
│   ├── minimal/            # Minimal
│   ├── contemporary/       # Contemporary
│   ├── custom/             # Custom overrides
│   ├── index.css          # Main entry point
│   └── config.json        # Design system config
│
├── layouts/                # Pre-built page shells
│   ├── landing/           # Landing page layout
│   ├── dashboard/         # Dashboard layout
│   └── blog/              # Blog/content layout
│
└── example-app/            # Demo application
```

## Design Systems

### 6 Personality Presets

| Personality | Description | Best For |
|-------------|-------------|----------|
| **Swiss** | Grid-focused, precision, high contrast | Fintech, Enterprise, Dashboards |
| **Editorial** | Sophisticated, curated, timeless | Publishing, Luxury, Content |
| **Tech Noir** | Dark, technical, cutting-edge | Developer tools, Web3, APIs |
| **Playful** | Friendly, energetic, bouncy | Consumer apps, Games, Social |
| **Minimal** | Essential, reductionist, gallery-quality | Agencies, Portfolios, Architecture |
| **Contemporary** | Bold, expressive, design-forward | Creative agencies, Design studios |

### CSS Variables

Each design system includes:
- **Typography**: heading, body, mono fonts + scale
- **Colors**: primary, secondary, accent, semantic
- **Spacing**: 4px base scale (0-24)
- **Border Radius**: sm, md, lg, xl, full
- **Shadows**: sm, md, lg, xl
- **Transitions**: fast, base, slow, slower
- **Layout**: max-widths, container-padding, grid-gap

### Custom Overrides

Use `design-systems/custom/tokens.css` to add your own:
- Custom brand colors
- Custom typography
- Custom spacing
- Dark/light mode
- High contrast mode
- Reduced motion (accessibility)

## Layouts

### 1. Landing Page
- Fixed navigation
- Hero with CTAs
- 3-column feature cards
- Social proof logos
- CTA section
- Multi-column footer

### 2. Dashboard
- Fixed sidebar navigation
- Top bar with title + actions
- 4-column stats grid
- 2-column content (table + activity)
- Responsive breakpoints

### 3. Blog/Content
- Standard navigation
- Featured article (image + content)
- Article list (image + excerpt)
- Sidebar with categories + newsletter
- Footer

## Usage

### Quick Start

1. **Choose a layout** from `/layouts/`
2. **Choose a design system** from `/design-systems/`
3. **Apply personality** by adding `data-personality` to your root:

```html
<html data-personality="swiss">
  <head>
    <link rel="stylesheet" href="/design-systems/swiss/tokens.css">
    <link rel="stylesheet" href="/layouts/landing/styles.css">
  </head>
  <body>
    <!-- Your content -->
  </body>
</html>
```

### Example: Landing with Swiss Design

```html
<html data-personality="swiss">
  <head>
    <link rel="stylesheet" href="./design-systems/swiss/tokens.css">
    <link rel="stylesheet" href="./layouts/landing/styles.css">
  </head>
  <body class="layout-landing">
    <nav class="nav">
      <div class="nav-inner">
        <a href="/" class="nav-logo">MyBrand</a>
        <ul class="nav-links">
          <li><a href="#" class="nav-link">Features</a></li>
          <li><a href="#" class="nav-link">Pricing</a></li>
        </ul>
        <button class="nav-cta">Get Started</button>
      </div>
    </nav>
    
    <section class="hero">
      <div class="hero-inner">
        <h1 class="hero-title">Build Something Amazing</h1>
        <p class="hero-subtitle">The modern way to build websites</p>
        <div class="hero-cta-group">
          <button class="hero-cta-primary">Start Free</button>
          <button class="hero-cta-secondary">Learn More</button>
        </div>
      </div>
    </section>
  </body>
</html>
```

### Switching Design Systems

Simply change the CSS import and data attribute:

```html
<!-- Swiss -->
<html data-personality="swiss">
  <link rel="stylesheet" href="./design-systems/swiss/tokens.css">

<!-- Tech Noir -->
<html data-personality="tech-noir">
  <link rel="stylesheet" href="./design-systems/tech-noir/tokens.css">

<!-- Custom -->
<html data-custom-color data-style="--custom-primary: #FF0000;">
```

### Adding Custom Tokens

In `design-systems/custom/tokens.css`:

```css
:root {
  /* Custom brand colors */
  --custom-primary: #FF0000;
  --custom-accent: #00FF00;
  
  /* Custom fonts */
  --custom-heading: 'Your Font', sans-serif;
  --custom-body: 'Your Font', sans-serif;
  
  /* Custom spacing */
  --custom-space-4: 1.5rem;
}
```

## Component Mapping

| Layout Component | CSS Class |
|-----------------|-----------|
| Navigation | `.nav`, `.nav-inner`, `.nav-links`, `.nav-link`, `.nav-logo`, `.nav-cta` |
| Hero | `.hero`, `.hero-inner`, `.hero-title`, `.hero-subtitle`, `.hero-cta-group` |
| Features | `.features`, `.features-grid`, `.feature-card`, `.feature-icon` |
| Footer | `.footer`, `.footer-inner`, `.footer-col-title`, `.footer-links` |
| Sidebar | `.sidebar`, `.sidebar-nav`, `.sidebar-link`, `.sidebar-section` |
| Cards | `.card`, `.card-header`, `.card-title`, `.card-body` |
| Tables | `.table`, `.table th`, `.table td` |

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Supports CSS custom properties

## Accessibility

- Reduced motion support via `prefers-reduced-motion`
- High contrast mode via `data-contrast="high"`
- Semantic HTML structure
- Keyboard navigable