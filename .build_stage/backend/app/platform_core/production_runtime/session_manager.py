class RuntimeSessionManager:
    def session(self):
        return {
            "ready": True,
            "session_id": "dev-session",
            "session_mode": "development",
            "active": True,
            "persistent": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

runtime_session_manager = RuntimeSessionManager()
