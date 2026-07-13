from app.platform_core.licensing.enforcement.demo_limits import DemoLimitationEnforcer
def test_v500_alpha10_demo_usage_indicator_violation():
    r = DemoLimitationEnforcer().check_usage({"indicators": 3})
    assert "indicator_limit_exceeded" in r["violations"]
