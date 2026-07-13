from app.platform_core.exchange_layer.market_data_report import exchange_market_data_report_service

class ExchangeMarketDataReadinessGate:
    def run(self):
        report = exchange_market_data_report_service.report()
        ready = report["ready"] and report["safety"]["market_data_only"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "market_data_only": report["safety"]["market_data_only"],
                "real_exchange_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

exchange_market_data_readiness_gate = ExchangeMarketDataReadinessGate()
