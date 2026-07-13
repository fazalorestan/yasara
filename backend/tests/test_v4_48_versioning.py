from app.platform_core.indicators.settings.versioning import YasaraPresetVersionRegistry

def test_v448_versioning():
    v = YasaraPresetVersionRegistry().versions()
    assert v["ready"] is True
    assert v["current"] == "v1.0"
