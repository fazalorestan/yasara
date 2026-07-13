from app.platform_core.indicators.readiness.safety import YaSaraIndicatorSafetyReport

def test_v449_safety():
    s = YaSaraIndicatorSafetyReport().report()
    assert s["ready"] is True
    assert s["auto_trade_enabled"] is False
    assert s["dashboard_changed"] is False
