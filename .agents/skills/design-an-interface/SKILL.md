---
name: design-an-interface
description: Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice".
---

# Design an Interface

Based on "Design It Twice" from "A Philosophy of Software Design": your first idea is unlikely to be the best. Generate multiple radically different designs, then compare.

## Workflow

### 1. Gather Requirements

Before designing, understand:
- [ ] What problem does this module solve?
- [ ] Who are the callers?
- [ ] What are the key operations?
- [ ] Any constraints?
- [ ] What should be hidden inside vs exposed?

### 2. Generate Designs (Parallel Sub-Agents)

Spawn 3+ sub-agents simultaneously. Each must produce a radically different approach.

Prompt each sub-agent:
```
Design an interface for: [module description]

Requirements: [gathered requirements]

Constraints for this design:
- Agent 1: "Minimize method count - aim for 1-3 methods max"
- Agent 2: "Maximize flexibility - support many use cases"
- Agent 3: "Optimize for the most common case"

Output:
1. Interface signature (types/methods)
2. Usage example
3. What this design hides internally
4. Trade-offs
```

### 3. Present Designs

Show each design with:
1. Interface signature
2. Usage examples
3. What it hides

### 4. Compare Designs

- **Interface simplicity**: fewer methods, simpler params
- **General-purpose vs specialized**
- **Implementation efficiency**
- **Depth**: small interface hiding significant complexity

### 5. Synthesize

Often the best design combines insights. Ask: "Which design best fits your primary use case?"

## Evaluation Criteria

**Interface simplicity**: Fewer methods, simpler params = easier to learn and use correctly.

**Depth**: Small interface hiding significant complexity = deep module (good). Large interface with thin implementation = shallow module (avoid).