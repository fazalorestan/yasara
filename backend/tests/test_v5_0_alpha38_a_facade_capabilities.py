from app.v500_alpha38_exchange_core.service import ExchangeCoreFacadeV500Alpha38

def test_v500_alpha38_a_facade_capabilities():
 r=ExchangeCoreFacadeV500Alpha38().capabilities(); assert r is not None
