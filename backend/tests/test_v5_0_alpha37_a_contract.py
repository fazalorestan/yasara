from app.platform_core.broker_layer.contract import BrokerContractService

def test_v500_alpha37_a_contract(): assert BrokerContractService().contract()['execution_allowed'] is False