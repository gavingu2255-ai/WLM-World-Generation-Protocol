"""
seed_engine.py — Convert world spec into a structural seed.

MVP behavior:
    - Normalize input spec.
    - Provide deterministic placeholders.
"""

def generate_seed(spec: dict):
    """
    Generate a structural seed from the world specification.

    Returns
    -------
    dict
        Seed structure.
    """
    return {
        "theme": spec.get("theme", "generic"),
        "scale": spec.get("scale", "medium"),
        "constraints": spec.get("constraints", []),
    }
