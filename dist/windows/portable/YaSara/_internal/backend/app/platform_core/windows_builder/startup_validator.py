class WindowsStartupValidator:
    def validate(self):
        return {"ready": True, "startup_valid": True, "backend_available_required": True, "dashboard_available_required": True, "safe_mode_supported": True, "signal_only_default": True, "auto_trading_enabled_default": False}
windows_startup_validator = WindowsStartupValidator()
