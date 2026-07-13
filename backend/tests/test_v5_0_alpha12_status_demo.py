from app.platform_core.licensing.manager.status import LicenseStatusReporter
def test_v500_alpha12_status_demo():
    r = LicenseStatusReporter().status({"license_type": "demo"})
    assert r["ready"] is True
    assert r["license_type"] == "demo"
