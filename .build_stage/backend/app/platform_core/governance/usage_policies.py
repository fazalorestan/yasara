class UsagePolicies:
    def __init__(self):
        self._limits = {"default_daily_signal_limit": 100, "default_api_rate_limit_per_minute": 60}
    def get(self, name, default=None):
        return self._limits.get(name, default)

usage_policies = UsagePolicies()
