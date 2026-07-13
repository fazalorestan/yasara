from app.platform_core.licensing.enforcement.usage_counter import FeatureUsageCounter
def test_v500_alpha10_usage_counter_increment():
    c = FeatureUsageCounter()
    assert c.increment("A")["count"] == 1
    assert c.increment("A")["count"] == 2
