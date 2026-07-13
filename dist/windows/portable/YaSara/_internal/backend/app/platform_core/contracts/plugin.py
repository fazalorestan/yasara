from app.platform_core.contracts.base import BaseContract

class PluginContract(BaseContract):
    contract_name = "plugin"

    def manifest(self):
        raise NotImplementedError("Plugins must expose manifest()")
