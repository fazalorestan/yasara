from app.platform_core.plugin_sdk.manifest import plugin_manifest_service

class PluginRuntimeService:
    def runtime_context(self, manifest: dict | None = None):
        manifest = manifest or plugin_manifest_service.sample_manifest()
        return {"ready": True, "plugin_id": manifest.get("plugin_id"), "runtime_mode": "sandboxed_contract", "dynamic_code_execution": False, "execution_allowed": False}

    def execute_contract(self, manifest: dict | None = None):
        ctx = self.runtime_context(manifest)
        return {"ready": True, "executed": False, "dry_run": True, "runtime_context": ctx, "reason": "contract_only_runtime"}

plugin_runtime_service = PluginRuntimeService()
