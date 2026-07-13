from app.platform_core.ai_decision.integration.portfolio_link import AIDecisionPortfolioLink

def test_v500_alpha33_c_portfolio_snapshot(): assert AIDecisionPortfolioLink().snapshot()['ready'] is True