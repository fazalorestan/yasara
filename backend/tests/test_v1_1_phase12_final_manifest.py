from app.v11_final_release.manifest import FinalReleaseManifestBuilderV11

def test_final_release_manifest():
    manifest = FinalReleaseManifestBuilderV11().build()
    assert manifest.version == "1.1.0"
    assert manifest.live_trading_enabled is False
    assert all(check.passed for check in manifest.checks)
