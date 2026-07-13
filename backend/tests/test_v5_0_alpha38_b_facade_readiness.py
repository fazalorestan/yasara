from app.v500_alpha38_exchange_market_data.service import ExchangeMarketDataFacadeV500Alpha38

def test_v500_alpha38_b_facade_readiness():
 r=ExchangeMarketDataFacadeV500Alpha38().readiness(); assert r is not None
