from app.v442_indicator_chart_integration.service import IndicatorChartIntegrationServiceV442

def test_v442_visibility():
    v = IndicatorChartIntegrationServiceV442().visibility()
    assert v["default_visible"] is True
    assert v["overlays"]["ema"] is True
