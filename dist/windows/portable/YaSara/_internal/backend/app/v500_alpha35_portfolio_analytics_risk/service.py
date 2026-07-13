from app.platform_core.portfolio_intelligence.analytics_readiness import portfolio_analytics_risk_readiness_gate
from app.platform_core.portfolio_intelligence.analytics_service import portfolio_analytics_risk_service
from app.v500_alpha35_portfolio_analytics_risk.models import PortfolioAnalyticsRiskSummaryV500Alpha35

class PortfolioAnalyticsRiskFacadeV500Alpha35:
    def summary(self): return PortfolioAnalyticsRiskSummaryV500Alpha35()
    def equity_curve(self): return portfolio_analytics_risk_service.equity_curve()
    def analytics(self): return portfolio_analytics_risk_service.analytics()
    def returns(self): return portfolio_analytics_risk_service.returns()
    def drawdown(self): return portfolio_analytics_risk_service.drawdown()
    def volatility(self): return portfolio_analytics_risk_service.volatility()
    def concentration(self): return portfolio_analytics_risk_service.concentration()
    def capital_allocation(self): return portfolio_analytics_risk_service.capital_allocation()
    def risk_score(self): return portfolio_analytics_risk_service.risk_score()
    def report(self): return portfolio_analytics_risk_service.report()
    def readiness(self): return portfolio_analytics_risk_readiness_gate.run()
    def contract(self): return {"ready": True, "portfolio_intelligence": "package_b_analytics_risk", "execution_allowed": False}
