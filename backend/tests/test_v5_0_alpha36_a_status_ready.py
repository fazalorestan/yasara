from app.platform_core.plugin_sdk.service import PluginSDKCoreService

def test_v500_alpha36_a_status_ready(): assert PluginSDKCoreService().status()['ready'] is True
