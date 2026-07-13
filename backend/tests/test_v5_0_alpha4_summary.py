from app.v500_alpha4_indicator_lifecycle.models import IndicatorLifecycleSummaryV500Alpha4

def test_v500_alpha4_summary():
    s = IndicatorLifecycleSummaryV500Alpha4()
    assert s.ready is True
    assert s.default_indicator == "yasara"
    assert s.live_execution_enabled is False
