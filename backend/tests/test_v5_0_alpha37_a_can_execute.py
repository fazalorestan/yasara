from app.platform_core.broker_layer.safety import BrokerExecutionSafetyContract

def test_v500_alpha37_a_can_execute(): assert BrokerExecutionSafetyContract().can_execute()['allowed'] is False