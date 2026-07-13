from app.platform_core.in_process_backend_runner.report import in_process_backend_runner_report_service
class InProcessBackendRunnerReadinessGate:
    def run(self):
        r=in_process_backend_runner_report_service.report()
        return {'ready':r['ready'] and r['fixes_recursive_frozen_exe_launch'] and not r['auto_trading_enabled'],'checks':r}
in_process_backend_runner_readiness_gate=InProcessBackendRunnerReadinessGate()
