from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_facade_health():
 r=BrokerMonitoringFacadeV500Alpha43().health(); assert r is not None
