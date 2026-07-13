from app.v428_plugin_state_snapshot.models import PluginStateSnapshotSummaryV428

def test_v428_summary():
    s = PluginStateSnapshotSummaryV428()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
