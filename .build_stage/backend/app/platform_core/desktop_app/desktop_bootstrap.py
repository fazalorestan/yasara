class DesktopBootstrapService:
    def bootstrap(self):
        return {"ready": True, "bootstrapped": True, "steps": ["load_config", "start_runtime", "connect_dashboard", "open_shell"], "exe_packaging_enabled": False, "real_execution_enabled": False}
desktop_bootstrap_service = DesktopBootstrapService()
