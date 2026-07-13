from app.platform_core.licensing.enforcement.feature_gate import LicenseFeatureGate
def test_v500_alpha10_feature_gate_allowed():
    r = LicenseFeatureGate().check({"license_type": "demo"}, "BASIC_ANALYSIS")
    assert r["allowed"] is True
