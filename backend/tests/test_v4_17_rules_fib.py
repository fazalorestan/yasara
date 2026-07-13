from app.v417_elliott.detectors import fibonacci_base
from app.v417_elliott.rules import ElliottRuleRegistryV417
def test_v417_rules_fib():
    waves=[
        {"direction":"up","from":{"price":0},"to":{"price":10},"price_change_abs":10},
        {"direction":"down","from":{"price":10},"to":{"price":5},"price_change_abs":5},
        {"direction":"up","from":{"price":5},"to":{"price":21},"price_change_abs":16},
        {"direction":"down","from":{"price":21},"to":{"price":12},"price_change_abs":9},
        {"direction":"up","from":{"price":12},"to":{"price":24},"price_change_abs":12},
    ]
    assert "score" in ElliottRuleRegistryV417().validate_impulse(waves)
    assert "ratios" in fibonacci_base(waves)
