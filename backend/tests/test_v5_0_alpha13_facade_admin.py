from app.v500_alpha13_license_ui.service import LicenseUIFacadeV500Alpha13
def test_v500_alpha13_facade_admin():
    assert LicenseUIFacadeV500Alpha13().admin_panel()["internal_only"] is True
