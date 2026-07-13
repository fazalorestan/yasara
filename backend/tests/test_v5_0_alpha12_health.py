from app.platform_core.licensing.manager.health import LicenseHealthCheck
def test_v500_alpha12_health():
    r = LicenseHealthCheck().check()
    assert r["ready"] is True
    assert r["execution_allowed"] is False
