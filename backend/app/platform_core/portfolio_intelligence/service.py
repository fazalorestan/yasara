from app.platform_core.portfolio_intelligence.allocation import portfolio_allocation_engine
from app.platform_core.portfolio_intelligence.correlation import portfolio_correlation_service
from app.platform_core.portfolio_intelligence.exposure import portfolio_exposure_analyzer
from app.platform_core.portfolio_intelligence.health import portfolio_health_service
from app.platform_core.portfolio_intelligence.rebalance import portfolio_rebalance_planner
from app.platform_core.portfolio_intelligence.sample import portfolio_intelligence_sample_data

class PortfolioIntelligenceCoreService:
    def profile(self): return {"ready": True, "profile": portfolio_intelligence_sample_data.profile()}
    def assets(self): return {"ready": True, "assets": portfolio_intelligence_sample_data.assets()}
    def allocation(self): return portfolio_allocation_engine.calculate_weights(self.assets()["assets"])
    def target_allocation(self): return portfolio_allocation_engine.target_allocation(self.assets()["assets"], self.allocation()["total_value"])
    def exposure(self): return portfolio_exposure_analyzer.analyze(self.assets()["assets"])
    def correlation(self): return portfolio_correlation_service.matrix([a["symbol"] for a in self.assets()["assets"]])
    def correlation_risk(self): return portfolio_correlation_service.risk_flag(self.correlation()["matrix"])
    def rebalance(self): return portfolio_rebalance_planner.plan(self.allocation())
    def health(self): return portfolio_health_service.evaluate(self.exposure(), self.correlation_risk())
    def status(self):
        health = self.health()
        return {"ready": health["ready"], "healthy": health["healthy"], "execution_allowed": False}

portfolio_intelligence_core_service = PortfolioIntelligenceCoreService()
