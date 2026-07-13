from app.platform_core.plugin_sdk.lifecycle import PluginLifecycleService

def test_v500_alpha36_b_lifecycle_transition(): assert PluginLifecycleService().transition('created','load')['to']=='loaded'