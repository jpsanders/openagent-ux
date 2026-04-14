---
name: ui-typography
description: >
  Professional typography rules for UI design, web applications, software interfaces, and all screen-based text. 
  Enforces timeless typographic correctness: proper quote marks, dashes, spacing, hierarchy, and layout.
  AUTO-APPLY when generating ANY HTML, CSS, React, JSX, or UI code containing visible text.
---

# UI Typography Skill

## Attribution
Based on **Matthew Butterick's Practical Typography** (practicaltypography.com)

## Mode of Operation
**ENFORCEMENT (default):** When generating ANY UI with visible text, apply every rule automatically. Do not ask permission. Just produce correct typography.

**AUDIT:** When reviewing existing code, identify violations and provide fixes.

## Characters

### Quotes and Apostrophes — Always Curly

Use `&ldquo;` `&rdquo;` for double, `&lsquo;` `&rsquo;` for single.

Apostrophes always point down — identical to closing single quote `&rsquo;`.

### Dashes and Hyphens — Three Distinct Characters

| Character | HTML | Use |
|-----------|------|-----|
| - (hyphen) | `-` | Compound words (cost-effective) |
| – (en dash) | `&ndash;` | Ranges (1–10), connections |
| — (em dash) | `&mdash;` | Sentence breaks |

### Ellipses
Use `&hellip;` (…), not three periods.

### Math Symbols
- `&times;` for multiplication
- `&minus;` for subtraction
- Foot/inch: `&#39;` and `&quot;` (STRAIGHT, not curly)

### Symbols
- Copyright: `&copy;` (not (c))
- Trademark: `&trade;` (not (TM))
- Registered: `&reg;` (not (R))
- Section: `&sect;` (§) followed by `&nbsp;`
- Paragraph: `&para;` (¶) followed by `&nbsp;`

## Spacing

### One Space After Punctuation
Exactly one space after any punctuation. Never two.

### Nonbreaking Spaces
Use `&nbsp;` before:
- Numeric refs: `&sect;&nbsp;42`, `Fig.&nbsp;3`
- Symbols: `&copy;&nbsp;2026`
- After initials: `J.&nbsp;S.` (never break)

### Word Spacing
- No space before `?`, `!`, `;`, `:` 
- Space AFTER:`;`, `:`, `?`, `!`
- Em dash: typically no space, use `&thinsp;` if crushed

## Type Scale

### Hierarchy (Web)
| Token | Size | Weight | Line Height | Use |
|------|------|--------|------------|-----|
| display | 48px+ | 700 | 1.1 | Hero headlines |
| h1 | 36px | 700 | 1.2 | Page titles |
| h2 | 28px | 600 | 1.3 | Section headers |
| h3 | 22px | 600 | 1.4 | Card titles |
| body | 16px | 400 | 1.6 | Content |
| small | 14px | 400 | 1.5 | Captions |
| tiny | 12px | 500 | 1.4 | Labels |

### Body Text Rules
- Minimum body: 16px for comfortable reading
- Line length: 45-75 characters optimal
- Line height: 1.4-1.6 for body text
- Paragraph spacing: 1em or 0.5em below

## Lists

### bullets
- Use bullet `•` (•) — NOT asterisk `*`
- OR hyphen `-` for compact lists
- Hanging indent for wraps

### Numbers
- Align on period or left edge
- Use `&nbsp;` between number and unit: `5&nbsp;%`

## UI-Specific Rules

### Buttons
- Sentence case (or title case for nav)
- No terminal punctuation in buttons
- 3-4 words maximum

### Forms
- Labels sentence case
- No colon after labels (unless split)
- Error messages: sentence case, no technical jargon

### Navigation
- Title case or sentence case (consistent)
- No terminal punctuation
- Abbreviate only if space critical

### Notifications
- Sentence case
- No exclamation (budget ONE per session)
- Be specific: "Save failed" not "Error!"

## Common Errors to Fix

### WRONG → CORRECT
- `"` → `&ldquo;` / `&rdquo;` (curly quotes)
- `'` → `&lsquo;` / `&rsquo;` (curly apostrophe)
- `...` → `&hellip;` (ellipsis)
- ` -- ` → ` &mdash; ` (em dash)
- `(c)` → `&copy;` (copyright)
- (TM) → `&trade;` (trademark)