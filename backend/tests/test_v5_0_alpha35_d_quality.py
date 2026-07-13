from app.platform_core.portfolio_intelligence.enterprise.quality_score import PortfolioEnterpriseQualityScoreService

def test_v500_alpha35_d_quality(): assert PortfolioEnterpriseQualityScoreService().calculate()['ready'] is True