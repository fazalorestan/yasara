from app.v424_plugin_registry_sync.sync import PluginRegistrySyncServiceV424

def test_v424_lifecycle_report():
    service = PluginRegistrySyncServiceV424()
    service.sync()
    report = service.lifecycle_report()
    assert report["ready"] is True
    assert report["plugin_count"] >= 5
