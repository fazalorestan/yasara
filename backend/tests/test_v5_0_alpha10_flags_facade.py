from app.v500_alpha10_license_enforcement.service import LicenseEnforcementFacadeV500Alpha10
def test_v500_alpha10_flags_facade():
    r = LicenseEnforcementFacadeV500Alpha10().flags("pro")
    assert r["ready"] is True
    assert r["flags"]["feature.advanced_ai"] is True
