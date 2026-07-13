from app.v500_alpha37_broker_enterprise.models import BrokerEnterpriseSummaryV500Alpha37

def test_v500_alpha37_d_summary():
 s=BrokerEnterpriseSummaryV500Alpha37(); assert s.ready and s.test_pack_size==65