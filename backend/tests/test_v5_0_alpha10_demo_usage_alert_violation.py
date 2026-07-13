from app.platform_core.licensing.enforcement.demo_limits import DemoLimitationEnforcer
def test_v500_alpha10_demo_usage_alert_violation():
    r = DemoLimitationEnforcer().check_usage({"alerts": 11})
    assert "alert_limit_exceeded" in r["violations"]
