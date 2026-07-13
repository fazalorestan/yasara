from app.platform_core.exchange_layer.connectivity_report import exchange_connectivity_report_service

class ExchangeConnectivityReadinessGate:
    def run(self):
        report = exchange_connectivity_report_service.report()
        ready = report["ready"] and report["heartbeat"]["alive"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "heartbeat_alive": report["heartbeat"]["alive"],
                "websocket_live": False,
                "real_exchange_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

exchange_connectivity_readiness_gate = ExchangeConnectivityReadinessGate()
