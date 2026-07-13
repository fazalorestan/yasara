from app.platform_core.build_pipeline.plugin_build_contract import PluginBuildContractService

def test_plugin(): assert PluginBuildContractService().contract()['plugin_based_required'] is True
