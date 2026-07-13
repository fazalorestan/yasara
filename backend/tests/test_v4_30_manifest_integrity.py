from app.platform_core.diagnostics.manifest_integrity import ManifestIntegrityCheck

def test_v430_manifest_integrity():
    result = ManifestIntegrityCheck().run()
    assert result.ready is True
    assert result.data["manifest_count"] >= 5
