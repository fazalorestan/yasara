from app.platform_core.indicators.signal_logic_expansion.safety import RuntimeSignalSafetyReport
def test_v500_alpha8_safety():
    r = RuntimeSignalSafetyReport().report()
    assert r["auto_trade_enabled"] is False
    assert r["live_execution_enabled"] is False
