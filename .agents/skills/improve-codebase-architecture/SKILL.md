---
name: improve-codebase-architecture
description: Explore a codebase to find opportunities for architectural improvement, focusing on making the codebase more testable by deepening shallow modules. Use when user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more AI-navigable.
---

# Improve Codebase Architecture

Explore a codebase like an AI would, surface architectural friction, discover opportunities for improving testability, and propose module-deepening refactors.

A **deep module** has a small interface hiding a large implementation. Deep modules are more testable and let you test at the boundary instead of inside.

## Process

### 1. Explore the codebase

Navigate organically. Note where you experience friction:
- Where does understanding one concept require bouncing between many small files?
- Where are modules so shallow that the interface is nearly as complex as the implementation?
- Where have pure functions been extracted just for testability?
- Where do tightly-coupled modules create integration risk?

### 2. Present candidates

For each candidate, show:
- **Cluster**: Which modules/concepts are involved
- **Why they're coupled**
- **Dependency category**
- **Test impact**

### 3. User picks a candidate

### 4. Frame the problem space

Write a user-facing explanation:
- Constraints any new interface would need
- Dependencies it would need
- Rough illustrative code sketch

### 5. Design multiple interfaces

Spawn 3+ sub-agents in parallel. Each with different constraint:
- Agent 1: "Minimize the interface — 1-3 entry points max"
- Agent 2: "Maximize flexibility"
- Agent 3: "Optimize for the most common caller"

Each outputs:
1. Interface signature
2. Usage example
3. What complexity it hides
4. Trade-offs

### 6. User picks an interface

### 7. Create GitHub issue

Create refactor RFC as GitHub issue.