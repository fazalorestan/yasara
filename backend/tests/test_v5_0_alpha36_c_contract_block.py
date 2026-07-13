from app.v500_alpha36_plugin_versioning.service import PluginVersioningFacadeV500Alpha36

def test_v500_alpha36_c_contract_block(): assert PluginVersioningFacadeV500Alpha36().contract()['execution_allowed'] is False
