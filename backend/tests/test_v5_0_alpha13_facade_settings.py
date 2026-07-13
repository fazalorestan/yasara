from app.v500_alpha13_license_ui.service import LicenseUIFacadeV500Alpha13
def test_v500_alpha13_facade_settings():
    assert LicenseUIFacadeV500Alpha13().settings_page()["ready"] is True
