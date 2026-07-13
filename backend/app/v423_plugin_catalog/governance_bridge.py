from dataclasses import dataclass, field

@dataclass
class GovernanceContextV423:
    permissions: list[str] = field(default_factory=list)
    licenses: list[str] = field(default_factory=list)
    feature_flags: dict[str, bool] = field(default_factory=dict)

class PluginGovernanceBridgeV423:
    def evaluate(self, manifest, context: GovernanceContextV423 | None = None):
        context = context or GovernanceContextV423()

        missing_permissions = [
            p for p in manifest.required_permissions
            if p not in context.permissions
        ]
        missing_licenses = [
            l for l in manifest.required_licenses
            if l not in context.licenses
        ]
        disabled_flags = [
            f for f in manifest.feature_flags
            if context.feature_flags and context.feature_flags.get(f) is False
        ]

        allowed = not missing_permissions and not missing_licenses and not disabled_flags

        return {
            "plugin": manifest.name,
            "allowed": allowed,
            "missing_permissions": missing_permissions,
            "missing_licenses": missing_licenses,
            "disabled_feature_flags": disabled_flags,
            "enforcement_mode": "report_only",
        }
