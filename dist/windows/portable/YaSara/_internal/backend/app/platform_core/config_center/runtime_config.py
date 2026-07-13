class RuntimeConfigStore:
    def __init__(self):
        self._values = {}

    def set(self, key: str, value):
        self._values[key] = value
        return {"key": key, "value": value}

    def get(self, key: str, default=None):
        return self._values.get(key, default)

    def all(self):
        return dict(self._values)

runtime_config_store = RuntimeConfigStore()
