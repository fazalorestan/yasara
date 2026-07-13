from app.cloud_v1.backup_manifest import BackupManifestBuilderV1

def test_backup_manifest():
    manifest = BackupManifestBuilderV1().build("u1", ["settings", "strategies"])
    assert manifest.backup_id == "backup_u1"
    assert "strategies" in manifest.sections
