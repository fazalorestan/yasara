from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43

def test_v43_signal_risk():
    data = AdvancedRiskEngineServiceV43().signal_risk()
    assert data["ready"] is True
    assert "signal" in data
    assert "risk" in data
    assert data["live_trading_enabled"] is False
