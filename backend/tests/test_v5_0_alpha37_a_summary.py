from app.v500_alpha37_broker_core.models import BrokerCoreSummaryV500Alpha37

def test_v500_alpha37_a_summary():
 s=BrokerCoreSummaryV500Alpha37(); assert s.ready and s.test_pack_size==60