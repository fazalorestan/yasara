from app.platform_core.licensing.enforcement.demo_limits import DemoLimitationEnforcer
def test_v500_alpha10_demo_limits():
    limits = DemoLimitationEnforcer().limits()
    assert limits["alert_limit"] == 10
    assert limits["auto_trading_allowed"] is False
