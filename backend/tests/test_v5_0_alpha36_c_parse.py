from app.platform_core.plugin_sdk.versioning import PluginVersionService

def test_v500_alpha36_c_parse(): assert PluginVersionService().parse('1.2.3')['minor']==2