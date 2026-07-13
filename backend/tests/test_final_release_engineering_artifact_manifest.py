from app.final_release_engineering_v1.artifact_manifest import ArtifactManifestBuilderV1

def test_artifact_manifest():
    manifest = ArtifactManifestBuilderV1().build()
    assert manifest.release_name == "YaSara Professional v1.0"
    assert any(a.name == "backend_source" for a in manifest.artifacts)
