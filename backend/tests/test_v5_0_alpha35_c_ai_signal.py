from app.platform_core.portfolio_intelligence.ai_link import PortfolioAILinkService

def test_v500_alpha35_c_ai_signal(): assert PortfolioAILinkService().confidence_signal()['signal_strength'] in ['strong','moderate','weak']