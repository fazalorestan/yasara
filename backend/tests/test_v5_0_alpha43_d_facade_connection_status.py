from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_facade_connection_status():
 r=BrokerMonitoringFacadeV500Alpha43().connection_status(); assert r is not None
