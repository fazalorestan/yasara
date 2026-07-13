from app.platform_core.indicators.marketplace.catalog import IndicatorCatalog

def test_v500_alpha2_catalog():
    c=IndicatorCatalog().seed_defaults(); assert "yasara" in c and c["yasara"]["installed"] is True
