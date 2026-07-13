from app.platform_core.portfolio_intelligence.enterprise.quality_score import PortfolioEnterpriseQualityScoreService

def test_v500_alpha35_d_quality_min(): assert PortfolioEnterpriseQualityScoreService().calculate()['overall'] >= 9.5