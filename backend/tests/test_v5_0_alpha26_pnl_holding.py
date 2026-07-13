from app.platform_core.portfolio_manager.pnl import PortfolioPnLService

def test_v500_alpha26_pnl_holding(): assert PortfolioPnLService().holding_unrealized_pnl(2,10,12)==4
