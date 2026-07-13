from app.v500_alpha36_plugin_sdk_core.service import PluginSDKCoreFacadeV500Alpha36

def test_v500_alpha36_a_facade_compatibility():
 r=PluginSDKCoreFacadeV500Alpha36().compatibility(); assert r is not None
