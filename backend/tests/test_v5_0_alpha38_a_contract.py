from app.platform_core.exchange_layer.contract import ExchangeContractService

def test_v500_alpha38_a_contract(): assert ExchangeContractService().contract()['execution_allowed'] is False