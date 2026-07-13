from app.v500_alpha12_license_manager.service import LicenseManagerFacadeV500Alpha12
def test_v500_alpha12_facade_status():
    assert LicenseManagerFacadeV500Alpha12().status("demo")["ready"] is True
