from app.platform_core.portfolio_intelligence.enterprise.service import PortfolioEnterpriseService

def test_v500_alpha35_d_service_final_report():
 r=PortfolioEnterpriseService().final_report(); assert r is not None
