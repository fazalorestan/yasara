from app.platform_core.enterprise_storage.local import local_storage_engine

class BackupStore:
    bucket = "backups"

    def write_backup(self, key: str, payload: dict):
        return local_storage_engine.write(self.bucket, key, payload)

    def list_backups(self):
        return local_storage_engine.list(self.bucket)

backup_store = BackupStore()
