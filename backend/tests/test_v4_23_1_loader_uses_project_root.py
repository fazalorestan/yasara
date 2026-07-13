from app.v423_plugin_catalog.loader import PluginManifestLoaderV423
from app.platform_core.paths import plugin_manifest_root

def test_v4231_loader_uses_project_root():
    loader = PluginManifestLoaderV423()
    assert loader.root == plugin_manifest_root()
    manifests = loader.load_all()
    assert len(manifests) >= 5
