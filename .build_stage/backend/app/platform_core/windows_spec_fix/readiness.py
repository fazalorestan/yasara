from app.platform_core.windows_spec_fix.report import windows_spec_output_fix_report_service
class WindowsSpecOutputFixReadinessGate:
    def run(self):
        r=windows_spec_output_fix_report_service.report()
        return {'ready':r['ready'] and r['standard_output'].endswith('YaSara.exe') and not r['auto_trading_enabled'],'checks':r}
windows_spec_output_fix_readiness_gate=WindowsSpecOutputFixReadinessGate()
