import os

class ConfigurationManager:
    def __init__(self):
        self._runtime = {}
    def set(self, key, value):
        self._runtime[key] = value
    def get(self, key, default=None):
        return self._runtime[key] if key in self._runtime else os.getenv(key, default)
    def all_runtime(self):
        return dict(self._runtime)

configuration_manager = ConfigurationManager()
