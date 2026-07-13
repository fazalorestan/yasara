from app.platform_core.portfolio_intelligence.risk_engine_link import PortfolioRiskEngineLinkService

def test_v500_alpha35_c_risk_block(): assert PortfolioRiskEngineLinkService().risk_check()['execution_allowed'] is False