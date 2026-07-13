from app.platform_core.plugin_sdk.models import PluginMetadata

def test_v500_alpha36_a_metadata_model(): assert PluginMetadata('p').sandbox_required is True