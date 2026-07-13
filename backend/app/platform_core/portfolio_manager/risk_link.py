from app.platform_core.risk_engine.exposure import exposure_guard

class PortfolioRiskLinkService:
    def check_portfolio_exposure(self, exposure_pct: float, max_exposure_pct: float = 60.0):
        result = exposure_guard.check_portfolio_exposure(exposure_pct, max_exposure_pct)
        return {"ready": result["ready"], "allowed": result["allowed"], "reason": result["reason"], "execution_allowed": False}

portfolio_risk_link_service = PortfolioRiskLinkService()
