from app.v500_alpha38_exchange_market_data.service import ExchangeMarketDataFacadeV500Alpha38

def test_v500_alpha38_b_contract_block(): assert ExchangeMarketDataFacadeV500Alpha38().contract()['execution_allowed'] is False
