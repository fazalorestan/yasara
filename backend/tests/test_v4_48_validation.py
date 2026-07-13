from app.platform_core.indicators.settings.validation import YasaraSettingsValidator

def test_v448_validation():
    v = YasaraSettingsValidator()
    assert v.validate({"ema_fast": 21, "ema_mid": 55, "ema_slow": 200, "min_score": 60}).valid is True
    assert v.validate({"ema_fast": 55, "ema_mid": 21, "ema_slow": 200, "min_score": 60}).valid is False
