from app.platform_core.governance.security_policies import security_policies

class SecurityReadinessReport:
    def report(self):
        policies = security_policies.policies
        checks = {
            "live_trading_default_disabled": policies.get("live_trading_default_enabled") is False,
            "requires_license_for_execution": policies.get("require_license_for_execution") is True,
            "requires_permission_for_execution": policies.get("require_permission_for_execution") is True,
            "requires_risk_approval_for_execution": policies.get("require_risk_approval_for_execution") is True,
        }
        return {
            "ready": all(checks.values()),
            "checks": checks,
            "mode": "report_only",
        }
