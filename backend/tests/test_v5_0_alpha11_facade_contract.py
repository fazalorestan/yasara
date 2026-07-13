from app.v500_alpha11_license_activation.service import LicenseActivationFacadeV500Alpha11
def test_v500_alpha11_facade_contract():
    c = LicenseActivationFacadeV500Alpha11().contract()
    assert c["offline_activation_supported"] is True
    assert c["execution_allowed"] is False
