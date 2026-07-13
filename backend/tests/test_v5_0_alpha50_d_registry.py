from app.platform_core.windows_artifact_registration.artifact_registry_update import LocalArtifactRegistryUpdateContract

def test_registry(): assert LocalArtifactRegistryUpdateContract().update()['requires_manifest'] is True
