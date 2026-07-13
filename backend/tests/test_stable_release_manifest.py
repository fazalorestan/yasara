from app.stable_release_v1.stable_manifest import StableReleaseManifestBuilderV1

def test_stable_release_manifest():
    manifest = StableReleaseManifestBuilderV1().build()
    assert manifest.channel == "stable"
    assert manifest.minimum_tests_required >= 242
