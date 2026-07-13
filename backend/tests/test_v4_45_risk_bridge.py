from app.platform_core.indicators.bridges.risk_bridge import IndicatorRiskBridge

def test_v445_risk_bridge():
    out = IndicatorRiskBridge().to_risk_panel({"signals": [{"confidence": 80}]})
    assert out["risk_level"] == "low"
    assert out["execution_allowed"] is False
