from app.platform_core.portfolio_intelligence.service import portfolio_intelligence_core_service

class PortfolioIntelligenceReadinessGate:
    def run(self):
        allocation = portfolio_intelligence_core_service.allocation()
        exposure = portfolio_intelligence_core_service.exposure()
        health = portfolio_intelligence_core_service.health()
        ready = allocation["ready"] and exposure["ready"] and health["ready"]
        return {"ready": ready, "checks": {"allocation_ready": allocation["ready"], "exposure_ready": exposure["ready"], "health_ready": health["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

portfolio_intelligence_readiness_gate = PortfolioIntelligenceReadinessGate()
