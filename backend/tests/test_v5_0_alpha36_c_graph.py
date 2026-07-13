from app.platform_core.plugin_sdk.dependencies import PluginDependencyContractService

def test_v500_alpha36_c_graph(): assert PluginDependencyContractService().graph([{'plugin_id':'a','dependencies':[]}])['nodes']==['a']