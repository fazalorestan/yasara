class ArtifactStoreContract:
    def store(self):
        return {
            "ready": True,
            "store": "artifact_store_contract",
            "storage_mode": "registry_contract",
            "artifacts": [],
            "artifact_count": 0,
            "write_enabled": False,
            "integrity_required": True,
        }

artifact_store_contract = ArtifactStoreContract()
