class PluginSandboxPolicy:
    def policy(self):
        return {"ready": True, "filesystem_access": "none", "network_access": "none", "subprocess_access": False, "secret_access": False, "dynamic_code_execution": False, "sandbox_required": True}

    def evaluate(self, manifest: dict):
        caps = set(manifest.get("capabilities", []))
        unsafe = sorted(caps.intersection({"network", "filesystem", "subprocess", "secret_access", "real_execution"}))
        return {"ready": True, "allowed": len(unsafe) == 0, "unsafe_capabilities": unsafe, "sandbox_required": True}

plugin_sandbox_policy = PluginSandboxPolicy()
