---
name: qa
description: Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".
---

# QA Session

Run an interactive QA session. User describes problems. You clarify, explore, and file GitHub issues that are durable and user-focused.

## For each issue

### 1. Listen and lightly clarify

At most 2-3 short questions focused on:
- What they expected vs what actually happened
- Steps to reproduce

### 2. Explore the codebase

While talking, explore relevant area to learn:
- Domain language used
- What the feature is supposed to do
- User-facing behavior boundary

### 3. Assess scope

Single issue or breakdown? Break down when:
- Fix spans multiple independent areas
- Clearly separable concerns
- Multiple distinct failure modes

### 4. File GitHub issue(s)

Issues must be durable - still make sense after major refactors.

Template:
```
## What happened
[Describe actual behavior]

## What I expected
[Describe expected behavior]

## Steps to reproduce
1. [Concrete numbered steps]
2. [Use domain terms]
3. [Include relevant inputs]

## Additional context
[Any helpful observations]
```

After filing, print URL and ask "Next issue, or done?"