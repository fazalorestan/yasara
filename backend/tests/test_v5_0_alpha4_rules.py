from app.platform_core.indicators.lifecycle.rules import IndicatorLifecycleRules

def test_v500_alpha4_rules():
    r = IndicatorLifecycleRules()
    assert r.can_transition("discovered", "validated") is True
    assert r.can_transition("enabled", "installed") is False
