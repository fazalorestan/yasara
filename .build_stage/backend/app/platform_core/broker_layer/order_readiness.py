from app.platform_core.broker_layer.order_report import broker_order_report
class BrokerOrderReadinessGate:
    def run(self):
        report = broker_order_report.report()
        ready = report["ready"] and report["order_mapping"]["mapped"] and report["execution_allowed"] is False
        return {"ready": ready, "checks": {"report_ready": report["ready"], "order_mapped": report["order_mapping"]["mapped"], "paper_routing_only": report["safety"]["paper_routing_only"], "real_broker_connection_allowed": False, "real_order_submit_allowed": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
broker_order_readiness_gate = BrokerOrderReadinessGate()
