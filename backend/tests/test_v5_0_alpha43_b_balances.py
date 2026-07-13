from app.platform_core.broker_layer.balance_contract import BrokerBalanceContractService

def test_v500_alpha43_b_balances(): assert len(BrokerBalanceContractService().balances()['balances']) == 2
