"""
High‑level API for WLM‑World‑Generation‑Protocol.

This module exposes a single entry point:

    generate_world(spec) -> WorldGraph

MVP behavior:
    - Returns a deterministic world structure.
"""

from .seed_engine import generate_seed
from .region_engine import generate_regions
from .entity_engine import generate_entities
from .rule_engine import generate_rules
from .timeline_engine import generate_timeline
from .graph_builder import build_world_graph


def generate_world(spec: dict) -> dict:
    """
    Generate a world from a dimensional specification.

    Parameters
    ----------
    spec : dict
        World generation parameters (theme, scale, constraints, etc.)

    Returns
    -------
    dict
        WorldGraph structure.
    """
    seed = generate_seed(spec)
    regions = generate_regions(seed)
    entities = generate_entities(seed, regions)
    rules = generate_rules(seed, regions, entities)
    timeline = generate_timeline(seed, regions, entities, rules)
    graph = build_world_graph(seed, regions, entities, rules, timeline)

    return {
        "seed": seed,
        "regions": regions,
        "entities": entities,
        "rules": rules,
        "timeline": timeline,
        "world_graph": graph,
    }
