from app.v500_alpha10_license_enforcement.service import LicenseEnforcementFacadeV500Alpha10
def test_v500_alpha10_facade():
    f = LicenseEnforcementFacadeV500Alpha10()
    assert f.summary().ready is True
    assert f.check_feature("BASIC_ANALYSIS", "demo")["allowed"] is True
