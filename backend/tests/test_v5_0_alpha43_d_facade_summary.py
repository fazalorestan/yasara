from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_facade_summary():
 r=BrokerMonitoringFacadeV500Alpha43().summary(); assert r is not None
