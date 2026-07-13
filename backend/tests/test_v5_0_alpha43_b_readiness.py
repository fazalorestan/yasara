from app.platform_core.broker_layer.account_readiness import BrokerAccountReadinessGate

def test_v500_alpha43_b_readiness(): assert BrokerAccountReadinessGate().run()['ready'] is True
