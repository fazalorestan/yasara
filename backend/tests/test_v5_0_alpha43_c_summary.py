from app.v500_alpha43_broker_order.models import BrokerOrderSummaryV500Alpha43

def test_v500_alpha43_c_summary():
 s=BrokerOrderSummaryV500Alpha43(); assert s.ready and s.test_pack_size==60
