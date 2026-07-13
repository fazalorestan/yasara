class SecurityPolicies:
    def __init__(self):
        self.policies = {
            "live_trading_default_enabled": False,
            "require_license_for_execution": True,
            "require_permission_for_execution": True,
            "require_risk_approval_for_execution": True,
        }
    def get(self, name, default=None):
        return self.policies.get(name, default)

security_policies = SecurityPolicies()
