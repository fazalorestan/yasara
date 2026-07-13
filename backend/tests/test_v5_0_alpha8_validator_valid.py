from app.platform_core.indicators.signal_logic_expansion.validator import RuntimeSignalValidator
def test_v500_alpha8_validator_valid():
    s = {"direction": "WAIT", "confidence": 0, "execution_allowed": False}
    assert RuntimeSignalValidator().validate(s)["valid"] is True
