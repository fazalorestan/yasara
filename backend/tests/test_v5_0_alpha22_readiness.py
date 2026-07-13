from app.platform_core.broker.readiness import BrokerLayerReadinessGate

def test_v500_alpha22_readiness():
    r=BrokerLayerReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
