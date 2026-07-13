class PluginLoaderContract:
    def load_contract(self, manifest: dict):
        return {
            "ready": True,
            "plugin_id": manifest.get("plugin_id"),
            "load_mode": "contract_only",
            "sandbox_required": True,
            "dynamic_code_execution": False,
            "execution_allowed": False,
        }

plugin_loader_contract = PluginLoaderContract()
