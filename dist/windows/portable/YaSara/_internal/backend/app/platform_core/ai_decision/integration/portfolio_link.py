from app.platform_core.portfolio_manager.service import portfolio_manager_foundation_service
class AIDecisionPortfolioLink:
    def snapshot(self):
        return {"ready": True, "snapshot": portfolio_manager_foundation_service.snapshot(), "source": "portfolio_manager", "execution_allowed": False}
    def portfolio_state(self):
        exposure = portfolio_manager_foundation_service.exposure()
        state = "normal" if exposure["exposure_pct"] <= 60 else "high_exposure"
        return {"ready": True, "state": state, "exposure": exposure, "execution_allowed": False}
ai_decision_portfolio_link = AIDecisionPortfolioLink()
