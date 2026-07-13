from app.platform_core.portfolio_intelligence.correlation import PortfolioCorrelationService

def test_v500_alpha35_a_corr_risk_ok(): assert PortfolioCorrelationService().risk_flag({'A':{'B':.3},'B':{'A':.3}})['correlation_ok'] is True