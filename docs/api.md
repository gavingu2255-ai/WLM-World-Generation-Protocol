# API Specification — WLM‑World‑Generation‑Protocol  
**Public API for generating dimensional worlds**

This document defines the official API surface for WLM‑World‑Generation‑Protocol.

The API is intentionally minimal, deterministic, and stable.

---

# 1. High‑Level API

The primary entry point is:

```python
generate_world(spec) -> dict
```

### Description
Generate a world from a dimensional specification.

### Signature

```python
def generate_world(spec: dict) -> dict:
    """
    Generate a world from a dimensional specification.
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `spec` | `dict` | World generation parameters |

### Returns

| Type | Description |
|------|-------------|
| `dict` | WorldGraph structure |

---

# 2. WorldGraph Structure

```json
{
  "seed": {},
  "regions": [],
  "entities": [],
  "rules": [],
  "timeline": [],
  "world_graph": {}
}
```

---

# 3. CLI API

The library provides a command‑line interface:

```
wlm-worldgen generate <spec>
```

### Usage

```
wlm-worldgen generate '{"theme": "ruins"}'
wlm-worldgen generate spec.json
wlm-worldgen generate spec.json --out world.json
```

---

# 4. Error Handling

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial worlds  

---

# 5. Versioning

Semantic versioning:

- `0.x` — experimental  
- `1.x` — spatial/temporal/causal world generation  
- `2.x` — narrative engine + simulation‑ready worlds  

---

# 6. Summary

The WLM‑World‑Generation‑Protocol exposes a single stable entry point:

```
generate_world(spec) → WorldGraph
```

This enables structured, deterministic, simulation‑ready world generation.
