from app.platform_core.licensing.validator import license_validator
def test_v500_alpha9_validator_auto_trade_block():
    r = license_validator.validate({"license_type": "enterprise", "features": ["AUTO_TRADING"]})
    assert r["valid"] is False
