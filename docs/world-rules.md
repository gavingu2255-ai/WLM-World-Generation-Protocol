# World Rules — WLM‑World‑Generation‑Protocol  
**How structure becomes worlds, environments, and simulations**

This document defines the rules that convert a world specification into  
regions, entities, rules, timelines, and a world graph.

The rules are deterministic, structural, and model‑agnostic.

---

# 1. Seed Rules

The seed is the **structural root** of the world.

Examples:

- theme: “ancient ruins”  
- scale: “small / medium / large”  
- constraints: “non‑magical”, “coherent physics”  

### MVP behavior

- normalize input spec  
- fill missing fields with defaults  

Future versions will include:

- dimensional seed expansion  
- theme‑based structural templates  
- constraint‑driven world shaping  

---

# 2. Region Rules

Regions define **spatial topology**:

- areas  
- zones  
- biomes  
- rooms  
- sectors  

### MVP behavior

- no region generation yet  

Future versions will include:

- spatial graph generation  
- topology constraints  
- navigable region maps  

---

# 3. Entity Rules

Entities include:

- objects  
- agents  
- resources  
- structures  
- artifacts  

### MVP behavior

- no entity generation yet  

Future versions will include:

- entity templates  
- faction systems  
- resource networks  

---

# 4. Rule Rules (Physical & Causal)

Rules define:

- physics  
- causality  
- world logic  
- systemic interactions  

### MVP behavior

- no rule generation yet  

Future versions will include:

- causal propagation  
- physical constraints  
- systemic rule networks  

---

# 5. Timeline Rules

Timelines define:

- eras  
- events  
- transitions  
- world evolution  

### MVP behavior

- no timeline generation yet  

Future versions will include:

- event chains  
- causal timelines  
- narrative arcs  

---

# 6. World Graph Rules

The world graph represents:

- nodes = regions + entities  
- edges = spatial/causal/temporal links  
- rules = world logic  
- timeline = world evolution  

### MVP behavior

- nodes only  
- no edges  

---

# 7. Determinism

World generation must be:

- deterministic  
- reproducible  
- structurally grounded  
- consistent across runs  

Same seed → same world.

---

# 8. Future Extensions

- spatial topology generation  
- entity population  
- causal rule systems  
- timeline generation  
- narrative engine  
- simulation‑ready world graphs  
