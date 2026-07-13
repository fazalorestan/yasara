from app.v500_alpha38_exchange_connectivity.service import ExchangeConnectivityFacadeV500Alpha38

def test_v500_alpha38_c_facade_summary():
 r=ExchangeConnectivityFacadeV500Alpha38().summary(); assert r is not None
