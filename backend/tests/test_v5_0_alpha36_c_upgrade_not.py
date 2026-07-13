from app.platform_core.plugin_sdk.upgrade import PluginUpgradePlanner

def test_v500_alpha36_c_upgrade_not(): assert PluginUpgradePlanner().plan('1.0.0','1.0.0')['upgrade_needed'] is False