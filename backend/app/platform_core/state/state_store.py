from app.platform_core.state.models import PluginStateRecord

class PluginStateStore:
    def __init__(self):
        self._states: dict[str, PluginStateRecord] = {}

    def set_state(self, plugin: str, state: dict):
        record = PluginStateRecord(plugin=plugin, state=state)
        self._states[plugin] = record
        return record

    def get_state(self, plugin: str):
        return self._states.get(plugin)

    def remove_state(self, plugin: str):
        return self._states.pop(plugin, None)

    def list_states(self):
        return {name: record.__dict__ for name, record in self._states.items()}

plugin_state_store = PluginStateStore()
