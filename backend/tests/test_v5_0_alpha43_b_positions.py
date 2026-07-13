from app.platform_core.broker_layer.position_contract import BrokerPositionContractService

def test_v500_alpha43_b_positions(): assert BrokerPositionContractService().positions()['count'] == 0
