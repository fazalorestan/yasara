from app.platform_core.plugin_sdk.runtime import PluginRuntimeService

def test_v500_alpha36_b_runtime(): assert PluginRuntimeService().runtime_context()['dynamic_code_execution'] is False