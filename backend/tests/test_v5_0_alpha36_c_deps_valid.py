from app.platform_core.plugin_sdk.dependencies import PluginDependencyContractService

def test_v500_alpha36_c_deps_valid(): assert PluginDependencyContractService().validate({'dependencies':[{'plugin_id':'a','version':'1'}]})['valid'] is True