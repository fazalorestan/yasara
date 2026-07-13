from app.platform_core.release_registry.artifact_store import ArtifactStoreContract

def test_store(): assert ArtifactStoreContract().store()['integrity_required'] is True
