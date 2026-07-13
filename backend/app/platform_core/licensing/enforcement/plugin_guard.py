from app.platform_core.licensing.entitlements import entitlement_engine
from app.platform_core.licensing.plugin_requirements import plugin_license_requirement_service

class PluginAccessGuard:
    def can_use_plugin(self, payload: dict, plugin_name: str):
        requirement = plugin_license_requirement_service.requirement_for(plugin_name)
        missing = []
        for feature in requirement["required_features"]:
            if not entitlement_engine.can_access(payload, feature)["enabled"]:
                missing.append(feature)
        return {
            "ready": len(missing) == 0,
            "plugin": plugin_name,
            "missing_features": missing,
            "allowed": len(missing) == 0,
            "execution_allowed": False,
        }

plugin_access_guard = PluginAccessGuard()
