from app.platform_core.licensing.validator import license_validator
def test_v500_alpha9_validator_invalid():
    r = license_validator.validate({"license_type": "bad"})
    assert r["valid"] is False
