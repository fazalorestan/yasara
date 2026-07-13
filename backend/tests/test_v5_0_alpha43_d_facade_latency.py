from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_facade_latency():
 r=BrokerMonitoringFacadeV500Alpha43().latency(); assert r is not None
