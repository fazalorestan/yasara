from app.platform_core.plugin_sdk.compat_matrix import PluginCompatibilityMatrixService

def test_v500_alpha36_c_supported(): assert PluginCompatibilityMatrixService().is_supported('v1','1.0.0')['supported'] is True