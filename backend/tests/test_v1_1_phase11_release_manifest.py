from app.v11_release_candidate.release_manifest import V11ReleaseManifestBuilder

def test_v11_release_manifest():
    manifest = V11ReleaseManifestBuilder().build()
    assert manifest.version == "1.1.0-rc1"
    assert manifest.live_trading_enabled is False
    assert all(item.passed for item in manifest.checklist)
