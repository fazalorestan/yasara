from app.platform_core.licensing.ui.service import LicenseUIContractService
def test_v500_alpha13_ui_service_locks():
    s = LicenseUIContractService()
    assert s.feature_locks(s.sample_payload())["ready"] is True
