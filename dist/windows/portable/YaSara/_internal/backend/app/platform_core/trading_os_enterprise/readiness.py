from app.platform_core.trading_os_enterprise.report import trading_os_enterprise_report_service


class TradingOSEnterpriseReadinessGate:
    def run(self):
        report = trading_os_enterprise_report_service.report()
        return {
            "ready": (
                report["ready"]
                and report["role_based_workspaces"]
                and report["real_backend_data_only"]
                and not report["mock_data"]
                and not report["auto_trading_enabled"]
            ),
            "checks": report,
        }


trading_os_enterprise_readiness_gate = TradingOSEnterpriseReadinessGate()
