from app.platform_core.plugin_sdk.runtime import PluginRuntimeService

def test_v500_alpha36_b_runtime_mode(): assert PluginRuntimeService().runtime_context()['runtime_mode']=='sandboxed_contract'
