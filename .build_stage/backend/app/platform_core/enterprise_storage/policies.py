from app.platform_core.enterprise_storage.models import StoragePolicy

class StoragePolicyRegistry:
    def __init__(self):
        self._policies: dict[str, StoragePolicy] = {}

    def register(self, policy: StoragePolicy):
        self._policies[policy.bucket] = policy
        return policy

    def list(self):
        return {k: v.__dict__ for k, v in self._policies.items()}

    def seed_defaults(self):
        if not self._policies:
            self.register(StoragePolicy(bucket="artifacts", retention_days=90))
            self.register(StoragePolicy(bucket="snapshots", retention_days=30))
            self.register(StoragePolicy(bucket="backups", retention_days=180))
        return self.list()

storage_policy_registry = StoragePolicyRegistry()
