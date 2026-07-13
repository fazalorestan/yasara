from app.platform_core.build_pipeline.artifact_registry import BuildArtifactRegistry

def test_artifacts(): assert BuildArtifactRegistry().artifacts()['requires_integrity_check'] is True
