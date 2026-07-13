from app.platform_core.plugin_sdk.versioning import plugin_version_service

class PluginUpgradePlanner:
    def plan(self, current_version: str, target_version: str):
        cmp = plugin_version_service.compare(target_version, current_version)
        needed = cmp["result"] > 0
        return {"ready": True, "upgrade_needed": needed, "current_version": current_version, "target_version": target_version, "steps": ["backup", "validate", "upgrade", "verify"] if needed else []}

plugin_upgrade_planner = PluginUpgradePlanner()
