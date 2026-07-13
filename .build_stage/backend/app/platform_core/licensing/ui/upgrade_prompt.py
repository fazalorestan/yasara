class UpgradePromptContract:
    def prompt_for(self, feature: str):
        mapping = {
            "ADVANCED_AI": "pro",
            "AI_COACH": "elite",
            "FOREX": "elite",
            "IRAN_MARKET": "enterprise",
            "API_ACCESS": "enterprise",
            "AUTO_TRADING": "internal",
        }
        return {
            "ready": True,
            "feature": feature,
            "recommended_plan": mapping.get(feature, "pro"),
            "message": f"Upgrade required for {feature}",
            "execution_allowed": False,
        }

upgrade_prompt_contract = UpgradePromptContract()
