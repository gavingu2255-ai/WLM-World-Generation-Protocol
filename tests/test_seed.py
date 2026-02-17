import pytest
from wlm_world_generation_protocol.seed_engine import generate_seed


def test_seed_generation_defaults():
    seed = generate_seed({})

    assert seed["theme"] == "generic"
    assert seed["scale"] == "medium"
    assert seed["constraints"] == []


def test_seed_generation_custom():
    seed = generate_seed({
        "theme": "ruins",
        "scale": "large",
        "constraints": ["non-magical"]
    })

    assert seed["theme"] == "ruins"
    assert seed["scale"] == "large"
    assert seed["constraints"] == ["non-magical"]
