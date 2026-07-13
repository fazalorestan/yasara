from app.v423_plugin_catalog.service import PluginCatalogServiceV423

def test_v423_evaluate():
    e = PluginCatalogServiceV423().evaluate()
    assert e["ready"] is True
    assert e["mode"] == "report_only"
