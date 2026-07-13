from app.v500_alpha11_license_activation.service import LicenseActivationFacadeV500Alpha11
def test_v500_alpha11_facade_revoke():
    r = LicenseActivationFacadeV500Alpha11().revoke_plan("KEY")
    assert r["ready"] is True
