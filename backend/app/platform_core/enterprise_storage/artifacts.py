from app.platform_core.enterprise_storage.local import local_storage_engine

class ArtifactStore:
    bucket = "artifacts"

    def write_artifact(self, key: str, payload: dict):
        return local_storage_engine.write(self.bucket, key, payload)

    def list_artifacts(self):
        return local_storage_engine.list(self.bucket)

artifact_store = ArtifactStore()
