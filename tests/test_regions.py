import pytest
from wlm_world_generation_protocol.region_engine import generate_regions


def test_region_generation_mvp():
    regions = generate_regions({"theme": "ruins"})
    assert regions == []  # MVP: no regions yet
