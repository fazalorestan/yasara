from app.platform_core.licensing.readiness.compatibility import LicenseCompatibilityMatrix
def test_v500_alpha14_compatibility_demo():
    r = LicenseCompatibilityMatrix().matrix()
    assert r["demo_supported"] is True
    assert r["trial_14_days_supported"] is True
    assert r["trial_30_days_supported"] is True
