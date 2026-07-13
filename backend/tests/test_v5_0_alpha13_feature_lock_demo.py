from app.platform_core.licensing.ui.feature_lock import FeatureLockStateBuilder
def test_v500_alpha13_feature_lock_demo():
    r = FeatureLockStateBuilder().build({"license_type": "demo"}, ["BASIC_ANALYSIS", "EXPORT"])
    assert r["items"][0]["locked"] is False
    assert r["items"][1]["locked"] is True
