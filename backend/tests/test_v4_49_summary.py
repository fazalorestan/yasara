from app.v449_indicator_final_readiness.models import IndicatorFinalReadinessSummaryV449

def test_v449_summary():
    s = IndicatorFinalReadinessSummaryV449()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
