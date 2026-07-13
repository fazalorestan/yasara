class VersionStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "version": "v5.0-alpha.44",
            "build": "44001",
            "channel": "alpha",
            "personal_execution_engine_enabled": True,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }
version_state_registry = VersionStateRegistry()
