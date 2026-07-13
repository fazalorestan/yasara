class ServiceRegistry:
    def __init__(self):
        self._services = {}
        self._factories = {}
    def register_instance(self, name, instance):
        self._services[name] = instance
        return instance
    def register_factory(self, name, factory):
        self._factories[name] = factory
    def get(self, name):
        if name in self._services:
            return self._services[name]
        if name in self._factories:
            self._services[name] = self._factories[name]()
            return self._services[name]
        raise KeyError(name)
    def exists(self, name):
        return name in self._services or name in self._factories
    def list(self):
        return sorted(set(self._services) | set(self._factories))

service_registry = ServiceRegistry()
