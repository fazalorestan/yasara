class WindowsDesktopStartupFlow:
    def flow(self):
        return {
            "ready": True,
            "flow": ["validate_environment", "load_secure_config", "start_backend", "connect_dashboard", "show_main_window"],
            "requires_auto_backup_before_update": True,
            "safe_mode_supported": True,
            "signal_only_default": True,
            "auto_trading_enabled_default": False,
        }

windows_desktop_startup_flow = WindowsDesktopStartupFlow()
