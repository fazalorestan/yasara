from app.release_pro_v1.pro_manifest import ProfessionalManifestBuilderV1

def test_pro_manifest_capabilities():
    manifest = ProfessionalManifestBuilderV1().build()
    assert manifest.edition == "Professional"
    assert "plugin_system" in manifest.capabilities
