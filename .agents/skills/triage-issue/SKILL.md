---
name: triage-issue
description: Triage a bug or issue by exploring the codebase to find root cause, then create a GitHub issue with a TDD-based fix plan. Use when user reports a bug, wants to file an issue, mentions "triage", or wants to investigate and plan a fix for a problem.
---

# Triage Issue

Investigate a reported problem, find its root cause, and create a GitHub issue with a TDD fix plan.

## Process

### 1. Capture the problem

Get a brief description of the issue from the user.

### 2. Explore and diagnose

Use the Agent tool to investigate. Find:
- **Where** the bug manifests
- **What** code path is involved
- **Why** it fails (root cause)
- **What** related code exists

### 3. Identify the fix approach

- Minimal change needed to fix root cause
- Which modules/interfaces are affected
- What behaviors need verification via tests

### 4. Design TDD fix plan

Create ordered RED-GREEN cycles. Each cycle is one vertical slice:
- **RED**: Describe test capturing broken/missing behavior
- **GREEN**: Describe minimal code change

Rules:
- Tests verify behavior through public interfaces
- One test at a time
- Each test should survive internal refactors
- Include refactor step if needed

### 5. Create the GitHub issue

Use this template:
```
## Problem
[What happens, What should happen, How to reproduce]

## Root Cause Analysis
[Code path involved, Why current code fails, Contributing factors]

## TDD Fix Plan
1. RED: Write test that [description]
   GREEN: [Minimal change]
2. RED: Write test that [description]
   GREEN: [Minimal change]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] All new tests pass
- [ ] Existing tests still pass
```

After creating, print the issue URL and one-line summary.