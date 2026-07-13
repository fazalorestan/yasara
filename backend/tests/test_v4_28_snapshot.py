from app.platform_core.state.state_store import plugin_state_store
from app.platform_core.state.snapshot import RuntimeSnapshotManager

def test_v428_snapshot():
    plugin_state_store.set_state("snapshot_test", {"ready": True})
    s = RuntimeSnapshotManager().export_snapshot("s1")
    assert s["snapshot_id"] == "s1"
    assert "snapshot_test" in s["plugins"]
