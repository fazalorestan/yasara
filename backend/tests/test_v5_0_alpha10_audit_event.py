from app.platform_core.licensing.enforcement.audit import LicenseAuditEventPublisher
def test_v500_alpha10_audit_event():
    r = LicenseAuditEventPublisher().publish("feature_check", {"license_type": "demo"})
    assert r["ready"] is True
    assert r["event"]["name"] == "LicenseAccessChecked"
