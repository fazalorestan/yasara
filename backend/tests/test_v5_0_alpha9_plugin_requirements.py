from app.platform_core.licensing.plugin_requirements import plugin_license_requirement_service
def test_v500_alpha9_plugin_requirements():
    r = plugin_license_requirement_service.requirement_for("ai_coach")
    assert "AI_COACH" in r["required_features"]
    assert r["execution_allowed"] is False
