from app.platform_core.indicators.release_gate.checkpoint import IndicatorPluginExpansionCheckpoint

def test_v500_alpha5_checkpoint():
    c = IndicatorPluginExpansionCheckpoint().checkpoint()
    assert c["ready"] is True
    assert "auto_trade_execution" in c["blocked_until_later"]
