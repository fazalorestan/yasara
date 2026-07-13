class PluginBuildContractService:
    def contract(self):
        return {
            "ready": True,
            "plugin_based_required": True,
            "plugin_manifest_required": True,
            "plugin_dependency_graph_required": True,
            "direct_core_coupling_allowed": False,
            "feature_modules_must_be_pluggable": True,
        }

plugin_build_contract_service = PluginBuildContractService()
