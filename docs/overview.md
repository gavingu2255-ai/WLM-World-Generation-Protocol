# WLM‑World‑Generation‑Protocol — Overview  
**Dimensional structure → coherent worlds, environments, narratives, simulations**

The **WLM‑World‑Generation‑Protocol (WGP)** is the world‑construction layer of the WLM ecosystem.  
It uses dimensional structure to generate **consistent, navigable, simulation‑ready worlds**.

This is the **seventh major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. WLM‑Knowledge‑Engine — Structure → Knowledge  
6. WLM‑Metacognition‑Engine — Structure → Self‑Monitoring  
7. **WLM‑World‑Generation‑Protocol — Structure → Worlds**

It provides the missing link between **understanding** and **creation**:

> **Structure → World → Simulation → Narrative**

---

## Why this exists

Most world‑generation systems are:

- ad‑hoc  
- inconsistent  
- not grounded in physics or causality  
- unable to maintain coherence across time  
- unable to support agent‑based simulation  

The WLM‑World‑Generation‑Protocol solves this by generating worlds from **dimensional structure**, not from random sampling.

It produces:

- spatially coherent environments  
- temporally consistent timelines  
- physically grounded interactions  
- causally valid world logic  
- identity‑consistent characters  
- stable narrative arcs  

This is **world generation as a protocol**, not as a prompt.

---

## What this engine does

Given a world specification, it produces:

- **seed** — normalized structural parameters  
- **regions** — spatial topology  
- **entities** — objects, agents, resources  
- **rules** — physical and causal laws  
- **timeline** — events and eras  
- **world_graph** — simulation‑ready world structure  

The output is a deterministic **WorldGraph** object.

---

## Architecture

```
Spec
  ↓
Seed Engine
  ↓
Region Engine
  ↓
Entity Engine
  ↓
Rule Engine
  ↓
Timeline Engine
  ↓
World Graph Builder
  ↓
WorldGraph
```

Each module is isolated, testable, and extensible.

---

## Design principles

- **Deterministic** — same seed → same world  
- **Interpretable** — explicit regions, entities, rules  
- **Modular** — each engine evolves independently  
- **Dimension‑aligned** — grounded in spatial/temporal/physical/causal structure  
- **Expandable** — supports richer semantics in future phases  

---

## Status

MVP architecture complete.  
Spatial/temporal/causal world generation planned for Phase 2.

See `docs/roadmap.md` for upcoming milestones.
