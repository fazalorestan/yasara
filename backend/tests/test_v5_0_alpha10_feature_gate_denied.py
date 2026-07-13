from app.platform_core.licensing.enforcement.feature_gate import LicenseFeatureGate
def test_v500_alpha10_feature_gate_denied():
    r = LicenseFeatureGate().check({"license_type": "demo"}, "EXPORT")
    assert r["allowed"] is False
