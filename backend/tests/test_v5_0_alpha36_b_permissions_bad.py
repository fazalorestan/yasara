from app.platform_core.plugin_sdk.permissions import PluginPermissionGate

def test_v500_alpha36_b_permissions_bad(): assert PluginPermissionGate().check({'capabilities':['secret_access']})['allowed'] is False