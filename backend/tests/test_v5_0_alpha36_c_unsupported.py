from app.platform_core.plugin_sdk.compat_matrix import PluginCompatibilityMatrixService

def test_v500_alpha36_c_unsupported(): assert PluginCompatibilityMatrixService().is_supported('v9','1.0.0')['supported'] is False