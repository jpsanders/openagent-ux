# Architecture - Folder Structure & Data Organization

## Overview
This document defines the standard folder structure and data patterns for all WebForge projects.

---

## Root Structure

```
project/
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── public/
│   ├── fonts/               # Self-hosted fonts
│   ├── images/              # Static images
│   └── favicon.ico
├── src/
│   ├── app/                 # Next.js App Router
│   ├── components/          # React components
│   ├── design-system/       # Design tokens & base components
│   ├── hooks/               # Custom hooks
│   ├── lib/                 # Utilities
│   └── types/               # TypeScript types
├── .env.local               # Local environment
├── .eslintrc.json           # ESLint config
├── .prettierrc              # Prettier config
├── next.config.js           # Next.js config
├── package.json
├── tailwind.config.ts       # Tailwind config
└── tsconfig.json            # TypeScript config
```

---

## App Router Structure

```
src/app/
├── layout.tsx               # Root layout
├── page.tsx                 # Home page
├── globals.css              # Global styles
├── favicon.ico
├── (marketing)/             # Route group
│   ├── about/
│   │   └── page.tsx
│   ├── pricing/
│   │   └── page.tsx
│   └── contact/
│       └── page.tsx
├── (app)/                   # Authenticated routes
│   ├── dashboard/
│   │   └── page.tsx
│   └── settings/
│       └── page.tsx
├── api/
│   ├── auth/[...nextauth]/
│   │   └── route.ts
│   └── health/
│       └── route.ts
└── not-found.tsx
```

---

## Components Structure

```
src/components/
├── ui/                      # Design system components
│   ├── button.tsx
│   ├── input.tsx
│   ├── card.tsx
│   ├── badge.tsx
│   ├── avatar.tsx
│   ├── toggle.tsx
│   ├── select.tsx
│   ├── modal.tsx
│   ├── toast.tsx
│   └── index.ts             # Barrel export
├── layout/
│   ├── header.tsx
│   ├── footer.tsx
│   ├── sidebar.tsx
│   └── container.tsx
├── forms/
│   ├── login-form.tsx
│   ├── contact-form.tsx
│   └── search-form.tsx
├── features/
│   ├── hero/
│   ├── pricing-table/
│   ├── testimonials/
│   └── blog-card/
└── index.ts
```

---

## Design System Structure

```
src/design-system/
├── tokens/
│   ├── colors.json
│   ├── typography.json
│   └── spacing.json
├── styles/
│   ├── tokens.css           # CSS custom properties
│   ├── typography.css
│   └── animations.css
├── components/              # Base components (internal)
│   ├── button.tsx
│   └── input.tsx
└── index.ts
```

---

## Library & Utils

```
src/lib/
├── utils.ts                 # cn() className merger
├── constants.ts             # App constants
├── db.ts                   # Database client
├── auth.ts                 # Auth config
├── storage.ts              # File storage
└── validators.ts           # Zod schemas
```

---

## Data Patterns

### Design Tokens (JSON)
```json
{
  "colors": {
    "background": {
      "DEFAULT": "#ffffff",
      "subtle": "#f8fafc"
    },
    "surface": {
      "DEFAULT": "#ffffff",
      "elevated": "#f1f5f9"
    }
  }
}
```

### Type Definitions
```typescript
// types/index.ts
export interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost' | 'destructive'
  size: 'sm' | 'md' | 'lg'
  loading?: boolean
  disabled?: boolean
  children: React.ReactNode
}

export interface CardProps {
  children: React.ReactNode
  variant?: 'default' | 'interactive' | 'selected'
  className?: string
}
```

---

## Environment Variables

### Required
```bash
NEXT_PUBLIC_API_URL=http://localhost:3000
DATABASE_URL=postgresql://...
```

### Optional
```bash
NEXTAUTH_SECRET=...
NEXTAUTH_URL=http://localhost:3000
NEXT_PUBLIC_ANALYTICS_ID=...
SENTRY_DSN=...
```

---

## Import Conventions

```typescript
// Design system
import { Button, Card, Input } from '@/components/ui'
import { colors, typography, spacing } from '@/design-system'

// Utils
import { cn } from '@/lib/utils'
import { db } from '@/lib/db'

// Types
import type { ButtonProps } from '@/types'
```

---

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `HeroSection.tsx` |
| Hooks | camelCase with `use` | `useAuth.ts` |
| Utils | camelCase | `formatDate.ts` |
| Types | PascalCase | `UserProfile.ts` |
| Constants | SCREAMING_SNAKE | `MAX_FILE_SIZE` |
| CSS Variables | kebab-case | `--color-brand` |

---

## File Size Guidelines

- **Components**: < 200 lines preferred
- **Utils**: < 100 lines preferred
- **Types**: No limit, but keep focused
- If a file exceeds guidelines, split into smaller modules
