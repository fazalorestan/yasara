from app.rc1_v1.rc_manifest import RCManifestBuilderV1

def test_rc1_manifest():
    manifest = RCManifestBuilderV1().build()
    assert manifest.version == "1.0.0-rc1"
    assert manifest.minimum_tests_required >= 217
