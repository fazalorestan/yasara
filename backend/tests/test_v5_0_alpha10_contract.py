from app.v500_alpha10_license_enforcement.service import LicenseEnforcementFacadeV500Alpha10
def test_v500_alpha10_contract():
    c = LicenseEnforcementFacadeV500Alpha10().contract()
    assert c["demo_limits_enforced"] is True
    assert c["execution_allowed"] is False
