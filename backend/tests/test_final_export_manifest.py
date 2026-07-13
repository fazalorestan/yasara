from app.final_export_v1.export_manifest import FinalExportManifestBuilderV1

def test_final_export_manifest():
    manifest = FinalExportManifestBuilderV1().build()
    assert manifest.version == "1.0.0"
    assert any(i.name == "source" for i in manifest.items)
