from app.platform_core.licensing.manager.demo_renewal import DemoRenewalPolicy
def test_v500_alpha12_demo_can_renew():
    p = DemoRenewalPolicy()
    assert p.can_renew(0) is True
    assert p.can_renew(1) is False
