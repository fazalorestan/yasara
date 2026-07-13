from app.platform_core.plugin_sdk.permissions import PluginPermissionGate

def test_v500_alpha36_b_permissions_allowed(): assert 'analytics' in PluginPermissionGate().allowed_permissions()['permissions']