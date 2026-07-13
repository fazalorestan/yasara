class ResourceManager:
    def __init__(self):
        self._resources = {}
    def register(self, name, metadata=None):
        self._resources[name] = metadata or {}
        return self._resources[name]
    def list(self):
        return self._resources

resource_manager = ResourceManager()
