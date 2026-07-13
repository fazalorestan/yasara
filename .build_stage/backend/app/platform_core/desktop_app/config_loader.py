class DesktopConfigLoader:
    def config(self):
        return {"ready": True, "config_loaded": True, "edition": "personal", "commercial_execution_engine_enabled": False, "commercial_api_key_required": False, "real_execution_enabled": False}
desktop_config_loader = DesktopConfigLoader()
