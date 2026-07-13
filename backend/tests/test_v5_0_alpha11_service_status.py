from app.platform_core.licensing.activation.service import LicenseActivationService
def test_v500_alpha11_service_status():
    r = LicenseActivationService().status({"license_key": "K", "license_type": "pro"})
    assert r["ready"] is True
    assert r["slots"] == 2
