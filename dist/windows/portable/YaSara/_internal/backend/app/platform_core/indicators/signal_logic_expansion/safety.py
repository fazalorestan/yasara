class RuntimeSignalSafetyReport:
    def report(self):
        return {
            "ready": True,
            "analysis_only": True,
            "auto_trade_enabled": False,
            "live_execution_enabled": False,
            "exchange_orders_allowed": False,
            "dashboard_changed": False,
            "mode": "runtime_signal_safety",
        }

runtime_signal_safety_report = RuntimeSignalSafetyReport()
