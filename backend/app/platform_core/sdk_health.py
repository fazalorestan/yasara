SDK_HEALTH_STATES = ["healthy", "warning", "deprecated", "experimental", "disabled", "broken"]

class SDKHealthReporter:
    def __init__(self):
        self._states = {}

    def set(self, plugin: str, state: str = "healthy", detail: str = ""):
        if state not in SDK_HEALTH_STATES:
            raise ValueError(state)
        self._states[plugin] = {"plugin": plugin, "state": state, "detail": detail}
        return self._states[plugin]

    def get(self, plugin: str):
        return self._states.get(plugin)

    def list(self):
        return dict(self._states)

sdk_health_reporter = SDKHealthReporter()
