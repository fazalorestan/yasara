from app.platform_core.plugin_sdk.health import PluginHealthService

def test_v500_alpha36_b_health(): assert PluginHealthService().health({'plugin_id':'p'})['status']=='ok'