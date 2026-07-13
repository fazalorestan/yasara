from app.production_packaging_v1.runtime_validator import RuntimeValidatorV1

def test_runtime_validator_ok():
    result = RuntimeValidatorV1().validate("3.12.10", True)
    assert result.ok is True
