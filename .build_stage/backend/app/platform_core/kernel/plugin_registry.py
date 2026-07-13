from dataclasses import dataclass, field
from typing import Any

PLUGIN_STATES = ["discovered","validated","licensed","loaded","initialized","running","paused","disabled","unloaded"]

@dataclass
class PluginManifest:
    name: str
    version: str = "0.0.1"
    dependencies: list[str] = field(default_factory=list)
    feature_flags: list[str] = field(default_factory=list)
    required_permissions: list[str] = field(default_factory=list)
    required_licenses: list[str] = field(default_factory=list)
    routes: list[str] = field(default_factory=list)
    services: list[str] = field(default_factory=list)
    tests: list[str] = field(default_factory=list)
    documentation: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

class PluginRegistry:
    def __init__(self):
        self._plugins = {}
    def register(self, manifest: PluginManifest, state="discovered"):
        if state not in PLUGIN_STATES:
            raise ValueError(state)
        self._plugins[manifest.name] = {"manifest": manifest, "state": state}
        return self._plugins[manifest.name]
    def set_state(self, name, state):
        if state not in PLUGIN_STATES:
            raise ValueError(state)
        if name not in self._plugins:
            raise KeyError(name)
        self._plugins[name]["state"] = state
        return self._plugins[name]
    def get(self, name):
        return self._plugins.get(name)
    def list(self):
        return self._plugins

plugin_registry = PluginRegistry()
