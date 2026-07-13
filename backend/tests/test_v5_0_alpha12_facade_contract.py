from app.v500_alpha12_license_manager.service import LicenseManagerFacadeV500Alpha12
def test_v500_alpha12_facade_contract():
    c = LicenseManagerFacadeV500Alpha12().contract()
    assert c["admin_ui_future_ready"] is True
    assert c["execution_allowed"] is False
