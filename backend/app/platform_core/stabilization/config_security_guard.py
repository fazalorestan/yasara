class ConfigSecurityGuardService:
    def policy(self):
        return {
            "ready": True,
            "hardcoded_api_keys_allowed": False,
            "secrets_in_code_allowed": False,
            "secure_config_required": True,
            "environment_override_supported": True,
            "commercial_api_key_required": False,
            "adds_new_feature": False,
        }

config_security_guard_service = ConfigSecurityGuardService()
