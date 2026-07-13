from app.v500_alpha38_exchange_connectivity.service import ExchangeConnectivityFacadeV500Alpha38

def test_v500_alpha38_c_facade_latency_grade():
 r=ExchangeConnectivityFacadeV500Alpha38().latency_grade(); assert r is not None
