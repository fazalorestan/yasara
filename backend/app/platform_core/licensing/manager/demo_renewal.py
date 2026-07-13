class DemoRenewalPolicy:
    def policy(self):
        return {
            "ready": True,
            "default_demo_days": 30,
            "short_demo_days": 14,
            "max_renewals": 1,
            "renewal_requires_admin": True,
            "auto_trading_allowed": False,
            "mode": "policy_only",
        }

    def can_renew(self, previous_renewals: int):
        return previous_renewals < self.policy()["max_renewals"]

demo_renewal_policy = DemoRenewalPolicy()
