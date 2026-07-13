class WindowsRealExeSmokeTestContract:
    def smoke(self):
        return {
            "ready": True,
            "checks": [
                "exe_file_exists",
                "app_launches",
                "backend_health_ok",
                "dashboard_loads",
                "signal_only_default",
                "auto_trading_off",
                "safe_shutdown"
            ],
            "requires_real_exe": True,
            "smoke_test_passed": False,
            "reason": "real_binary_not_generated_in_contract_package",
        }
windows_real_exe_smoke_test_contract = WindowsRealExeSmokeTestContract()
