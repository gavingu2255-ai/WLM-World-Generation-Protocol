"""
graph_builder.py — Build a structured world graph.

MVP behavior:
    - Wraps regions, entities, rules, and timeline into a graph dict.
"""

def build_world_graph(seed, regions, entities, rules, timeline):
    """
    Build a world graph structure.

    Returns
    -------
    dict
        Graph structure.
    """
    return {
        "nodes": regions + entities,
        "edges": [],
        "rules": rules,
        "timeline": timeline,
        "seed": seed,
    }
