from app.final_release_v1.final_manifest import FinalReleaseManifestBuilderV1

def test_final_release_manifest():
    manifest = FinalReleaseManifestBuilderV1().build()
    assert manifest.version == "1.0.0"
    assert manifest.live_trading_enabled_by_default is False
