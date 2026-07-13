from app.platform_core.portfolio_manager.readiness import portfolio_manager_readiness_gate
from app.platform_core.portfolio_manager.service import portfolio_manager_foundation_service
from app.v500_alpha26_portfolio_manager.models import PortfolioManagerSummaryV500Alpha26

class PortfolioManagerFacadeV500Alpha26:
    def summary(self): return PortfolioManagerSummaryV500Alpha26()
    def holdings(self): return {"ready": True, "holdings": portfolio_manager_foundation_service.sample_holdings()}
    def snapshot(self): return portfolio_manager_foundation_service.snapshot()
    def allocation(self): return portfolio_manager_foundation_service.allocation()
    def pnl(self): return portfolio_manager_foundation_service.pnl()
    def equity_curve(self): return portfolio_manager_foundation_service.equity_curve()
    def exposure(self): return portfolio_manager_foundation_service.exposure()
    def risk_check(self): return portfolio_manager_foundation_service.risk_check()
    def readiness(self): return portfolio_manager_readiness_gate.run()
    def contract(self): return {"ready": True, "portfolio_manager": "foundation_only", "requires_broker_layer": True, "requires_risk_engine": True, "execution_allowed": False}
