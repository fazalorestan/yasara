from app.platform_core.portfolio_intelligence.correlation import PortfolioCorrelationService

def test_v500_alpha35_a_corr_matrix(): assert PortfolioCorrelationService().matrix(['A','B'])['matrix']['A']['A']==1.0