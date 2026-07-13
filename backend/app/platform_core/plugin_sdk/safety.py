class PluginSafetyContract:
    def evaluate(self, manifest: dict):
        caps = set(manifest.get("capabilities", []))
        blocked_caps = {"real_execution", "auto_trading", "secret_access"}
        blocked = sorted(caps.intersection(blocked_caps))
        return {
            "ready": True,
            "safe": len(blocked) == 0,
            "blocked_capabilities": blocked,
            "real_execution_allowed": False,
            "auto_trading_allowed": False,
            "sandbox_required": True,
        }

plugin_safety_contract = PluginSafetyContract()
