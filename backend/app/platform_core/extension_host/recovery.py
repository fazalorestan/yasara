RECOVERY_STEPS = ["retry", "recover", "disable", "report"]

class RecoveryManager:
    def __init__(self):
        self._history = []

    def recover(self, plugin: str, error: str = ""):
        item = {
            "plugin": plugin,
            "error": error,
            "steps": RECOVERY_STEPS,
            "final_state": "reported",
            "mode": "report_only",
        }
        self._history.append(item)
        return item

    def history(self):
        return list(self._history)

recovery_manager = RecoveryManager()
