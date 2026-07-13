from app.platform_core.indicators.settings.overrides import YasaraUserSettingsOverrideService

def test_v448_overrides():
    r = YasaraUserSettingsOverrideService().apply_override("default", {"min_score": 70})
    assert r["ready"] is True
    assert r["settings"]["min_score"] == 70
