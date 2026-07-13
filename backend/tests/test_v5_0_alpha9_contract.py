from app.v500_alpha9_license_core.service import LicenseCoreFacadeV500Alpha9
def test_v500_alpha9_contract():
    c = LicenseCoreFacadeV500Alpha9().contract()
    assert c["offline_license_supported"] is True
    assert c["execution_allowed"] is False
