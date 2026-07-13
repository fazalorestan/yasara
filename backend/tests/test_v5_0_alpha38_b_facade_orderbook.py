from app.v500_alpha38_exchange_market_data.service import ExchangeMarketDataFacadeV500Alpha38

def test_v500_alpha38_b_facade_orderbook():
 r=ExchangeMarketDataFacadeV500Alpha38().orderbook(); assert r is not None
