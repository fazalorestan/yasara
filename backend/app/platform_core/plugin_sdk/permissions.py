class PluginPermissionGate:
    def allowed_permissions(self):
        return {"ready": True, "permissions": ["analytics", "reporting", "read_only_market_context"]}

    def check(self, manifest: dict):
        allowed = set(self.allowed_permissions()["permissions"])
        requested = set(manifest.get("capabilities", []))
        denied = sorted(requested - allowed)
        return {"ready": True, "allowed": len(denied) == 0, "denied": denied, "execution_allowed": False}

plugin_permission_gate = PluginPermissionGate()
