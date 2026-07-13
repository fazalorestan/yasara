from app.platform_core.portfolio_intelligence.service import PortfolioIntelligenceCoreService

def test_v500_alpha35_a_service_corr_risk(): assert PortfolioIntelligenceCoreService().correlation_risk()['ready'] is True