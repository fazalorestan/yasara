from app.platform_core.indicators.handoff.v5_contract import IndicatorV5PluginContract

def test_v450_v5_contract():
    c = IndicatorV5PluginContract().contract()
    assert c["ready"] is True
    assert "direct_live_execution" in c["forbidden"]
