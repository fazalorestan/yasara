from app.platform_core.stabilization.config_security_guard import ConfigSecurityGuardService

def test_config(): assert ConfigSecurityGuardService().policy()['hardcoded_api_keys_allowed'] is False
