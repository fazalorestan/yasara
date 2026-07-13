from app.platform_core.licensing.enforcement.service import LicenseEnforcementService
def test_v500_alpha10_service_check_feature():
    r = LicenseEnforcementService().check_feature({"license_type": "demo"}, "BASIC_ANALYSIS")
    assert r["allowed"] is True
