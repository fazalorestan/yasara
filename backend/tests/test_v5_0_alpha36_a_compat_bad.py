from app.platform_core.plugin_sdk.compatibility import PluginCompatibilityService

def test_v500_alpha36_a_compat_bad(): assert PluginCompatibilityService().check({'api_version':'v2'})['compatible'] is False