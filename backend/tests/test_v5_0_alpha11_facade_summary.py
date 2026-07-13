from app.v500_alpha11_license_activation.service import LicenseActivationFacadeV500Alpha11
def test_v500_alpha11_facade_summary():
    assert LicenseActivationFacadeV500Alpha11().summary().ready is True
