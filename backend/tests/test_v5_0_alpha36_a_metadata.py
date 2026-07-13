from app.platform_core.plugin_sdk.metadata import PluginMetadataService

def test_v500_alpha36_a_metadata(): assert PluginMetadataService().metadata({'plugin_id':'p','metadata':{}})['sandbox_required'] is True