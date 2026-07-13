from app.v425_policy_gate.models import PolicyContextV425, PolicyRequirementV425

POLICY_ORDER = [
    "authentication",
    "role",
    "permission",
    "license",
    "entitlement",
    "feature_flag",
    "risk_approval",
    "execution",
]

class PluginPolicyGateV425:
    def evaluate(self, context: PolicyContextV425, requirement: PolicyRequirementV425):
        checks = []

        auth_ok = True if not requirement.require_authentication else context.authenticated
        checks.append({"step": "authentication", "allowed": auth_ok})

        role_ok = context.role not in ["blocked", "disabled"]
        checks.append({"step": "role", "allowed": role_ok, "role": context.role})

        permission_ok = True
        if requirement.permission:
            permission_ok = requirement.permission in context.permissions
        checks.append({"step": "permission", "allowed": permission_ok, "required": requirement.permission})

        license_ok = True
        if requirement.license:
            license_ok = requirement.license in context.licenses
        checks.append({"step": "license", "allowed": license_ok, "required": requirement.license})

        entitlement_ok = True
        if requirement.entitlement:
            entitlement_ok = requirement.entitlement in context.entitlements
        checks.append({"step": "entitlement", "allowed": entitlement_ok, "required": requirement.entitlement})

        feature_flag_ok = True
        if requirement.feature_flag:
            feature_flag_ok = context.feature_flags.get(requirement.feature_flag, False) is True
        checks.append({"step": "feature_flag", "allowed": feature_flag_ok, "required": requirement.feature_flag})

        risk_ok = True if not requirement.require_risk_approval else context.risk_approved
        checks.append({"step": "risk_approval", "allowed": risk_ok})

        allowed = all(c["allowed"] for c in checks)
        return {
            "ready": True,
            "allowed": allowed,
            "mode": "report_only",
            "policy_order": POLICY_ORDER,
            "checks": checks,
            "execution_allowed": False,
            "live_execution_enabled": False,
        }

    def default_report(self):
        return self.evaluate(
            PolicyContextV425(),
            PolicyRequirementV425(require_authentication=False),
        )
