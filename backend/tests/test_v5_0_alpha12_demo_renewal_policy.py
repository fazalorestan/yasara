from app.platform_core.licensing.manager.demo_renewal import DemoRenewalPolicy
def test_v500_alpha12_demo_renewal_policy():
    p = DemoRenewalPolicy().policy()
    assert p["max_renewals"] == 1
    assert p["auto_trading_allowed"] is False
