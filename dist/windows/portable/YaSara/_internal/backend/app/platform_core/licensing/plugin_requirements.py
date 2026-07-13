class PluginLicenseRequirementService:
    def requirement_for(self, plugin_name: str):
        mapping = {
            "yasara_indicator": ["BASIC_ANALYSIS"],
            "advanced_ai": ["ADVANCED_AI"],
            "scanner": ["SCANNER"],
            "ai_coach": ["AI_COACH"],
            "forex": ["FOREX"],
            "iran_market": ["IRAN_MARKET"],
            "auto_trading": ["AUTO_TRADING"],
        }
        return {
            "ready": True,
            "plugin": plugin_name,
            "required_features": mapping.get(plugin_name, []),
            "execution_allowed": False,
        }

plugin_license_requirement_service = PluginLicenseRequirementService()
