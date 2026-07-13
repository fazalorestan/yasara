class PluginDependencyContractService:
    def validate(self, manifest: dict):
        deps = manifest.get("dependencies", [])
        missing = [d for d in deps if not d.get("plugin_id") or not d.get("version")]
        return {"ready": True, "valid": len(missing) == 0, "dependencies": deps, "missing": missing}

    def graph(self, manifests: list[dict]):
        return {"ready": True, "nodes": [m.get("plugin_id") for m in manifests], "edges": [(m.get("plugin_id"), d.get("plugin_id")) for m in manifests for d in m.get("dependencies", [])]}

plugin_dependency_contract_service = PluginDependencyContractService()
