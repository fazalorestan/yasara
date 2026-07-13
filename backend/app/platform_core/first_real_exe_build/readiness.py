from app.platform_core.first_real_exe_build.report import first_real_exe_build_report_service
class FirstRealExeBuildReadinessGate:
    def run(self):
        r = first_real_exe_build_report_service.report()
        return {
            'ready': r['ready'] and r['signal_only_default'] and not r['auto_trading_enabled'],
            'checks': r
        }
first_real_exe_build_readiness_gate = FirstRealExeBuildReadinessGate()
