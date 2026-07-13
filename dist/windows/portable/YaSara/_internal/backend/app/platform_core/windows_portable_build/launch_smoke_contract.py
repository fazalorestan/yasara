class WindowsPortableLaunchSmokeContract:
    def smoke(self):
        return {"ready": True, "checks": ["portable_folder_exists", "entrypoint_exists", "backend_starts", "dashboard_loads", "signal_only_default", "auto_trading_off"], "expected_result": "pass", "actual_result": "contract_only", "final_exe_generated": False}
windows_portable_launch_smoke_contract = WindowsPortableLaunchSmokeContract()
