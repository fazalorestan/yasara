from app.platform_core.indicators.signal_logic_expansion.service import RuntimeSignalExpansionService
def test_v500_alpha8_service_edge():
    r = RuntimeSignalExpansionService().evaluate({})
    assert r["direction"] == "WAIT"
    assert r["validation"]["valid"] is True
