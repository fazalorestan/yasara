from app.v500_alpha15_market_data.service import MarketDataFacadeV500Alpha15
def test_v500_alpha15_facade_contract():
    c = MarketDataFacadeV500Alpha15().contract()
    assert c["real_exchange_connection"] is False
    assert c["execution_allowed"] is False
