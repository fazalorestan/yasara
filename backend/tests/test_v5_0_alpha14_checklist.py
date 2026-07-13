from app.platform_core.licensing.readiness.checklist import LicenseSecurityChecklist
def test_v500_alpha14_checklist():
    r = LicenseSecurityChecklist().checklist()
    assert r["ready"] is True
    assert len(r["items"]) >= 10
