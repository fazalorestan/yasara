from app.platform_core.licensing.manager.service import LicenseManagerService
def test_v500_alpha12_manager_health():
    assert LicenseManagerService().health()["ready"] is True
