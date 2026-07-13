from app.v500_alpha38_exchange_core.service import ExchangeCoreFacadeV500Alpha38

def test_v500_alpha38_a_facade_default_exchange():
 r=ExchangeCoreFacadeV500Alpha38().default_exchange(); assert r is not None
