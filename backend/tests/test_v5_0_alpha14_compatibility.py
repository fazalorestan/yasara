from app.platform_core.licensing.readiness.compatibility import LicenseCompatibilityMatrix
def test_v500_alpha14_compatibility():
    r = LicenseCompatibilityMatrix().matrix()
    assert r["v5_compatible"] is True
    assert r["offline_mode"] is True
