# Example: Simple World  
**Spec → Seed → WorldGraph**

This example shows how a minimal world specification becomes a structured world graph.

---

## Input

```json
{
  "theme": "ancient ruins",
  "scale": "small"
}
```

---

## Code

```python
from wlm_world_generation_protocol import generate_world

world = generate_world({
    "theme": "ancient ruins",
    "scale": "small"
})

print(world)
```

---

## Output (MVP)

```
{
  "seed": {
    "theme": "ancient ruins",
    "scale": "small",
    "constraints": []
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
      "theme": "ancient ruins",
      "scale": "small",
      "constraints": []
    }
  }
}
```

---

## Explanation

In the MVP:

- **Seed** is normalized  
- **Regions / Entities / Rules / Timeline** are empty  
- **WorldGraph** contains nodes only  

Future versions will generate:

- spatial ruins topology  
- ancient artifacts  
- environmental hazards  
- historical timeline of the ruins  
