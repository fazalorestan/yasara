from app.v423_plugin_catalog.service import PluginCatalogServiceV423

def test_v423_catalog():
    c = PluginCatalogServiceV423().catalog()
    assert c["ready"] is True
    assert c["plugins"]
