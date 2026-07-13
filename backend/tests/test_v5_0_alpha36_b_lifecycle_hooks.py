from app.platform_core.plugin_sdk.lifecycle import PluginLifecycleService

def test_v500_alpha36_b_lifecycle_hooks(): assert 'on_load' in PluginLifecycleService().hooks()['hooks']