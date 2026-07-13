from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_reconnect_policy():
 r=BrokerConnectivityFacadeV500Alpha37().reconnect_policy(); assert r is not None
