from app.platform_core.licensing.ui.admin_panel import LicenseAdminPanelContract
def test_v500_alpha13_admin_panel():
    c = LicenseAdminPanelContract().contract()
    assert c["internal_only"] is True
    assert c["requires_admin_permission"] is True
