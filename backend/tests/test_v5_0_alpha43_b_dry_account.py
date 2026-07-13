from app.platform_core.broker_layer.account_contract import BrokerAccountContractService

def test_v500_alpha43_b_dry_account(): assert BrokerAccountContractService().dry_account()['real_account'] is False
