from app.platform_core.plugin_sdk.registry import plugin_registry_service

def test_v500_alpha36_a_registry_list(): assert plugin_registry_service.list_plugins()['count'] >= 1