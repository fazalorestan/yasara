from app.platform_core.diagnostics.plugin_registry_integrity import PluginRegistryIntegrityCheck

def test_v430_plugin_registry_integrity():
    result = PluginRegistryIntegrityCheck().run()
    assert result.ready is True
    assert result.data["plugin_count"] >= 5
