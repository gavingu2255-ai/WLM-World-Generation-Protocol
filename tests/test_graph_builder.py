import pytest
from wlm_world_generation_protocol.graph_builder import build_world_graph


def test_graph_builder_basic():
    seed = {"theme": "ruins"}
    regions = []
    entities = []
    rules = []
    timeline = []

    graph = build_world_graph(seed, regions, entities, rules, timeline)

    assert graph["nodes"] == []
    assert graph["edges"] == []
    assert graph["rules"] == rules
    assert graph["timeline"] == timeline
    assert graph["seed"] == seed
