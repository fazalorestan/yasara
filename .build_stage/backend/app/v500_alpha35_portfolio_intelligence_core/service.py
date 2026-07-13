from app.platform_core.portfolio_intelligence.readiness import portfolio_intelligence_readiness_gate
from app.platform_core.portfolio_intelligence.service import portfolio_intelligence_core_service
from app.v500_alpha35_portfolio_intelligence_core.models import PortfolioIntelligenceCoreSummaryV500Alpha35

class PortfolioIntelligenceCoreFacadeV500Alpha35:
    def summary(self): return PortfolioIntelligenceCoreSummaryV500Alpha35()
    def profile(self): return portfolio_intelligence_core_service.profile()
    def assets(self): return portfolio_intelligence_core_service.assets()
    def allocation(self): return portfolio_intelligence_core_service.allocation()
    def target_allocation(self): return portfolio_intelligence_core_service.target_allocation()
    def exposure(self): return portfolio_intelligence_core_service.exposure()
    def correlation(self): return portfolio_intelligence_core_service.correlation()
    def correlation_risk(self): return portfolio_intelligence_core_service.correlation_risk()
    def rebalance(self): return portfolio_intelligence_core_service.rebalance()
    def health(self): return portfolio_intelligence_core_service.health()
    def status(self): return portfolio_intelligence_core_service.status()
    def readiness(self): return portfolio_intelligence_readiness_gate.run()
    def contract(self): return {"ready": True, "portfolio_intelligence": "package_a_core_allocation", "execution_allowed": False}
