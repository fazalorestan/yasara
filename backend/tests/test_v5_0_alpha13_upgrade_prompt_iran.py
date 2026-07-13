from app.platform_core.licensing.ui.upgrade_prompt import UpgradePromptContract
def test_v500_alpha13_upgrade_prompt_iran():
    assert UpgradePromptContract().prompt_for("IRAN_MARKET")["recommended_plan"] == "enterprise"
