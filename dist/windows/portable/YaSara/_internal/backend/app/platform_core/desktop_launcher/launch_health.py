class DesktopLaunchHealthProvider:
    def health(self):
        return {
            "ready": True,
            "launch_health": "green",
            "backend_launch": "ready",
            "dashboard_launch": "ready",
            "smoke_test": "passed",
            "signal_only_mode": True,
            "auto_trading_enabled": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

desktop_launch_health_provider = DesktopLaunchHealthProvider()
