from app.platform_core.licensing.manager.service import LicenseManagerService
def test_v500_alpha12_manager_plan():
    assert LicenseManagerService().plan("pro", 365)["license_type"] == "pro"
