from app.platform_core.execution_engine.audit_contract import execution_audit_contract_service
from app.platform_core.execution_engine.compliance_log import execution_compliance_log_service
from app.platform_core.execution_engine.execution_metrics import execution_metrics_service
from app.platform_core.execution_engine.execution_statistics import execution_statistics_service
from app.platform_core.execution_engine.execution_timeline import execution_timeline_service
from app.platform_core.execution_engine.analytics_safety import execution_analytics_safety_policy

class ExecutionAnalyticsReport:
    def report(self):
        return {
            "ready": True,
            "metrics": execution_metrics_service.metrics(),
            "timeline": execution_timeline_service.timeline(),
            "audit_contract": execution_audit_contract_service.contract(),
            "audit_record": execution_audit_contract_service.record_stub(),
            "compliance_log": execution_compliance_log_service.log(),
            "statistics": execution_statistics_service.statistics(),
            "safety": execution_analytics_safety_policy.policy(),
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

execution_analytics_report = ExecutionAnalyticsReport()
