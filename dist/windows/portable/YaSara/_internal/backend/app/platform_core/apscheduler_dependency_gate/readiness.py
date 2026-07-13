from app.platform_core.apscheduler_dependency_gate.report import apscheduler_dependency_gate_report_service
class APSchedulerDependencyGateReadinessGate:
    def run(self):
        r=apscheduler_dependency_gate_report_service.report()
        return {'ready':r['ready'] and r['apscheduler_gate'] and r['legacy_j_test_fix'] and not r['auto_trading_enabled'],'checks':r}
apscheduler_dependency_gate_readiness_gate=APSchedulerDependencyGateReadinessGate()
