from app.platform_core.risk_engine.exposure import exposure_guard
from app.platform_core.portfolio_intelligence.analytics_service import portfolio_analytics_risk_service

class PortfolioRiskEngineLinkService:
    def risk_check(self):
        risk = portfolio_analytics_risk_service.risk_score()
        exposure = exposure_guard.check_portfolio_exposure(50.0, 60.0)
        allowed = risk["risk_grade"] != "high" and exposure["allowed"]
        return {"ready": True, "risk_grade": risk["risk_grade"], "risk_score": risk["score"], "allowed": allowed, "execution_allowed": False}

portfolio_risk_engine_link_service = PortfolioRiskEngineLinkService()
