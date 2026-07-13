from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_timeout_check():
 r=BrokerConnectivityFacadeV500Alpha37().timeout_check(); assert r is not None
