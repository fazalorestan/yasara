from app.platform_core.licensing.readiness.handoff import LicenseSubsystemHandoff
def test_v500_alpha14_handoff():
    r = LicenseSubsystemHandoff().handoff()
    assert r["ready"] is True
    assert "license_core" in r["completed"]
