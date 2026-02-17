# Example: Causal World  
**Spec → Rules → (Future) Causal Structure**

This example shows how the engine handles a world with causal constraints.

---

## Input

```json
{
  "theme": "volcanic island",
  "constraints": ["coherent physics", "no magic"]
}
```

---

## Code

```python
from wlm_world_generation_protocol import generate_world

world = generate_world({
    "theme": "volcanic island",
    "constraints": ["coherent physics", "no magic"]
})

print(world)
```

---

## Output (MVP)

```
{
  "seed": {
    "theme": "volcanic island",
    "scale": "medium",
    "constraints": ["coherent physics", "no magic"]
  },
  "regions": [],
  "entities": [],
  "rules": [],
  "timeline": [],
  "world_graph": {
    "nodes": [],
    "edges": [],
    "rules": [],
    "timeline": [],
    "seed": {
      "theme": "volcanic island",
      "scale": "medium",
      "constraints": ["coherent physics", "no magic"]
    }
  }
}
```

---

## Explanation

In the MVP:

- **Rules** are empty  
- **Causal structure** is not yet generated  

Future versions will infer:

- volcanic activity cycles  
- heat zones and safe zones  
- eruption‑driven causal chains  
- resource scarcity dynamics  
