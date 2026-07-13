from app.platform_core.portfolio_intelligence.enterprise.service import PortfolioEnterpriseService

def test_v500_alpha35_d_service_quality_score():
 r=PortfolioEnterpriseService().quality_score(); assert r is not None
