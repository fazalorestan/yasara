from app.v11_risk_control.service import RiskControlServiceV11

def test_risk_control_service_status():
    status = RiskControlServiceV11().status()
    assert status["ready"] is True
    assert status["live_trading_enabled"] is False
