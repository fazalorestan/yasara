class NativeDesktopHealthService:
    def health(self):
        return {
            "ready": True,
            "desktop_host": "green",
            "backend_supervisor": "green",
            "dashboard_host": "green",
            "single_instance_guard": "green",
            "safe_shutdown": "green",
            "signal_only_mode": True,
            "auto_trading_enabled": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

native_desktop_health_service = NativeDesktopHealthService()
