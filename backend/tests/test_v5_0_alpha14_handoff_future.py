from app.platform_core.licensing.readiness.handoff import LicenseSubsystemHandoff
def test_v500_alpha14_handoff_future():
    r = LicenseSubsystemHandoff().handoff()
    assert "online_license_server" in r["future_extensions"]
