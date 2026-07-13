from app.platform_core.broker_layer.capability_matrix import BrokerCapabilityMatrixService

def test_v500_alpha43_b_matrix(): assert BrokerCapabilityMatrixService().matrix()['features']['real_trading'] is False
