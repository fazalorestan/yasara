from app.platform_core.portfolio_intelligence.health import PortfolioHealthService

def test_v500_alpha35_a_health_bad(): assert PortfolioHealthService().evaluate({'exposure_ok':False},{'correlation_ok':True})['healthy'] is False