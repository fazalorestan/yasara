class DesktopLaunchFlow:
    def flow(self):
        return {
            "ready": True,
            "steps": [
                "single_instance_check",
                "load_secure_config",
                "start_backend",
                "wait_for_backend_health",
                "open_main_window",
                "mount_dashboard",
                "run_smoke_test"
            ],
            "signal_only_default": True,
            "auto_trading_enabled_default": False,
            "safe_shutdown_required": True,
        }

desktop_launch_flow = DesktopLaunchFlow()
