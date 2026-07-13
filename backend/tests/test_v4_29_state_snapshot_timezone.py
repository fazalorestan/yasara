from app.platform_core.state.snapshot import RuntimeSnapshotManager

def test_v429_state_snapshot_timezone():
    snap = RuntimeSnapshotManager().export_snapshot("x")
    assert "+00:00" in snap["created_at"]
    assert "+00:00" in snap["exported_at"]
