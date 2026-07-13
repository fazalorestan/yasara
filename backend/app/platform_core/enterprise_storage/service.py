from app.platform_core.enterprise_storage.artifacts import artifact_store
from app.platform_core.enterprise_storage.backups import backup_store
from app.platform_core.enterprise_storage.metrics import storage_metrics_reporter
from app.platform_core.enterprise_storage.object_contract import object_storage_contract_service
from app.platform_core.enterprise_storage.policies import storage_policy_registry
from app.platform_core.enterprise_storage.snapshots import snapshot_store

class EnterpriseStorageService:
    def seed(self):
        return {"ready": True, "policies": storage_policy_registry.seed_defaults(), "mode": "report_only"}

    def write_artifact(self, key: str = "artifact_latest", payload: dict | None = None):
        record = artifact_store.write_artifact(key, payload or {"ready": True})
        return {"ready": True, "record": record.__dict__}

    def write_snapshot(self, key: str = "snapshot_latest", payload: dict | None = None):
        record = snapshot_store.write_snapshot(key, payload or {"ready": True})
        return {"ready": True, "record": record.__dict__}

    def write_backup(self, key: str = "backup_latest", payload: dict | None = None):
        record = backup_store.write_backup(key, payload or {"ready": True})
        return {"ready": True, "record": record.__dict__}

    def inventory(self):
        return {
            "ready": True,
            "artifacts": artifact_store.list_artifacts(),
            "snapshots": snapshot_store.list_snapshots(),
            "backups": backup_store.list_backups(),
        }

    def metrics(self):
        return storage_metrics_reporter.report()

    def object_contract(self):
        return {"ready": True, "object_storage": object_storage_contract_service.contract()}

enterprise_storage_service = EnterpriseStorageService()
