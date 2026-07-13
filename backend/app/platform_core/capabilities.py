CAPABILITIES = [
    "analysis",
    "execution",
    "dashboard",
    "notification",
    "storage",
    "ai",
    "market_data",
    "scanner",
    "strategy",
    "risk",
    "backtest",
    "journal",
    "paper_trading",
]

class CapabilityRegistry:
    def __init__(self):
        self._plugin_capabilities: dict[str, list[str]] = {}

    def register(self, plugin: str, capabilities: list[str]):
        invalid = [c for c in capabilities if c not in CAPABILITIES]
        if invalid:
            raise ValueError(f"Invalid capabilities: {invalid}")
        self._plugin_capabilities[plugin] = capabilities
        return {"plugin": plugin, "capabilities": capabilities}

    def get(self, plugin: str):
        return self._plugin_capabilities.get(plugin, [])

    def list(self):
        return dict(self._plugin_capabilities)

capability_registry = CapabilityRegistry()
