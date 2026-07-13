from app.platform_core.extension_host.snapshot_bridge import ExtensionHostSnapshotBridge

def test_v428_extension_host_snapshot_bridge():
    result = ExtensionHostSnapshotBridge().capture()
    assert result["snapshot_id"] == "extension_host_snapshot"
    assert result["plugins"]
