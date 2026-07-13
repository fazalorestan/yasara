from app.v43_risk_engine.models import RiskRequestV43, RiskStateV43
from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43

def test_v43_circuit_breaker():
    req = RiskRequestV43(state=RiskStateV43(kill_switch_active=True))
    data = AdvancedRiskEngineServiceV43().evaluate(req)
    assert data["guards"]["allowed"] is False
    assert "kill_switch_active" in data["guards"]["reasons"]
