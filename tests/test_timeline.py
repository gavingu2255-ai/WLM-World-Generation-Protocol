import pytest
from wlm_world_generation_protocol.timeline_engine import generate_timeline


def test_timeline_generation_mvp():
    timeline = generate_timeline({"theme": "ruins"}, [], [], [])
    assert timeline == []  # MVP: no timeline yet
