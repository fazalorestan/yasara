from app.platform_core.licensing.activation.audit import LicenseActivationAuditPublisher
def test_v500_alpha11_audit():
    r = LicenseActivationAuditPublisher().publish("activate", "demo")
    assert r["ready"] is True
    assert r["event"]["name"] == "LicenseActivationChanged"
