from app.v500_alpha43_broker_monitoring.models import BrokerMonitoringSummaryV500Alpha43

def test_v500_alpha43_d_summary():
 s=BrokerMonitoringSummaryV500Alpha43(); assert s.ready and s.test_pack_size==60
