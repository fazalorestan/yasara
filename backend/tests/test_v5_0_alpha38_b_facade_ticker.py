from app.v500_alpha38_exchange_market_data.service import ExchangeMarketDataFacadeV500Alpha38

def test_v500_alpha38_b_facade_ticker():
 r=ExchangeMarketDataFacadeV500Alpha38().ticker(); assert r is not None
