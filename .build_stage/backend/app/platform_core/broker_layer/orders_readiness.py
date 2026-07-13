from app.platform_core.broker_layer.account_report import broker_account_report_service
from app.platform_core.broker_layer.order_preview import broker_order_preview_service

class BrokerOrdersReadinessGate:
    def run(self):
        preview = broker_order_preview_service.preview()
        report = broker_account_report_service.report()
        ready = preview["ready"] and report["ready"] and preview["execution_allowed"] is False
        return {"ready": ready, "checks": {"preview_ready": preview["ready"], "report_ready": report["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

broker_orders_readiness_gate = BrokerOrdersReadinessGate()
