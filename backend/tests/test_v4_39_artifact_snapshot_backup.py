from app.platform_core.enterprise_storage.artifacts import ArtifactStore
from app.platform_core.enterprise_storage.snapshots import SnapshotStore
from app.platform_core.enterprise_storage.backups import BackupStore

def test_v439_artifact_snapshot_backup():
    assert ArtifactStore().write_artifact("a", {"ok": True}).bucket == "artifacts"
    assert SnapshotStore().write_snapshot("s", {"ok": True}).bucket == "snapshots"
    assert BackupStore().write_backup("b", {"ok": True}).bucket == "backups"
