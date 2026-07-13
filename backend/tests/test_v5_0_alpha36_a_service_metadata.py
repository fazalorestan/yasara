from app.platform_core.plugin_sdk.service import PluginSDKCoreService

def test_v500_alpha36_a_service_metadata():
 r=PluginSDKCoreService().metadata(); assert r is not None
