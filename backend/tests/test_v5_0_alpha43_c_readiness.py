from app.platform_core.broker_layer.order_readiness import BrokerOrderReadinessGate

def test_v500_alpha43_c_readiness(): assert BrokerOrderReadinessGate().run()['ready'] is True
