from app.platform_core.windows_exe_smoke_build.exe_existence_check import windows_exe_existence_check
from app.platform_core.windows_exe_smoke_build.launch_smoke import windows_exe_launch_smoke_contract
class WindowsExeSmokeDashboardStatus:
    def status(self):
        exe=windows_exe_existence_check.check(); smoke=windows_exe_launch_smoke_contract.smoke()
        return {'ready': True,'build_id':'2026.51.A.001','exe_exists':exe['exists'],'smoke_status':smoke['smoke_status'],'status':'pending_local_build','signal_only_mode':True,'auto_trading_enabled':False,'hardcoded_dashboard':False}
windows_exe_smoke_dashboard_status=WindowsExeSmokeDashboardStatus()
