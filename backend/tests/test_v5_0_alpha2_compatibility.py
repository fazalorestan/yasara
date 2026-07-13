from app.platform_core.indicators.marketplace.compatibility import IndicatorMarketplaceCompatibility

def test_v500_alpha2_compatibility():
    r=IndicatorMarketplaceCompatibility().check({"name":"x","compatible":True}); assert r["ready"] is True and r["execution_allowed"] is False
