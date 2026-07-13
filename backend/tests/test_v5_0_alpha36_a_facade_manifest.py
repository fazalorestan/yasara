from app.v500_alpha36_plugin_sdk_core.service import PluginSDKCoreFacadeV500Alpha36

def test_v500_alpha36_a_facade_manifest():
 r=PluginSDKCoreFacadeV500Alpha36().manifest(); assert r is not None
