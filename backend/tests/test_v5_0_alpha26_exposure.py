from app.platform_core.portfolio_manager.exposure import PortfolioExposureService

def test_v500_alpha26_exposure():
    r=PortfolioExposureService().exposure([{'quantity':1,'last_price':100}], 1000); assert r['exposure_pct']==10
