from app.platform_core.plugin_sdk.dependencies import PluginDependencyContractService

def test_v500_alpha36_c_deps_invalid(): assert PluginDependencyContractService().validate({'dependencies':[{}]})['valid'] is False