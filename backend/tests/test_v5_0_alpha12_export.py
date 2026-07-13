from app.platform_core.licensing.manager.export_import import LicenseExportImportContract
def test_v500_alpha12_export():
    r = LicenseExportImportContract().export_license({"license_type": "demo"})
    assert r["ready"] is True
    assert r["format"] == "offline_signed_blob"
