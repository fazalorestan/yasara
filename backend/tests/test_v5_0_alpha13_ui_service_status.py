from app.platform_core.licensing.ui.service import LicenseUIContractService
def test_v500_alpha13_ui_service_status():
    s = LicenseUIContractService()
    assert s.status_card(s.sample_payload())["ready"] is True
