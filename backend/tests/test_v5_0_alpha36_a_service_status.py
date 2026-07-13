from app.platform_core.plugin_sdk.service import PluginSDKCoreService

def test_v500_alpha36_a_service_status():
 r=PluginSDKCoreService().status(); assert r is not None
