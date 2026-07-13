class RuntimeModeResolver:
    def resolve(self, edition: str = "personal"):
        commercial = edition == "commercial"
        return {
            "ready": True,
            "edition": edition,
            "runtime_mode": "development",
            "execution_engine_enabled": not commercial,
            "api_key_required": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

runtime_mode_resolver = RuntimeModeResolver()
