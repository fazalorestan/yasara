from app.v442_indicator_chart_integration.models import IndicatorChartIntegrationSummaryV442

def test_v442_summary():
    s = IndicatorChartIntegrationSummaryV442()
    assert s.ready is True
    assert s.default_indicator == "yasara"
    assert s.chart_overlay_enabled is True
    assert s.live_execution_enabled is False
