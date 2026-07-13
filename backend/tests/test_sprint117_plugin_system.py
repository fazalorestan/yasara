from app.release_pro_v1.plugin_system import PluginManifestV1, PluginRegistryV1

def test_plugin_registry_register():
    registry = PluginRegistryV1()
    registry.register(PluginManifestV1(plugin_id="p1", name="Demo"))
    assert registry.list()[0].plugin_id == "p1"
