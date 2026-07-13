class DesktopSafeShutdownController:
    def policy(self):
        return {
            "ready": True,
            "stop_new_orders_first": True,
            "force_signal_only": True,
            "stop_backend_gracefully": True,
            "flush_logs": True,
            "save_window_state": True,
            "shutdown_timeout_seconds": 10,
        }

desktop_safe_shutdown_controller = DesktopSafeShutdownController()
