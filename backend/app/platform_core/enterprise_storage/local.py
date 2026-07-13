from app.platform_core.enterprise_storage.models import StorageRecord

class LocalStorageEngine:
    def __init__(self):
        self._items: dict[str, StorageRecord] = {}

    def write(self, bucket: str, key: str, payload: dict):
        record = StorageRecord(key=key, bucket=bucket, payload=payload)
        self._items[f"{bucket}:{key}"] = record
        return record

    def read(self, bucket: str, key: str):
        return self._items.get(f"{bucket}:{key}")

    def list(self, bucket: str | None = None):
        records = self._items.values()
        if bucket:
            records = [r for r in records if r.bucket == bucket]
        return [r.__dict__ for r in records]

    def delete(self, bucket: str, key: str):
        return self._items.pop(f"{bucket}:{key}", None)

local_storage_engine = LocalStorageEngine()
