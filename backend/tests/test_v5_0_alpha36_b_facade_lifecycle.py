from app.v500_alpha36_plugin_runtime_sandbox.service import PluginRuntimeSandboxFacadeV500Alpha36

def test_v500_alpha36_b_facade_lifecycle():
 r=PluginRuntimeSandboxFacadeV500Alpha36().lifecycle(); assert r is not None
