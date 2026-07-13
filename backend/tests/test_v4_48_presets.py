from app.platform_core.indicators.settings.presets import YasaraPresetRegistry

def test_v448_presets():
    r = YasaraPresetRegistry()
    p = r.seed_defaults()
    assert "default" in p
    assert "scalping" in p
    assert p["conservative"]["settings"]["min_score"] == 75
