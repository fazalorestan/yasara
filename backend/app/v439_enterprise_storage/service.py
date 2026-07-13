from app.platform_core.enterprise_storage.service import enterprise_storage_service
from app.v439_enterprise_storage.models import EnterpriseStorageSummaryV439

class EnterpriseStorageFacadeV439:
    def summary(self):
        return EnterpriseStorageSummaryV439()

    def seed(self):
        return enterprise_storage_service.seed()

    def write_artifact(self, key: str = "artifact_latest", payload: dict | None = None):
        return enterprise_storage_service.write_artifact(key, payload)

    def write_snapshot(self, key: str = "snapshot_latest", payload: dict | None = None):
        return enterprise_storage_service.write_snapshot(key, payload)

    def write_backup(self, key: str = "backup_latest", payload: dict | None = None):
        return enterprise_storage_service.write_backup(key, payload)

    def inventory(self):
        return enterprise_storage_service.inventory()

    def metrics(self):
        return enterprise_storage_service.metrics()

    def object_contract(self):
        return enterprise_storage_service.object_contract()
