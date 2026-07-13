from app.platform_core.licensing.manager.export_import import LicenseExportImportContract
def test_v500_alpha12_import():
    c = LicenseExportImportContract()
    blob = c.export_license({"license_type": "demo"})["export"]
    assert c.import_license(blob)["ready"] is True
