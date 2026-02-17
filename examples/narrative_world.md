# Example: Narrative World  
**Spec → Timeline → (Future) Narrative Engine**

This example shows how the engine handles a world with narrative potential.

---

## Input

```json
{
  "theme": "post-collapse city",
  "scale": "large"
}
```

---

## Code

```python
from wlm_world_generation_protocol import generate_world

world = generate_world({
    "theme": "post-collapse city",
    "scale": "large"
})

print(world)
```

---

## Output (MVP)

```
{
  "seed": {
    "theme": "post-collapse city",
    "scale": "large",
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
      "theme": "post-collapse city",
      "scale": "large",
      "constraints": []
    }
  }
}
```

---

## Explanation

In the MVP:

- **Timeline** is empty  
- **Narrative structure** is not yet generated  

Future versions will generate:

- collapse timeline  
- faction emergence  
- resource conflicts  
- long‑arc narrative structures  
