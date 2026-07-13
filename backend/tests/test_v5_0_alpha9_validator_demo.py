from app.platform_core.licensing.validator import license_validator
def test_v500_alpha9_validator_demo():
    r = license_validator.validate({"license_type": "demo"})
    assert r["valid"] is True
    assert "BASIC_ANALYSIS" in r["features"]
