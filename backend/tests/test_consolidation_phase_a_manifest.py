from app.consolidation_v1.project_manifest import ConsolidatedProjectManifestBuilderV1

def test_consolidation_manifest():
    manifest = ConsolidatedProjectManifestBuilderV1().build()
    assert manifest.version == "1.0.0-pro"
    assert manifest.total_confirmed_tests >= 179
    assert "multi_exchange" in manifest.modules
