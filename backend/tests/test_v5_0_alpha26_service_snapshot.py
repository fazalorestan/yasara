from app.platform_core.portfolio_manager.service import PortfolioManagerFoundationService

def test_v500_alpha26_service_snapshot(): assert PortfolioManagerFoundationService().snapshot()['total_equity']==10000.0
