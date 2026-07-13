from app.v445_indicator_engine_bridge.models import IndicatorEngineBridgeSummaryV445

def test_v445_summary():
    s = IndicatorEngineBridgeSummaryV445()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
