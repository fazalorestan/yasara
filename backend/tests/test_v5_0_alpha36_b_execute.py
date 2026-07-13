from app.platform_core.plugin_sdk.runtime import PluginRuntimeService

def test_v500_alpha36_b_execute(): assert PluginRuntimeService().execute_contract()['executed'] is False