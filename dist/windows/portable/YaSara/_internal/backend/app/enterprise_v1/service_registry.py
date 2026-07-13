from pydantic import BaseModel

class ServiceDescriptorV1(BaseModel):
    name: str
    module: str
    healthy: bool = True

class ServiceRegistryV1:
    def __init__(self):
        self.services: dict[str, ServiceDescriptorV1] = {}

    def register(self, service: ServiceDescriptorV1) -> ServiceDescriptorV1:
        self.services[service.name] = service
        return service

    def healthy_services(self) -> list[ServiceDescriptorV1]:
        return [s for s in self.services.values() if s.healthy]
