from app.platform_core.licensing.ui.service import LicenseUIContractService
def test_v500_alpha13_ui_service_full():
    s = LicenseUIContractService()
    r = s.full_ui_contract(s.sample_payload())
    assert r["ready"] is True
    assert r["execution_allowed"] is False
