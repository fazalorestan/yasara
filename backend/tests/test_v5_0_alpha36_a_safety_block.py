from app.platform_core.plugin_sdk.safety import PluginSafetyContract

def test_v500_alpha36_a_safety_block(): assert PluginSafetyContract().evaluate({})['auto_trading_allowed'] is False