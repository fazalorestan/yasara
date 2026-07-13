from app.platform_core.stabilization.plugin_boundary_guard import PluginBoundaryGuardService

def test_plugin(): assert PluginBoundaryGuardService().policy()['plugin_based_required'] is True
