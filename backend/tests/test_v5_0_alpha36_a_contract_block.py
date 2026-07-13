from app.v500_alpha36_plugin_sdk_core.service import PluginSDKCoreFacadeV500Alpha36

def test_v500_alpha36_a_contract_block(): assert PluginSDKCoreFacadeV500Alpha36().contract()['execution_allowed'] is False
