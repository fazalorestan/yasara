from app.v500_alpha37_broker_connectivity.models import BrokerConnectivitySummaryV500Alpha37

def test_v500_alpha37_c_summary():
 s=BrokerConnectivitySummaryV500Alpha37(); assert s.ready and s.test_pack_size==60