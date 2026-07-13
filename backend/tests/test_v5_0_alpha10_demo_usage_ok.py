from app.platform_core.licensing.enforcement.demo_limits import DemoLimitationEnforcer
def test_v500_alpha10_demo_usage_ok():
    r = DemoLimitationEnforcer().check_usage({"alerts": 1, "indicators": 1, "workspaces": 1})
    assert r["ready"] is True
