from app.platform_core.portfolio_manager.risk_link import PortfolioRiskLinkService

def test_v500_alpha26_risk_link(): assert PortfolioRiskLinkService().check_portfolio_exposure(50)['allowed'] is True
