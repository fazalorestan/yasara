from app.platform_core.plugin_sdk.manifest import PluginManifestService

def test_v500_alpha36_a_sample_manifest(): assert PluginManifestService().sample_manifest()['plugin_id']=='demo.analytics'