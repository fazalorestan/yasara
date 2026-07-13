class PluginBoundaryGuardService:
    def policy(self):
        return {
            "ready": True,
            "plugin_based_required": True,
            "core_must_remain_small": True,
            "feature_modules_must_be_pluggable": True,
            "direct_feature_coupling_allowed": False,
            "adds_new_feature": False,
        }

plugin_boundary_guard_service = PluginBoundaryGuardService()
