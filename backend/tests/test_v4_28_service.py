from app.v428_plugin_state_snapshot.service import PluginStateSnapshotServiceV428

def test_v428_service():
    s = PluginStateSnapshotServiceV428()
    assert s.summary().ready is True
    assert s.set_state()["ready"] is True
    assert s.snapshot()["ready"] is True
