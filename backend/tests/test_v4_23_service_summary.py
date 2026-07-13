from app.v423_plugin_catalog.service import PluginCatalogServiceV423

def test_v423_service_summary():
    s = PluginCatalogServiceV423().summary()
    assert s["ready"] is True
    assert s["no_new_trading_features"] is True
    assert s["manifest_count"] >= 5
