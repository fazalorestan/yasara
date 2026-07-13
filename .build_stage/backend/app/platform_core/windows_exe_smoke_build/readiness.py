from app.platform_core.windows_exe_smoke_build.report import windows_exe_smoke_build_report_service
class WindowsExeSmokeBuildReadinessGate:
    def run(self):
        r=windows_exe_smoke_build_report_service.report()
        ready=r['ready'] and r['build_attempt']['requires_execute_flag'] and r['build_attempt']['requires_tests_passed'] and r['exe_check']['required_for_smoke'] and r['launch_smoke']['signal_only_mode'] and r['diagnostics']['dashboard_visible'] and r['real_execution_enabled'] is False and r['real_broker_connection_enabled'] is False
        return {'ready': ready,'checks':{'build_attempt_ready':r['build_attempt']['ready'],'requires_execute_flag':r['build_attempt']['requires_execute_flag'],'exe_check_ready':r['exe_check']['ready'],'smoke_contract_ready':r['launch_smoke']['ready'],'diagnostics_ready':r['diagnostics']['ready'],'signal_only_mode':r['launch_smoke']['signal_only_mode'],'auto_trading_enabled':r['launch_smoke']['auto_trading_enabled']}}
windows_exe_smoke_build_readiness_gate=WindowsExeSmokeBuildReadinessGate()
