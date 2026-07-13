from app.platform_core.ai_decision.integration.portfolio_link import AIDecisionPortfolioLink

def test_v500_alpha33_c_portfolio_state(): assert AIDecisionPortfolioLink().portfolio_state()['state'] in ['normal','high_exposure']