from app.platform_core.config_center.validation import ConfigValidator

def test_v435_validation():
    bad = ConfigValidator().validate({"live_execution_enabled": True})
    good = ConfigValidator().validate({"live_execution_enabled": False, "debug": False})
    assert bad.valid is False
    assert good.valid is True
