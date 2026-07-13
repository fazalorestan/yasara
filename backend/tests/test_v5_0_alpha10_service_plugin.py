from app.platform_core.licensing.enforcement.service import LicenseEnforcementService
def test_v500_alpha10_service_plugin():
    r = LicenseEnforcementService().check_plugin({"license_type": "demo"}, "yasara_indicator")
    assert r["allowed"] is True
