from app.platform_core.execution_engine.routing_report import order_routing_report

class OrderRoutingReadinessGate:
    def run(self):
        report = order_routing_report.report()
        ready = report["ready"] and report["validation"]["valid"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "order_valid": report["validation"]["valid"],
                "pre_trade_passed": report["pre_trade_checks"]["passed"],
                "routing_only": report["safety"]["routing_only"],
                "real_execution_allowed": False,
                "broker_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

order_routing_readiness_gate = OrderRoutingReadinessGate()
