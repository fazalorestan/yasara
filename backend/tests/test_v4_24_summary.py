from app.v424_plugin_registry_sync.models import PluginRegistrySyncSummaryV424

def test_v424_summary():
    s = PluginRegistrySyncSummaryV424()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.backward_compatible is True
