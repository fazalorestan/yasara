from app.platform_core.broker_layer.broker_diagnostics import broker_diagnostics_service
from app.platform_core.broker_layer.broker_health_monitor import broker_health_monitor_service
from app.platform_core.broker_layer.connection_status import broker_connection_status_service
from app.platform_core.broker_layer.latency_monitor import broker_latency_monitor_service
from app.platform_core.broker_layer.monitoring_readiness import broker_monitoring_readiness_gate
from app.platform_core.broker_layer.monitoring_report import broker_monitoring_report
from app.platform_core.broker_layer.monitoring_safety import broker_monitoring_safety_policy
from app.v500_alpha43_broker_monitoring.models import BrokerMonitoringSummaryV500Alpha43

class BrokerMonitoringFacadeV500Alpha43:
    def summary(self): return BrokerMonitoringSummaryV500Alpha43()
    def health(self): return broker_health_monitor_service.health()
    def connection_status(self): return broker_connection_status_service.status()
    def latency(self): return broker_latency_monitor_service.latency()
    def diagnostics(self): return broker_diagnostics_service.diagnostics()
    def safety(self): return broker_monitoring_safety_policy.policy()
    def report(self): return broker_monitoring_report.report()
    def readiness(self): return broker_monitoring_readiness_gate.run()
    def contract(self): return {"ready": True, "broker_layer": "package_d_monitoring_health", "execution_allowed": False}

broker_monitoring_facade_v500_alpha43 = BrokerMonitoringFacadeV500Alpha43()
