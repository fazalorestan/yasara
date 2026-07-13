from app.platform_core.plugin_sdk.compat_matrix import PluginCompatibilityMatrixService

def test_v500_alpha36_c_matrix(): assert 'v1' in PluginCompatibilityMatrixService().matrix()['matrix']