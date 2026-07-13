from app.platform_core.portfolio_manager.service import PortfolioManagerFoundationService

def test_v500_alpha26_service_holdings(): assert len(PortfolioManagerFoundationService().sample_holdings())==2
