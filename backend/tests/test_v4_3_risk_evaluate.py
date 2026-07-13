from app.v43_risk_engine.models import RiskRequestV43
from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43

def test_v43_evaluate():
    data = AdvancedRiskEngineServiceV43().evaluate(RiskRequestV43())
    assert data["ready"] is True
    assert data["position"]["size"] > 0
    assert data["real_order_execution_enabled"] is False
