from app.platform_core.licensing.ui.settings_contract import LicenseSettingsPageContract
def test_v500_alpha13_settings_page():
    c = LicenseSettingsPageContract().contract()
    assert "license_status" in c["sections"]
    assert "enter_license_key" in c["actions"]
