from pydantic import BaseModel, Field

class CapabilityV1(BaseModel):
    key: str
    category: str
    enabled: bool = True

class CapabilityRegistryV1:
    def __init__(self):
        self.capabilities: dict[str, CapabilityV1] = {}

    def register(self, capability: CapabilityV1) -> CapabilityV1:
        self.capabilities[capability.key] = capability
        return capability

    def list_enabled(self) -> list[CapabilityV1]:
        return [c for c in self.capabilities.values() if c.enabled]
