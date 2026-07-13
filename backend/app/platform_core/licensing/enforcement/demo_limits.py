from app.platform_core.licensing.trial import trial_policy

class DemoLimitationEnforcer:
    def limits(self):
        p = trial_policy.policy()
        return {
            "ready": True,
            "license_type": "demo",
            "alert_limit": p["alert_limit"],
            "indicator_limit": p["indicator_limit"],
            "workspace_limit": p["workspace_limit"],
            "export_allowed": p["export_enabled"],
            "api_access_allowed": p["api_access_enabled"],
            "auto_trading_allowed": p["auto_trading_enabled"],
        }

    def check_usage(self, usage: dict):
        limits = self.limits()
        violations = []
        if int(usage.get("alerts", 0)) > limits["alert_limit"]:
            violations.append("alert_limit_exceeded")
        if int(usage.get("indicators", 0)) > limits["indicator_limit"]:
            violations.append("indicator_limit_exceeded")
        if int(usage.get("workspaces", 0)) > limits["workspace_limit"]:
            violations.append("workspace_limit_exceeded")
        return {
            "ready": len(violations) == 0,
            "violations": violations,
            "limits": limits,
            "execution_allowed": False,
        }

demo_limitation_enforcer = DemoLimitationEnforcer()
