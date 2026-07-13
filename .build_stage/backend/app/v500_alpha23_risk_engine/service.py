from app.platform_core.risk_engine.readiness import risk_engine_readiness_gate
from app.platform_core.risk_engine.service import risk_engine_foundation_service
from app.v500_alpha23_risk_engine.models import RiskEngineSummaryV500Alpha23

class RiskEngineFacadeV500Alpha23:
    def summary(self): return RiskEngineSummaryV500Alpha23()
    def policy(self): return risk_engine_foundation_service.policy()
    def position_size(self): return risk_engine_foundation_service.position_size()
    def daily_loss(self): return risk_engine_foundation_service.daily_loss()
    def drawdown(self): return risk_engine_foundation_service.drawdown()
    def exposure(self): return risk_engine_foundation_service.exposure()
    def preflight(self): return risk_engine_foundation_service.preflight()
    def blocked_preflight(self): return risk_engine_foundation_service.blocked_preflight()
    def readiness(self): return risk_engine_readiness_gate.run()
    def contract(self): return {"ready": True, "risk_engine": "foundation_only", "order_execution": "blocked_by_default", "execution_allowed": False}
