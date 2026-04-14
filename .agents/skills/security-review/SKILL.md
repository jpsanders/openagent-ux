---
name: security-review
description: Use when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment features. Provides comprehensive security checklist and patterns.
---

# Security Review Skill

## When to Activate
- Implementing authentication or authorization
- Handling user input or file uploads
- Creating new API endpoints
- Working with credentials
- Payment features

## Security Checklist

### 1. Secrets Management
NEVER: Hardcode secrets in source
ALWAYS: Use environment variables
```typescript
const apiKey = process.env.OPENAI_API_KEY
if (!apiKey) throw new Error('API key not configured')
```

Verify:
- [ ] No hardcoded API keys/tokens/passwords
- [ ] All secrets in env vars
- [ ] .env.local in .gitignore
- [ ] No secrets in git history

### 2. Input Validation
Validate all user input with Zod:
```typescript
const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100)
})
```

Verify:
- [ ] All user inputs validated
- [ ] File uploads restricted (size, type)
- [ ] No direct user input in queries
- [ ] Whitelist validation (not blacklist)

### 3. SQL Injection Prevention
NEVER concatenate SQL:
```typescript
// DANGEROUS
const query = `SELECT * FROM users WHERE email = '${email}'`
```
ALWAYS use parameterized:
```typescript
const { data } = await supabase
  .from('users')
  .select('*')
  .eq('email', email)
```

### 4. Authentication & Authorization
Store tokens in httpOnly cookies, NOT localStorage:
```typescript
res.setHeader('Set-Cookie', 
  `token=${token}; HttpOnly; Secure; SameSite=Strict`)
```

### 5. XSS Prevention
Sanitize user HTML:
```typescript
import DOMPurify from 'isomorphic-dompurify'
const clean = DOMPurify.sanitize(html)
```

### 6. Rate Limiting
```typescript
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
})
```

## Pre-Deployment Checklist

- [ ] No hardcoded secrets
- [ ] All inputs validated
- [ ] SQL queries parameterized
- [ ] User content sanitized
- [ ] CSRF protection enabled
- [ ] Tokens in httpOnly cookies
- [ ] Rate limiting on endpoints
- [ ] Dependencies up to date