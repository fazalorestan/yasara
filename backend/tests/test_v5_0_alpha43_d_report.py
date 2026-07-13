from app.platform_core.broker_layer.monitoring_report import BrokerMonitoringReport

def test_v500_alpha43_d_report(): assert BrokerMonitoringReport().report()['ready'] is True
