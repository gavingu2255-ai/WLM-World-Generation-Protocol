import pytest
from wlm_world_generation_protocol.api import generate_world


def test_end_to_end_world_generation():
    spec = {"theme": "ruins", "scale": "small"}

    world = generate_world(spec)

    assert world["seed"]["theme"] == "ruins"
    assert world["regions"] == []
    assert world["entities"] == []
    assert world["rules"] == []
    assert world["timeline"] == []
    assert isinstance(world["world_graph"], dict)
