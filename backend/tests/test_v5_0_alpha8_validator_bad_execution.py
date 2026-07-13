from app.platform_core.indicators.signal_logic_expansion.validator import RuntimeSignalValidator
def test_v500_alpha8_validator_bad_execution():
    s = {"direction": "LONG", "confidence": 50, "execution_allowed": True}
    assert "execution_must_remain_false" in RuntimeSignalValidator().validate(s)["errors"]
