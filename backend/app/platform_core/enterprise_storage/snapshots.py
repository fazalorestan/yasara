from app.platform_core.enterprise_storage.local import local_storage_engine

class SnapshotStore:
    bucket = "snapshots"

    def write_snapshot(self, key: str, payload: dict):
        return local_storage_engine.write(self.bucket, key, payload)

    def list_snapshots(self):
        return local_storage_engine.list(self.bucket)

snapshot_store = SnapshotStore()
