from app.platform_core.plugin_sdk.loader import PluginLoaderContract

def test_v500_alpha36_a_loader_contract(): assert PluginLoaderContract().load_contract({'plugin_id':'p'})['dynamic_code_execution'] is False