from app.v424_plugin_registry_sync.service import PluginRegistrySyncFacadeV424

def test_v424_governance_report():
    result = PluginRegistrySyncFacadeV424().governance()
    assert result["ready"] is True
    assert result["mode"] == "report_only"
