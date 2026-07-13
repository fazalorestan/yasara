from app.v500_alpha36_plugin_sdk_core.service import PluginSDKCoreFacadeV500Alpha36

def test_v500_alpha36_a_facade_readiness():
 r=PluginSDKCoreFacadeV500Alpha36().readiness(); assert r is not None
