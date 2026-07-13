from app.platform_core.plugin_sdk.versioning import PluginVersionService

def test_v500_alpha36_c_compare_eq(): assert PluginVersionService().compare('1.0.0','1.0.0')['result']==0