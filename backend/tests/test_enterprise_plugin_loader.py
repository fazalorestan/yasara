from app.enterprise_v1.plugin_loader import PluginLoaderV1
from app.enterprise_v1.plugin_sdk import PluginSDKManifestV1

def test_plugin_loader():
    plugin = PluginLoaderV1().load(PluginSDKManifestV1(plugin_id="p1", name="Demo"))
    assert plugin.loaded is True
