from app.platform_core.licensing.manager.service import LicenseManagerService
def test_v500_alpha12_manager_status():
    assert LicenseManagerService().status({"license_type": "demo"})["ready"] is True
