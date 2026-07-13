from app.platform_core.indicators.handoff.release_manifest import IndicatorReleaseManifestService

def test_v450_release_manifest():
    m = IndicatorReleaseManifestService().manifest()
    assert m["indicator"] == "yasara"
    assert m["status"] == "ready_for_v5"
    assert "runtime" in m["contracts"]
