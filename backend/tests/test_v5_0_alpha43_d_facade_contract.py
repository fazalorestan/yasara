from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_facade_contract():
 r=BrokerMonitoringFacadeV500Alpha43().contract(); assert r is not None
