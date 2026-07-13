class DesktopSessionManager:
    def session(self):
        return {"ready": True, "session_id": "desktop-dev-session", "active": True, "mode": "development", "dashboard_connected": True, "real_execution_enabled": False}
desktop_session_manager = DesktopSessionManager()
