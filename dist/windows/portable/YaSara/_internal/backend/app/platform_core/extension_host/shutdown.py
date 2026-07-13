SAFE_SHUTDOWN_STEPS = [
    "stop_accepting_events",
    "flush_queue",
    "save_state",
    "unload",
    "stopped",
]

class SafeShutdownContract:
    def plan(self, plugin: str):
        return {
            "plugin": plugin,
            "steps": SAFE_SHUTDOWN_STEPS,
            "mode": "contract_only",
            "destructive": False,
        }

safe_shutdown_contract = SafeShutdownContract()
