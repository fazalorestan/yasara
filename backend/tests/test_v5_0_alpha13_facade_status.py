from app.v500_alpha13_license_ui.service import LicenseUIFacadeV500Alpha13
def test_v500_alpha13_facade_status():
    assert LicenseUIFacadeV500Alpha13().status_card("demo")["ready"] is True
