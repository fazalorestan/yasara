from app.platform_core.plugin_sdk.safety import PluginSafetyContract

def test_v500_alpha36_a_safety_bad(): assert PluginSafetyContract().evaluate({'capabilities':['real_execution']})['safe'] is False