from app.platform_core.portfolio_manager.allocation import portfolio_allocation_service
from app.platform_core.portfolio_manager.equity_curve import equity_curve_service
from app.platform_core.portfolio_manager.exposure import portfolio_exposure_service
from app.platform_core.portfolio_manager.models import PortfolioSnapshot
from app.platform_core.portfolio_manager.pnl import portfolio_pnl_service
from app.platform_core.portfolio_manager.risk_link import portfolio_risk_link_service
from app.platform_core.portfolio_manager.valuation import portfolio_valuation_service

class PortfolioManagerFoundationService:
    def sample_holdings(self):
        return [
            {"symbol": "BTCUSDT", "quantity": 0.1, "average_price": 50000.0, "last_price": 52000.0, "asset_class": "crypto"},
            {"symbol": "ETHUSDT", "quantity": 1.5, "average_price": 3000.0, "last_price": 3100.0, "asset_class": "crypto"},
        ]

    def snapshot(self):
        holdings = self.sample_holdings()
        value = portfolio_valuation_service.total_holdings_value(holdings)
        pnl = portfolio_pnl_service.summary(holdings)
        return PortfolioSnapshot(account_id="demo", total_equity=10000.0, cash_balance=10000.0-value, holdings_value=value, unrealized_pnl=pnl["unrealized_pnl"]).__dict__

    def allocation(self): return portfolio_allocation_service.allocation(self.sample_holdings())
    def pnl(self): return portfolio_pnl_service.summary(self.sample_holdings())
    def equity_curve(self): return equity_curve_service.build_sample()
    def exposure(self): return portfolio_exposure_service.exposure(self.sample_holdings(), 10000.0)

    def risk_check(self):
        exposure = self.exposure()
        return portfolio_risk_link_service.check_portfolio_exposure(exposure["exposure_pct"])

portfolio_manager_foundation_service = PortfolioManagerFoundationService()
