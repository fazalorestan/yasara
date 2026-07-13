from app.v442_indicator_chart_integration.service import IndicatorChartIntegrationServiceV442

def test_v442_update_contract():
    c = IndicatorChartIntegrationServiceV442().update_contract()
    assert c["editable_file"].endswith("yasara-script.ts")
    assert c["backward_compatible"] is True
