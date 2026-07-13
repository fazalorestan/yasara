from app.v500_alpha38_exchange_connectivity.service import ExchangeConnectivityFacadeV500Alpha38

def test_v500_alpha38_c_facade_latency():
 r=ExchangeConnectivityFacadeV500Alpha38().latency(); assert r is not None
