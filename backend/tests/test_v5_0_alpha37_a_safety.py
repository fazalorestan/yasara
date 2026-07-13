from app.platform_core.broker_layer.safety import BrokerExecutionSafetyContract

def test_v500_alpha37_a_safety(): assert BrokerExecutionSafetyContract().policy()['dry_run_only'] is True