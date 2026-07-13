from app.platform_core.broker_layer.account_report import broker_account_report_service
from app.platform_core.broker_layer.connectivity_report import broker_connectivity_report_service
from app.platform_core.broker_layer.service import broker_layer_core_service
class BrokerEnterpriseReportBuilder:
    def build(self):
        return {"ready": True, "sprint": "v5.0-alpha.37", "name": "Broker Abstraction Layer", "packages": ["A-Core-Capabilities", "B-Orders-Account", "C-Session-Connectivity", "D-Enterprise"], "core_status": broker_layer_core_service.status(), "orders_account_report": broker_account_report_service.report(), "connectivity_report": broker_connectivity_report_service.report(), "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
broker_enterprise_report_builder = BrokerEnterpriseReportBuilder()
