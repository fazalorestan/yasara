class LicenseFeatureMatrix:
    matrix = {
        "demo": ["DASHBOARD", "BASIC_ANALYSIS", "SCANNER", "ALERTS"],
        "personal": ["DASHBOARD", "BASIC_ANALYSIS", "SCANNER", "ALERTS", "JOURNAL"],
        "pro": ["DASHBOARD", "BASIC_ANALYSIS", "ADVANCED_AI", "SCANNER", "ALERTS", "JOURNAL", "BACKTEST", "STRATEGY_BUILDER"],
        "elite": ["DASHBOARD", "BASIC_ANALYSIS", "ADVANCED_AI", "SCANNER", "ALERTS", "JOURNAL", "BACKTEST", "STRATEGY_BUILDER", "FOREX", "MARKETPLACE", "AI_COACH"],
        "enterprise": ["DASHBOARD", "BASIC_ANALYSIS", "ADVANCED_AI", "SCANNER", "ALERTS", "JOURNAL", "BACKTEST", "STRATEGY_BUILDER", "FOREX", "IRAN_MARKET", "MARKETPLACE", "EXPORT", "API_ACCESS", "ENTERPRISE_DASHBOARD", "TELEGRAM_COACH"],
        "lifetime": ["DASHBOARD", "BASIC_ANALYSIS", "ADVANCED_AI", "SCANNER", "ALERTS", "JOURNAL", "BACKTEST", "STRATEGY_BUILDER", "FOREX", "IRAN_MARKET", "MARKETPLACE", "EXPORT", "API_ACCESS", "AI_COACH"],
        "internal": ["DASHBOARD", "BASIC_ANALYSIS", "ADVANCED_AI", "SCANNER", "ALERTS", "JOURNAL", "BACKTEST", "STRATEGY_BUILDER", "FOREX", "IRAN_MARKET", "MARKETPLACE", "EXPORT", "API_ACCESS", "AUTO_TRADING", "AI_COACH", "ENTERPRISE_DASHBOARD", "TELEGRAM_COACH"],
    }

    def features_for(self, license_type: str):
        return self.matrix.get(license_type, [])

    def is_enabled(self, license_type: str, feature: str):
        return feature in self.features_for(license_type)

license_feature_matrix = LicenseFeatureMatrix()
