from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_close_session():
 r=BrokerConnectivityFacadeV500Alpha37().close_session(); assert r is not None
