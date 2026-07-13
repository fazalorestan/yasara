from app.platform_core.portfolio_intelligence.analytics import portfolio_analytics_service
from app.platform_core.portfolio_intelligence.capital_allocation import portfolio_capital_allocation_advisor
from app.platform_core.portfolio_intelligence.concentration import portfolio_concentration_risk_service
from app.platform_core.portfolio_intelligence.drawdown import portfolio_drawdown_analyzer
from app.platform_core.portfolio_intelligence.risk_score import portfolio_risk_score_service
from app.platform_core.portfolio_intelligence.service import portfolio_intelligence_core_service
from app.platform_core.portfolio_intelligence.volatility import portfolio_volatility_analyzer

class PortfolioAnalyticsRiskService:
    def equity_curve(self):
        return {"ready": True, "equity_curve": [10000.0, 10200.0, 9800.0, 10500.0, 10300.0, 10800.0]}

    def analytics(self):
        curve = self.equity_curve()["equity_curve"]
        return portfolio_analytics_service.summary(curve)

    def returns(self):
        return portfolio_analytics_service.returns(self.equity_curve()["equity_curve"])

    def drawdown(self):
        return portfolio_drawdown_analyzer.analyze(self.equity_curve()["equity_curve"])

    def volatility(self):
        return portfolio_volatility_analyzer.calculate(self.returns()["returns"])

    def concentration(self):
        return portfolio_concentration_risk_service.analyze(portfolio_intelligence_core_service.assets()["assets"])

    def capital_allocation(self):
        allocated = portfolio_intelligence_core_service.allocation()["assets"]
        return portfolio_capital_allocation_advisor.advise(allocated, 1000.0)

    def risk_score(self):
        return portfolio_risk_score_service.score(self.drawdown(), self.volatility(), self.concentration())

    def report(self):
        return {"ready": True, "analytics": self.analytics(), "drawdown": self.drawdown(), "volatility": self.volatility(), "concentration": self.concentration(), "capital_allocation": self.capital_allocation(), "risk_score": self.risk_score(), "execution_allowed": False}

portfolio_analytics_risk_service = PortfolioAnalyticsRiskService()
