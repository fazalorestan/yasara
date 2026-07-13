from app.platform_core.risk_engine.service import RiskEngineFoundationService

def test_v500_alpha23_service(): assert RiskEngineFoundationService().preflight()['allowed'] is True
