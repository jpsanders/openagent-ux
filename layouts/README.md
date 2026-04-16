# OpenAgent UX Layouts

Pre-built page structures ready to combine with any design system.

## Available Layouts

### 1. Landing Page (`landing/`)
**Purpose**: High-conversion landing pages

**Sections**:
- Fixed navigation with logo, links, CTA
- Hero with title, subtitle, dual CTAs
- 3-column feature cards
- Social proof logo grid
- CTA section
- Multi-column footer

**Use for**: Marketing pages, product launches,SaaS homepages

### 2. Dashboard (`dashboard/`)
**Purpose**: Admin dashboards and web applications

**Sections**:
- Fixed sidebar with nav sections
- Sticky top bar with title + actions
- 4-column stats cards
- 2-column content area (table + activity)
- Responsive collapse for mobile

**Use for**: Admin panels, analytics, user dashboards

### 3. Blog/Content (`blog/`)
**Purpose**: Content-focused publishing

**Sections**:
- Standard navigation
- Featured article (image + full content)
- Article list (thumbnail + excerpt)
- Sidebar with categories + newsletter signup
- Footer

**Use for**: Blogs, news sites, magazine, documentation

## Usage

Each layout includes:
- **styles.css**: All structural styles using design system tokens
- Classes follow BEM-like naming: `.layout-{name}-{component}`

### Combining with Design Systems

```html
<!-- Step 1: Import design system tokens -->
<link rel="stylesheet" href="../design-systems/swiss/tokens.css">

<!-- Step 2: Import layout styles -->
<link rel="stylesheet" href="../layouts/landing/styles.css">

<!-- Step 3: Set personality on root -->
<html data-personality="swiss">

<!-- Step 4: Apply layout class -->
<body class="layout-landing">
```

## Responsive Behavior

| Layout | Desktop | Tablet | Mobile |
|--------|---------|--------|--------|
| Landing | Full 3-col features | 2-col features | Single column, hidden nav |
| Dashboard | Fixed sidebar | Collapsed sidebar | Hidden sidebar, hamburger |
| Blog | Sidebar visible | Sidebar below | Single column |

## Extending Layouts

Add custom sections by using the design token spacing:

```css
.my-custom-section {
  padding: var(--space-8) var(--container-padding);
  background: var(--color-surface);
}
```

## Class Reference

### Landing
- `.layout-landing` - Root container
- `.nav`, `.nav-inner`, `.nav-links`, `.nav-link`, `.nav-logo`, `.nav-cta`
- `.hero`, `.hero-inner`, `.hero-title`, `.hero-subtitle`, `.hero-cta-group`, `.hero-cta-primary`, `.hero-cta-secondary`
- `.features`, `.features-inner`, `.features-header`, `.features-title`, `.features-grid`, `.feature-card`
- `.social-proof`, `.logos`, `.logo-item`
- `.cta-section`, `.cta-section-inner`
- `.footer`, `.footer-inner`, `.footer-col-title`, `.footer-links`

### Dashboard
- `.layout-dashboard` - Root container with flex
- `.sidebar`, `.sidebar-header`, `.sidebar-logo`, `.sidebar-nav`, `.sidebar-section`, `.sidebar-link`
- `.main-content`, `.topbar`, `.topbar-left`, `.topbar-title`, `.topbar-right`
- `.stats-grid`, `.stat-card`, `.stat-label`, `.stat-value`, `.stat-change`
- `.dashboard-grid`, `.card`, `.card-header`, `.card-title`, `.card-body`
- `.table`, `.activity-list`, `.activity-item`, `.activity-icon`, `.activity-content`

### Blog
- `.layout-blog` - Root container
- `.main-layout` - Grid for content + sidebar
- `.articles`, `.featured-article`, `.featured-image`, `.featured-content`
- `.article`, `.article-image`, `.article-title`, `.article-category`, `.article-meta`, `.article-excerpt`
- `.sidebar`, `.sidebar-section`, `.sidebar-title`, `.categories`, `.category-item`
- `.newsletter`, `.newsletter-form`, `.newsletter-input`, `.newsletter-button`