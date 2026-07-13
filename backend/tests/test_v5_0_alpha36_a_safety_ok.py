from app.platform_core.plugin_sdk.safety import PluginSafetyContract

def test_v500_alpha36_a_safety_ok(): assert PluginSafetyContract().evaluate({'capabilities':['analytics']})['safe'] is True