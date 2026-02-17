import pytest
from wlm_world_generation_protocol.entity_engine import generate_entities


def test_entity_generation_mvp():
    entities = generate_entities({"theme": "ruins"}, [])
    assert entities == []  # MVP: no entities yet
