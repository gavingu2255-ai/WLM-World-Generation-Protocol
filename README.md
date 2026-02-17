# WLM‑World‑Generation‑Protocol  
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
7. **WLM‑World‑Generation‑Protocol — Structure → Worlds** ← *this repo*

It provides the missing link between **understanding** and **creation**:

> **Structure → World → Simulation → Narrative**

---

## ✨ Why this exists

Most world‑generation systems are:

- ad‑hoc  
- inconsistent  
- non‑structural  
- not grounded in physics, causality, or identity  
- unable to maintain coherence across time  

The WLM‑World‑Generation‑Protocol fixes this by generating worlds from **dimensional structure**, not from random sampling.

It produces:

- spatially coherent environments  
- temporally consistent timelines  
- physically grounded interactions  
- causally valid world logic  
- identity‑consistent characters  
- stable narrative arcs  

This is **world generation as a protocol**, not as a prompt.

---

## ✨ Features

### **1. Dimensional World Templates**
Worlds are generated from four core dimensions:

- **Spatial** — maps, topology, regions, navigation  
- **Temporal** — timelines, eras, event sequences  
- **Physical** — forces, constraints, affordances  
- **Causal** — world logic, rules, consequences  

### **2. Entity & Region Generation**
Creates:

- regions  
- locations  
- objects  
- agents  
- factions  
- resources  

All grounded in dimensional structure.

### **3. Narrative Structure Engine**
Generates:

- arcs  
- quests  
- conflicts  
- resolutions  
- emergent storylines  

### **4. Simulation‑Ready Output**
Produces a world graph that can be used by:

- game engines  
- simulators  
- agent systems  
- narrative engines  
- multi‑agent environments  

### **5. Deterministic Protocol**
Same structure → same world.

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-world-generation-protocol
```

### **Use**

```python
from wlm_world_generation_protocol import generate_world

world = generate_world({
    "theme": "ancient ruins",
    "scale": "medium",
    "constraints": ["non-magical", "coherent physics"]
})

print(world)
```

### **Output (MVP)**

```
{
  "regions": [],
  "entities": [],
  "timeline": [],
  "rules": [],
  "world_graph": {}
}
```

---

## 🧠 How it works

The engine performs five steps:

### **1. Input → Structural Seed**
Themes, constraints, and parameters become dimensional structure.

### **2. Structure → Regions**
Spatial topology is generated.

### **3. Structure → Entities**
Objects, agents, and resources are instantiated.

### **4. Structure → Rules**
Causal and physical rules are applied.

### **5. Structure → World Graph**
A coherent, simulation‑ready world graph is produced.

---

## 📦 API

### `generate_world(spec: dict) → dict`

```python
def generate_world(spec: dict) -> dict:
    """
    Generate a world from a dimensional specification.
    """
```

### WorldGraph structure (MVP)

```json
{
  "regions": [],
  "entities": [],
  "timeline": [],
  "rules": [],
  "world_graph": {}
}
```

---

## 🏗 Repository Structure

```
wlm-world-generation-protocol/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_world_generation_protocol/
│       ├── __init__.py
│       ├── api.py
│       ├── seed_engine.py
│       ├── region_engine.py
│       ├── entity_engine.py
│       ├── rule_engine.py
│       ├── timeline_engine.py
│       ├── graph_builder.py
│       └── cli.py
│
├── examples/
│   ├── simple_world.md
│   ├── causal_world.md
│   └── narrative_world.md
│
├── tests/
│   ├── test_seed.py
│   ├── test_regions.py
│   ├── test_entities.py
│   ├── test_rules.py
│   ├── test_timeline.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── world-rules.md
    ├── api.md
    └── roadmap.md
```

---

## 📄 License

MIT License  
Copyright (c) 2026  
**Wujie Gu**

---

## 🧩 Summary

The **WLM‑World‑Generation‑Protocol** is the structural world‑generation layer of the WLM ecosystem.  
It turns dimensional structure into **coherent, simulation‑ready worlds**.

It enables:

- stable world generation  
- consistent physics  
- causal world logic  
- narrative coherence  
- agent‑ready environments  

A foundational component of the **WLM generative stack**.
