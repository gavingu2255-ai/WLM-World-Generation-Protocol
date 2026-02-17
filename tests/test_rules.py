import pytest
from wlm_world_generation_protocol.rule_engine import generate_rules


def test_rule_generation_mvp():
    rules = generate_rules({"theme": "ruins"}, [], [])
    assert rules == []  # MVP: no rules yet
