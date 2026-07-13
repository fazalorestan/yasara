from app.platform_core.portfolio_intelligence.ai_link import PortfolioAILinkService

def test_v500_alpha35_c_ai_block(): assert PortfolioAILinkService().confidence_signal()['execution_allowed'] is False