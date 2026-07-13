from app.v424_plugin_registry_sync.sync import PluginRegistrySyncServiceV424

def test_v424_sync():
    service = PluginRegistrySyncServiceV424()
    result = service.sync()
    assert result["ready"] is True
    assert result["synced_count"] >= 5
