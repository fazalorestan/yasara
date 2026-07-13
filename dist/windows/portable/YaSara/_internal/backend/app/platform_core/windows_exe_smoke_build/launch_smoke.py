class WindowsExeLaunchSmokeContract:
    def smoke(self):
        return {'ready': True,'requires_exe_exists':True,'launch_timeout_seconds':30,'checks':['process_starts','backend_health','dashboard_loads','safe_shutdown'],'smoke_status':'pending_until_local_build','auto_trading_enabled':False,'signal_only_mode':True}
windows_exe_launch_smoke_contract=WindowsExeLaunchSmokeContract()
