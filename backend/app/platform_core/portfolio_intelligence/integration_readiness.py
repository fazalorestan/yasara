from app.platform_core.portfolio_intelligence.integration_report import portfolio_integration_report_service

class PortfolioIntegrationReadinessGate:
    def run(self):
        report = portfolio_integration_report_service.report()
        return {"ready": report["ready"] and report["execution_allowed"] is False, "checks": {"report_ready": report["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

portfolio_integration_readiness_gate = PortfolioIntegrationReadinessGate()
