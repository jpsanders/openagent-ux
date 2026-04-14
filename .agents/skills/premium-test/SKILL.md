---
name: premium-test
description: >-
  Run test suite with unit, e2e, visual regression, and accessibility tests.
  Triggers on: "/test", "run tests", "test coverage", "e2e", "visual test".
  Requires: Vitest + Playwright configured.
---

# Premium Test Command

## Syntax

```
/test unit         - Run Vitest unit tests
/test e2e         - Run Playwright E2E tests
/test visual      - Run visual regression tests
/test a11y       - Run accessibility audit
/test all        - Full test suite
/test coverage    - Generate coverage report
```

## Test Structure

```
tests/
├── unit/              # Vitest
│   ├── components/
│   ├── lib/
│   └── hooks/
├── e2e/              # Playwright
│   ├── critical-path/
│   ├── auth/
│   └── forms/
└── visual/            # Screenshot comparison
```

## Unit Tests (Vitest)

### Component Test
```typescript
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Button } from './Button'

describe('Button', () => {
  it('renders with children', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByRole('button')).toHaveTextContent('Click me')
  })

  it('handles click', async () => {
    const user = userEvent.setup()
    const onClick = vi.fn()
    render(<Button onClick={onClick}>Click me</Button>)
    
    await user.click(screen.getByRole('button'))
    expect(onClick).toHaveBeenCalled()
  })

  it('shows loading state', () => {
    render(<Button loading>Loading</Button>)
    expect(screen.getByRole('button')).toBeDisabled()
  })

  it('is accessible by keyboard', async () => {
    const user = userEvent.setup()
    render(<Button>Keyboard</Button>)
    
    await user.keyboard('{Tab}')
    expect(screen.getByRole('button')).toHaveFocus()
  })
})
```

### Hook Test
```typescript
import { renderHook, act } from '@vitest/react'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('initializes at 0', () => {
    const { result } = renderHook(() => useCounter())
    expect(result.current.count).toBe(0)
  })

  it('increments', () => {
    const { result } = renderHook(() => useCounter())
    
    act(() => result.current.increment())
    expect(result.current.count).toBe(1)
  })
})
```

## E2E Tests (Playwright)

### Critical Path Test
```typescript
import { test, expect } from '@playwright/test'

test.describe('Authentication', () => {
  test('user can sign up', async ({ page }) => {
    await page.goto('/signup')
    
    await page.fill('[name="email"]', 'test@example.com')
    await page.fill('[name="password"]', 'SecurePass123!')
    await page.click('[type="submit"]')
    
    await expect(page).toHaveURL('/dashboard')
    await expect(page.locator('[data-user-email]')).toHaveText('test@example.com')
  })

  test('invalid email shows error', async ({ page }) => {
    await page.goto('/signup')
    
    await page.fill('[name="email"]', 'invalid-email')
    await page.click('[type="submit"]')
    
    await expect(page.locator('[data-error]')).toBeVisible()
    await expect(page.locator('[data-error]')).toContainText('valid email')
  })
})
```

### Page Object Pattern
```typescript
// tests/e2e/pages/Dashboard.ts
export class DashboardPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/dashboard')
  }

  async getUserEmail() {
    return this.page.locator('[data-user-email]')
  }

  async logout() {
    await this.page.click('[data-logout-btn]')
  }
}

// Usage
test('dashboard shows user', async ({ page }) => {
  const dashboard = new DashboardPage(page)
  await dashboard.goto()
  await expect(dashboard.getUserEmail()).toBeVisible()
})
```

## Visual Regression

### Screenshot Test
```typescript
import { test, expect } from '@playwright/test'

test('homepage matches design', async ({ page }) => {
  await page.goto('/')
  await page.waitForLoadState('networkidle')
  
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    maxDiffPixelRatio: 0.02,  // 2% tolerance
  })
})

test('button states render correctly', async ({ page }) => {
  await page.goto('/components/button')
  
  // Default
  await expect(page.locator('#default')).toMatchScreenshot('btn-default.png')
  
  // Hover
  await page.locator('#default').hover()
  await expect(page.locator('#default')).toMatchScreenshot('btn-hover.png')
})
```

## Accessibility Testing

### Axe Integration
```typescript
import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

test('homepage has no accessibility violations', async ({ page }) => {
  await page.goto('/')
  
  const accessibilityScanner = new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
  
  const results = await accessibilityScanner.analyze()
  
  expect(results.violations).toEqual([])
})
```

### Keyboard Navigation
```typescript
test('full keyboard navigation works', async ({ page }) => {
  await page.goto('/')
  
  // Tab through page
  const steps = await page.keyboard.board({
    from: page.locator('body'),
    to: page.locator('[data-last-focusable]'),
  })
  
  // Verify no traps (more than basic tab works)
  expect(steps.length).toBeGreaterThan(5)
})
```

## Test Commands

### Run Unit Tests
```bash
npm run test          # vitest run
npm run test:watch  # vitest --watch
npm run test:ui     # vitest --ui
```

### Run E2E Tests
```bash
npm run test:e2e           # playwright test
npm run test:e2e:ui      # playwright test --ui
npm run test:e2e:debug    # playwright test --debug
```

### Run Visual Tests
```bash
npm run test:visual       # Only visual tests
npm run test:visual:update # Update baselines
```

### Run With Coverage
```bash
npm run test:coverage     # vitest --coverage
```

## Quality Gates

| Test Type | Coverage Target | Time Target |
|-----------|--------------|------------|
| Unit | 80%+ | < 30s |
| E2E (Critical) | Core flows | < 60s |
| Visual | Key pages | < 30s |
| A11y | All pages | < 30s |

## CI Integration

```yaml
# .github/workflows/test.yml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      
      - run: npm ci
      - run: npm run test:unit
      - run: npm run test:e2e
      - run: npm run test:coverage
```

## Interactive States Test Checklist

For all interactive components:
- [ ] Renders default state
- [ ] Hover state works
- [ ] Active/press state works
- [ ] Focus state visible (keyboard)
- [ ] Disabled state prevents action
- [ ] Loading state shows feedback
- [ ] Error state displays message
- [ ] Empty state designed