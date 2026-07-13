from app.platform_core.licensing.enforcement.plugin_guard import PluginAccessGuard
def test_v500_alpha10_plugin_guard_denied():
    r = PluginAccessGuard().can_use_plugin({"license_type": "demo"}, "ai_coach")
    assert r["allowed"] is False
    assert "AI_COACH" in r["missing_features"]
