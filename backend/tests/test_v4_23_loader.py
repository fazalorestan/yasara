from app.v423_plugin_catalog.loader import PluginManifestLoaderV423

def test_v423_loader():
    loader = PluginManifestLoaderV423()
    manifests = loader.load_all()
    assert len(manifests) >= 5
    assert any(m.name == "market_structure_pro" for m in manifests)
