from app.platform_core.licensing.ui.upgrade_prompt import UpgradePromptContract
def test_v500_alpha13_upgrade_prompt_ai():
    assert UpgradePromptContract().prompt_for("ADVANCED_AI")["recommended_plan"] == "pro"
