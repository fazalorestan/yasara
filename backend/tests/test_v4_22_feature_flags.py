from app.platform_core.governance.feature_flags import FeatureFlagCenter

def test_v422_feature_flags():
    f=FeatureFlagCenter(); f.set_global('advanced_ai', True); assert f.is_enabled('advanced_ai') is True; assert f.is_enabled('missing') is False
