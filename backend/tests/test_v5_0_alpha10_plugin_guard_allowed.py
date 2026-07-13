from app.platform_core.licensing.enforcement.plugin_guard import PluginAccessGuard
def test_v500_alpha10_plugin_guard_allowed():
    r = PluginAccessGuard().can_use_plugin({"license_type": "demo"}, "yasara_indicator")
    assert r["allowed"] is True
