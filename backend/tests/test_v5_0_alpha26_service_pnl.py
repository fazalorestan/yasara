from app.platform_core.portfolio_manager.service import PortfolioManagerFoundationService

def test_v500_alpha26_service_pnl(): assert PortfolioManagerFoundationService().pnl()['ready'] is True
