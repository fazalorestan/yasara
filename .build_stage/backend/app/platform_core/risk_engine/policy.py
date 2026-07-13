from app.platform_core.risk_engine.models import RiskPolicy

class RiskPolicyProvider:
    def default_policy(self):
        return RiskPolicy().__dict__

risk_policy_provider = RiskPolicyProvider()
