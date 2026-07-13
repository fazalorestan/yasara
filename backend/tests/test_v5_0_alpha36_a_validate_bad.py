from app.platform_core.plugin_sdk.manifest import PluginManifestService

def test_v500_alpha36_a_validate_bad(): assert PluginManifestService().validate({})['valid'] is False