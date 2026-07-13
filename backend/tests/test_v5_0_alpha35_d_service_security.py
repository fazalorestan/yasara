from app.platform_core.portfolio_intelligence.enterprise.service import PortfolioEnterpriseService

def test_v500_alpha35_d_service_security():
 r=PortfolioEnterpriseService().security(); assert r is not None
