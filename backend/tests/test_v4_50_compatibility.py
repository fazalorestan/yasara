from app.platform_core.indicators.handoff.compatibility import IndicatorCompatibilityMatrix

def test_v450_compatibility():
    m = IndicatorCompatibilityMatrix().matrix()
    assert m["ready"] is True
    assert m["execution_allowed"] is False
    assert m["dashboard_unchanged"] is True
