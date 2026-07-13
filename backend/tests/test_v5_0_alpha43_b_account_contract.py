from app.platform_core.broker_layer.account_contract import BrokerAccountContractService

def test_v500_alpha43_b_account_contract(): assert BrokerAccountContractService().contract()['real_account_read_enabled'] is False
