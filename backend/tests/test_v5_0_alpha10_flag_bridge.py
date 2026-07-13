from app.platform_core.licensing.enforcement.feature_flag_bridge import LicenseFeatureFlagBridge
def test_v500_alpha10_flag_bridge():
    r = LicenseFeatureFlagBridge().build_flags({"license_type": "demo"})
    assert r["flags"]["feature.basic_analysis"] is True
