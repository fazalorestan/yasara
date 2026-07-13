from app.platform_core.release_registry.artifact_integrity import ArtifactIntegrityContract

def test_integrity(): assert ArtifactIntegrityContract().integrity()['tamper_detected'] is False
