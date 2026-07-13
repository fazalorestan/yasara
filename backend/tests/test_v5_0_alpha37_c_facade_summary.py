from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_facade_summary():
 r=BrokerConnectivityFacadeV500Alpha37().summary(); assert r is not None
