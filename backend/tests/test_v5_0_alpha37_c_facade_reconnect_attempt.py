from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_reconnect_attempt():
 r=BrokerConnectivityFacadeV500Alpha37().reconnect_attempt(); assert r is not None
