from app.platform_core.portfolio_intelligence.service import PortfolioIntelligenceCoreService

def test_v500_alpha35_a_service_status(): assert PortfolioIntelligenceCoreService().status()['execution_allowed'] is False