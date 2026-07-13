from app.platform_core.licensing.features import feature_catalog
def test_v500_alpha9_feature_catalog():
    f = feature_catalog.features()
    assert "BASIC_ANALYSIS" in f
    assert "AUTO_TRADING" in f
