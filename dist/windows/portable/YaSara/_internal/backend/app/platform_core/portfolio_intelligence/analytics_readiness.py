from app.platform_core.portfolio_intelligence.analytics_service import portfolio_analytics_risk_service

class PortfolioAnalyticsRiskReadinessGate:
    def run(self):
        report = portfolio_analytics_risk_service.report()
        risk = portfolio_analytics_risk_service.risk_score()
        ready = report["ready"] and risk["ready"]
        return {"ready": ready, "checks": {"report_ready": report["ready"], "risk_score_ready": risk["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

portfolio_analytics_risk_readiness_gate = PortfolioAnalyticsRiskReadinessGate()
