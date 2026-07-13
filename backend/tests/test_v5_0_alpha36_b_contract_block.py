from app.v500_alpha36_plugin_runtime_sandbox.service import PluginRuntimeSandboxFacadeV500Alpha36

def test_v500_alpha36_b_contract_block(): assert PluginRuntimeSandboxFacadeV500Alpha36().contract()['execution_allowed'] is False
