from app.archive_handoff_v1.handoff_manifest import HandoffManifestBuilderV1

def test_handoff_manifest():
    manifest = HandoffManifestBuilderV1().build()
    assert any(i.name == "source_code" for i in manifest.items)
