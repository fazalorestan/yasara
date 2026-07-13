from app.platform_core.strategy_engine.allocation_report import strategy_allocation_report
class StrategyAllocationReadinessGate:
    def run(self):
        report = strategy_allocation_report.report()
        ready = report["ready"] and report["exposure"]["within_limits"] and report["execution_allowed"] is False
        return {"ready": ready, "checks": {"report_ready": report["ready"], "exposure_within_limits": report["exposure"]["within_limits"], "allocation_only": report["safety"]["allocation_only"], "real_execution_allowed": False, "broker_connection_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
strategy_allocation_readiness_gate = StrategyAllocationReadinessGate()
