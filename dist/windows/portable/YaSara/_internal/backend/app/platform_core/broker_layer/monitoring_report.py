from app.platform_core.broker_layer.broker_diagnostics import broker_diagnostics_service
from app.platform_core.broker_layer.broker_health_monitor import broker_health_monitor_service
from app.platform_core.broker_layer.connection_status import broker_connection_status_service
from app.platform_core.broker_layer.latency_monitor import broker_latency_monitor_service
from app.platform_core.broker_layer.monitoring_safety import broker_monitoring_safety_policy

class BrokerMonitoringReport:
    def report(self):
        return {
            "ready": True,
            "health": broker_health_monitor_service.health(),
            "connection_status": broker_connection_status_service.status(),
            "latency": broker_latency_monitor_service.latency(),
            "diagnostics": broker_diagnostics_service.diagnostics(),
            "safety": broker_monitoring_safety_policy.policy(),
            "real_broker_connection_enabled": False,
            "real_account_read_enabled": False,
            "real_order_submit_enabled": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

broker_monitoring_report = BrokerMonitoringReport()

# Backward Compatibility
BrokerMonitoringReportService = BrokerMonitoringReport
broker_monitoring_report_service = broker_monitoring_report
