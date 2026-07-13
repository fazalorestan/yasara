from app.platform_core.plugin_sdk.manifest import PluginManifestService

def test_v500_alpha36_a_validate_ok(): assert PluginManifestService().validate(PluginManifestService().sample_manifest())['valid'] is True