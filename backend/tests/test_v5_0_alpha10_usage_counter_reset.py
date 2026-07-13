from app.platform_core.licensing.enforcement.usage_counter import FeatureUsageCounter
def test_v500_alpha10_usage_counter_reset():
    c = FeatureUsageCounter()
    c.increment("A")
    assert c.reset()["usage"] == {}
