from app.v500_alpha43_broker_core.models import BrokerCoreSummaryV500Alpha43

def test_v500_alpha43_a_summary():
 s=BrokerCoreSummaryV500Alpha43(); assert s.ready and s.test_pack_size==60
