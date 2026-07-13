from app.platform_core.indicators.marketplace.discovery import IndicatorCatalogDiscovery

def test_v500_alpha2_discovery():
    d=IndicatorCatalogDiscovery().discover(); assert d["ready"] is True and d["count"] >= 2
