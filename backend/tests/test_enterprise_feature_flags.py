from app.enterprise_v1.feature_flags import FeatureFlagServiceV1, FeatureFlagV1

def test_feature_flag_enabled():
    assert FeatureFlagServiceV1().is_enabled([FeatureFlagV1(key="x", enabled=True)], "x") is True
