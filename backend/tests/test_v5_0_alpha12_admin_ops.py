from app.platform_core.licensing.manager.admin_ops import AdminLicenseOperationsContract
def test_v500_alpha12_admin_ops():
    r = AdminLicenseOperationsContract().operations()
    assert r["requires_admin_permission"] is True
    assert "create_license" in r["operations"]
