from app.platform_core.licensing.enforcement.demo_limits import DemoLimitationEnforcer
def test_v500_alpha10_demo_usage_workspace_violation():
    r = DemoLimitationEnforcer().check_usage({"workspaces": 2})
    assert "workspace_limit_exceeded" in r["violations"]
