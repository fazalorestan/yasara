from app.platform_core.plugin_sdk.models import PluginManifest

def test_v500_alpha36_a_manifest_model(): assert PluginManifest('p','Plugin','1').plugin_id=='p'