from app.v442_indicator_chart_integration.service import IndicatorChartIntegrationServiceV442

def test_v442_service_binding():
    s = IndicatorChartIntegrationServiceV442()
    binding = s.chart_binding()
    assert binding["ready"] is True
    assert binding["default_indicator"] == "yasara"
