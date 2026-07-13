from app.v444_indicator_pine_source.models import IndicatorPineSourceSummaryV444

def test_v444_summary():
    s = IndicatorPineSourceSummaryV444()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
