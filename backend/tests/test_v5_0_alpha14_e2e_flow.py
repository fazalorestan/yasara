from app.platform_core.licensing.readiness.e2e import LicenseE2EFlow
def test_v500_alpha14_e2e_flow():
    r = LicenseE2EFlow().run_demo_flow()
    assert r["ready"] is True
    assert r["execution_allowed"] is False
