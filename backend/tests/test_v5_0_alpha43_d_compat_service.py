from app.platform_core.broker_layer.monitoring_report import BrokerMonitoringReportService, broker_monitoring_report_service

def test_v500_alpha43_d_compat_service(): assert BrokerMonitoringReportService().report()['ready'] and broker_monitoring_report_service.report()['ready']
