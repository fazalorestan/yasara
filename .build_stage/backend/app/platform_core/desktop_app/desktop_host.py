class DesktopHostService:
    def status(self):
        return {"ready": True, "host": "yasara_desktop_host", "platform": "windows", "mode": "development_shell", "exe_packaging_enabled": False, "dashboard_connected": True, "real_execution_enabled": False, "real_broker_connection_enabled": False}
desktop_host_service = DesktopHostService()
