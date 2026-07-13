from app.platform_core.portfolio_intelligence.correlation import PortfolioCorrelationService

def test_v500_alpha35_a_corr_risk_bad(): assert PortfolioCorrelationService().risk_flag({'A':{'B':.9},'B':{'A':.9}})['correlation_ok'] is False