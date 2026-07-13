from app.platform_core.indicators.lifecycle.manager import IndicatorLifecycleStateManager

def test_v500_alpha4_transition():
    m = IndicatorLifecycleStateManager()
    r = m.transition("x", "validated")
    assert r["allowed"] is True
