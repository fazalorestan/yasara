from app.platform_core.native_windows_launcher.report import native_windows_launcher_report_service
class NativeWindowsLauncherReadinessGate:
    def run(self):
        r=native_windows_launcher_report_service.report()
        return {'ready':r['ready'] and r['dashboard_bootstrap'] and not r['auto_trading_enabled'],'checks':r}
native_windows_launcher_readiness_gate=NativeWindowsLauncherReadinessGate()
