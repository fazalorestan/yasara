class WindowsAppHealthService:
    def health(self):
        return {
            "ready": True,
            "app_health": "green",
            "bootstrap_ready": True,
            "runtime_shell_ready": True,
            "main_window_ready": True,
            "backend_connector_ready": True,
            "dashboard_host_ready": True,
            "crash_detected": False,
            "signal_only_mode": True,
            "auto_trading_enabled": False,
        }

windows_app_health_service = WindowsAppHealthService()
