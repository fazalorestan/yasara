from app.platform_core.indicators.sandbox.security_validator import IndicatorSecurityPolicyValidator

def test_v500_alpha3_security_validator():
    v = IndicatorSecurityPolicyValidator()
    assert v.validate({})["valid"] is True
    assert v.validate({"allow_live_execution": True})["valid"] is False
