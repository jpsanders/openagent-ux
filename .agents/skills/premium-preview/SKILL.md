---
name: premium-preview
description: >-
  Start dev server with performance audit and premium checks.
  Triggers on: "/preview", "start server", "dev server", "run dev", "preview mode".
  Opens: Local server with Lighthouse audit.
---

# Premium Preview Command

## Syntax

```
/preview              - Start dev server with audit
/preview [path]         - Preview specific page
/preview prod         - Production preview
/preview lighthouse   - Full Lighthouse audit
```

## Preview Features

### Dev Server with Extras

1. **Hot reload** - Instant updates
2. **Error overlay** - Clear error messages
3. **Dev tools** - React/Framer devtools

### Premium Additions

```bash
# Dev with premium features
npm run dev:audit    # Opens localhost with audit panel
npm run dev:perf    # Runtime performance tracking
npm run dev:audit --verbose
```

### Audit Panel

When running preview, shows:
- LCP (Largest Contentful Paint)
- FID/INP (First Input Delay / Interaction to Next Paint)
- CLS (Cumulative Layout Shift)
- TBT (Total Blocking Time)
- Bundle size

## Lighthouse Audit

### Quick Audit
```bash
npm run lighthouse    # All pages
npm run lighthouse --path=/homepage
```

### Full Audit
```bash
npx lighthouse http://localhost:3000 \
  --view \
  --preset=desktop \
  --throttling.cpuSlowdownMultiplier=2 \
  --emulatedFormFactor=desktop
```

### What to Check

#### Performance (Target: 90+)
- [ ] LCP < 2.5s
- [ ] INP < 200ms
- [ ] CLS < 0.1
- [ ] TBT < 200ms
- [ ] Bundle under 200KB initial

#### Accessibility (Target: 100)
- [ ] All images have alt
- [ ] Color contrast 4.5:1
- [ ] Focus visible
- [ ] Labels for forms
- [ ] Skip links

#### Best Practices (Target: 100)
- [ ] No console errors
- [ ] HTTPS (production)
- [ ] No vulnerable deps
- [ ] Modern formats (WebP)

#### SEO (Target: 100)
- [ ] Title tag
- [ ] Meta description
- [ ] Viewport meta
- [ ] H1 unique
- [ ] Crawlable

## Performance Profiling

### Bundle Analysis
```bash
npm run analyze    # Bundle analyzer
npm run profile   # React profiler
```

### Runtime Performance

```bash
# Performance traces
npm run perf:trace

# Memory leaks
npm run perf:memory
```

### Core Web Vitals

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | < 2.5s | 2.5s - 4s | > 4s |
| INP | < 200ms | 200ms - 500ms | > 500ms |
| CLS | < 0.1 | 0.1 - 0.25 | > 0.25 |

## Premium Device Testing

### Viewport Sizes
```
Mobile: 375x667 (iPhone SE)
Mobile Large: 414x896 (iPhone 11)
Tablet: 768x1024 (iPad)
Laptop: 1366x768
Desktop: 1920x1080
```

### Network Throttling
```bash
# Fast 3G
npm run dev:fast3g

# Slow 3G
npm run dev:slow3g
```

### Test Commands
```bash
# Mobile viewport
npm run preview:mobile

# Tablet viewport
npm run preview:tablet
```

## Output

### Preview Report

```
╔══════════════════════════════════════════╗
║         PREVIEW AUDIT               ║
╠═════════════════════════════════════╣
║ Performance:    ████████████ 95    ║
║ Accessibility: ████████████ 100   ║
║ Best Practices: ████████████ 100   ║
║ SEO:           ████████████ 100   ║
╠═════════════════════════════════════╣
║ LCP: 1.2s  ✓                       ║
║ INP: 45ms  ✓                       ║
║ CLS: 0.01  ✓                       ║
╚══════════════════════════════════════╝
```

## Quality Gates

Before marking preview complete:
- [ ] Performance score: 90+
- [ ] Accessibility score: 100
- [ ] No console errors
- [ ] Responsive at 320px, 768px, 1024px
- [ ] Touch targets tested
- [ ] Keyboard navigation works
- [ ] No layout shifts

## Common Fixes

### Slow LCP
- Optimize images (WebP, lazy load below fold)
- Font subsetting
- Code splitting
- CDN for static assets

### High INP
- Remove hydration
- Defer non-critical JS
- Optimize event handlers
- Use transition.js

### CLS
- Reserve space for images
- Font-display: swap fallback
- Skeleton for dynamic content