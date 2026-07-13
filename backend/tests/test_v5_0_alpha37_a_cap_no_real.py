from app.platform_core.broker_layer.capabilities import BrokerCapabilityService

def test_v500_alpha37_a_cap_no_real(): assert BrokerCapabilityService().detect({'broker_id':'b'})['real_execution_capable'] is False