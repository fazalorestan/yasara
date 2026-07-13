from app.v450_indicator_platform_handoff.models import IndicatorPlatformHandoffSummaryV450

def test_v450_summary():
    s = IndicatorPlatformHandoffSummaryV450()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
