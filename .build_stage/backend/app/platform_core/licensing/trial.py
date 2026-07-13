class TrialPolicy:
    def default_demo_days(self):
        return 30

    def short_demo_days(self):
        return 14

    def policy(self):
        return {
            "ready": True,
            "default_days": 30,
            "short_days": 14,
            "auto_trading_enabled": False,
            "export_enabled": False,
            "api_access_enabled": False,
            "marketplace_enabled": False,
            "alert_limit": 10,
            "indicator_limit": 2,
            "workspace_limit": 1,
        }

trial_policy = TrialPolicy()
