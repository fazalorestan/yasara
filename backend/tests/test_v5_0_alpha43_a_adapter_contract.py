from app.platform_core.broker_layer.broker_adapter_contract import BrokerAdapterContractService

def test_v500_alpha43_a_adapter_contract(): assert BrokerAdapterContractService().contract()['real_connection_enabled'] is False
