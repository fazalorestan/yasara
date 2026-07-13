class BuildConfigurationLoader:
    def config(self):
        return {
            "ready": True,
            "config_loaded": True,
            "secure_config_required": True,
            "hardcoded_api_keys_allowed": False,
            "commercial_api_key_required": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

build_configuration_loader = BuildConfigurationLoader()
