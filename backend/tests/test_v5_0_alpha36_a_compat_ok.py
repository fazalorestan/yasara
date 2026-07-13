from app.platform_core.plugin_sdk.compatibility import PluginCompatibilityService

def test_v500_alpha36_a_compat_ok(): assert PluginCompatibilityService().check({'api_version':'v1'})['compatible'] is True