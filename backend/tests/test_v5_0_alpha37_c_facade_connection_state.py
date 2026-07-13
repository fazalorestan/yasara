from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_connection_state():
 r=BrokerConnectivityFacadeV500Alpha37().connection_state(); assert r is not None
