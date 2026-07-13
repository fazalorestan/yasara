from app.v500_alpha36_plugin_runtime_sandbox.service import PluginRuntimeSandboxFacadeV500Alpha36

def test_v500_alpha36_b_facade_execute_contract():
 r=PluginRuntimeSandboxFacadeV500Alpha36().execute_contract(); assert r is not None
