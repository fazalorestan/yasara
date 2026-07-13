from app.v500_alpha38_exchange_core.service import ExchangeCoreFacadeV500Alpha38

def test_v500_alpha38_a_facade_readiness():
 r=ExchangeCoreFacadeV500Alpha38().readiness(); assert r is not None
