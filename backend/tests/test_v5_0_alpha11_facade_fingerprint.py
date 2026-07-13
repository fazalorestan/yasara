from app.v500_alpha11_license_activation.service import LicenseActivationFacadeV500Alpha11
def test_v500_alpha11_facade_fingerprint():
    assert LicenseActivationFacadeV500Alpha11().fingerprint()["ready"] is True
