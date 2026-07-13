from app.platform_core.licensing.manager.status import LicenseStatusReporter
def test_v500_alpha12_status_invalid():
    r = LicenseStatusReporter().status({"license_type": "bad"})
    assert r["ready"] is False
