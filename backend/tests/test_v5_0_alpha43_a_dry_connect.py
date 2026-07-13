from app.platform_core.broker_layer.broker_adapter_contract import BrokerAdapterContractService

def test_v500_alpha43_a_dry_connect(): assert BrokerAdapterContractService().dry_connect()['connected'] is False
