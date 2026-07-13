from app.platform_core.licensing.ui.service import LicenseUIContractService
def test_v500_alpha13_ui_service_countdown():
    s = LicenseUIContractService()
    assert s.countdown(s.sample_payload())["show_countdown"] is True
