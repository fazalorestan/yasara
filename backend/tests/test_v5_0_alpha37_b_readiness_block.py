from app.platform_core.broker_layer.orders_readiness import BrokerOrdersReadinessGate

def test_v500_alpha37_b_readiness_block(): assert BrokerOrdersReadinessGate().run()['execution_allowed'] is False