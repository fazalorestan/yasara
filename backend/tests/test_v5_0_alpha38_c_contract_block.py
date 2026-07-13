from app.v500_alpha38_exchange_connectivity.service import ExchangeConnectivityFacadeV500Alpha38

def test_v500_alpha38_c_contract_block(): assert ExchangeConnectivityFacadeV500Alpha38().contract()['execution_allowed'] is False
