from app.v500_alpha38_exchange_connectivity.service import ExchangeConnectivityFacadeV500Alpha38

def test_v500_alpha38_c_facade_close_session():
 r=ExchangeConnectivityFacadeV500Alpha38().close_session(); assert r is not None
