from app.platform_core.broker.safety import BrokerSafetyPolicy

def test_v500_alpha22_safety_policy():
    p=BrokerSafetyPolicy().policy(); assert p['live_execution_allowed'] is False; assert p['requires_risk_approval'] is True
