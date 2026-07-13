from app.v500_alpha36_plugin_sdk_core.service import PluginSDKCoreFacadeV500Alpha36

def test_v500_alpha36_a_facade_validate():
 r=PluginSDKCoreFacadeV500Alpha36().validate(); assert r is not None
